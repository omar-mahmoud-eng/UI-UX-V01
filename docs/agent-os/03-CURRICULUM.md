# 03 — Engineering curriculum: from agent to evidence-backed senior engineer
This course changes durable prompts/playbooks and practical task behavior; it does NOT retrain the foundation model weights. An agent may forget the conversation, so source-of-truth must be in versioned repo files and tests.

## Universal 7-step lesson loop
1. Diagnose knowledge gaps with a short pretest; label unknowns.
2. Read pinned primary official docs; record exact page/version.
3. Restate invariants, tradeoffs and a counterexample in own words.
4. Execute one safe isolated kata with a failing test first, then passing test.
5. Independently review the diff and run negative cases.
6. Record mistakes, root cause and targeted skill/rule improvements.
7. Re-test on a NEW holdout task to measure transfer; pass only with evidence.

## E1 Foundations / TypeScript architecture
Study TS Handbook strict mode, contracts, DDD bounded contexts, SOLID pragmatically, composition over inheritance. Kata: implement two separately owned domain modules with public DTO contract and tests; attempt a forbidden private cross-module import and explain why rejected.

## E2 Git/reproducibility
Study git worktrees/revert/merge, package lockfiles, CI rules. Kata: isolated worktrees, conflict/resolution, rollback a bad change and reinstall from lockfile. No force push to main.

## E3 Spec-driven requirements
Study Spec Kit constitution/specify/clarify/plan/tasks/analyze/converge. Kata: spec with measurable acceptance and traceability; inject contradiction and detect before implementation.

## E4 Test-driven development
Study Superpowers TDD/verification, Medusa official integration runners, Playwright. Kata: real failing test of input validation, GREEN minimal implementation, refactor; mutation test and negative case; distinguish unit/mock success from end-to-end proof.

## E5 Systematic debugging
Study Superpowers systematic-debugging/root-cause, Node diagnostics, Postgres connectivity/logs. Kata: distinguish port collision, wrong DB URL, Redis unavailable, version incompatibility, auth 401/403. Capture error, one hypothesis/test, avoid random reinstall or timeout increases.

## E6 App security
Study OWASP ASVS/API Top 10, least privilege, CSRF, SSRF, XSS, authz, supply chain and secrets. Kata: synthetic customer A must not read customer B object; test malicious image URL and duplicate action. Deny on server.

## E7 Reliability and capacity
Study Google SRE SLO/error budgets, Medusa deployment, PostgreSQL EXPLAIN and pooling. Kata: synthetic workload with specified host/data; measure p95/error, find one bottleneck, retest. Never claim infinity scale.

## E8 Medusa mastery
Study installed Medusa v2 official modules, links, query, workflows, Admin extensions, infrastructure providers and bundled Next starter. Kata: create Medusa-native ownership matrix for catalog/cart/order/price/inventory/customers/payments, and show exact custom module gap; no core fork.

## E9 Extension and operations
Study modular monolith, ADR, safe migrations, rollouts/rollback, worker idempotency and plugin lifecycle. Kata: evaluate uninstalling a CRM plugin holding tables, protect data, explain feature-disable vs schema removal.

## Rubric per competence
0 no evidence; 1 can repeat terms; 2 identifies APIs; 3 works with prompts and tests; 4 autonomous test-backed correct tradeoff; 5 succeeds in unseen holdout with critical edge cases. Require >=4 on E1-E9 plus AG07 total >=90/100. If below, prescribe remediation and novel retest, NOT endless reading.
