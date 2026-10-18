# ADR-001: Architecture Topology — Modular Monolith vs Microservices for CommerceOS (Remediated)

**Document ID**: `ADR-001`  
**Status**: APPROVED (Remediated Architecture Baseline)  
**Date**: 2026-10-18  
**Author**: Principal Software Architect (CommerceOS Engineering)  
**Scope**: **Single-Store Self-Hosted Deployment per Client** (Dedicated database and runtime per merchant installation).  

---

## 1. Context and Problem Statement

CommerceOS is an e-commerce operating system designed for self-hosted merchant deployments in Saudi Arabia and the GCC market. Each client runs an isolated, self-hosted installation with its own dedicated PostgreSQL database, Redis instance, and Medusa backend.

The system combines:
- Core Commerce (Catalog, Pricing, Cart, Checkout, Order, Inventory, Customer, Payments, Fulfillment via Medusa v2).
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
  * High Network Overhead & Latency: Microservice network hops add latency, degrading checkout response times.
  * Violates Constitution Principle III & VI (premature distributed systems).

### Alternative B: Unstructured Traditional Monolith
* *Description*: A single codebase where all tables share foreign keys and code freely imports models across domains without boundaries.
* *Drawbacks*:
  * Tight coupling, impossible to maintain or refactor cleanly.
  * Schema migrations in one feature easily break unrelated domains.

### Alternative C: Medusa v2 Modular Monolith (CHOSEN)
* *Description*: A single deployable codebase running on Medusa v2, structured into strictly isolated **Domain Modules**. Modules communicate in-memory via service contracts and Medusa Workflows, with data decoupling enforced by **Module Links** and **Remote Query**. No cross-module database foreign keys. Background tasks execute via dedicated Medusa Worker processes sharing the codebase.

---

## 3. Decision

We decisively choose **Alternative C: Medusa v2 Modular Monolith**.

CommerceOS will be implemented as a unified modular monolith deployed on a per-merchant self-hosted basis. Modules will have distinct schema prefixes, strict public service interfaces, and zero direct foreign keys across boundaries.

For **Analytics** and **CRM**:
* They will start as **cohesive bounded-context modules within the modular monolith**, consuming internal domain events asynchronously via the Medusa Redis event bus.
* They will NOT be split into remote microservices prematurely.

---

## 4. Deep Architectural Analysis of the Core Dimensions

### 1. Module Independence & Bounded Contexts
* Each module (e.g. `src/modules/cms`, `src/modules/customizer`, `src/modules/loyalty`) lives in its own directory, defining its own data models, migrations, and service classes.
* A module can only access another module's capabilities through public service methods resolved via the Medusa container, or through Medusa Workflows. Direct database table joins across module boundaries are strictly prohibited.

### 2. Preventing Duplication of Medusa Core Features
* Medusa v2 native engines (Product, Pricing, Promotion, Cart, Order, Inventory, Payment, Fulfillment) are the sole authority for commerce operations.
* **Inventory Authority**: Stock levels and reservations are owned exclusively by Medusa's native `InventoryModule` (`ReservationItem`). Reservations occur automatically inside `completeCartWorkflow` upon order placement. No secondary shadow inventory in Redis or temporary cart TTL holds exist.
* Custom modules augment core entities via **Module Links** (`defineLink`) and inject business logic via **Workflow Steps**. No parallel pricing, cart, or order tables will ever be created.

### 3. PostgreSQL Transaction Integrity & Connection Pooling
* **ACID Guarantees**: Checkout operations (cart completion, payment authorization, inventory reservation, order placement) execute within a unified database transaction or coordinated Medusa workflow with compensation rollbacks.
* **Connection Pooling**: A centralized `PgBouncer` layer handles connection pooling between Node.js processes and PostgreSQL 17, preventing connection exhaustion under traffic spikes.
* **Safe Migrations**: Schema updates adhere strictly to the non-destructive Expand/Contract pattern.

