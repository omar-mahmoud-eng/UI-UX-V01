# Medusa workflow orchestration
## When to invoke
When operation spans several modules or external effects.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Use official workflows and steps, define side-effect compensation and retry/idempotency, validate input and handle timeouts. Explicitly decide sync vs async. Test success and induced failure paths.
## Prohibited
Direct cross-DB writes, infinite retries, hiding failed steps, ignoring duplicate events.
## Evidence
medusaIntegrationTestRunner logs, failed/retry trace, transactional consistency report.
## References
https://docs.medusajs.com/learn/fundamentals/workflows
