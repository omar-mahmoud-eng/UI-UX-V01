# F09 — Operations: inventory, purchasing, shipping, returns
Prereqs stable base.
A. Extend Medusa stock/location semantics rather than inventing inventory ledger; add purchase orders and suppliers only for true gaps.
B. Warehouse receiving, transfers, cycle counting, reorder threshold forecasts, delivery windows and pick/pack; separate workflows for each.
C. Shipping carrier providers under sandbox with webhook signature/idempotency; no production carrier credential until acceptance.
D. Returns and exchanges with consistent Medusa order/refund/fulfillment states, staff approvals and customer notifications.
E. Negative scenarios: oversell, concurrent reservation, lost webhooks, partial shipment, split refund, failed worker, invalid inventory adjustments, RBAC.
Gate: no mismatch among stock/order/fulfillment; independently tested migrations, no duplicated core records, real UI E2E, recovery path.
