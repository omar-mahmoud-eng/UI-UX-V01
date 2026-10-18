# 06 — Security architecture, checks and threat model

## Trust boundaries
Untrusted browser/customer/API client; staff/Admin roles; server app and workers; PostgreSQL/Redis; file/object storage; integrations/providers; build system and package supply chain; agent working environment.

## Mandatory controls
- Auth: use Medusa-supported auth/session patterns; HTTP-only/Secure/SameSite cookie choices based on actual deployment, CSRF defense for state-changing authenticated browser actions, MFA/step-up for privileged actions where supported. No homebrew tokens or customer secret storage.
- Authorization: explicit route guards, per-object ownership checks, tenant/store/channel and staff permission scoping server-side. Test horizontal and vertical privilege escalation (BOLA/BFLA).
- Input: schema validation, allowlists, length and media constraints, output encoding. Do not expose arbitrary file paths or private server URLs. Avoid SSRF from image import, preview fetch, integrations and webhook handling.
- HTML/UI: page builder only renders approved component registry and sanitized structured content. No arbitrary tenant-supplied scripts without separate threat model/sandbox/CSP. Safe image/SVG uploads and XSS/HTML sanitization.
- Secrets: never commit .env, tokens, JWT/COOKIE secrets or live payment credentials; use secret manager/environment and rotation. Public GitHub scan before each merge.
- Supply chain: pin lockfile, scan vulnerabilities, provenance/maintainer review, minimal dependencies, no random unreviewed agent skills executing hooks.
- API: rate limits at edge and app as needed, request size/timeouts, pagination limits, idempotency, CORS allowlist, webhook signature/timestamp/replay controls.
- Data: encryption in transit, backups encrypted, least-privilege DB users, no direct public DB/Redis, retention/delete policy for PII, data export and audit logging.
- Commerce: server recomputes prices/taxes/shipping; client cannot forge discounts or stock. Reconcile charge/fulfillment order events; test double-click/retry and concurrent stock reservations.
- Admin: audit mutations, explicit RBAC, safe background import, permission-aware navigation AND APIs, brute-force protection and optional IP allowlist.
- Operations: current security patches, SSH keys, firewall, TLS, health probes, backup restore drills, incident response with secret rotation and rollback.

## Security testing catalog
OWASP ASVS 5 verification mapping per implemented surface; OWASP API Security Top 10; SAST, SCA, secret scanning, dynamic authorized tests on staging, dependency update policy and manual review. Block exploitable critical/high issues and document lower-risk remediation.

## Threat examples / abuse stories
Customer A reads B's order; unprivileged Admin exports financial records; malicious upload executes HTML/JS; checkout double-order through concurrent requests; forged shipping webhook marks an order fulfilled; API key grants unexpected sales channel scope; marketing automation sends without consent; rogue plug-in exfiltrates secrets; stale analytics cache exposes personal identifiers.

## Hard truth
A Module/Plugin is a *code boundary* inside the same process, NOT a sandbox or independent least-privilege security boundary. A plugin may require controlled migrations and cannot always be removed just by feature flag. Strong isolation requires a separate process/OS policy or externally reviewed sandbox. Future plugins must be trusted, reviewed, versioned and permissioned.

## Security exit
"All checks completed" means only those actually run on documented scope; does NOT mean zero vulnerabilities. Independent pentest and legal/compliance validation required where risk/regulated operations justify them.
