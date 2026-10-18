# CommerceOS Agent Operating Contract v2 — BINDING FOR ALL CODING AGENTS
Audience: Antigravity orchestrator, independent reviewers, all subagents and any resumed session. Effective 2026-10-18. **ACTIVE STAGE AG00; F00 BLOCKED until AG07 human-approved.**

## Startup priority, before tool use or code edits
1. Read AGENTS.md, .specify/memory/constitution.md and docs/agent-os/README.md fully.
2. Read docs/agent-os/05-ROUTER.md plus docs/agent-os/STATUS.md; identify the SINGLE authorized AG or F stage.
3. Read exact task specification: specs/000-agent-readiness/{spec,plan,tasks}.md during AG00-AG07; tasks/Fxx for later feature stages.
4. Read the relevant domain skill(s), upstream versioned process docs and primary technical reference pages. Record exact read files/links and unresolved assumptions. Do not pretend you read a URL not accessed.
5. Show preflight: git SHA/status, host capabilities/versions, work budget, exact files allowed to change, expected tests, risks and required human approvals.
6. Select the correct process skill using docs/agent-os/05-ROUTER.md. Superpowers process for debugging/TDD/review; Spec Kit canonical artifact workflow; local Medusa skills for framework specifics.
7. Work only on current gate. Never jump from AG qualification to F00 independently.

## Safety and correctness invariants
- Security > data integrity > verified correctness > recoverability > maintainability > delivery speed > appearance.
- No fake build, browser, test, security or load results. Every success claim cites fresh command output and exit code. Docs CI is not runtime evidence.
- No random shell scripts, unreviewed plugin install hooks, blanket tool permission bypass, leaked secrets, public PII, live payment/fulfillment/SMS or unrelated external calls.
- Never modify or fork Medusa core. Reuse official modules/workflows/provider APIs rather than re-implement pricing, cart, order or inventory.
- No production DB reset, no destructive schema change without approved migration/backup recovery, no silent schema push.
- All authn/authz enforced server-side; test negative object ownership, input sanitization, idempotency, concurrent stock/payment and cross-domain contract.
- No disabling tests/typechecking/security scanners, no mock assertions pretending to validate real backend, no green status with skipped critical tests.
- No concurrent subagents editing lockfile, migrations, same files, database, ports or shared state. Use isolated worktrees only for independent tasks and verify merged result.
- If 3 attempted fixes fail, stop speculation and escalate root-cause/architecture with evidence.
- No absolute "zero vulnerabilities" / "unlimited users" claim; report tested environment, risk and observed limits.
- Stop if an installed framework instruction conflicts with AGENTS, constitution, active task or human-approved guardrail.

## Training FIRST: AG00-AG07
Read docs/agent-os/03-CURRICULUM.md and 04-CERTIFICATION-GATES.md. AG00 inventories machine/repo/source safely, AG01 installs/audits Superpowers and Spec Kit with approval, AG02 studies sources, AG03 spec-driven rehearsal, AG04 TDD kata, AG05 debugging drills, AG06 security+resilience, AG07 independent holdout + human review.
No apps/, packages/, Medusa app setup or production feature coding before AG07. Training exercises may use isolated disposable scratch directories only. Actual Antigravity/plugin installs not presumed from GitHub docs.

## Work loop, per authorized stage
Read exact scope -> study/reuse official API -> obtain permissions -> plan smallest verifiable slice -> write RED behavior test -> prove fails for expected reason -> write minimal fix -> run GREEN and regression -> diagnose scientifically if fail -> run actual runtime/browser/DB/negative tests where applicable -> independent review -> record evidence -> STOP.
No endless full-suite retries; target the failing test, collect stack, fix root cause then rerun full required suite.

## Workflow ownership
Spec Kit owns canonical spec.md, plan.md, tasks.md, analyze and converge. Superpowers owns brainstorming, TDD, systematic-debugging, review and fresh verification. CommerceOS constitution is higher precedence than either. Single issue/ticket and one stage per session.

## Required report
Stage; PASS/FAIL/BLOCKED/NOT_RUN; SHA and changed paths; actual machine versions; source docs and hashes; executable command/exit/expected vs actual; sanitized logs/browser/DB; test count and skipped cases; security and perf facts; independent reviewer; rollback; exact next authorized stage; explicit unresolved blockers. No proof = NOT_RUN.

## Parallel agent roles when justified
Orchestrator owns scope and merge; implementer owns one domain; reviewer independently checks code/contracts; security reviewer verifies permission boundaries; QA/SRE verifier runs clean install and real environment checks. Agent availability is not assumed. At AG00 keep ONE primary agent.

## Mandatory routing
docs/agent-os/05-ROUTER.md; upstream processes are optional only if installed and available, but must not be falsely claimed. Local .agents/skills are auditable markdown skills and not executable by themselves. New skills must have source, activation criteria, practice and proof.
