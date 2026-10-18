# 16 — Curated agent skill specifications (lightweight, auditable)
Skills are short prompt/tool instructions, not substitutes for reading docs or executing tests. Agent tools must be explicitly available and permissioned, and reviewed before installation. No unreviewed third-party super-skills.

For each skill: TRIGGER; READ; DO; NEVER; PROOF.

## 1. medusa-core-inventory
Trigger: new commerce feature; read pinned docs+docs/02; map Medusa native owner and API; never fork core; proof capability comparison.

## 2. medusa-domain-module
Trigger: actual domain gap; read docs/01+08; create isolated model/service/link; never direct cross-table; proof module integration tests.

## 3. medusa-workflow-events
Trigger: multi-module operation; use official workflows/steps and compensation; never unbounded retries; proof success/failure/duplicate execution.

## 4. next-storefront
Trigger: customer journey; reuse official storefront; never local duplicate price/order authority; proof Playwright + real backend records.

## 5. medusa-admin
Trigger: staff UI; use official Admin Extensions; never new password stack; proof role-aware Admin E2E.

## 6. database-migration
Trigger: schema mutation; check DBA plan, forward/backwards compatibility, backups; never ORM auto-push to production; proof fresh+upgrade migrations.

## 7. security-review
Trigger: routes, privileged UI, integrations, plugin, secrets; assess OWASP ASVS/API Top 10, validate BOLA and auth; never claim zero flaws; proof findings/tests.

## 8. quality-browser
Trigger: stage gate; test real running app, network/console and DB; never declare PASS from screenshot alone; proof traces/HTTP/SQL.

## 9. performance-reliability
Trigger: stage perf gate; measure realistic loads with stated host/data, SQL, backpressure; never assert universal capacity; proof k6/Artillery profiles.

## 10. deploy-sre
Trigger: staging/production; TLS/env/process manager/backup/restore; never deploy unreviewed secrets; proof rollback and alerts.

## 11. sa-localization
Trigger: KSA flows; locale/region/currency/current tax rules and phone/address tests; never hard-code unverified legal compliance; proof E2E + compliance review.

## 12. cms-design-system
Trigger: page builder/theme; approved component schema, revision, preview; never arbitrary JS injection; proof XSS/revision/E2E.

Each skill can be recorded as separate AGENT_SKILL.md in the implementation stage if the agent runtime uses those files. Do not install 12 external repositories in F00.
