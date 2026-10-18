# 09 — Saudi Arabia commerce profile

## Defaults
KSA sales region with SAR currency; ar-SA as default locale with correct RTL/layout/typography and en available; Asia/Riyadh business time zone; translated store/Admin-facing user content where practical, locale-specific numbers/dates without altering stored UTC instants.

## Address & phone
Support 13 administrative regions, city/district/street/building details as needed for the shipping provider and Saudi National Address; validate Saudi phone +966/05 inputs with a reviewed normalization library, not simplistic regex only; accessibility and direction-switch E2E.

## Taxes and invoicing
Configure VAT rates only after verifying current ZATCA rules for the business and category; avoid hard-coded calculation outside Medusa tax authority. Saudi VAT standard 15% historically, subject to current legal confirmation at deployment. ZATCA e-invoicing and phase obligations must be assessed by registered tax status and regulatory rules; do not claim compliance via merely generating a PDF invoice. Invoice fields, QR, credit notes, audit/retention and fiscal integrations require audited acceptance.

## Payments/shipping
Initial environment uses only sandbox/manual test flows. Later payment rails (mada/cards/wallets) and local courier services via supported providers and explicit credential handling; webhooks signed/verified, duplicate deliveries safe, refunds/cancellations reconciled. COD may need OTP/WhatsApp provider and explicit consent controls.
No real payment or shipping API calls during F00/F01.

## Commerce content
Price inclusive/exclusive display, fees/shipping estimate, return/refund/terms/privacy in Arabic and English after legal review; no deceptive promotional prices; accessibility and mobile-speed budgets.

## Gate
RTL/LTR screenshots and interactive E2E, SAR tax totals from backend, zone and currency fallback, phone normalization tests, Arabic email templates and legal compliance review before production.
