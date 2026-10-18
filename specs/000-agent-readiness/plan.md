# Feature 000 Engineering Plan — agent bootcamp before application code

**Design objective:** introduce curated methodology, prove tool integration and professional competence using isolated, reproducible kata and independent review. Not a programming sprint for CommerceOS.

## Architecture of the agent process
Human-governed constitution -> stage router -> canonical Spec Kit feature artifacts -> Superpowers process skills -> local domain playbooks -> real tool/runtime evidence -> independent qualification gate. Upstream frameworks are installed on the USER workstation only after source/hook audit; docs in GitHub don't magically install them.

## Staged implementation
AG00 inventory: inspect actual machine/repo and source release without altering product code.
AG01 install: review plugin manifest and requirements, initialize Spec Kit in separate worktree; verify skills discovery and no collision, record diff.
AG02 study: versioned official sources, nine competence cards + gap diagnosis.
AG03 SDD: toy spec with contradictory requirement, detect via analyze, map tests to requirements.
AG04 TDD: disposable TypeScript validator; capture failing and passing tests, injection of negative cases.
AG05 debug: sandbox Node-like API with connectivity/config/auth defects; one hypothesis at a time, third-fix escalation.
AG06 security/reliability: synthetic authorization, SSRF, concurrency, worker and resource tests with review.
AG07 independent board: holdout tasks and human signoff based on rubric.

## Contract and file boundaries
Persistent instructions in AGENTS + constitution; machine-local plugin installs audited; canonical spec artifacts under specs; shared local skills under .agents/skills. No application folders may be generated in AG stages. Do not copy upstream copyrighted assets without MIT attribution and source hash.

## Risks
Third-party script execution; CLI missing; version drift; Spec Kit --force overwriting .agents/skills and constitution; contradictory process mandates; agent scoring itself; fabricated logs; uncontrolled parallel agents. Mitigate with branch backup, explicit approvals, fresh evidence and reviewer.

## Verification plan
Static GitHub CI: docs and skill manifest/schema, links and stage state only. Practical qualification: real Antigravity and sandbox local commands, reviewed logs, scores and rejected bad cases. A static CI success cannot replace practical certification.

## Rollback
Revert AG worktree; remove added files using verified tool procedures; preserve archive and main, no destructive DB changes. Each external tool install must document its supported uninstall path and source SHA.

## Stop
F00 can begin ONLY with AG07 approved evidence by human. Never automatically run F00 from an agent training session.
