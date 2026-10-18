# F04 — Staging VPS deploy, recoverability and monitoring
Prereqs F00-F03 PASS. Work only on deployment/reliability; no new commerce feature.
1. Write repeatable Ubuntu Linux VPS install/run for current pinned Node, PostgreSQL/Redis, Medusa API/Admin, worker mode if documented, Next server, TLS/reverse proxy, firewall, least-privilege users and environment secrets. No mandatory Docker, no leaking DB/Redis publicly.
2. Staging with fake buyers, providers disabled/sandbox only, production build and migrations staged, deploy + rollback from tagged commit.
3. Off-host encrypted backup and restoration drill; verify schema, count, catalog and test checkout after recovery. Time RPO/RTO; do not make targets up.
4. Monitoring: API and worker health, uptime, checkout success, errors, queue failures, DB slow queries, CPU/RAM, p95, storage; actionable alert.
5. Load test baseline 50 VU/15m provisional on stated hardware with clean metrics. Stress and soak planned F12. No absolute capacity promise.
Gate: staged browser journey, backup restore report, release and rollback tested, SCA/secrets scans, operational runbook updated. Stop.
