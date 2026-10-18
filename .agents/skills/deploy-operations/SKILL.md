---
name: deploy-operations
description: Use on VPS/Hostinger staging, environment setup, service supervision and production readiness.
---

# deploy-operations — CommerceOS verified engineering skill

## Activation — mandatory
Use on VPS/Hostinger staging, environment setup, service supervision and production readiness. Read AGENTS.md, .specify/memory/constitution.md, docs/agent-os/05-ROUTER.md, the current AG/F stage and the named primary reference BEFORE actions. This skill is a scoped adapter: it cannot authorize a stage, install a third-party tool or weaken constitution requirements.

## Required preflight
State current gate, known-good git SHA/status, involved modules/data owners, actual host/framework versions, named source URL/release, allowed file paths, assumptions and missing evidence. If tool or environment unavailable, mark BLOCKED rather than pretending success.

## Procedure (in order)
Review portable Linux Node/Postgres/Redis/Medusa/Next support; configure least-privilege process manager/worker modes, TLS/firewall, secret env, logs/metrics; rehearse migration backup and release rollback; test actual store/admin on staging.

## Security / scope red lines
Exposed DB, inline secrets, destructive reset, deploy unreviewed plugins/live providers. Also never commit secrets or user data, disable failing tests, or allow agent autonomy to cross current gate. Human permission for plugin install, destructive migration and live integrations is mandatory.

## Test-first and failure protocol
Specify a positive acceptance and at least two negative/edge cases; for code changes capture RED failing assertion before fix, smallest GREEN, regression and real runtime user path when applicable. On failure use upstream systematic-debugging: reproduce, isolate layers, one falsifiable hypothesis, experiment, record; after three incorrect fixes STOP and request architecture review.

## Evidence that proves completion
Runbook, sanitized process statuses, health/browser smoke, restore time and rollback proof. Include exact commands, cwd, exit codes, source versions, sanitized logs/trace and reviewer verdict. A mock, documentation pass or typecheck alone is insufficient to declare a running feature.

## Independent assessor prompt
Ask another reviewer to invent one adversarial edge case outside the implementer's happy path, identify the intended source-of-truth, run the negative test against an isolated fixture, inspect the diff/permissions, and challenge any unsupported PASS claim.

## Canonical references
docs/07-DEPLOYMENT-SRE.md
https://github.com/obra/superpowers/blob/v7.0.0/skills/verification-before-completion/SKILL.md
docs/agent-os/07-EVIDENCE.md
