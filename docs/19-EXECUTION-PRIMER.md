# 19 — How to execute the full blueprint without recreating previous failures

## First implementation session
Ask Antigravity to work only on F00 using root START_AGENT_AR.md. Use the official bundled Next.js starter; keep all plans; no incomplete module folders. Pin toolchain from official docs. The installed app must actually run for F00 before generating any business-domain code.

## How future sessions proceed
1. User specifies one phase or agent reads verified last PASS in docs/15 ledger; next stage is F number +1.
2. Agent reads only applicable references with full roadmap context. Then writes a bounded task plan: exact files, reused Medusa capability, acceptance, security and rollback.
3. Work in a PR branch, do one functional slice; if large break down into UI/API/migration/reliability PRs without breaking tested contracts.
4. Reviewer executes production-like startup and real browser API+DB proof, not merely visual inspection.
5. Once gate is PASS in docs/15, agent can receive next phase. No autonomous 12-phase mega-run.

## Example task handoff
Phase F05, task CMS draft/publish: one Module owning Page/Revision; one Admin UI Route, two public API paths read/render; no price/order changes. Tests: permission (author/publisher/unauthenticated), migration, publish rollback, XSS, real Next render; evidence with SHA; stop.

## Version management
Never pin a Medusa version in the plan spec based on hearsay. Choose validated release using official starter in F00 and commit lockfile; verify Node and React/router compatibility, including Medusa Admin; update in planned isolated dependency upgrade with regression proof. Reuse @medusajs/dashboard exports only if pinned release supports them.

## First launch vs final vision
A commercial pilot may launch after F04 plus mandatory legal/security/payment/provider acceptance, NOT after F00. F05-F11 are expandable business capabilities. A feature is 'future' until its own test proofs exist. First store can be customized Yasmina (cake), but backend platform remains brand-independent.

## Red lines
No build-only proof. No fabricated data as customers. No production credentials. No guaranteed no vulnerabilities. No unnecessary service splitting. No simultaneous migration agents. No skipped security gate. No fake plugin hot-uninstall promise.

## Useful official references
https://docs.medusajs.com/resources/nextjs-starter
https://docs.medusajs.com/learn/fundamentals/admin/ui-routes
https://docs.medusajs.com/resources/admin-components
https://puckeditor.com/docs
