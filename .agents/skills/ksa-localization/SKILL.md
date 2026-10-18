# KSA Arabic commerce & compliance
## When to invoke
Any Saudi customer/store/accounting requirements.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Review current ZATCA and business policies; configure Medusa SAR/region, ar-SA RTL/en, +966 phone, National Address fields, timezone and VAT via official modules; test locale and checkout totals.
## Prohibited
Hard-coded legal compliance, financial totals computed in browser, unverified VAT exemptions, real providers in test.
## Evidence
RTL+English Playwright, backend tax total tests, current regulation source and business signoff.
## References
https://docs.medusajs.com/learn/fundamentals/modules
