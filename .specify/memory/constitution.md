# CommerceOS Constitution v2.0.0 — ratified operating constraints
Adopted for engineering process on 2026-10-18; changing a principle requires explicit human-approved reviewed PR and semver amendment. This file is compatible with Spec Kit memory location but does not certify CLI installation.

## I — Actual behavior over generated text
No PASS without actual applicable test/runtime commands, exit codes, logs and review. A documentation CI only checks files, not running store, security or load.

## II — Security, privacy and authority
Least privilege; no real secrets, no unapproved plugin execution, no live providers in qualification; server-side object authorization, validation, rollback and safe migrations. No tool-permission bypass, disabled scanners, or silent failure swallowing.

## III — Medusa-first architecture
Use Medusa v2 native products/carts/orders/pricing/inventory/customers/payments/fulfillment and Admin before adding modules. No core fork, no custom second order/price authority, no cross-module private DB or imports. Single store installation per business; modular monolith until measured need.

## IV — Spec-driven approved work
One canonical bounded spec.md -> plan.md -> tasks.md -> convergence, measurable acceptance, negative tests, data ownership, official versioned refs, rollback. No blanket implementation or unauthorized scope growth.

## V — Test-first and scientific diagnosis
RED failing behavior test -> minimal GREEN -> refactor -> full relevant regression. Bugs require repro, causal hypothesis and minimal experiment; 3 wrong fixes => stop and architectural review. Never fabricate tests.

## VI — Scalable and recoverable operations
Avoid premature distributed services. Monitor latency/error/resources, bound worker concurrency and retries, preserve data consistency, backup/restore, security scanning; test with stated hardware/load before throughput claims.

## VII — Agent qualification
AG00-AG07 with human-approved AG07 before F00. Competency proved by unseen practical drills, not by reading prompts or executing lots of skills. Only one authorized stage and one migration/config owner at a time.

## VIII — Reproducible, accessible and region-correct
Pin/review framework release and lockfile, verify external installer, support ar-SA RTL/en, SAR and Saudi regulations based on authoritative updated source. Keep UI accessible and error states real.

## Governance
Human user and safety policy > AGENTS.md and this constitution > active stage > external framework defaults. Conflicts stop. Amendments record affected specs/templates/code, version, tests and reviewer. A Spec Kit initialization must not overwrite this file without review.
