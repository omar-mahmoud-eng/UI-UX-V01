# 06 — Technical debug playbook: startup, migrations, E2E, security and load

## Iron rule
NO FIX BEFORE ROOT-CAUSE INVESTIGATION. NO PASS BEFORE FRESH VERIFICATION. A successful compile proves only compilation. Past Antigravity versions repeatedly failed at runtime; capture layers objectively rather than altering many packages.

## Diagnostic snapshot before edits
Git SHA/status/diff, OS/architecture, package manager/lockfile hash, Node/Medusa/Next/React versions, Postgres/Redis states, process/port map, env variable PRESENCE (never values), logs and timestamps. Ensure all commands safe and limited to disposable development data.

## Reproduce in layers
1. Installation: clean checkout+lockfile, supported runtime, exact failing package command and exit.
2. Infrastructure: real Postgres/Redis connectivity, port listening and service logs.
3. Backend: start output, actual health response, migration revision, Admin serving and auth.
4. UI: Next process, real browser load, console/network/SSR error, proper publishable key, Admin auth.
5. Domain: API with real persisted test product/cart/order, permissions negative tests, stock/price truth.
6. Release: prod build, worker mode, restart data retention, staging smoke and migration recovery.
7. Performance: repeatable workload, SQL EXPLAIN, queue backlog, p95/error on stated hardware.

## Root-cause journal
Record symptom+minimal reproducer; actual stack/error; layers already proved; change diff before failure; one falsifiable hypothesis; smallest diagnostic experiment; observation; permanent regression test; one targeted fix; fresh full relevant suite and actual browser/DB verification. Do not replace unknown 500 with fake 200, hide errors, skip tests or blindly increase timeout.

## Defect-specific recipes
- ECONNREFUSED -> verify process/port/network interface and target URL BEFORE changing code.
- EADDRINUSE -> inspect owning PID/process and dev port choice; do not kill unknown production process.
- 401 vs 403 -> identify identity/session/CSRF vs object-level authorization; never remove guard.
- SQL migration failed -> review data type/permissions/current revision, test fresh+upgrade; do not drop database to pretend fix.
- React hydration/Admin router mismatch -> inspect actual pinned peer dependencies and server/client boundaries; no forced global upgrades.
- Timeout/hang -> inspect open handles, async conditions, DB pool exhaustion; condition polling rather than massive delays.
- Failed worker -> durable queue state, idempotent retry, dead-letter observation; never silently swallow.
- OOM/slow -> measure memory/queries/connection pools, isolate hot path before proposing new microservice.

## Escalation
After 3 failed correction hypotheses, stop and question architecture/API assumptions with evidence; propose one ADR or ask human approval. Dangerous schema changes or security exceptions always require approval. Status remains FAIL/BLOCKED.
