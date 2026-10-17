# Proposed UI-to-domain architecture (not a code implementation)

- **Medusa v2 core (verify exact version)**: product/catalog, cart/checkout, order, customer, promotions, inventory, pricing, stock locations, shipping/payment provider interfaces. Extend its business workflows instead of duplicating native entities.
- **Custom domain modules**: gift personalization design/proof, wood production jobs, floristry recipes/batches, production capacity, gift recipient/privacy, delivery slots, corporate RFQ, multi-recipient gifting, support, marketing, loyalty, advanced returns.
- **Specialized service or integration candidates**: accounting/ledger, ZATCA compliant invoicing, WMS algorithms, private fleet routing, telephony, BPMN/DMN, analytics warehouse, marketplace seller settlements, GDSN.
- **Admin**: Medusa Admin extension widgets/pages for native integrations; consider fully separate React admin if full visual identity and enterprise IA cannot fit extension points. All privileged mutations via typed APIs with RBAC checks, idempotency, audit and approval rather than direct DB edits.
- **UI-only status**: Planned (not implemented) / Connected (demo concept) / Disabled until provider verification. Do not portray unfinished capability as running.
