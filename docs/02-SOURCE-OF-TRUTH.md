# 02 — Capability ownership / build-vs-reuse register

Before creating any package, check the pinned Medusa version's official modules, providers, workflows, Admin and storefront components, then record exact source and gap.

| Capability | Default owner | Rule |
| --- | --- | --- |
| Product/variants/categories/collections/facets | Medusa commerce | configure + add safe custom metadata/links; never fork |
| Prices/currencies/promotions/taxes | Medusa modules | one price/tax authority; KSA config after verification |
| Cart, checkout, orders, returns | Medusa workflows | extend official workflow/hooks; preserve idempotency |
| Customer/account/auth | Medusa supported auth | route authz + secure session cookies; no second passwords DB |
| Inventory, reservation, locations | Medusa inventory/stock | no parallel custom counters |
| Payment/fulfillment | Medusa providers | test/sandbox only until compliance+business sign-off |
| Admin UI | Medusa Admin + Admin Extensions | augment, not rebuild core |
| Storefront | Official Next.js starter | customize experience while preserving documented contracts |
| Event/workers/cache/storage | Medusa infrastructure modules/providers | check supported providers before building |
| CMS/page builder | custom bounded context | Medusa-linked content entities; output sanitized, versioned |
| Customizer (cake/flowers/gifts) | product-personalization module | cart/order integration via documented extension points |
| CRM/campaigns | custom bounded context | customer/order references, consent controls |
| Accounting | later custom/integration | ledger accounting and reconciliation, never shadow order state |
| Analytics | custom projection | asynchronous read-model; immutable source references |
| Helpdesk/POS/B2B | custom modules where Medusa gaps | explicit scope per vertical slice |

Each new module proposal must answer:
A. Is an official Medusa feature available? B. What exactly is missing? C. Why module rather than configuration/workflow? D. Data owner? E. AuthZ/threat boundary? F. Integration test? G. Upgrade compatibility? H. Operational cost?
A duplicate core-commerce implementation is a blocking architecture defect.
