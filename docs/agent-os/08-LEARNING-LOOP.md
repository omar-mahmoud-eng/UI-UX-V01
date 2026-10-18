# 08 — Measurable continuous skill development for a coding agent

## What "teach the agent" actually means
Skill files, tested heuristics, official references and persistent lessons make future sessions better. They do not update model weights or guarantee that the model learned from a single chat. The repository is the persistent engineering memory.

## Continuous improvement protocol
1. Detect bug, unsafe shortcut or misunderstood API during execution.
2. Classify: tool mismatch, version, missing context, architecture, test, security, data or performance.
3. Reproduce and write actual failing negative case.
4. Identify root cause and authoritative updated official documentation.
5. Modify ONE precise playbook rule/skill, add versioned reference, do not expand all skills blindly.
6. Execute before/after evaluation in scratch harness; check for regressions and overfitting.
7. Independent reviewer challenges the rule using an unseen variant.
8. Promote rule only after evidence; append decision log and update source hash/version. Stop repeated failure after three wrong fixes.

## Lesson card format
ID/date/skill affected; symptom; reproducible failure; source and version; cause; new short rule; counterexample; test ID; before score/after score; reviewer; expiry/revisit trigger. Keep unverified ideas tagged HYPOTHESIS.

## Anti-Goodhart safeguards
Do not score agent competence by Markdown page count, number of skills loaded, invented test counts or how many prompts it followed. Use blinded holdouts, error-rate, root-cause accuracy, regression preservation and safety violations. A fake PASS automatically fails qualification.

## Agent skill quality rubric
Activation description specific, smallest necessary context, official link, non-goals, API/data trust boundary, start conditions, exact sequence, negative tests, failure handling, reviewer checklist, proof format and examples. A skill without a runnable exercise is a reference memo, not a qualified skill.

## Handoffs
Every session emits a state packet: current gate, known-good SHA, last test command/output, unresolved blockers, selected source versions, only the next allowed task. The next agent MUST recheck on disk rather than trust summary alone.
