# 07 — Deployment, scalability, recovery and SRE runbook

## Supported initial profile (to implement, not yet deployed)
- Linux VPS (e.g. Hostinger VPS) with suitable Node LTS, PostgreSQL, Redis, reverse proxy/Nginx or equivalent, TLS, systemd/process supervision. Local native Postgres/Redis acceptable; Docker optional, never mandatory.
- Deploy Medusa API/Admin, Next.js storefront and if beneficial Medusa Worker per documented MEDUSA_WORKER_MODE, with secret env and least-privilege service accounts.
- Medusa official general deployment calls for PostgreSQL+Redis and describes separate server/worker modes. Follow version-accurate guide, including migration/predeploy order.
- Database/Redis bound to private interfaces, backups encrypted/off-host and validated, object storage for user media with IAM/per-object access restrictions.

## Reliable release
1. Immutable dependency versions/lockfile + clean CI; artifact version+SHA.
2. Stage and run production build + migrations against cloned sanitized schema.
3. Backup/snapshot + health/metrics before deployment.
4. Apply backwards-compatible expand migrations; roll new server/worker/web; smoke real API/Admin/storefront; background job validation.
5. Monitor error rate, p95/p99, resource saturation, queue lag, SQL contention, slow queries, logs, crash loops and dependency error rates.
6. Roll back binaries/configs if degraded. For data migrations use forward fix/restore plan; DO NOT assume down migration safe.
7. Run contract and E2E after release; explicit approval for production cutover.

## Scaling ladder
0. Optimize indexes, queries, payloads, images and Next cache strategies.
1. Add application instances behind load balancer with shared PostgreSQL/Redis and stateless request behavior; test sessions.
2. Separate Medusa worker execution and constrain concurrency; backpressure, retries and failed job monitoring.
3. Add CDN for static assets, object storage and bounded application caches.
4. Introduce read replicas and analytical projections only after proving primary DB pressure and consistency requirements; split heavy exports.
5. Sharding/cells/services only after hotspot analysis and approved ADR; preserve single-store ownership and operability.

## SLO / incident management (establish baselines first)
Availability and p95 targets must be specified by business and measured in realistic staging; publish SLI dashboard for request errors/latency, checkout success, DB health, worker lag. Alert on sustained customer impact, not every isolated exception. Set realistic RPO/RTO after actual restore drill; never promise instant recovery without proof.

## Host hardening
Non-root services, SSH key auth, automatic security updates under staging rehearsal, firewall, TLS renewals, log redaction, restricted outbound where feasible, no exposed admin on public unauthenticated routes, secrets rotation, backups and incident playbook.

## Disaster recovery drill
Simulate instance loss; restore PostgreSQL from off-host backup plus object assets; start API/Admin/storefront/worker on clean host; confirm order counts and checkout test, record recovery duration and gaps. Never claim PITR without configured WAL archives and test.

## Integration resilience
Timeouts, bounded retries + jitter, idempotent handlers, queue backpressure, circuit breaking where needed; maintain order reconciliation and observable failures. Do not silently drop tasks.
