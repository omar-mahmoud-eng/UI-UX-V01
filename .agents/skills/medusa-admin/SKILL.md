# Official Medusa Admin extensions
## When to invoke
When staff needs a new page, widget or setting.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Prefer existing Admin screen. Add official UI Route/Widget with Medusa UI/dashboards where pinned version supports exports. Enforce RBAC server-side and test staff roles.
## Prohibited
Rebuilding Admin wholesale, self-made auth stack, relying only on hidden buttons for security.
## Evidence
Admin browser trace for authorized/unauthorized roles, API denial, screenshot and logs.
## References
https://docs.medusajs.com/learn/fundamentals/admin/ui-routes
