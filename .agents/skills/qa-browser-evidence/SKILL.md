---
name: qa-browser-evidence
description: Use whenever claiming a feature really works, including first Medusa install.
---

# qa-browser-evidence — CommerceOS verified engineering skill

## Activation — mandatory
Use whenever claiming a feature really works, including first Medusa install. Read AGENTS.md, .specify/memory/constitution.md, docs/agent-os/05-ROUTER.md, the current AG/F stage and the named primary reference BEFORE actions. This skill is a scoped adapter: it cannot authorize a stage, install a third-party tool or weaken constitution requirements.

## Required preflight
State current gate, known-good git SHA/status, involved modules/data owners, actual host/framework versions, named source URL/release, allowed file paths, assumptions and missing evidence. If tool or environment unavailable, mark BLOCKED rather than pretending success.

## Procedure (in order)
Run and verify backend, Redis, Postgres, Admin and Next processes; real browser journeys with trace and network console inspection; verify persisted DB records and restart; correlate result with exact SHA/version; rerun full relevant regression.

## Security / scope red lines
Claim based on screenshot alone, compile-only PASS, fake response, tests from a different SHA. Also never commit secrets or user data, disable failing tests, or allow agent autonomy to cross current gate. Human permission for plugin install, destructive migration and live integrations is mandatory.

## Test-first and failure protocol
Specify a positive acceptance and at least two negative/edge cases; for code changes capture RED failing assertion before fix, smallest GREEN, regression and real runtime user path when applicable. On failure use upstream systematic-debugging: reproduce, isolate layers, one falsifiable hypothesis, experiment, record; after three incorrect fixes STOP and request architecture review.

## Evidence that proves completion
Exact commands/exits, accessible URLs, real console/network trace and DB evidence, skipped test list. Include exact commands, cwd, exit codes, source versions, sanitized logs/trace and reviewer verdict. A mock, documentation pass or typecheck alone is insufficient to declare a running feature.

## Independent assessor prompt
Ask another reviewer to invent one adversarial edge case outside the implementer's happy path, identify the intended source-of-truth, run the negative test against an isolated fixture, inspect the diff/permissions, and challenge any unsupported PASS claim.

## Canonical references
docs/05-TEST-STRATEGY.md
https://github.com/obra/superpowers/blob/v7.0.0/skills/verification-before-completion/SKILL.md
docs/agent-os/07-EVIDENCE.md
