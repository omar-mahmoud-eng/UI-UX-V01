# AG02 Engineering Competency Exam: Architectural Scenarios & Remediation Analysis

**Project**: CommerceOS (`UI-UX-V01`)  
**Architecture Scope**: **Single-Store Self-Hosted Deployment per Client**  
**Evaluation Standard**: Cross-Domain Engineering Competency (E1–E9)  
**Status**: `PROPOSED ARCHITECTURAL DESIGNS — UNVERIFIED AT RUNTIME`  
*(In accordance with AG02 invariants, no live Medusa application code has been executed. All solutions represent design specifications subject to empirical verification in stages AG04–AG07).*

---

## Part I: Remediated Core Scenarios

### Scenario 1 (TRAP 1): Broken Object-Level Authorization (BOLA/IDOR) in Order Retrieval

#### 1. Problem Description
A junior engineer implemented an API endpoint for invoice viewing:
```typescript
// Route: GET /store/customers/invoices/:orderId
export async function GET(req: MedusaRequest, res: MedusaResponse) {
  const { orderId } = req.params;
  const orderService = req.scope.resolve("orderModuleService");
  const order = await orderService.retrieveOrder(orderId);
  return res.json({ invoice: order });
}
```
An authenticated customer alters the `orderId` parameter to another customer's ID and downloads unauthorized PII, items, and address records.

#### 2. Proposed Architectural Design (Database Query Scoping)
1. **Query-Level Scoping**: Avoid retrieving the entity into memory before authorization. Enforce ownership at the database query level:
   ```typescript
   export async function GET(req: MedusaRequest, res: MedusaResponse) {
     const customerId = req.auth_context?.actor_id;
     const { orderId } = req.params;
     const orderService = req.scope.resolve("orderModuleService");

     // 1. Authenticated Customer Path
     if (customerId) {
       const [order] = await orderService.listOrders({
         id: orderId,
         customer_id: customerId,
       }, { select: ["id", "customer_id", "total", "items", "shipping_address"] });
       
       if (!order) {
         throw new MedusaError(MedusaError.Types.NOT_FOUND, "Order not found");
       }
       return res.json({ invoice: order });
     }

     // 2. Guest Checkout Path: Require cryptographically signed HMAC token
     const guestToken = req.headers["x-guest-order-token"] as string;
     if (guestToken && verifyGuestOrderHmac(orderId, guestToken)) {
       const [order] = await orderService.listOrders({
         id: orderId,
         customer_id: null, // Strictly verify order has no registered customer owner
       });
       if (order) return res.json({ invoice: order });
     }

     throw new MedusaError(MedusaError.Types.NOT_FOUND, "Order not found");
   }
   ```
2. **Staff / Admin Context**: CSR representatives use the authenticated Medusa Admin API (`/admin/orders/:id`) governed by native staff RBAC, keeping customer storefront routes strictly scoped.

---

### Scenario 2 (TRAP 2): Distributed Transaction & Payment Failure in Checkout

#### 1. Problem Description
During cart completion, a payment is authorized or captured, but a database timeout occurs before the order is finalized. How does CommerceOS ensure consistency without split-brain records?

#### 2. Proposed Architectural Design (Medusa `completeCartWorkflow` Alignment)
1. **Adherence to Native Workflow**:
   * CommerceOS utilizes Medusa v2's official `completeCartWorkflow` (`https://docs.medusajs.com/resources/storefront-development/checkout/complete-cart`).
   * The workflow coordinates: Cart validation $\rightarrow$ Inventory Reservation $\rightarrow$ Payment Authorization $\rightarrow$ Order Creation $\rightarrow$ Cart Deactivation.
2. **Compensation Mechanics**:
   * If order creation fails after payment authorization: Medusa's workflow compensation calls `paymentProvider.cancelPayment()` to release the authorization hold.
   * If payment was already captured by an instant-capture provider: Medusa invokes `paymentProvider.refundPayment()` to return funds to the customer.
