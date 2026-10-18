# 01 — Upstream source selection and audit, researched 2026-10-18

## Name disambiguation
1. obra/superpowers is the mature original development methodology with roughly fifteen upstream skill files. Chosen primary. Latest examined release v7.0.0 published 2026-10-10, GitHub main inspected at bb92a77741419a4ab5f06e711a283343f1ada0c3, license MIT. https://github.com/obra/superpowers
2. chwzr/super-skills is a rebranded fork of obra/superpowers, not a separate authority; do not install a duplicate bootstrap copy.
3. TaylorChen/super-skills is a different, smaller cross-functional set; may inform research/product skills but NOT our core implementation process.
4. github/spec-kit is the official SDD toolkit. Examined release v1.2.1 published 2026-10-16; GitHub main inspected at c6a4c18f1d01a8bec241c618eb6dfea952508744; MIT. https://github.com/github/spec-kit
**Important:** main branch SHA and release tag ref differ; do not equate them. On AG01 verify the actual tag SHA and installed source digest.

## What was read in upstream
Superpowers skills: using-superpowers, systematic-debugging, test-driven-development, writing-plans, verification-before-completion, dispatching-parallel-agents and Antigravity tool mapping. Key ideas: call relevant process skill before coding; test RED-GREEN-REFACTOR; investigate root cause with reproducible evidence; after 3 speculative fixes escalate; fresh full verification BEFORE claims; parallelize only independent tasks, verify integration.
Spec Kit official docs: installation, existing-project adoption, quickstart, agent integrations, and constitution model. Actual workflow: constitution -> specify -> clarify -> plan -> checklist -> tasks -> analyze -> implement -> converge. Antigravity integration key agy installs slash skills under .agents/skills. CLI existing-project initialization can overwrite colliding managed paths; backup/branch and inspect diff.

## Complementary jobs
Spec Kit owns one canonical requirement/spec/plan/task chain. Superpowers owns HOW to execute with review, TDD, debugging and evidence. CommerceOS constitution/AGENTS controls permissions, Medusa reuse, data and acceptance. Avoid two conflicting implementation plans or autonomous next-stage commands.

## Supply chain
Before installing anything, audit license, source tag/commit, manifests, postinstall/hooks, dependencies, executable scripts, network behavior and requested permissions; compare changed files after install. Do not run arbitrary third-party scripts or turn off approval. Upstream v7 Antigravity bootstrap relies on skill discovery; DO NOT invent a session-start hook. Upstream might change; inspect pinned docs again at install time.

## Provenance and licensing
These files adapt ideas and link sources, not pretend external executable plugins are vendored. If upstream source is copied later, preserve license/copyright, path, tag/hash and local modifications and test compatibility.

Sources:
- https://github.com/obra/superpowers/releases/tag/v7.0.0
- https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/using-superpowers/references/antigravity-tools.md
- https://github.com/github/spec-kit/releases/tag/v1.2.1
- https://github.com/github/spec-kit/blob/main/docs/installation.md
- https://github.com/github/spec-kit/blob/main/docs/guides/existing-projects.md
- https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md

## Honesty
No actual Antigravity install or runtime test has been done by writing docs on GitHub. Only AG01 on the user's machine can prove integration.
