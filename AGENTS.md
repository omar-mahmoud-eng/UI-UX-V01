# Mandatory instructions for ALL AI coding agents (Antigravity, subagents, etc.)

Priority: security > verified correctness > recoverability > maintainability > delivery speed > visual polish.

## Mandatory reading before touching code
Read README.md, START_AGENT_AR.md, docs/00 through docs/15, current tasks/Fxx file, and the actual Medusa docs relevant to the task. Print a 10-line comprehension summary citing project file paths and list of exact files you intend to edit. Do not claim reading unseen files. The task gate controls scope.

## Hard prohibitions
1. NO blanket implementation of the roadmap; execute only the assigned task.
2. NO modification, fork or copy of Medusa core internals; use official extension points.
3. NO mocked successful runtime/CI/browser results, fabricated security assurances, or fake data represented as production.
4. NO bypassing or silencing failing tests, TypeScript errors, ESLint, scanners or migrations; if blocked, report evidence.
5. NO introducing new frameworks/dependencies without audit of Medusa-native alternative, ADR and maintainer approval.
6. NO commits of secrets, PII, credentials, private keys, artifacts, logs with tokens, database dumps.
7. NO uncontrolled parallel agents touching same directories/DB/migrations.
8. NO uncontrolled schema edits: generate and test proper migrations, backup before irreversible changes.
9. NO direct imports of private module internals across domain boundaries, direct cross-module tables, circular dependencies or expensive synchronous side effects.
10. NO claim of 100% security or zero crashes; provide risk/coverage/measurement instead.
11. NO production payments, SMS, courier, WhatsApp or external messaging without explicit feature approval and safe credentials.
12. NO deletion/force push of reference branches, archived materials, or unrelated resources.

## Work protocol
- Identify current stage in docs/15-CHANGE-LOG.md; if its status is not PASS, do not proceed.
- Preflight: inspect repo, pinned versions/lockfile, toolchain, DB, Redis, host capabilities, clean git status.
- Plan changed files, dependencies, API/domain contract and test cases before coding.
- Write smallest testable vertical slice; aim for focused PRs.
- Validate: typecheck, lint, unit, module/integration, Playwright E2E (where applicable), security checks, clean install, actual runtime, migrations, and regression. No green claims without command output/exit codes.
- Browser proof: backend /health; Admin /app login; real product detail; cart + simulated checkout; capture sanitized screenshots/videos and HTTP evidence.
- Always record environment, test command, exit status, migration version, failures, changed paths, next exact command, rollback SHA.
- Agent must stop at task gate. Release/merge only on human-approved passing proof.

## Parallelism
Parallel tasks permitted only after folder ownership allocation. Each agent owns unique branch/worktree; one agent at a time owns core config/dependencies/migrations. Integration reviewer checks contracts and test evidence before merge.

## Required task report format
Stage / status PASS-FAIL-BLOCKED / commit SHA / what changed / environment versions / executed commands and exit codes / URLs tested / screenshots or traces / tests pass-fail-skipped / vulnerabilities open / known limitations / rollback / next single task. If not executed, state NOT RUN. Never substitute planning for verification.
