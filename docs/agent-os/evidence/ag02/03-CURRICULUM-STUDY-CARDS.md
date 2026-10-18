# AG02 Engineering Curriculum Study Cards (E1 — E9) (Remediated)

**Audience**: Principal Engineering Review, Antigravity Autonomous Orchestrator  
**Reference Baseline**: `docs/agent-os/03-CURRICULUM.md` & `docs/agent-os/12-READING-LIST.md`  
**Architecture Scope**: **Single-Store Self-Hosted Deployment per Client**  
**Evaluation Standard**: Architectural literacy and conceptual rigor grounded in official documentation. (Empirical runtime behavior is deferred to practical drill stages AG04–AG07).

---

## E1: TypeScript Architecture & Domain-Driven Design (DDD)

### 1. Core Principles in Practical Application
* **Strict Compile-Time Invariants**: Configuration must enable `"strict": true`, `"noImplicitAny": true`, `"strictNullChecks": true`, and `"exactOptionalPropertyTypes": true`. Types model system states and reject invalid states at compile time.
* **Domain-Driven Design (DDD) Bounded Contexts**: Modules own their private domain models, entities, and services. Inter-module communication occurs strictly via explicit public Data Transfer Objects (DTOs) and service contracts. Direct database cross-table joins or importing another module's internal schema models is an architectural violation.
* **Pragmatic SOLID & Composition over Inheritance**: Avoid deep inheritance hierarchies. Compose specialized functions and injected dependencies. Program to interfaces and DTOs.
* **Type Narrowing & Nominal/Branded Typing**: Use Discriminated Unions for state machines (e.g. `OrderStatus = 'pending' | 'authorized' | 'captured' | 'failed'`). Use branded types for identifiers to prevent accidental transposition of `CustomerId` and `OrderId` strings.

### 2. Architectural Comparison: Correct Choice vs Counterexample
* **Correct Choice**:
  ```typescript
  // Branded Nominal Types preventing accidental ID mixing
  type Brand<K, T> = K & { readonly __brand: T };
  export type CustomerId = Brand<string, "CustomerId">;
  export type OrderId = Brand<string, "OrderId">;

  // Discriminated Union modeling explicit payment lifecycle states
  export type PaymentState =
    | { status: "requires_action"; clientSecret: string }
    | { status: "authorized"; authorizationId: string; expiresAt: Date }
    | { status: "captured"; transactionId: string; amount: number; capturedAt: Date }
    | { status: "failed"; errorCode: string; errorMessage: string };
  ```
* **Anti-Pattern (Counterexample)**:
  ```typescript
  // Sloppy primitive obsession and optional property soup
  export interface PaymentResponse {
    status: string; // Any random string
    clientSecret?: string;
    authorizationId?: any;
    transactionId?: string;
    amount?: number;
    error?: any; // Swallows type safety, allows impossible combinations (e.g. status='failed' with a transactionId)
  }
  ```

### 3. Operational & Security Pitfalls
* **TypeScript Erased at Runtime**: Relying solely on compile-time interfaces for external API requests or webhook payloads allows corrupted or malicious payloads into the system. Always validate inputs at the runtime boundary using schemas (e.g. `zod` or `@medusajs/framework` validation schemas).
* **`any` and Blind Type Assertions (`as TargetType`)**: Bypasses compiler protection, creating latent `TypeError: Cannot read properties of undefined` during production checkout.

### 4. Mandatory Agent Coding Invariants
* Never use `any`. Use `unknown` and narrow down with type guards or runtime validators.
* Never import private internal paths. Import only from the module's public entry point (`index.ts`).
* Enforce runtime schema validation for all external HTTP inputs, job queue payloads, and webhook payloads.

