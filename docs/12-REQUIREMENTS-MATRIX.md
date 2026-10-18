# 12 — Requirements -> stage -> test traceability (living register)
Each requirement is NOT DONE unless linked to real test evidence. Initial status on 2026-10-18 is PLANNED everywhere.

| ID | Requirement | Phase | Evidence target |
|---|---|---|---|
| R-001 | Official Medusa + Next starter clean install | F00 | fresh install, locked versions, process logs |
| R-002 | PostgreSQL/Redis connection and migrations | F00 | DB health, migration command status |
| R-003 | Admin /app actual login; storefront actual load | F00 | Playwright/browser trace |
| R-004 | seeded product with variant, price and inventory | F01 | DB query + store detail |
| R-005 | cart / test payment / shipping / order | F01 | DB order + Admin order UI |
| R-006 | rollback/test of invalid inputs and out-of-stock | F01 | integration + browser E2E |
| R-007 | customer/admin object-level authz and secrets | F01-F02 | BOLA/BFLA negative cases, secrets scan |
| R-008 | module, link, workflow, API and first UI feature | F02 | moduleIntegrationTestRunner + E2E |
| R-009 | TypeScript contract and boundaries | F02 | static dependency test |
| R-010 | SAR, KSA address, mobile normalization | F03 | data/locale E2E |
| R-011 | ar-SA RTL and en LTR | F03 | screenshot and a11y + functional tests |
| R-012 | VAT / ZATCA readiness scoped by law | F03/F10 | audited tax tests and legal review |
| R-013 | production build, secret config, TLS & service split | F04 | staging deployment proof |
| R-014 | backups, restore, release rollback | F04 | restoration drill and measured RTO/RPO |
| R-015 | reliable workers, retry and duplicate handling | F04 | induced fault and idempotency cases |
| R-016 | Admin extensions and role-aware screens | F05 | Admin E2E with permission matrix |
| R-017 | CMS page builder preview/draft/publish | F05 | content version/roll back E2E |
| R-018 | safe media uploads, XSS/SSRF resilience | F05-F06 | negative upload/XSS tests |
| R-019 | configurable product/cake builder, server-side price | F06 | tampering and order record test |
| R-020 | search, import/export and content depth | F07 | UI + query performance tests |
| R-021 | Marketing/consent/customer segmentation | F08 | suppression, idempotent sending and consent tests |
| R-022 | CRM/tickets/loyalty | F08-F09 | permission/integration/E2E tests |
| R-023 | inventory operations and returns | F09 | concurrency and data consistency tests |
| R-024 | analytics/profit/invoicing/finance | F10 | reconciliation, locale/tax and report checks |
| R-025 | B2B/POS/automation/integrations | F11 | independent extension contract tests |
| R-026 | load/soak/fault tests and SLO | F12 | k6/Artillery results on stated hardware |
| R-027 | no unauthorized core duplication | all | architecture review and import rules |
| R-028 | no production live payments/fulfillment until approved | all | config guard and manual release check |
| R-029 | zero high/critical untriaged exploitable vulnerabilities | all | scans, mitigation evidence |
| R-030 | no claim of working functionality without proof | all | gate log with actual command exits |

## Update process
After each task append traceability row status NOT_STARTED/IN_PROGRESS/PASS/FAIL/BLOCKED, test URL/path, SHA, tester and date. No silent checkbox-only green state.
