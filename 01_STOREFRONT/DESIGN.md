# DESIGN.md — Storefront design language

## Brand & principles
وَرْد وَخَشَب (temporary concept name; replace with approved brand). Emotional, artisan-made gift commerce: flowers + natural wood; premium but approachable. **This is a proposed visual concept**, adjustable on receipt of a real logo or brand palette. Default RTL Arabic, optional LTR English; Saudi Riyals (ر.س).

## Color tokens
- Canvas / background: `#FAF6F0`
- Surface: `#FFFFFF`
- Primary dark walnut: `#4B312B`
- Rose accent: `#BF8594`
- Sage secondary: `#849184`
- Antique gold restrained highlight: `#BA985C`
- Text ink: `#292522`
- Border: `#E6DDD4`
- Error: `#A6383B`
- Success: `#2E6A55`

## Typography
- Arabic: IBM Plex Sans Arabic; fallback system Arabic-safe sans-serif.
- English editorial display: Cormorant Garamond; fallback Georgia.
- Body text Arabic 16–18px on mobile; compact labels 13–14px only when legible.
- Headings H1 42–64 desktop, 30–40 mobile. Avoid decorative text in checkout.

## Grid, shapes & motion
- Desktop 12-column responsive grid, max content 1320px; tablet 8, mobile 4.
- Radius: cards 16, buttons 12, editor panels 18. 8px spacing scale.
- Editorial asymmetry, large photography, detailed close-up of walnut grain and real flowers.
- 150–250ms restrained transitions, soft hover scale, no distracting parallax; respect reduced motion.

## Canonical commerce patterns
- Product imagery + personalization preview; always reveal customization cost and lead time BEFORE add-to-cart.
- Gift recipient shipping separate from buyer billing, gift card text, anonymous sender option, optional conceal pricing.
- Delivery date and slot represent estimated or actual availability honestly; no fabricated promise of next-day fulfillment.
- Perishable flowers show handling/substitution consent and city serviceability; wooden gifts show production lead-time and proof approval.
- Guest checkout, transparent itemization in SAR including VAT and delivery, bilingual navigation, visible customer help.
- Avoid fake urgency, fake stock counters, fake reviews, dark patterns, fake guaranteed delivery.
- WCAG accessible keyboard interactions, 44px touch targets, form errors associated with inputs.
