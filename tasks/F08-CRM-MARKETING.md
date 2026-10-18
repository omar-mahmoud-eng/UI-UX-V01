# F08 — CRM + marketing + automation MVP, safely isolated
Prereqs stable base. Build sequentially, not one giant PR.
A. Customer profile enrichment as Medusa-linked domain records: interactions, tags, segments, notes, opt-in/opt-out, retention, access controls; preserve customer source of truth.
B. Customer segments and reporting using efficient query/read models. Role/data object tests.
C. Notification adapter sandbox for email/SMS/WhatsApp; idempotent jobs, retries, suppression/unsubscribe, consent and regional data policy. No live campaigns until approved.
D. Marketing triggers: cart abandoned, order confirmation, delivery updates (simulated), winback, coupons, loyalty. Add rule editor only after safe event processing proven.
E. Audit, throttling, duplicate deliver and unsubscribe tests, no leaked PII in logs.
Gate each subtask: scheduled events real and traceable in test/sandbox; unrelated checkout unaffected; security+deliverability controls proved.
