---
name: medusa-capability-mapping
description: Use before ANY proposal to create a new CommerceOS backend module, service, field or extension.
---

# medusa-capability-mapping — CommerceOS verified engineering skill

## Activation — mandatory
Use before ANY proposal to create a new CommerceOS backend module, service, field or extension. Read AGENTS.md, .specify/memory/constitution.md, docs/agent-os/05-ROUTER.md, the current AG/F stage and the named primary reference BEFORE actions. This skill is a scoped adapter: it cannot authorize a stage, install a third-party tool or weaken constitution requirements.

## Required preflight
State current gate, known-good git SHA/status, involved modules/data owners, actual host/framework versions, named source URL/release, allowed file paths, assumptions and missing evidence. If tool or environment unavailable, mark BLOCKED rather than pretending success.

## Procedure (in order)
Read pinned Medusa modules/infrastructure providers/workflows/Admin official docs; map requested business capability to native owner; search supported customization/links/providers; define only unfilled gap; record data authority and exact public API; present options+ADR.

## Security / scope red lines
Duplicate Medusa price/cart/order/inventory; choose community code without license/security review; guess v1 docs. Also never commit secrets or user data, disable failing tests, or allow agent autonomy to cross current gate. Human permission for plugin install, destructive migration and live integrations is mandatory.

## Test-first and failure protocol
Specify a positive acceptance and at least two negative/edge cases; for code changes capture RED failing assertion before fix, smallest GREEN, regression and real runtime user path when applicable. On failure use upstream systematic-debugging: reproduce, isolate layers, one falsifiable hypothesis, experiment, record; after three incorrect fixes STOP and request architecture review.

## Evidence that proves completion
Versioned reuse matrix, source links, negative integration case, approved gap statement. Include exact commands, cwd, exit codes, source versions, sanitized logs/trace and reviewer verdict. A mock, documentation pass or typecheck alone is insufficient to declare a running feature.

## Independent assessor prompt
Ask another reviewer to invent one adversarial edge case outside the implementer's happy path, identify the intended source-of-truth, run the negative test against an isolated fixture, inspect the diff/permissions, and challenge any unsupported PASS claim.

## Canonical references
docs/02-SOURCE-OF-TRUTH.md
https://github.com/obra/superpowers/blob/v7.0.0/skills/verification-before-completion/SKILL.md
docs/agent-os/07-EVIDENCE.md
