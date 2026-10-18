# ADR-001: Architecture Topology — Modular Monolith vs Microservices for CommerceOS

**Document ID**: `ADR-001`  
**Status**: APPROVED  
**Date**: 2026-10-18  
**Author**: Principal Software Engineer (CommerceOS Engineering)  
**Stakeholders**: CommerceOS Architecture Team, Antigravity Orchestrator, SRE  

---

## 1. Context and Problem Statement

CommerceOS is a multi-tenant e-commerce operating system targeting the Saudi Arabian and GCC markets, combining core retail commerce with vertical-specific features:
- Core Commerce (Catalog, Pricing, Cart, Checkout, Order, Inventory, Customer, Payments, Fulfillment).
- Vertical Extensions (Bakery/Flower Customizer, Event-based Gifting).
- Operational Modules (Page Builder / CMS, CRM & Loyalty, Saudi ZATCA Phase 2 E-Invoicing, Analytics Read-Models).

A critical architectural decision must be codified prior to development: **Should CommerceOS be architected as a fleet of distributed microservices, or as a Modular Monolith built on Medusa v2?**

Furthermore, for large operational capabilities such as **Analytics** and **CRM**, should they be deployed as independent remote microservices from day one, or contained as cohesive bounded-context modules within the monolith?

---

## 2. Alternatives Considered

### Alternative A: Distributed Microservices Architecture
* *Description*: Deploying separate independently deployable services (Catalog Service, Order Service, Cart Service, Analytics Service, CRM Service, ZATCA Service) communicating over gRPC / REST with individual databases per service.
* *Drawbacks*:
  * Extreme operational complexity: Requires distributed tracing, service meshes, distributed saga coordinators, and complex local dev environments.
  * Distributed Transaction Fallacy: Coordinating checkout across 4 microservices requires distributed two-phase commits or complex event sagas, creating high risk of partial failure (e.g. money deducted, inventory reserved, but order creation failed).
  * High Network Overhead & Latency: Microservice network hops add 20–50ms per interaction, degrading p95 checkout response times.
  * Violates Constitution Principle III & VI (premature distributed systems).

### Alternative B: Unstructured Traditional Monolith
* *Description*: A single codebase where all tables share foreign keys and code freely imports models across domains without boundaries.
* *Drawbacks*:
  * Spaghetti architecture, tight coupling, impossible to maintain or refactor.
  * Schema migrations in one feature easily break unrelated domains.

### Alternative C: Medusa v2 Modular Monolith (CHOSEN)
* *Description*: A single deployable codebase running on Medusa v2, structured into strictly isolated **Domain Modules**. Modules communicate in-memory via service contracts and Medusa Workflows, with data decoupling enforced by **Module Links** and **Remote Query**. No cross-module database foreign keys. Background tasks execute via dedicated Medusa Worker processes sharing the codebase.

---

## 3. Decision

We decisively choose **Alternative C: Medusa v2 Modular Monolith**.

CommerceOS will be implemented as a unified modular monolith. Modules will have distinct schema prefixes, strict public service interfaces, and zero direct foreign keys across boundaries.

For **Analytics** and **CRM**:
* They will start as **cohesive bounded-context modules within the modular monolith**, consuming internal domain events asynchronously via the Medusa Redis event bus.
* They will NOT be split into remote microservices until explicit performance or regulatory thresholds are breached.

---

## 4. Deep Architectural Analysis of the 10 Dimensions

### 1. Module Independence & Bounded Contexts
* Each module (e.g. `src/modules/cms`, `src/modules/customizer`, `src/modules/loyalty`) lives in its own directory, defining its own data models, migrations, and service classes.
* A module can only access another module's capabilities through public service methods resolved via the Medusa container, or through Medusa Workflows. Direct database table joins across module boundaries are strictly prohibited.

### 2. Preventing Duplication of Medusa Core Features
* Medusa v2 native engines (Product, Pricing, Promotion, Cart, Order, Inventory, Payment, Fulfillment) are the sole authority for commerce operations.
* Custom modules augment core entities via **Module Links** (`defineLink`) and inject business logic via **Workflow Steps**. No parallel pricing, cart, or order tables will ever be created.

### 3. PostgreSQL Transaction Integrity & Connection Pooling
* **ACID Guarantees**: Checkout operations (cart completion, payment authorization, inventory reservation, order placement) execute within a unified database transaction or coordinated Medusa workflow with compensation rollbacks.
* **Connection Pooling**: A centralized `PgBouncer` layer handles connection pooling between Node.js processes and PostgreSQL 17, preventing connection exhaustion under flash traffic spikes.
* **Safe Migrations**: Schema updates adhere strictly to the non-destructive Expand/Contract pattern.

### 4. Redis, BullMQ Workers & Asynchronous Failure Management
* **Process Separation**: In production, two distinct process modes are deployed from the same image:
  1. *Web API Process* (`medusa start`): Handles HTTP requests, stateless, scaled horizontally.
  2. *Worker Process* (`medusa worker`): Pulls jobs from Redis streams / BullMQ queues, handles long-running tasks.
* **Idempotent Job Processing**: Every event handler records processed event IDs to guarantee that at-least-once message delivery never creates duplicate invoices, billing charges, or reward points.

### 5. Multi-Layer Security & Tenant Isolation
* **Server-Side Enforcement**: Object-level authorization (BOLA prevention) is enforced at the controller and service layer. Every query for customer data checks `WHERE customer_id = :authenticated_user_id`.
* **Zero Trust Boundary**: Webhooks and image uploaders strictly enforce SSRF protection, rejecting internal IP addresses (`10.x.x.x`, `192.168.x.x`, `169.254.169.254`).

