# 13 — Risk register, release and change-control policy

## High risks
- Generated but nonworking code: gate runtime browser proof at every step.
- Unpinned/incompatible dependencies: use official starter; lock, clean reinstall and verify supported Node/Medusa/Next combos.
- Cross-domain spaghetti: module boundaries/Medusa links/workflow tests, no private imports.
- Startup/migration failures: fresh DB and upgrade DB test before each release.
- Customer data or payment leakage: deny-by-default authz, secret & SCA scans, no live providers initially, log redaction.
- Overselling/duplicate orders/charges: atomic stock and idempotency, concurrent negative cases.
- Vulnerable or untrusted plugins: audit provenance/license/dependencies and trust boundary.
- Slow/fragile application under load: staging profile, query instrumentation, soak/fault testing, bounded concurrency.
- Lost data during updates: off-host backups, restore drill, expand/contract migrations.
- Vendor/deployment lock-in: portable VPS profile and a single business per install.
- Public repo secrets: automated scan, historical secret incident response if necessary.
- Unsupported Saudi legal claims: specialist compliance validation before launch.

## Change management
Each PR specifies changed scope, feature flags, data migrations, exact supported versions, new privileges, risk, test evidence, safe rollback and impacted workflows. Two independent reviews for auth/payments/financial logic and new privileged plugins. Any blocked critical test stops progression. An emergency fix uses same proof for the affected path and post-change full regression.

## Definition of Ready
Bounded story, Medusa reuse check, validated contract, DB ownership, test acceptance, complexity budget, rollout and rollback. If absent, return to design before generating code.

## Definition of Done
Code + tested path + security permission test + error handling + documentation + migration/rollback + observability + successful clean runtime + evidence SHA; no TODO/disabled tests concealing missing functionality.

## Release process
Staging -> smoke/E2E -> security triage -> load budget -> backup -> deploy -> monitor -> publish release notes -> post-deploy verification. Use immutable artifact SHA and release tags, not "works on my machine."
