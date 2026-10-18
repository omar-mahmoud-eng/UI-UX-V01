# 03 — Complete envisioned functional module inventory
**Vision/backlog, NOT a claim of implemented features.** Each line is a bounded-context feature family, not an immediate package or microservice. Use Medusa first; build only specific gaps. Prioritize using acceptance matrix.

## Tier 0: baseline commerce
- Identity & roles: Admin/customer login, RBAC and scoped permissions, sessions, MFA integration where supported, staff access and audit.
- Catalog/PIM: variants, multilingual content, media, categories, collections, brands, attributes/facets, SEO, imports/exports, bundles/kits, product rules.
- Commerce: sales channels, regions/currencies, taxes, price lists, promotions, coupons, gift cards, cart, checkout, orders, returns, exchange/cancellation, refunds with provider controls.
- Inventory/operations: multiple warehouses/locations, stock reservation, purchasing later, batch/lot/serial only when business needs, suppliers.
- Customer/storefront: Arabic/English RTL/LTR, account, search/filter, wishlist/reviews as first expansions, responsive/mobile, accessibility and performance.
- Payments/fulfillment: provider abstraction, sandbox payments, shipping options, later KSA carriers, tracking, COD verification and risk control.

## Tier 1: complete modern storefront + Admin
- Site builder: themes, drag-drop pages/sections, templates, responsive variants, reusable components, visual preview, draft/publish/rollback, SEO/structured data, brand kits, media library, safe custom code policy.
- Content/SEO: pages, blogs, landing pages, editorial workflow, redirects, sitemap, localization, A/B experiments only after analytics.
- Admin workspace: dashboards, global search, bulk editing/actions, imports, approval flows, configurable widgets, shortcut commands, audit trails, workspace preferences and accessibility.
- Product personalization: extensible schema for custom cakes, boxes, flowers, engraving, upload artwork, multi-step wizard, custom pricing/versioned configuration, thumbnail and proof attached to line item.
- Analytics: sales funnel, cohort, margin, acquisition, channels, attribution caveats, live dashboards, alerting, scheduled reports, exports.
- CRM/engagement: segments, tags, notes, interactions, customer lifetime value, consent, service cases, loyalty/referrals, reviews, customer feedback.
- Marketing automation: email/WhatsApp/SMS provider adapters opt-in, abandoned cart and order notifications, journeys, campaigns, suppression, unsubscribe, UTM and measurement.
- Search & recommendations: full-text/facets, merchandising, synonyms, related items, personalization with privacy and bias review.

## Tier 2: operations and enterprise extensions
- B2B: companies, contacts, RFQ/quotations, negotiated prices, credit terms, PO numbers, account approvals, budget/approval hierarchy, wholesale catalogs.
- POS/omnichannel: checkout at store, register, staff, cashier shifts, mixed payments (after provider approval), offline sync design only after explicit need.
- Procurement/inventory planning: suppliers, reorder thresholds, transfers, receiving, forecast, cycle counts, stock aging.
- Finance: chart of accounts, ledger, journals, AR/AP, bank reconciliation, VAT reporting, invoices/credit notes, cost/margin, export to accounting systems; regulated decisions need independent validation.
- Shipping & returns: carrier adapters, labels, pick/pack, SLA, address validation, COD, returns portal.
- HR/permissions/task workflows: staff roles, approval chains, responsibilities and team assignment (NOT a full HCM by default).
- Support: tickets, omnichannel inbox, service SLA, knowledge base, CSAT and escalation.
- Automation engine: workflow triggers/rules/actions, retries, approvals, schedules, dry runs, audit, safe webhooks.
- Integrations: APIs, webhook registry, ERP/accounting/payment/courier providers, import pipelines, API credentials scoped/revocable.
- Product verticals: subscriptions, bookings, rentals, digital downloads, configurable products, memberships, marketplace seller module (only if product changes).

## Tier 3: optimization (evidence-based)
AI-assisted content/search/support with strict approvals; advanced recommendation/risk; self-hosted reporting warehouse if metrics demand; multi-region disaster recovery; federation to independent customer instances only if explicitly commissioned.

## Module acceptance template
Business outcome | user stories | commands/queries/events | API/schema | Admin/Store UX | data ownership | permission matrix | error cases | unit/integration/E2E | performance budget | rollout/rollback | docs/upgrade.
