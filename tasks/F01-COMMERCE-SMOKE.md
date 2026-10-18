# F01 — Real seeded commerce and simulated order
**Prerequisite:** F00 gate verified PASS by reviewer with SHA/evidence.

## Objective
One visible product in real Next storefront persisted in PostgreSQL via Medusa; complete a genuine Store API checkout using safe mock/test provider, and view actual order in Admin.

## Slice
- Create test KSA region/currency and sales channel, variant price, sufficient inventory, supported fulfillment option, Medusa-provided compatible manual/test payment provider.
- Use existing Medusa flows; do not create custom cart/order/price/stock services or access Medusa private internals.
- Bind publishable API key and proper CORS; never embed admin key in client bundle.
- Test create/list product, cart lifecycle, address entry, shipping selection, payment session/test success, completion, Admin visibility, saved order and totals.
- Capture order and stock before-after; use synthetic buyer data.
- Build Playwright E2E for success plus invalid variant, insufficient stock, missing address, unauthenticated Admin, double-click idempotency and customer object isolation.
- Include rollback to previous F00 SHA; commit only scoped changes.

## Gate
Real browser trace with HTTP/DB evidence and stable restart; all relevant integration, static and E2E tests green; known high/critical issues absent/blocked. Failed checkout should preserve consistency. No external real payments or fulfillment invoked. Stop after reporting.
