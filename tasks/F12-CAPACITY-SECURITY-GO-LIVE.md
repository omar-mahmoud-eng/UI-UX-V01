# F12 — Measured high-load readiness, resilience and launch
Prereqs F00-F11 **applicable** acceptance; optional future modules need not block the first production launch.
1. Produce realistic workload profile: product browse/search, Admin, cart, order/checkout with configured test payment, variant and user mix, seeded data scale. Declare host CPU/RAM, PostgreSQL/Redis, load tool and concurrency.
2. Ramp/soak/peak/failure tests; measure p50/p95/p99, error rate, DB locks/connection pool, memory/GC, worker backlog, recovery and data integrity. No "infinite scaling" language.
3. Fix measured bottlenecks in order: schema indexes and N+1, cache/asset optimization, stateless horizontal app/workers, DB tuning, read replica and async reports; separate service only via accepted ADR.
4. Security assessment: OWASP API auth/BOLA, privilege matrix, upload SSRF/XSS, secrets and SCA/SAST, dependency CVEs, CSRF, webhook replay, rate limits, audit, staff authentication. External pentest where exposure/risk demands.
5. Disaster drill: DB/instance fault, backup/restore, worker restart, migration rollback strategy, incident response, tested RPO/RTO.
6. Production Go/No-Go: security findings triaged, no exploitable high/critical; functional/E2E and data correctness pass; operations on-call and legal notices verified.
Gate: signed acceptance report with actual evidence and known limits. No zero-bug claims, no claims beyond tested load envelope.
