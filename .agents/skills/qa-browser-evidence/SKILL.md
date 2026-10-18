# Runtime and browser verification
## When to invoke
For every F00+ stage gate and any claim of completed functionality.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Start all required local services, record ports/health, do actual browser actions, inspect backend/order DB, capture trace, network and console. Run focused regressions and report failed/skipped tests.
## Prohibited
PASS from successful build alone, mocked API evidence, screenshots instead of transactions.
## Evidence
OS/versions, URLs, trace/screens, HTTP statuses, DB verification, commands+exit codes.
## References
https://docs.medusajs.com/learn/debugging-and-testing/testing-tools/integration-tests