### 6. Horizontal Scalability & Performance Budgets
* The stateless Web API tier scales horizontally behind a cloud load balancer.
* Database reads are optimized via PostgreSQL indexes, read-replicas for analytical queries, and Next.js ISR (Incremental Static Regeneration) on the CDN edge.
* Performance budgets: Checkout p95 latency < 400ms; Catalog browse p95 latency < 150ms.

### 7. Dependency & Semantic Versioning Management
* Dependencies are strictly locked in `package-lock.json`. Updates are managed via automated security audits (`npm audit`) and tested in CI before merging.
* Core Medusa packages are kept aligned on the exact minor/patch releases to prevent internal container resolution mismatches.

### 8. Storefront & Admin Integration Contracts
* **Storefront (Next.js)**: Interacts with the backend via REST Store API endpoints authenticated by a publishable API key, utilizing `@medusajs/js-sdk`.
* **Admin Dashboard**: Custom modules inject UI Widgets, Custom Routes, and Setting Pages into the native Medusa Admin via standard React extension points, styling with `@medusajs/ui`.

### 9. Error Handling, Disaster Recovery & Zero-Downtime Rollbacks
* Medusa Workflows implement automatic compensation steps on failure.
* Point-In-Time Recovery (PITR) is enabled on PostgreSQL via continuous WAL archiving.
* Zero-downtime rolling deployments are supported because all database migrations are backward-compatible.

### 10. Service Extraction Thresholds (When to Split)
A bounded-context module (such as Analytics or CRM) will remain inside the modular monolith until at least ONE of the following objective criteria is satisfied:
1. **CPU/Resource Asymmetry**: Analytical processing or image rendering consumes > 40% of the host CPU/memory, degrading checkout latency despite worker process separation.
2. **Independent Deployment Cadence**: A specialized team requires daily independent releases that destabilize core commerce CI/CD pipelines.
3. **Data Compliance / Regulatory Isolation Boundary**: Legal regulations mandate that certain sensitive data (e.g. banking records) must reside in a geographically or physically isolated database cluster.
4. **Interface Stability**: The module's API contract has been 100% stable for at least 6 months with zero cross-module dependency churn.

---

## 5. Trade-offs and Risks

| Trade-off / Risk | Mitigation Strategy |
| :--- | :--- |
| **Monolith deployment coupling**: A bug in one module could delay a release of another. | Strong module unit & integration tests in CI. Modular directory structure keeps code review diffs localized. |
| **Database shared resource contention**: A heavy analytical query could slow down OLTP checkout queries. | Route analytical queries to dedicated read-replicas. Analytical summaries are pre-computed asynchronously into dedicated rollup tables. |
| **Developer discipline required**: Engineers might be tempted to bypass service boundaries and write raw cross-module queries. | Enforced architecture linting rules and code reviews prohibiting raw cross-schema imports. |

---

## 6. Rollback and Migration Plan
If a specific module must eventually be extracted into a standalone service:
1. Because the module already interacts exclusively via public DTOs and Medusa Workflows, its internal implementation can be replaced with an HTTP/gRPC remote client.
2. The module's dedicated database tables (which have zero foreign keys to core tables) can be cleanly migrated to a separate database instance using standard pg_dump.


---

## 7. Addendum: Audit Feedback & Enhanced Invariants (Post-Review Amendments)

Following the formal independent review by the Senior Principal Architect and Security Auditor, three mandatory architectural amendments have been codified into ADR-001:

### 1. Multi-Tenancy Enforcement via PostgreSQL Row-Level Security (RLS)
* **Invariant**: To prevent cross-tenant data leaks caused by application developer omission in custom queries, multi-tenancy is enforced at the database engine level via **PostgreSQL Row-Level Security (RLS)**.
* **Mechanism**: Every table containing merchant data carries a `tenant_id` column. When a database connection is checked out from the PgBouncer pool, the application sets the session configuration:
  `SET LOCAL app.current_tenant_id = :tenant_id;`
  An RLS policy enforces:
  `CREATE POLICY tenant_isolation_policy ON orders USING (tenant_id = current_setting('app.current_tenant_id'));`
  Even if an application-level SQL query forgets the `WHERE tenant_id = ...` clause, PostgreSQL physically blocks access to other tenants' data.

### 2. Transactional Outbox Pattern for Dual-Write Consistency
* **Invariant**: Eliminate the dual-write problem between PostgreSQL transactions and the Redis event bus.
* **Mechanism**: When an order, payment, or fulfillment state changes, an event record is written into an `outbox_events` table *within the exact same PostgreSQL database transaction*:
  `INSERT INTO outbox_events (id, topic, payload, created_at, status) VALUES (:id, 'order.placed', :payload, NOW(), 'pending');`
* An asynchronous background publisher daemon uses PostgreSQL Logical Decoding / LISTEN-NOTIFY to stream pending outbox events to Redis with guaranteed at-least-once delivery, ensuring events are never dropped if Redis is temporarily unreachable during checkout.

### 3. Read-Replica Segregation & Read-Your-Own-Writes Safety
* **Invariant**: Read replicas are strictly segregated to asynchronous analytical projections, merchant reporting, and cached public catalog browsing.
* **Rule**: All transactional shopper paths (cart updates, shipping selection, payment authorization, and checkout order confirmation) query the **Primary PostgreSQL Writer Node** exclusively, completely eliminating replication lag race conditions.
