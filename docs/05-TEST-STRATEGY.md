# 05 — Evidence-first test plan

## Pyramid and tools
1. Static: exact dependency lock, TypeScript strict, ESLint, format, import boundaries, dependency/SBOM scan, secret detection.
2. Unit: pure business logic, validators, transforms and permission policies (table-driven, edge cases).
3. Medusa module integration: use official moduleIntegrationTestRunner and DB; verify migrations and isolation.
4. Medusa API/workflow integration: medusaIntegrationTestRunner; HTTP auth and object scope, transaction compensation, idempotency, failure injection.
5. Browser E2E: Playwright for storefront and real Admin; avoid screenshot-only proof. Capture trace/sanitized console and network errors.
6. Deployment: prod build, separate process startup, health, DB/Redis connection, clean boot and warm restart; upgrade migration path.
7. Security: OWASP ASVS-inspired control matrix, API authorization/BOLA, cross-site scripts, CSRF/session, file upload, SSRF, secrets, dependencies, privilege escalation.
8. Load, stress, soak, concurrency, resilience: k6/Artillery (choose one by ADR); test on documented hardware/staging; never against unknown third-party live resources.

## Minimum test cases before accepting F01
- Catalog list/detail and variant price consistent with backend data.
- Valid cart with line item, positive/negative quantity, invalid variant, deleted variant.
- Successful simulated checkout with confirmed order visible in Admin; invalid address, stock exhaustion.
- Two simultaneous checkouts of last unit; no inventory oversell or duplicate charge (test provider).
- Retry duplicate checkout event and webhooks; results idempotent where required.
- Unauthenticated Admin attempts denied; customer A cannot access customer B cart/order/data.
- Broken dependency gracefully errors, logs and preserves consistent order state.
- Locale direction, mobile viewport and first page load without blocking console failures.

## Pass matrix
Static: 0 unresolved build/type errors; tests return actual exit code 0; no test skip hiding a critical journey.
Runtime: clean DB + restart + browser real request paths verified; no app crash or unhandled rejection.
Data: migrations and links consistent; backfills and rollback rehearsal when schema changes.
Security: authn/authz server-side, no known exploitable critical/high, secret scan clean, dependency findings triaged with evidence.
Perf: establish hardware, dataset, route scenario, number of virtual users, p95/p99, error rate, DB resource/queue lag baseline. Compare changes against baseline; no fixed "millions" guarantee.

## Initial candidate performance acceptance (to calibrate)
On a **documented staging host**, prove 15-minute steady workload of 50 concurrent virtual users for read/catalog/cart with error rate <1%, p95 latency under 1000ms, and no process crash or DB exhaustion. EXCLUDE payment provider responses and use only synthetic traffic. Treat these as provisional engineering targets, not achieved results or general capacity promises. Add checkout stress and 60-minute soak before production go-live; set stronger targets based on traffic SLO.

## Artifact and evidence format
Record exact command, cwd, git SHA, OS, tool versions, container/service state, start/end, exit code, sanitized logs, baseline dataset and screenshot/trace links. Security reports may require private storage; never commit sensitive details to public repo. Report PASS/FAIL/NOT_RUN with reason. Fail means stop and fix within scope, not advance.