3. **Handling Asynchronous Payment & 3DS**:
   * In Saudi retail, Mada 3D Secure authentication is asynchronous. The payment session remains in `requires_action` while the shopper completes SMS OTP verification.
   * Order completion is triggered via either customer redirect or asynchronous gateway webhook.
   * **Webhook vs Workflow Coordination**: Distributed locks (`pg_advisory_xact_lock` on `cart_id`) ensure that a webhook and a customer redirect cannot concurrently create duplicate orders.

---

### Scenario 3: Modifying Medusa Core Tables (Anti-Pattern)

#### 1. Problem Description
A developer proposes `ALTER TABLE product_variant ADD COLUMN custom_message VARCHAR(255);` to support cake messages.

#### 2. Proposed Architectural Design
* **Rejection**: Violates Constitution Principle III (no core forks/edits). Direct core table modifications break Medusa migrations during framework updates.
* **Medusa v2 Solution**:
  1. Store product personalization rules in a dedicated module (`src/modules/product-personalization`) linked via `defineLink`.
  2. Store the customer's dynamic cake message inside `cart_line_item.metadata.personalization = { text: "Happy Birthday" }`, which natively transfers to order line item metadata upon cart completion.

---

## Part II: Deep-Dive Analysis of the 5 Security & Operational Findings

Below is the rigorous evaluation of the 5 critical findings identified during audit, structured across the 6 mandatory dimensions:

---

### Finding 1: Server-Side Request Forgery (SSRF) in Image Previews

1. **Problem (Verified Vulnerability)**:
   A naive URL validation function resolves DNS, checks the IP, and then calls `fetch(url)`. This is vulnerable to:
   * **DNS Rebinding TOCTOU**: The domain's DNS TTL expires immediately, and the second DNS lookup during `fetch` resolves to an internal IP (`169.254.169.254` or `127.0.0.1`).
   * **HTTP Redirect Bypass**: The target server responds with `HTTP 302` pointing to an internal service, which standard HTTP clients follow automatically.
2. **Proposed Architectural Design**:
   * **Preferred Strategy**: Offload uploads entirely to the client browser via pre-signed direct-to-S3/GCS URLs. The server never fetches arbitrary external URLs.
   * **Fallback Server-Side Fetching**: If server-side fetching is mandatory (e.g. Sharp thumbnailing), use socket-level connection pinning via a custom `undici` dispatcher:
     * Hook into the socket connection creation (`connect.lookup`).
     * Block all private IPv4/IPv6 ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `127.0.0.0/8`, `169.254.0.0/16`, `::1`, `fc00::/7`, `fe80::/10`).
     * Set `maxRedirections: 0` to disallow following HTTP 301/302 redirects.
3. **Limitations & Risks**:
   * Custom socket dispatchers require low-level maintenance across Node.js runtime upgrades.
   * Multi-homed domains with both public and private IPs can still present edge cases if IPv6 fallback is improperly configured.
