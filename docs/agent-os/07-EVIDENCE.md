# 07 — Proof ledger, claims and reviewer obligations

## Status words
NOT_STARTED, STUDIED, IN_PROGRESS, PASS, FAIL, BLOCKED, NOT_RUN. Documentation integrity is not software functionality; static build does not prove login or checkout.

## Each evidence record
Stage + task ID; git SHA/dirty files; source versions and URLs read; OS/hardware; current tool versions; exact command with cwd and exit code; expected vs actual result; sanitized stdout/stderr path; browser actions/screens/traces/HTTP; DB migration and row proof; security negative tests/findings; load scenario/resources/p95/error where applicable; reviewer and confidence/limitations; rollback; approved next stage. Never commit tokens, cookies or real client data.

## Evidence standards
To claim install, show clean lockfile install/exit. To claim API, show running GET and response. To claim Admin, show logged-in browser interactions plus denied unauthorized API. To claim checkout, show a persisted synthetic order in DB/Admin after restart. To claim security, show threat matrix and reproduced negative cases; no "0 vulnerabilities" promise. To claim high load, show VUs/data/host, p95/p99, error and resource metrics. To claim an agent skill installed, show fresh session discovery.

## Review
Independent reviewer examines diff and reruns representative checks, inspects browser console/network and database, marks skipped/failing tests visibly. Reviewer MUST NOT trust agent PASS text. Reviewer's absence must be disclosed as lower assurance, and AG07 requires human signoff.

## Log schema template (EXAMPLE, not performed)
- Stage AG04; status NOT_RUN
- Command: pending, Exit: null; target scratch quantity validator
- Expected RED on invalid input, then GREEN, negative tests and full suite
- Actual proof: NONE
- Reviewer: NONE; next stage: unauthorized
This is not execution evidence.

## Public GitHub policy
Only sanitized proof; full traces/recordings with auth headers or secrets stay in approved private storage. Never include environment values. No personal data or credentials.
