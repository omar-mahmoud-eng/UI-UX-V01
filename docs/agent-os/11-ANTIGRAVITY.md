# 11 — Antigravity-specific integration and tool behavior

## Verify tool availability
Inspect agy --help, agy plugin install --help, installed version, IDE and sandbox permissions on actual machine. If user has IDE but not CLI, state that and follow supported UI/manual read fallback; never fabricate tool calls. Use read-only research tool for documentation, actual shell only with approved scope.

## Superpowers mapping from upstream
The upstream Antigravity skill reference says supported task tracking in CLI variants uses a task artifact via write_to_file with IsArtifact true and ArtifactMetadata ArtifactType task; manage_task handles background processes, not task checklists. Its subagent mapping refers to invoke_subagent type research/read-only and self/full, WHEN ACTUALLY AVAILABLE. Check current harness support before invoking. If absent use scoped markdown task file rather than pretending agents ran.

## Parallel isolation
No agents edit same files/lockfile/database/migrations concurrently. Each agent receives only relevant context and exact change paths, own branch/worktree, test environment and proof. One integration reviewer reruns combined smoke/E2E. Not every task benefits from multiple agents.

## Session entry
Read root rules + constitution + current gate, record git SHA, list discoverable skills, identify actual relevant Superpowers/Spec Kit/domain skills, map to expected commands, stop point. Never load 30 skill files blindly to impress the user.

## Security
Never set SPECKIT_AGY_ALLOW_ALL_TOOLS=1, SPECKIT_INTEGRATION_AGY_ALLOW_ALL_TOOLS=1, or --dangerously-skip-permissions for this project. External code hooks require review and explicit permission. No silent shell profile/global configuration changes.

## Session exit
Report stage status, exact commands+exit, sanitized traces, changed paths, unresolved defects, rollback SHA and next authorized single task. AG07 and feature-gate human approval remain necessary.
