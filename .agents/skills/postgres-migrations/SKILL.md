# PostgreSQL migrations & integrity
## When to invoke
When adding or changing database schema, indexes, links, or read models.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Identify owner, generate supported migration, test empty DB install and upgrade DB with backup; benchmark queries and check schema link integrity; document expand/contract and safe rollback.
## Prohibited
ORM schema pushes to production, dropping customer tables by default, sharing other module private models.
## Evidence
Migration command/exit, schema before-after, preserved row count, restore plan.
## References
https://www.postgresql.org/docs/
