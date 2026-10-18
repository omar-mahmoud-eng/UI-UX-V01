# 09 — Canonical Spec Kit protocol for CommerceOS

## Files and ownership
.specify/memory/constitution.md is our binding project constitution. Each bounded feature lives in specs/NNN-name/spec.md, plan.md, tasks.md and checklists/ if relevant; source-of-truth code remains existing official Medusa modules. Do not generate one spec for all CommerceOS at once: split by accepted vertical F stage.

## Flow
(0) Ratify constitution once; human approves security/data principles.
(1) Specify what and why, observable user stories, success and failure cases; no made-up API names.
(2) Clarify unknown behaviors before planning; never reask settled decisions.
(3) Plan how: compare official Medusa, data ownership, contracts, migration, authz, deployment, rollback, error budget.
(4) Quality checklist: test spec clarity/consistency, not implementation.
(5) Tasks: break into small dependency-ordered tasks, exact modified paths, tests and acceptance, one owner.
(6) Analyze: cross-artifact consistency and requirement-to-test completeness; fail if missing.
(7) Implement ONLY if AG07 passed and current F stage explicitly authorized, using Superpowers test-first and debugging skills.
(8) Converge: inspect actual implementation vs spec/tasks, create bounded follow-up within same stage for real gaps. Convergence is not a substitute for runtime/security evidence.

## Agent syntax
Official Spec Kit Antigravity integration key agy uses skills named /speckit-constitution, /speckit-specify, /speckit-clarify, /speckit-plan, /speckit-checklist, /speckit-tasks, /speckit-analyze, /speckit-implement and /speckit-converge after installation. Some docs for other integrations use dots; use actual discovered tools.

## Existing project caveat
Official adoption runs specify init --here --force --integration agy only on backup feature branch with file-diff review. It can overwrite managed paths. Preserve our local skills, AGENTS and constitution; restore collisions and seek approval rather than silent overwrite.

## How it complements Superpowers
Spec Kit produces the single canonical spec/plan/tasks. Superpowers provides brainstorming, writing clear task steps, TDD, bug diagnosis, verification, independent review. No second authoritative plan and no automatic execution beyond current stage.
Sources: https://github.github.com/spec-kit/quickstart ; https://github.com/github/spec-kit/blob/main/docs/guides/existing-projects.md