### 5. Official Versioned Citations
* TypeScript Handbook (v5.x): [TypeScript Strict Mode & Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) (Accessed: 2026-10-18).
* Martin Fowler: [Bounded Context](https://martinfowler.com/bliki/BoundedContext.html).

### 6. Evaluative Comprehension Question
* **Scenario**: A developer writes a function `calculateRefund(order: Order, amount: number)`. During high-concurrency processing, an engineer accidentally passes `calculateRefund(order, customerId as any)`. How does TypeScript's type branding solve this at compile time without any runtime overhead?
* **Answer**: By creating nominal branded types `type CurrencyAmount = Brand<number, "CurrencyAmount">`, the compiler rejects passing a string, raw float, or identifier into the amount parameter, catching the bug during static analysis before runtime execution.

---

## E2: Git & Reproducible Engineering

### 1. Core Principles in Practical Application
* **Hermetic & Deterministic Builds**: Re-running an install or test today must produce identical results as tomorrow. All dependencies must be pinned via exact lockfiles (`package-lock.json` or `uv.lock`). Zero floating semver ranges in lockfiles.
* **Isolated Workspaces via Git Worktrees**: Concurrent exploration or multi-agent execution must use dedicated `git worktree` instances. Never let parallel tasks write to the same branch or uncommitted working directory.
* **Atomic, Reversible Commits**: Every commit must be a self-contained, reviewable unit with passing tests. Never mix refactoring with business logic changes.
* **Strict History Integrity**: Force pushing (`git push --force`) to shared branches (`main`, `master`, staging) is strictly prohibited. Rollbacks must be executed via `git revert` to preserve transparent audit trails.

### 2. Architectural Comparison: Correct Choice vs Counterexample
* **Correct Choice**:
  * Using `npm ci` rather than `npm install` in CI/CD pipelines to guarantee byte-for-byte installation matching `package-lock.json`.
  * Using `git revert <commit-sha>` to undo an erroneous migration in production, creating an explicit forward-moving audit trail.
* **Anti-Pattern (Counterexample)**:
  * Running `npm install package-name` without checking lockfile diffs, accidentally updating 40 transitive dependencies with breaking changes.
  * Running `git reset --hard HEAD~1 && git push --force` on main, destroying history and desynchronizing developer workspaces.

### 3. Operational & Security Pitfalls
* **Lockfile Desynchronization**: If `package.json` is modified without updating `package-lock.json`, CI and local developer machines will run different dependency graphs, leading to "works on my machine" failures.
* **Secret Leaks in Git History**: Once committed, secrets remain in git object blobs even if removed in subsequent commits. Must use `.gitignore` and pre-commit secret scanners.

### 4. Mandatory Agent Coding Invariants
* Always verify `git status` before and after operations. Never leave untracked artifacts dangling.
* Run `npm ci` for automated dependency installations, never `npm install` in CI or headless environments.
* Use conventional commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`) with informative descriptions.

### 5. Official Versioned Citations
* Git Documentation: [Git Worktree Reference](https://git-scm.com/docs/git-worktree) (Accessed: 2026-10-18).
* npm Documentation: [npm ci Reference](https://docs.npmjs.com/cli/v10/commands/npm-ci) (Accessed: 2026-10-18).

### 6. Evaluative Comprehension Question
* **Scenario**: Two autonomous subagents are dispatched simultaneously. Agent A works on the CMS module, and Agent B works on the Loyalty module. If they work in the same working tree, what happens to git staging and dependency installation?
* **Answer**: They will cause git index lock contentions (`index.lock`), overwrite each other's unstaged files, and corrupt `node_modules` during concurrent installs. They must work in isolated `git worktree` branches.

---

## E3: Spec-Driven Requirements (Spec Kit v1.2.1)

### 1. Core Principles in Practical Application
* **Specification Precedes Implementation**: Code written without an approved, unambiguous specification is technical debt by definition.
* **The Spec Kit Pipeline**:
  `constitution` -> `specify` -> `clarify` -> `plan` -> `checklist` -> `tasks` -> `analyze` -> `converge`.
* **Inconsistency Analysis & Contradiction Traps**: Before writing code, cross-artifact analysis must verify that tasks do not contradict requirements, out-of-scope boundaries are respected, and constitutional invariants are upheld.
* **Bidirectional Traceability**: Every acceptance test must map to a specific Functional Requirement (`FR-xxx`), and every implementation task must be tied to a testable user story.

### 2. Architectural Comparison: Correct Choice vs Counterexample
* **Correct Choice**:
  * Writing a clear specification (`spec.md`) that explicitly states: "Out of scope: external Redis clusters; token bucket state must be stored in-memory." Running `speckit-analyze` to detect if an implementer wrote a task connecting to Redis, catching the discrepancy before any code is typed.
* **Anti-Pattern (Counterexample)**:
  * "Vibe coding": jumping straight to implementation based on a vague chat prompt, inventing architectural dependencies (like adding an unreviewed Redis or MongoDB database) that violate project constraints.

### 3. Operational & Security Pitfalls
* **Scope Creep / Architectural Drift**: Features expanding silently during development without architectural review, introducing unneeded third-party libraries and expanding the security attack surface.
* **Ignoring Constitutional Guardrails**: A task specifying insecure defaults (such as bypassing authentication for testing convenience) slipping into production because no cross-artifact compliance check was executed.

### 4. Mandatory Agent Coding Invariants
* Always run cross-artifact consistency checks (`speckit-analyze`) before proceeding to implementation.
* If a contradiction is detected (`INC-xxx`), mark the gate as BLOCKED; never implement contradictory tasks.
* Preserve `.specify/memory/constitution.md` as the supreme immutable law of the project.

### 5. Official Versioned Citations
* GitHub Spec Kit: [Spec Kit Documentation v1.2.1](https://github.github.com/spec-kit/) (Release: `9dca9bf`, Accessed: 2026-10-18).
* CommerceOS Constitution: `.specify/memory/constitution.md` (v2.0.0).

### 6. Evaluative Comprehension Question
* **Scenario**: A business requirement states "All invoices must be delivered to customers within 10 seconds of payment." A task is drafted: "T005: Synchronously call external tax authority API in the checkout HTTP request thread." What contradiction does `speckit-analyze` identify?
* **Answer**: It flags a latency and reliability contradiction: synchronous external network calls in the checkout thread jeopardize the 10-second SLA and violate resilience invariants. The task must be revised to an asynchronous background job triggered via event bus with retries.

---

## E4: Test-Driven Development (TDD) & Multi-Tier Verification

### 1. Core Principles in Practical Application
* **The Iron Law of TDD**: Write the failing behavior test FIRST (RED) -> verify it fails for the EXACT expected reason -> write the minimal code to pass (GREEN) -> REFACTOR for clean architecture -> run full regression.
* **Test Isolation & Hermetic Environments**: Unit tests must have zero shared state. Integration tests must use isolated databases (or transaction rollbacks per test).
* **Multi-Tier Testing Pyramid**:
  1. *Unit Tests*: Business logic, calculations, pure utility functions (Fast, in-memory).
  2. *Integration Tests*: Medusa workflows, database queries, module links using `@medusajs/test-utils` with real PostgreSQL.
  3. *End-to-End (E2E) Tests*: Playwright browser journeys verifying user interactions, accessibility, and visual correctness.
* **Negative & Mutation Testing**: A test suite that only tests the happy path provides false confidence. Tests must prove that invalid inputs, expired tokens, negative amounts, and unauthorized access are decisively rejected.

### 2. Architectural Comparison: Correct Choice vs Counterexample
* **Correct Choice**:
  * Writing an integration test that creates an order, attempts to capture payment twice simultaneously, and asserts that exactly one capture succeeds while the second returns an idempotency conflict.
* **Anti-Pattern (Counterexample)**:
  * Mocking out the entire database and payment gateway in a unit test so thoroughly that the test passes, while in production the actual PostgreSQL query fails due to a missing table index or transaction lock timeout.

### 3. Operational & Security Pitfalls
* **Mock-Only Hallucinations**: Mocks passing while real database schema migrations fail. Tests must run against a real PostgreSQL instance to validate constraints, foreign keys, and indexes.
* **Flaky Tests**: Tests dependent on `setTimeout` or network race conditions causing intermittent CI failures and eroding developer trust in the test suite.

### 4. Mandatory Agent Coding Invariants
* Always observe the test fail first (RED) before writing implementation code.
* Always include negative test cases (malformed input, expired timestamps, boundary conditions).
* Never bypass or disable failing tests with `.skip` or `// @ts-ignore`.

### 5. Official Versioned Citations
* Superpowers TDD Skill: [Superpowers v7.0.0 TDD](https://github.com/obra/superpowers/blob/v7.0.0/skills/test-driven-development/SKILL.md).
* Medusa Documentation: [Testing Tools with @medusajs/test-utils](https://docs.medusajs.com/learn/debugging-and-testing/testing-tools).
* Playwright Documentation: [Playwright Best Practices](https://playwright.dev/docs/best-practices).

### 6. Evaluative Comprehension Question
* **Scenario**: An agent claims 100% test pass on a discount code calculation feature. However, upon code review, the test suite only checked `calculateDiscount(100, 10%) = 10`. What critical test cases are missing?
* **Answer**: Missing boundary and negative cases:
  1. Discount greater than 100% (prevent negative cart total).
  2. Expired promotion dates.
  3. Usage limit exhausted (concurrency test).
  4. Currency mismatch (applying a USD coupon to a SAR cart).
  5. Negative cart subtotal.

---

## E5: Systematic Debugging & Root Cause Analysis

### 1. Core Principles in Practical Application
* **The 4-Phase Scientific Debugging Method**:
  1. *Phase 1: Precise Reproduction*: Reproduce the issue reliably with a deterministic minimal test case.
  2. *Phase 2: Root Cause Isolation*: Formulate a single, falsifiable hypothesis. Inspect logs, traces, and state transitions to verify or disprove it.
  3. *Phase 3: Minimal, Surgical Fix*: Implement only the changes necessary to fix the root cause. Avoid broad, speculative refactoring.
  4. *Phase 4: Regression Verification*: Re-run reproduction test (verify GREEN), followed by full suite regression testing.
* **Layered Fault Localization**: When a service fails, systematically decouple layers:
  * *Network/DNS*: Is the port listening? (`netstat`, `Test-NetConnection`)
  * *Infrastructure*: Is PostgreSQL or Redis running and accepting connections?
  * *Application Layer*: Is the configuration valid? Are credentials matching?
  * *Domain/Business Logic*: Is a constraint or validation error being thrown?
* **3-Strike Escalation Rule**: If 3 successive fix attempts fail, STOP speculating. Escalate to fundamental architecture review.

### 2. Architectural Comparison: Correct Choice vs Counterexample
* **Correct Choice**:
  * An API returns `500 Internal Server Error`. The engineer inspects structured application logs, extracts the correlation ID, finds `ECONNREFUSED 127.0.0.1:5432`, verifies PostgreSQL container status with `docker ps`, identifies an exited container due to disk space exhaustion, resolves disk space, restarts container, and verifies health check passes.
* **Anti-Pattern (Counterexample)**:
  * The API returns 500. The developer randomly updates npm packages, increases HTTP timeouts from 5s to 60s, adds arbitrary `console.log` statements, and guesses that rewriting the query will fix it.

### 3. Operational & Security Pitfalls
* **Symptom Masking**: Catching exceptions and silently returning `null` or `{ success: false }` without logging the stack trace. This turns detectable errors into silent data corruption.
* **Timeout Creep**: Increasing timeouts to "fix" slow queries or deadlocks instead of analyzing query plans (`EXPLAIN ANALYZE`) or resolving lock contention.

### 4. Mandatory Agent Coding Invariants
* Always capture exact error messages, exit codes, and stack traces before touching code.
* Change one variable at a time when diagnosing an issue.
* Never commit speculative "try this" code to the repository.

### 5. Official Versioned Citations
* Superpowers Systematic Debugging: [Superpowers v7.0.0 Systematic Debugging](https://github.com/obra/superpowers/blob/v7.0.0/skills/systematic-debugging/SKILL.md).
* Node.js Diagnostics Guide: [Node.js Diagnostic Tools](https://nodejs.org/en/learn/diagnostics).

### 6. Evaluative Comprehension Question
* **Scenario**: A checkout request fails with HTTP 403 Forbidden. Is this an authentication error or an authorization error, and what diagnostic steps should be taken?
* **Answer**: HTTP 403 Forbidden is an **authorization** error (the client's identity is authenticated, but they lack permission to access the requested resource). Diagnostic steps:
  1. Inspect the decoded JWT / session claims for `customer_id` and role permissions.
  2. Verify if the requested `cart_id` or `order_id` belongs to another customer (BOLA check).
  3. Inspect server access logs to check if middleware rejected a CSRF token or publishable API key scope.

---

## E6: Application Security & OWASP ASVS

### 1. Core Principles in Practical Application
* **Server-Side Enforcement Over Client-Side Hiding**: Security rules and object permissions must be verified on the server for every HTTP route. Hiding buttons in the UI is zero security.
* **Broken Object-Level Authorization (BOLA / IDOR Prevention)**: Never allow `GET /store/orders/:id` to fetch an order purely by its primary key ID into memory before checking ownership. The database query must enforce: `orderService.listOrders({ id: orderId, customer_id: authenticatedCustomerId })`.
* **Guest Checkout Security**: Support guest orders securely by requiring a cryptographically signed token (HMAC with order ID and secret) for post-purchase tracking, preventing guest order enumeration.
* **Server-Side Request Forgery (SSRF) Defense**: When downloading external assets (e.g. merchant image URLs in Page Builder or webhooks in Payment/Fulfillment), strictly validate URLs against an IP allowlist, block RFC 1918 private IP ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), and block cloud metadata IP (`169.254.169.254`) at the socket connection level.
* **Input Sanitization & Output Encoding**: Prevent Stored XSS in CMS page builders and product customizers by sanitizing raw HTML using robust parsers (`DOMPurify`) and escaping dynamic variables in templates.

### 2. Architectural Comparison: Correct Choice vs Counterexample
* **Correct Choice**:
  ```typescript
  // Secure: Database-level query scoping preventing BOLA
  export async function getCustomerOrder(authenticatedCustomerId: string, orderId: string) {
    const [order] = await orderService.listOrders({
      id: orderId,
      customer_id: authenticatedCustomerId,
    }, { select: ["id", "total", "items", "shipping_address"] });
    if (!order) {
      throw new MedusaError(MedusaError.Types.NOT_FOUND, "Order not found");
    }
    return order;
  }
  ```
* **Anti-Pattern (Counterexample)**:
  ```typescript
  // Insecure: In-memory filtering after full entity retrieval
  export async function getCustomerOrder(authenticatedCustomerId: string, orderId: string) {
    const order = await orderService.retrieve(orderId); // PII loaded into memory before authorization!
    if (order.customer_id !== authenticatedCustomerId) {
      throw new MedusaError(MedusaError.Types.NOT_FOUND, "Order not found");
    }
    return order;
  }
  ```

### 3. Operational & Security Pitfalls
* **Leaking Secrets via Logs / Transcripts**: Logging full request headers (containing Authorization tokens, session cookies) or request bodies (containing passwords, credit card numbers).
* **Mass Assignment Vulnerabilities**: Blindly spreading request bodies into database update queries (`orderService.update(id, req.body)`), allowing attackers to overwrite fields like `role = 'admin'` or `is_paid = true`.

### 4. Mandatory Agent Coding Invariants
* Every data retrieval endpoint must verify customer ownership at the database query level.
* Never commit real API keys, passwords, or credentials. Use sanitized mocks in tests.
* Parameterize all SQL queries. Never concatenate raw strings into database queries.

### 5. Official Versioned Citations
* OWASP ASVS: [Application Security Verification Standard v4.0.3 Stable / v5.0 Draft](https://owasp.org/www-project-application-security-verification-standard/) (Accessed: 2026-10-18).
* OWASP API Security: [API Security Top 10 (2023)](https://owasp.org/API-Security/).

### 6. Evaluative Comprehension Question
* **Scenario**: A Page Builder feature allows merchants to supply an image URL to preview in the admin dashboard. An attacker supplies `http://169.254.169.254/latest/meta-data/iam/security-credentials/`. What attack is this, and how is it mitigated?
* **Answer**: This is a **Server-Side Request Forgery (SSRF)** attack targeting the cloud metadata service to steal IAM role credentials. Mitigation:
  1. Do not fetch external images server-side; let the client's browser render them.
  2. If server-side fetching is mandatory (e.g. for resizing/optimizing), resolve the domain's DNS, verify the resolved IP is not in private/loopback/link-local ranges (`169.254.x.x`), disable HTTP redirects, and enforce strict timeouts.

---

## E7: Site Reliability Engineering (SRE) & Performance Heuristics

### 1. Core Principles in Practical Application
* **SLOs and Error Budgets**: Define clear Service Level Indicators (SLIs) and Objectives (SLOs) (e.g. checkout API responsiveness under normal operating conditions).
* **Database Query Performance & Indexing**: Use PostgreSQL `EXPLAIN (ANALYZE, BUFFERS)` to detect sequential scans (`Seq Scan`) on large tables, index bloat, and missing composite indexes.
* **Connection Pooling**: Node.js applications open multiple connections. Use a connection pooler (`PgBouncer`) to avoid exhausting PostgreSQL max connections under load spikes.
* **Cascading Failure Prevention**: Implement circuit breakers, request timeouts, and bulkhead isolation. When an external payment gateway experiences latency, fail fast rather than exhausting all Node.js web server worker threads.

### 2. Architectural Comparison: Correct Choice vs Counterexample
* **Correct Choice**:
  * Offloading non-critical side effects (e.g. email notifications, asynchronous reporting projections) to background worker queues (`medusa worker` via Redis/BullMQ), keeping the checkout HTTP response fast and focused.
* **Anti-Pattern (Counterexample)**:
  * Generating PDFs, calling 3 external REST APIs, and running un-indexed heavy analytical aggregation queries synchronously inside the `POST /store/carts/:id/complete` HTTP request handler.

### 3. Operational & Security Pitfalls
* **Unbounded Concurrency**: Allowing an unlimited number of concurrent background jobs to fire, overwhelming the database connection pool.
* **Memory Leaks in Node.js Event Loop**: Accumulating event listeners or caching unbounded objects in global memory variables, leading to heap out-of-memory (OOM) crashes under sustained traffic.

### 4. Mandatory Agent Coding Invariants
* Measure execution duration for all critical database transactions and external API calls.
* Add database indexes to any foreign key or column frequently used in `WHERE`, `ORDER BY`, or `JOIN` clauses.
* Offload non-critical side effects to background workers.

### 5. Official Versioned Citations
* Google SRE Book: [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) (Accessed: 2026-10-18).
* PostgreSQL 17 Docs: [Using EXPLAIN](https://www.postgresql.org/docs/17/using-explain.html).

### 6. Evaluative Comprehension Question
* **Scenario**: During heavy traffic, the database CPU spikes to 100%, and connection timeout errors occur. An `EXPLAIN ANALYZE` on the cart query reveals a `Seq Scan on line_item` with `Filter: (cart_id = $1)`. What is the root cause and remedy?
* **Answer**: The root cause is a missing index on `line_item.cart_id`, forcing PostgreSQL to scan the entire table for every cart fetch. Remedy: Create a B-tree index `CREATE INDEX idx_line_item_cart_id ON line_item(cart_id);`, reducing query complexity from $O(N)$ to $O(\log N)$.

---

## E8: Medusa v2 Architecture & Extension Mastery

### 1. Core Principles in Practical Application
* **The Medusa v2 Architecture**: Built around isolated **Commerce Modules**, **Workflows**, **Module Links**, and **Remote Query**.
* **Workflows with Compensation**: Business transactions spanning multiple steps are orchestrated via `createWorkflow` and `createStep`. Mutating steps declare an explicit compensation function that rolls back changes if subsequent steps fail.
* **Native Inventory Authority**: Stock levels and reservations are owned exclusively by Medusa's `InventoryModule` (`ReservationItem`). Reservations are placed during checkout and converted to stock deduction upon fulfillment.
* **Official Complete Cart Semantics**: Medusa's official `completeCartWorkflow` validates the cart, reserves inventory, and authorizes payment sessions. On failure, it can cancel authorization OR issue a refund if payment was captured.
* **Module Links & Remote Query**: Connect custom models to core models (e.g. linking `Product` to `CmsBlock`) using `defineLink`. Fetch connected data graphs cleanly via `RemoteQuery` without touching database schemas directly.

### 2. Architectural Comparison: Correct Choice vs Counterexample
* **Correct Choice**:
  ```typescript
  import { createStep, createWorkflow, StepResponse } from "@medusajs/framework/workflows-sdk";

  // Mutating step with explicit compensation contract
  export const reserveLoyaltyPointsStep = createStep(
    "reserve-loyalty-points",
    async ({ customerId, points }: { customerId: string; points: number }, { container }) => {
      const loyaltyService = container.resolve("loyaltyModuleService");
      const reservation = await loyaltyService.reservePoints(customerId, points);
      // Return output AND explicit rollback payload
      return new StepResponse(reservation, { reservationId: reservation.id });
    },
    async (compensationData, { container }) => {
      if (!compensationData) return;
      const loyaltyService = container.resolve("loyaltyModuleService");
      await loyaltyService.cancelReservation(compensationData.reservationId);
    }
  );
  ```
* **Anti-Pattern (Counterexample)**:
  * Manually calling mutating service methods inside an API route handler without a workflow. When payment fails 3 lines later, customer data is left corrupted because no compensation logic was registered.

### 3. Operational & Security Pitfalls
* **Direct Database Manipulation**: Bypassing Medusa Module services and writing raw SQL updates to core Medusa tables. This corrupts internal caches, bypasses event emission, and breaks future framework upgrades.
* **Inventing Non-Existent APIs**: Guessing Medusa v1 methods inside a Medusa v2 project. Always consult official Medusa v2 API references.

### 4. Mandatory Agent Coding Invariants
* Always define compensation logic for mutating steps in Medusa Workflows.
* Use `RemoteQuery` to query across module boundaries.
* Never fork or edit files within the `@medusajs/*` node_modules packages.

### 5. Official Versioned Citations
* Medusa Documentation: [Medusa Workflows](https://docs.medusajs.com/learn/fundamentals/workflows) (Accessed: 2026-10-18).
* Medusa Documentation: [Inventory Reservations Lifecycle](https://docs.medusajs.com/resources/commerce-modules/inventory/reservations-lifecycle) (Accessed: 2026-10-18).
* Medusa Documentation: [Checkout Complete Cart](https://docs.medusajs.com/resources/storefront-development/checkout/complete-cart) (Accessed: 2026-10-18).

### 6. Evaluative Comprehension Question
* **Scenario**: You need to link a custom `Review` model to Medusa's native `Product` model. How should this be implemented in Medusa v2 without adding a foreign key to the native `product` table?
* **Answer**:
  1. Define a custom module `ReviewModule` with a `Review` data model.
  2. In `src/links/product-review.ts`, use `defineLink` to establish a link between `ProductModule.linkable.product` and `ReviewModule.linkable.review`.
  3. Query products and their reviews together using `container.resolve("remoteQuery")`.

---

## E9: Extension Lifecycle & Operational Resilience

### 1. Core Principles in Practical Application
* **Modular Monolith Lifecycle**: Single deployable modular monolith on a per-merchant self-hosted basis. Modules communicate via internal contracts so future extraction is possible without rewrites.
* **Safe Migrations & Zero-Downtime Rollbacks**: All schema migrations follow the **Expand/Contract pattern**:
  1. *Expand*: Add new nullable column or table. Deploy code that writes to both old and new columns.
  2. *Backfill*: Migrate existing historical data in chunked batches.
  3. *Contract*: Deploy code that reads exclusively from new column. Drop old column in a subsequent release.
* **Idempotency in Workers & Subscribers**: Event buses deliver messages with *at-least-once* semantics. Worker subscribers must record processed event IDs (`message_id` or `idempotency_key`) to prevent duplicate operations (e.g. charging a card twice or issuing duplicate invoices).
* **Disaster Recovery & Point-In-Time Recovery (PITR)**: Production databases must have continuous Write-Ahead Log (WAL) archiving to allow restoring to any specific second before a disaster occurred.

### 2. Architectural Comparison: Correct Choice vs Counterexample
* **Correct Choice**:
  * Adding a column: Migration 1 adds `address_line_2` as nullable. App deploys cleanly without breaking active queries. In next release, field is utilized.
* **Anti-Pattern (Counterexample)**:
  * Deploying a migration that renames a column `customer_name` to `full_name` in a live production table. The active web application instantly crashes on all customer profile reads because it still queries `customer_name`.

### 3. Operational & Security Pitfalls
* **Destructive Migrations Without Rollback Plans**: Running `DROP TABLE` or `ALTER COLUMN NOT NULL` without a tested backward-compatible migration plan.
* **Plugin Deletion Data Loss**: Uninstalling a plugin whose database tables contain historical financial records. Plugins must distinguish between *disabling feature logic* vs *purging historical database tables*.

### 4. Mandatory Agent Coding Invariants
* All database migrations must be non-destructive and backward compatible with running application code.
* Event handlers and background workers must be strictly idempotent.
* Every architectural decision must be recorded in an Architecture Decision Record (ADR).

### 5. Official Versioned Citations
* Martin Fowler: [Evolutionary Database Design & Expand/Contract](https://martinfowler.com/articles/evodb.html).
* PostgreSQL 17 Docs: [Continuous Archiving & PITR](https://www.postgresql.org/docs/17/continuous-archiving.html).

### 6. Evaluative Comprehension Question
* **Scenario**: A background worker receives an event to generate a tax invoice. Due to a network blip, the worker crashes after saving the invoice but before acknowledging the message. The event is redelivered 5 seconds later. How does idempotency protect the merchant?
* **Answer**: The worker checks the database for an existing invoice linked to `order_id` in a database transaction (`SELECT id FROM invoices WHERE order_id = $1`). Because an invoice already exists, the worker safely skips regeneration, acknowledges the message, and exits, preventing duplicate sequential invoice numbers.
