# F00 — Official Starter Baseline (MANDATORY FIRST TASK)
**Goal:** a verifiably running official Medusa application, Admin and Next.js storefront using native/local Postgres and Redis. **No custom features.**

## Inputs / permitted work
Read AGENTS, README, docs/00..18, official starter guide. Work in new feature branch from new main. Bootstrap the official monorepo into apps/backend + apps/storefront with deterministic package manager and lockfile. Keep project docs. If generator insists on a new folder, migrate generated official files without overwriting policy docs. Document exact scaffold commands and generator version. Do not implement F01.

## Preflight
- clean branch/status; OS and Node engines; check PostgreSQL service, database user, schema and version; Redis connection; port 9000 and storefront port.
- documented supported Node and package manager versions. Official currently illustrates "yarn dlx create-medusa-app@latest --with-nextjs-starter"; verify before running. Do not require Docker.
- never write secrets to repo; .env files locally ignored. Generate strong local-only JWT/COOKIE secrets; never print them in reports.
- check network/dependency availability; if blocker, report actual error.

## Actions
1. Bootstrap and pin official dependencies; commit source+lockfile, no node_modules.
2. Configure real PostgreSQL and Redis, create/reset only dedicated local dev database; run Medusa official migrations/seed as supported.
3. Start and KEEP processes live for browser checks.
4. Verify backend health HTTP with actual response, Admin login with test staff created using documented Medusa command, storefront loads and fetches from backend without critical browser console/network errors.
5. Restart processes; verify health + Admin and storefront still work.
6. Record versions, commands/exits, logs (redacted), exact URLs, browser trace/screens, migration IDs, and clean install repro.
7. Update docs/15 ledger, mark F00 PASS only after every criterion; include reference to evidence (public-safe).

## PASS/FAIL grid
[ ] Clean install from clone on supported environment with lockfile
[ ] PostgreSQL and Redis connected; schema migrated; no crash
[ ] GET http://localhost:9000/health returns documented healthy response
[ ] Actual browser Admin /app renders and staff can log in
[ ] Actual browser Storefront renders and backend connection verified
[ ] Restart retains startup success and data
[ ] No committed secrets or fake data presented as production
[ ] Run commands + exit codes + sanitized console/network traces recorded
[ ] No architecture scope violations, documented rollback SHA

## Disallowed
Custom module, analytics, theme rewrite, Puck, production credentials, external shipping/payment, fake tests, mass-dependency upgrades, arbitrary project structure replacement.

## Stop rule
Failure => F00 FAIL/BLOCKED, root-cause report, do not proceed. PASS => stop and hand off F01; no autonomous future stage.
