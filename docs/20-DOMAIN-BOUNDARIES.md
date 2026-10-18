# 20 — Domain blueprint: module ownership, contracts and evolution

## Architecture contract
A "large" domain module is allowed: many internal sub-features, one cohesive business responsibility and a stable public service boundary. No separate service deployment simply due to module size. "Module" is not the same as "plugin": Medusa modules isolate a domain; a plugin packages reusable code/routes/workflows/Admin customizations.

| Bounded context | Data owner and core records | Integration / public contract | Critical invariant |
| --- | --- | --- | --- |
| Commerce catalog | Medusa Product, variants, prices, inventory | Store/Admin API, Medusa query/workflow | no custom second price or stock authority |
| Customers and auth | Medusa customer/auth modules | scoped profile and server RBAC | ownership, retention and session security |
| Checkout and orders | Medusa cart, order, payment, tax, shipping modules | official create/update/complete flows | no double charge, oversell or stale totals |
| Design/CMS | CommerceOS Page/Revision/Theme/MediaRef | page resolver + Admin UI Route + component registry | no arbitrary code execution, rollback |
| Personalization | ConfigSchema/Option/Choice/Proof | validated configuration reference on Medusa line item | server computes price, immutable ordered snapshot |
| CRM | ContactAnnotation/Tag/Interaction/Segment | links to Medusa customer, subscribed events | consent and object ownership |
| Marketing | Campaign/Journey/Delivery/Suppression | Medusa events + workers + provider adapters | retries safe and opt-outs authoritative |
| Loyalty | PointsTransaction/Tier/Redemption | order events, anti-fraud checks, workflow | no double award or redemption |
| Analytics | Projection/MetricDefinition/ExportJob | read-only event/order references; worker-built views | never block checkout, documented eventual consistency |
| Finance | Journal/Account/Reconciliation | documented order/payment/refund inputs | double-entry balancing and fiscal audit trail |
| B2B | Organization/Contact/Approval/RFQ | Medusa pricing/customer/product references | company-level permissions, no cross-company leak |
| POS | Terminal/Shift/RegisterPolicy | Medusa order/inventory and payment provider | consistent stock and refunds |
| Fulfillment ops | Supplier/PO/Receiving/PickTask | official Medusa inventory/fulfillment references | prevent negative reservation inconsistencies |
| Support | Ticket/Conversation/Resolution | reference customer/order, authorized staff | redact private messages, audit access |
| Workflow automation | Rule/Trigger/Execution/ActionLog | audited allowed action registry | no privilege escalation, cycles or unbounded retries |
| Integrations | ProviderConfig/WebhookDelivery/Mapping | versioned signed API/webhook; secret manager | replay protection, revocation, idempotency |

## Inter-module rule examples
- Order placed -> official Medusa transaction commits -> queued CRM, analytics and notification work; failure in analytics doesn't roll back completed order.
- Customized cake -> custom config validated and priced by backend -> official cart/order workflow -> order stores immutable choice snapshot.
- Admin CMS publishes revision -> atomic pointer switch -> frontend invalidates affected page cache; no migration needed for content changes.
- Payment/refund -> official state + signed verified provider event -> finance reconciliation; never trust a browser "paid" flag.
- Stock reservation -> official inventory state only; procurement may project stock, must not write shadow balances.

## Database policy
Logical module model ownership even if sharing one PostgreSQL instance. Cross-module link tables through official Medusa supported module link mechanism; Query for composed reads; workflows for cross-domain commands. Build read-only projections for analytics with versioned import contracts. Migrations backward-compatible and tested fresh+upgrade.

## Process-level security
Module isolation is structural not security sandbox. Trusted signed/reviewed plugin code shares runtime privileges. Third-party code with distinct trust needs separate process and secret boundary, not merely folder structure.

## Capability flags
Feature off disables routes/menus/jobs when safe; schema and existing data remain until explicit migration/decommission plan. Do not promise arbitrary runtime hot swap or uninstall.

## Required per-module record
owner, source-of-truth, scope, all entities, API/events, auth matrix, idempotency, migrations, UI interactions, latency/error budget, tests, rollback, operational alerts, release/compatibility policy.
