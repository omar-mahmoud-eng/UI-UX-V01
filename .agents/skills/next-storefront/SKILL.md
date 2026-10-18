# Real Next.js Medusa storefront
## When to invoke
When implementing customer-visible UI/commerce flow.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Extend official Next.js starter, retain backend source-of-truth, use scoped Store API/public publishable key. Include loading, error, mobile and RTL states; Playwright interactive path and network console inspection.
## Prohibited
Fake list with no backend, client-side authoritative pricing, exposing Admin API key, blank UI buttons.
## Evidence
Browser trace/video, Store API calls, underlying DB data, no console errors.
## References
https://docs.medusajs.com/resources/nextjs-starter
