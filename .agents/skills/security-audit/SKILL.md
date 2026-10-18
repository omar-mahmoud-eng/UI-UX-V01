# Security, privacy & abuse-case audit
## When to invoke
Every privileged API, file, plugin, webhook, payment-like flow, and release.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Threat-model actors and objects; test BOLA/BFLA, XSS, SSRF, CSRF, secrets, rate limits, input validation and session security. Scan dependencies and record severity/remediation.
## Prohibited
Claiming zero vulnerabilities, bypassing tests, logging credentials, ignoring exploitable high/critical.
## Evidence
Authz table + negative HTTP results, scan outputs, fix evidence and remaining risk.
## References
https://owasp.org/www-project-application-security-verification-standard/