### 4. Redis, BullMQ Workers & Asynchronous Failure Management
* **Process Separation**: In production, two distinct process modes can be deployed from the same image:
  1. *Web API Process* (`medusa start`): Handles HTTP requests, stateless, scaled horizontally.
  2. *Worker Process* (`medusa worker`): Pulls jobs from Redis streams / BullMQ queues, handles long-running tasks.
* **Idempotent Job Processing**: Every event handler records processed event IDs to guarantee that at-least-once message delivery never creates duplicate invoices, billing charges, or reward points.

### 5. Single-Store Security & Authorization Boundaries
* **Architecture Clarification**: CommerceOS is a single-store self-hosted installation per merchant. There is no multi-tenant database partitioning or `tenant_id` on Medusa core tables.
* **Backoffice Access Control & Auth Gap**: Authenticated via Medusa Admin Authentication (`@medusajs/auth`). Fine-grained Staff RBAC (role-based endpoint permissions) requires custom authorization middleware/extensions; protected endpoints enforce fail-closed authorization even during Redis outages.
* **Storefront Access Control**: Server-side object-level authorization (BOLA/IDOR prevention) verifies that customer queries match the authenticated session (`customer_id` check on all order/cart queries). Guest checkouts are secured via cryptographically signed tokens (HMAC).

### 6. Horizontal Scalability & Performance Objectives
* The stateless Web API tier scales horizontally behind a load balancer.
* Database reads are optimized via PostgreSQL indexes and Next.js ISR (Incremental Static Regeneration) on the CDN edge.
* Performance goals (e.g. responsive checkout latency) are target engineering heuristics to be empirically benchmarked during AG06 load tests.

### 7. Dependency & Semantic Versioning Management
* Dependencies are strictly locked in `package-lock.json`. Updates are managed via automated security audits (`npm audit`) and tested in CI before merging.
* Core Medusa packages are kept aligned on the exact minor/patch releases to prevent internal container resolution mismatches.

### 8. Storefront & Admin Integration Contracts
* **Storefront (Next.js)**: Interacts with the backend via REST Store API endpoints authenticated by a publishable API key, utilizing `@medusajs/js-sdk` branched from `medusajs/nextjs-starter-medusa`.
* **Admin Dashboard**: Custom modules inject UI Widgets, Custom Routes, and Setting Pages into the native Medusa Admin via standard React extension points, styling with `@medusajs/ui`.

### 9. Error Handling, Disaster Recovery & Zero-Downtime Rollbacks
* Medusa Workflows implement automatic compensation steps on failure (canceling authorized payments or refunding captured payments per official `completeCartWorkflow` semantics).
* Point-In-Time Recovery (PITR) is enabled on PostgreSQL via continuous WAL archiving.
* Zero-downtime rolling deployments are supported because all database migrations are backward-compatible.

### 10. Service Extraction Heuristics (When to Consider Splitting)
A bounded-context module (such as Analytics or CRM) will remain inside the modular monolith until objective operational indicators justify separation, such as:
1. **Severe Resource Contention**: Analytical processing or image rendering consistently starves core checkout operations despite separate worker processes.
2. **Team / Deployment Independence**: A dedicated engineering team requires an independent release pipeline that destabilizes core commerce deployments.
3. **Regulatory / Data Compliance Isolation**: Specific legal requirements mandate physically separate infrastructure.
4. **Interface Maturity**: The module's API contract has demonstrated sustained stability without cross-module churn.

---

## 5. Trade-offs and Mitigations

| Trade-off / Risk | Mitigation Strategy |
| :--- | :--- |
| **Monolith deployment coupling**: A bug in one module could delay a release of another. | Strong module unit & integration tests in CI. Modular directory structure keeps code review diffs localized. |
| **Database shared resource contention**: A heavy analytical query could slow down OLTP checkout queries. | Analytical summaries are pre-computed asynchronously into dedicated rollup tables or offloaded to read replicas. |
| **Developer discipline required**: Engineers might be tempted to bypass service boundaries and write raw cross-module queries. | Enforced architecture linting rules and code reviews prohibiting raw cross-schema imports. |
