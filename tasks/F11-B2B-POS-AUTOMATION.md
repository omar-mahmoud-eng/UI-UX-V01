# F11 — Optional B2B, POS and integration domains
Prereqs stable commerce base.
A. B2B: company hierarchy, buyer permissions, account pricelists, RFQ/quote approvals, purchasing, credit terms and per-company data scope; use Medusa concepts where supported.
B. POS: staff/register/shift, products/stock/order synchrony, refund flow with sandbox provider, race conditions; offline path ONLY after explicit consistency design.
C. Integration catalogue: webhooks, provider adapters, credential scopes, signature/nonce/idempotency, version, throttling and retry.
D. Workflow/rule builder: allowlisted triggers/actions and approval gates, sandbox/dry-run and rollback/disable; prevent privilege escalation and loops.
Implement each bounded context in tiny PRs with module service/data/API/permission/e2e; opt-in at installation by migration/feature flag, not guaranteed hot plugin.
Gate: cross-module contract tests, concurrency tests, BOLA auth, no checkout regression, separate release for each module.
