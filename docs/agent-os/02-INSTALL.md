# 02 — Installation on Antigravity under review (AG01 only)
AG00 first: clean feature branch/worktree, git SHA and status; actual CLI/IDE availability; OS; Python >=3.11; uv; permissions. If Antigravity IDE exists but agy CLI is absent, report exact blocker instead of inventing CLI availability.

## Before touching machine
Read exact upstream release README, MIT license, plugin manifest, skill descriptions and executable hooks. Verify tag refs and network/permission scope. Save baseline file list/status and ideally a disposable OS sandbox. Do not grant global tool approvals or disable security guardrails.

## Official Superpowers installation path
Documented upstream command:
    agy plugin install https://github.com/obra/superpowers
This command may pull HEAD, NOT necessarily pin v7.0.0. Investigate actual CLI help before any alternative local-tag install; do not invent a tag flag. Record resolved commit, audit drift from reviewed tag, get approval for executable hooks. Verify a new Antigravity session recognizes using-superpowers and that a sample bug calls systematic-debugging BEFORE changes. Upstream Antigravity support is skill-discovery based; do not assume session-start hook.

## Spec Kit source install pinned to reviewed release
    uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v1.2.1
    specify version
For an existing repository, official procedure *only after branch and backup*:
    specify init --here --force --integration agy --non-interactive
The --force flag permits overwriting conflicting files. Immediately review git diff and restore/reconcile existing .agents/skills and .specify/memory/constitution.md if changed. Do not overwrite our safety constitution. Check agent is recent enough for .agents/skills discovery; confirm by inspecting installed CLI output.
In Windows choose documented --script ps if appropriate, on Unix --script sh if needed.

## Validation checklist
- Actual agy version and installed Superpowers skill discovery observed in fresh chat.
- Actual specify version and upstream source SHA recorded.
- Installed speckit-* skills present in .agents/skills and show valid Antigravity slash skill names.
- Existing 20 local skills and constitution preserved (upstream add-ons do not override).
- No unexpected hooks, altered secrets, broad tool bypass or unapproved global mutation.
- Command outputs, exit codes, path changes, approvals and rollback documented.

## Rollback
If conflict or install failure, revert installer changes from isolated branch, disable/uninstall only with verified CLI commands, do not remove unrelated files. Report BLOCKED until a reproduced compatible setup exists. This blueprint does NOT claim plugins already installed.
