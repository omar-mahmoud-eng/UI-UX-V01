# 04 — Stage roadmap and stop/go gates

## Work doctrine
Every stage delivers a real vertically usable increment. The previous stage is a verified release candidate (tag/commit + evidence); failure never means advancing with a longer TODO list. One stage per agent session. No parallel migration owners.

### F00 — Official runnable baseline (FIRST, ONLY CURRENT EXECUTION AUTHORITY)
Official bundled create-medusa-app + Next.js starter, backed by PostgreSQL, Redis; a real Admin login and accessible storefront. Clean install/start/restart verified. No custom modules. Gate: start and browser proof; no known crash; tracked version lockfile.

### F01 — Basic real e-commerce path
Create test region, currency, shipping/payment dummy/test provider using officially supported flows. Seed a product/variant/inventory, discover product in storefront, cart, address, shipping/payment sandbox, complete order in DB; Admin sees order. Test out-of-stock and invalid inputs. Gate: repeatable Playwright trace plus integration evidence, no live transactions.

### F02 — First custom module and extension contract
Choose Product Reviews or Wishlist (single bounded context) with Medusa Module model/service, Module Link, Workflow/API, permissions, Admin/store UI as needed, migrations and isolated integration tests. Gate: install/disable safely, verified no regression in F01.

### F03 — Saudi foundation
ar-SA default/en fallback, SAR, responsive RTL, Saudi regions/mobile/address normalization and policy, configurable VAT from verified authoritative rules, transactional content, shipping/payment adapters still sandboxed. Gate: locale/price/tax/error/E2E tests.

### F04 — Safe deployability
VPS/Hostinger-compatible server + worker + PostgreSQL/Redis + TLS, environment segregation, rolling/blue-green or tested restart plan, log/metrics/alerts, backup & restore drill, migration rehearsal, minimal privileges, no exposed DB. Gate: staging run and rollback tested.

### F05 — Admin design system and CMS shell
Medusa Admin Extensions, role-aware navigation, visual page-builder proof of concept with Puck evaluated by ADR, draft/publish/preview revision, safe allowed components, asset uploads, SEO. Gate: no arbitrary script injection, accessibility and publish rollback.

### F06 — Product personalization
Composable configurable product engine; start with cake builder example, store validated configuration/version, server-side pricing re-evaluation and file safety, cart+order link proof. Gate: tamper and price spoof tests.

### F07 — Catalog/experience depth
Search, SEO, imports, wishlists, reviews, rich filters, page templates, collections, content, performance budgets and regression.

### F08 — Customer engagement
CRM, segmentation, consent, notifications, marketing journeys, coupon and loyalty design, anti-spam/suppression, audits.

### F09 — Operations
Inventory enhancements, multi-location, purchasing, suppliers, fulfillment, returns, customer service and reporting.

### F10 — Commercial intelligence / accounting integration
Read-only analytics first, dashboard, financial model, real reconciliation, VAT/ZATCA external compliance review. No payment/accounting ledger implemented speculatively.

### F11 — Advanced B2B, POS, automations and integrations
Enable independently per installation. Feature flags, versioned contract, RBAC, isolated tests.

### F12 — Hardening and capacity qualification
Production-equivalent load/soak/fault/restore/security assessments; tune app workers/cache/indexes; independently approved external pentest/compliance where required; only then higher-load claims.

## Feature granularity
Each F04+ splits into bounded tasks T001... with one business result, <= one domain boundary migration, clear acceptance and rollback. Development of later vision can be reprioritized, not used to skip early stage gates.

## Universal exit criteria
- Actual clean install and services boot.
- New feature green type/lint/unit/module-integration/API/E2E as applicable.
- No critical or high security findings accepted without explicit written exception and deadline (production exceptions prohibited for exploitable high risk).
- DB migrations validated on fresh and existing schema; backup/restore considered.
- Existing acceptance suite passes; known failures documented not suppressed.
- Logs/metrics cover failure path; rollback demonstrably possible.
- Reviewer verifies evidence and signs gate in docs/15-CHANGE-LOG.md.

## Explicitly not promised
No number of files proves completeness. No guaranteed 0 bugs or exploits. No arbitrary throughput figures without hardware/scenario results. F00 and F01 must succeed before building the feature catalog.