4. **Official Sources**:
   * Node.js Undici Documentation: [Custom Dispatchers & Connect Options](https://undici.nodejs.org/).
   * OWASP: [Server-Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html).
5. **Required Tests Before Execution**:
   * Automated negative tests against mock DNS rebinding servers.
   * Tests verifying that HTTP 301/302 redirects to `127.0.0.1` and `169.254.169.254` are rejected immediately.
6. **What Remains Unproven**:
   * The custom dispatcher has not been compiled or benchmarked against high-concurrency image rendering under live load.

---

### Finding 2: Inventory Concurrency & Stock Authority

1. **Problem (Verified Architecture Scope Conflict)**:
   The previous proposal introduced an atomic Redis Lua `DECR` script to manage stock balances.
   * **Scope Violation**: This created a "shadow inventory authority" in Redis, violating Constitution Principle III.
   * **Operational Defect**: If a customer abandoned checkout or payment was declined, stock in Redis was permanently lost unless complex, fragile TTL reclamation logic was maintained.
2. **Proposed Architectural Design**:
   * **Single Source of Truth**: Medusa v2 native `InventoryModule` is the **sole business authority** for stock.
   * **Native Reservation Lifecycle**: Stock reservations (`ReservationItem`) are created automatically inside Medusa's native `completeCartWorkflow` upon order placement. Uncompleted carts hold no reservations and have no TTL holds.
   * **Separation of Rate Limiting vs Stock**: If flash sales require traffic throttling, implement a **generic HTTP Admission Controller** in Redis (rate limiting incoming requests per IP/user), completely decoupled from inventory logic.
3. **Limitations & Risks**:
   * High database lock contention can still occur on PostgreSQL if thousands of concurrent requests attempt to reserve the same inventory item simultaneously.
4. **Official Sources**:
   * Medusa Documentation: [Inventory Reservations Lifecycle](https://docs.medusajs.com/resources/commerce-modules/inventory/reservations-lifecycle).
   * Medusa Documentation: [Complete Cart Workflow](https://docs.medusajs.com/resources/storefront-development/checkout/complete-cart).
5. **Required Tests Before Execution**:
   * Concurrent checkout stress tests simulating 50 simultaneous shoppers purchasing the last 5 inventory units.
   * Verification that abandoned checkouts automatically release Medusa reservations without stock loss.
6. **What Remains Unproven**:
   * Database throughput and lock wait times under PostgreSQL with PgBouncer under 1,000+ simultaneous reservation requests.

---

### Finding 3: Saudi ZATCA Phase 2 E-Invoicing & Hash Chain Integrity

1. **Problem (Verified Regulatory Invariant)**:
   The previous proposal acquired an advisory lock on `orderId` during background worker processing.
   * **Regulatory Failure**: ZATCA Phase 2 mandates that all tax invoices from an EGS device have an unbroken sequential counter (`ICV`: 1, 2, 3...) and a cryptographic hash chain ($\text{PIH} = \text{SHA256}(\text{Invoice}_{N-1})$). Locking per `orderId` allows concurrent workers to process orders in parallel, reading stale PIHs and generating broken hash chains.
2. **Proposed Architectural Design**:
   * **Sequential EGS Pipeline**: Invoice generation must be serialized per Cryptographic Stamp ID (`egs_id`) using a dedicated BullMQ queue (`concurrency: 1`).
   * **Atomic Database Sequence**: Within a serial transaction, fetch and lock the last invoice state:
     ```sql
     SELECT id, last_icv, last_hash FROM zatca_devices WHERE id = :egs_id FOR UPDATE;
     ```
   * **Durable Error Handling**: If ZATCA rejects the invoice or a network failure occurs, the job must throw so BullMQ pauses the queue, preventing subsequent invoices from being generated with an invalid prior hash.
3. **Limitations & Risks**:
   * Serializing invoice generation per EGS device introduces a throughput ceiling ($\sim 20\text{--}50$ invoices/second per device). For high-volume merchants, multiple EGS devices must be registered with ZATCA.
4. **Official Sources**:
   * ZATCA Portal: [ZATCA E-Invoicing Phase 2 Technical Specifications](https://zatca.gov.sa/).
5. **Required Tests Before Execution**:
   * Integration tests verifying sequential hash continuity across 100 simulated invoices.
   * Negative tests injecting a worker crash mid-hash generation and proving recovery without chain corruption.
6. **What Remains Unproven**:
   * **Unverified Regulatory Status**: This design has NOT been tested in ZATCA's sandbox, nor certified with an official cryptographic stamp (CSID).

---

### Finding 4: Customer Session Invalidation & Stale JWT Handling

1. **Problem (Verified Operational Defect)**:
   Stateless JWTs cannot be revoked immediately upon password reset without a revocation check. However, querying Redis on every request introduces a single point of failure (SPOF), and a Redis cache-miss bug (`Number(null) === 0`) can inadvertently lock out legitimate users.
2. **Proposed Architectural Design**:
   * Store `token_version` in customer `metadata.token_version` (or a dedicated custom auth extension table).
   * Embed `token_version` in the JWT payload.
   * Check token version against cached Redis state. **Crucial Fix on Cache Miss**:
     ```typescript
     let cachedVersion = await redis.get(`customer:${customerId}:token_version`);
     if (cachedVersion === null) {
       // Cache miss: Fallback to PostgreSQL customer record
       const customer = await customerService.retrieve(customerId, { select: ["id", "metadata"] });
       const dbVersion = Number(customer?.metadata?.token_version ?? 0);
       await redis.setex(`customer:${customerId}:token_version`, 3600, String(dbVersion));
       cachedVersion = String(dbVersion);
     }
     if (decoded.token_version !== Number(cachedVersion)) {
       throw new MedusaError(MedusaError.Types.UNAUTHORIZED, "Session expired or revoked.");
     }
     ```
3. **Limitations & Risks**:
   * Adds an asynchronous Redis lookup to authenticated customer routes.
4. **Official Sources**:
   * OWASP: [JSON Web Token Cheat Sheet for Token Revocation](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html).
5. **Required Tests Before Execution**:
   * Unit tests verifying that password reset increments `token_version` and rejects previously issued tokens.
   * Tests verifying that Redis eviction does not cause false authentication rejections.
6. **What Remains Unproven**:
   * Memory overhead and latency impact of Redis version checks under sustained request volume.

---

### Finding 5: Transactional Outbox Pattern & Event Reliability

1. **Problem (Verified Dual-Write Vulnerability)**:
   In distributed architectures, writing an order to PostgreSQL while publishing an event to Redis creates a dual-write failure mode: if the database commits but Redis is unreachable, the event is lost.
2. **Proposed Architectural Design**:
   * Reconcile with Medusa native event bus: Medusa v2 already manages internal event dispatching.
   * For critical external integrations (e.g. ZATCA, ERP synchronization), record domain events in an `outbox_events` table within the same PostgreSQL transaction.
   * A reliable background publisher polls or listens to outbox events and dispatches them with at-least-once delivery guarantees.
3. **Limitations & Risks**:
   * Outbox tables accumulate records and require automated table partitioning or cleanup jobs.
   * Consumers must implement strict idempotency to handle potential duplicate event deliveries.
4. **Official Sources**:
   * Martin Kleppmann: [Designing Data-Intensive Applications (Reliable Message Delivery)](https://dataintensive.net/).
5. **Required Tests Before Execution**:
   * Tests simulating Redis connection drop during order placement, verifying that outbox events are safely persisted and dispatched upon Redis reconnection.
6. **What Remains Unproven**:
   * Performance overhead of outbox inserts during high-concurrency checkout bursts.

---

## Part III: Five New Challenging Architectural Scenarios

In accordance with the review mandate, the following 5 novel scenarios explore complex, real-world edge cases:

---

### Scenario 11: Inventory Reservation Conflict During Concurrent Cart Checkouts

* **Problem**: Two shoppers add the final available unit of an item to their carts. Shoppers A and B attempt to complete checkout around the same time. How does Medusa v2 prevent overselling without deadlocks or unverified cart TTL reservations?
* **Solution**:
  1. In standard Medusa v2, active shopping carts do NOT hold reserved stock; reservations are created automatically inside `completeCartWorkflow` when the cart is completed and the order is placed.
  2. Both Shoppers A and B can have the item in their carts simultaneously without contention.
  3. Contention occurs at the database level when `completeCartWorkflow` executes. Shopper A's checkout completes first, atomically creating the `ReservationItem` and confirming the order. Available stock (`stocked_quantity - reserved_quantity`) drops to 0.
  4. When Shopper B's `completeCartWorkflow` executes, the inventory reservation step detects insufficient available stock (`available_quantity < requested_quantity`) and fails cleanly with an inventory allocation error.
  5. Medusa's workflow compensation runs for Shopper B: any authorized payment hold is immediately canceled (or refunded if captured), and the shopper is notified that the item sold out before checkout completion.
* **Limitations & Invariants**: No parallel inventory hold or unverified cart TTL is assumed. The stock check is strictly transactional at cart completion.

---

### Scenario 12: Customer PII Leak via Unscoped Storefront Search API

* **Problem**: A developer exposes an elasticsearch/meilisearch indexing hook that indexes all order data, including customer full names, phone numbers, and addresses, into a public storefront search index. An unauthenticated attacker queries `/store/search?q=SAR` and receives a list of recent customer shipping addresses.
* **Solution**:
  1. **Strict Field Whitelisting**: Only public product fields (`title`, `description`, `handle`, `thumbnail`, `variants.prices`) are sent to public search indexes.
  2. **Security Gate in Search Module**: The search indexer must reject any data payload containing customer or order models:
     ```typescript
     if (entityType !== "product") {
       throw new Error("Security Violation: Only product entities may be indexed into public search.");
     }
     ```
  3. Customer order searches must remain server-side, querying PostgreSQL directly with mandatory `customer_id` filtering.

---

### Scenario 13: Workflow Compensation Failure Following External Payment Capture

* **Problem**: A workflow step captures 1,000 SAR via an external payment provider. The subsequent step (creating an ERP booking) crashes due to an unhandled exception. The workflow compensation callback for payment (`paymentProvider.refundPayment()`) is invoked, but the payment provider's API returns `504 Gateway Timeout`. The compensation itself has now failed!
* **Solution**:
  1. **Dual-Failure Handling**: Medusa v2 marks the workflow execution as `FAILED` and records the compensation error in the execution log.
  2. **Durable Dead-Letter Queue (DLQ)**: The failed compensation payload is automatically pushed to a dead-letter queue (`failed_compensations`).
  3. **Alerting & Automated Retry**: A background reconciliation worker retries the refund with exponential backoff and idempotency keys. If 5 retries fail, an immediate high-priority PagerDuty / Sentry alert notifies on-call engineering with the transaction ID for manual merchant reconciliation.

---

### Scenario 14: Erroneous Proposal to Fork Medusa Core for Custom Pricing Rules

* **Problem**: A client requests custom pricing rules where VIP customers receive a 15% discount only on products tagged "VIP-Exclusive" during weekends. A contractor submits a Pull Request modifying `@medusajs/medusa/pricing/services/pricing.js`.
* **Solution**:
  1. **Immediate Rejection**: Violates Constitution Principle III (zero core forks).
  2. **Official Medusa v2 Architecture**:
     * Use Medusa's native **Promotion Module** rules engine.
     * Configure a Campaign with rule conditions: `customer_group = 'VIP'`, `product_tag = 'VIP-Exclusive'`, and valid date ranges.
     * Native Medusa promotions evaluate these rules automatically in `computePromotionWorkflow` during cart calculation without a single line of core code modification.

---

### Scenario 15: Background Retry Failure in Sequential Tax Invoice Generation

* **Problem**: An order is placed and the invoice generation worker runs. The worker contacts the tax authority API, but the authority returns `HTTP 500`. The worker has already incremented the local sequential counter (`ICV = 42`). If the worker blindly retries with a new sequence, `ICV = 43` will be used, leaving sequence `42` missing and breaking the regulatory audit trail.
* **Solution**:
  1. **Transactional Sequence Increment**: The sequence counter `last_icv` must only be committed to the database in the *exact same transaction* that saves the certified invoice XML.
  2. If the API call fails, the database transaction rolls back, reverting `last_icv` to `41`.
  3. The next worker retry re-reads `last_icv = 41`, attempts generation with `ICV = 42`, and preserves the unbroken sequential chain.
