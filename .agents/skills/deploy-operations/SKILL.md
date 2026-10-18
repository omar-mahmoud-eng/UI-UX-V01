# Portable VPS deployment
## When to invoke
Staging deployment, secret handling, release and disaster recovery.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Build official production artifacts; configure API/worker/storefront TLS+reverse proxy, Postgres/Redis private interfaces, systemd; test staged migration, backups, restore, rollback, monitoring.
## Prohibited
Embedding credentials, exposed database, untested deployment, claiming recovery time without drill.
## Evidence
Staging URL, health+checkout proof, restore report, rollback logs, operating runbook.
## References
https://docs.medusajs.com/learn/deployment/general
