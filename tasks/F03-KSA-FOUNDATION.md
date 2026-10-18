# F03 — Saudi localization, no production services
Prerequisites: F00,F01,F02 PASS. Scope only Saudi country profile; no CRM/CMS.
1. Compare Medusa native regions/currencies/tax/address capabilities with gaps. Configure KSA region + SAR, ar-SA default and en alternate, Asia/Riyadh business zone; write testable address and mobile normalization policy (without rewriting identity).
2. Define a small locale component contract and accessible RTL/LTR styling. Localize product UI, checkout, transactional templates and visible Admin extension screens added so far.
3. Verify KSA 13 region list from current official data and applicable VAT legislation; route price/tax totals through official Medusa modules. ZATCA compliance is a separate audit, never claim certified invoices in this stage.
4. E2E: locale switch persists, checkout total stable, format correctly, KSA region selection, invalid phone rejected, SAR decimals handled; no browser console errors.
5. Test data sanitized; migration fresh+upgrade, fallback translation policy, accessibility.
Gate: actual screenshots plus test output, no tax calculation fork, regress F01/F02, stop.
