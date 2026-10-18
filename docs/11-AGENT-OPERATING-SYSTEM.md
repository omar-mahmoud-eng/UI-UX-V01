# 11 — Antigravity agent operating system: do less, prove more

## Roles, not uncontrolled swarm
- Orchestrator (one): reads plan, allocates one stage, enforces gates, does not invent feature scope.
- Medusa Engineer (one): owner of backend changes, migrations, integration tests.
- Storefront Engineer (one): owner of UI route flow and browser E2E.
- Security Reviewer (independent): auth/permissions/abuse-case check, dependency scan, does not waive issues silently.
- QA/SRE Reviewer (independent): clean install, runtime, migration, log and load proof.
At F00 use ONE primary agent, one independent reviewer after implementation. Parallelize only clearly disjoint modules later. Avoid magic skills or instructions buried in 100 files.

## Preflight decision
Explicit current F-number; expected SHA; changed-file allowlist; test exit criteria; previous gate reference; test data rules; host and network assumptions. If missing, read task file before writing code.

## Finite loop
Read -> inspect system -> present 1-page plan -> edit <= small coherent slice -> run real tests -> fix root cause -> log evidence -> stage summary -> STOP. Never re-run a full suite endlessly; first narrow failing component, run targeted test, then full gate once fixed.

## Fault classification
- INFRA: DB/Redis/Node/package manager/firewall/port. Diagnose using process/network/log checks, without changing domain code.
- BUILD: dependency/compiler/typing. Check pin+lock/version mismatch.
- MIGRATION: schema/connectivity/permission. Save DB state and reproduce fresh+existing.
- RUNTIME: API/worker Admin/storefront startup. Inspect process stack and health.
- DOMAIN: test customer/order/price/inventory state, query execution and contract.
- SECURITY: privilege, spoofing, injection, secrets; block dangerous deploy.
- PERFORMANCE: measured hot path/resource contention, no speculative rewrites.

## Prompt guards
Each phase's prompt must include "one task only"; no agent can change architecture without ADR and reviewer approval. Agent may add supporting tests/docs for the current task. Scope expansion is FAIL, not initiative.

## Evidence report
- status: PASS / FAIL / BLOCKED / NOT_RUN
- tree SHA + clean git and dirty files
- environment manifest versions of Node, pnpm/yarn/npm, PostgreSQL, Redis, Medusa, Next.js
- cmd exit codes and sanitized logs, URLs and actual browser traces
- migration revision on clean + upgrade schema, retention of seeded data
- security findings and remediation/limitations, tests skipped with reasons
- rollback SHA, handoff and next single task

## Curation of skills
Only audited local skill markdown files: Medusa native modules; API workflow; Next.js storefront; PostgreSQL migration; tests/browser; security; SRE; architecture/contracts; Saudi localization; CMS builder; QA reporter. Each skill has trigger, inputs, prohibited actions, output acceptance, references. Don't install arbitrary external "super skills" via shell without reviewing contents, ownership and supply-chain risk.

## Enforcement
Automate checks in CI when F00 code exists; validate changed-file allowlists and tests. Human verifies real browser evidence; cannot call a broken installation PASS.
