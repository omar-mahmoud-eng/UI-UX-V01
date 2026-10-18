# 10 — Safe agent practical labs (disposable localhost + synthetic data ONLY)
Never target external services, customer data, or production. Explicit target and permission required. A described test is NOT an executed test.

L1 BOLA: synthetic customer A reads fabricated customer B order. Deny at server 403/404 with no private fields; verify UI and API both.
L2 Client tampering: fake cart quantity/price/discount. Backend computes total and stock using official Medusa flow; no client-authoritative financial values.
L3 Double checkout: duplicate idempotency keys, one unit stock, two simultaneous buyers, test provider delayed response. Assert no oversell or duplicate payment/orders; durable state after restart.
L4 Media/SSRF: SVG script, malicious file extension, oversized image, file fetch to loopback/private host. Reject executable content and SSRF; sanitize rendered content.
L5 Failed job: synthetic worker stopped and restarted, duplicate notification events; bounded retries and no duplicate side effects, observable failure queue.
L6 Database/Redis missing: kill only disposable sandbox processes, confirm failing readiness, user-safe error and recovery. Never kill unknown services or shared DB.
L7 Supply chain: third-party plugin with postinstall/hook asks for home directory/credentials. Reject, document license/source/version and safer reviewed plan.
L8 Performance: seeded synthetic catalog on known host, fixed concurrency/duration; intentionally slow query, observe p95, CPU, DB locks and EXPLAIN; fix based on measurement, compare before/after.

For EACH lab: objective, sanitized fixtures, initial failing assertion, commands/exit, diagnosis, minimal fix, positive+negative retest, regression result, reviewer, rollback and limitations. Without real host proof state NOT_RUN.
