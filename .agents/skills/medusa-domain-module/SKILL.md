# Isolated Medusa domain modules
## When to invoke
When creating a genuine new bounded context and its own model.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Define model/service, register module, generate migrations, export public service API; use Module Links and Query to collaborate; test module isolation and required permissions.
## Prohibited
Cross-module private imports, direct foreign table writes, changing Medusa core or implementing multiple unrelated domains per task.
## Evidence
Migration ID; moduleIntegrationTestRunner exit code; interface tests; clean+upgrade DB proof.
## References
https://docs.medusajs.com/learn/fundamentals/modules/isolation
