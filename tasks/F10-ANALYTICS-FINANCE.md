# F10 — Analytics, reporting, finance integration
Prereqs stable commerce/ops.
A. Implement read-only analytics projections and job scheduling for sales, cohorts, margin, funnel and inventory, with timezone/currency awareness. Source remains Medusa. Record consistency delay explicitly.
B. Reporting Admin: saved filters, date ranges, CSV export as background job, role-based access and masking of PII, audit.
C. Finance domain decision: integrate an approved accounting ledger/provider or implement isolated double-entry journal AFTER finance sign-off. Never assume checkout order state equals booked revenue.
D. Reconciliation: payments/refunds/fees/tax vs order and ledger; immutable audit, idempotent imports, manual discrepancy resolution.
E. KSA tax/e-invoicing legality scoped by verified ZATCA obligations, professional compliance validation and tested provider adapters.
Gate: reports reconciled to seeded facts; no report query overwhelms checkout; data export access tests; accountant/legal review for live finance.
