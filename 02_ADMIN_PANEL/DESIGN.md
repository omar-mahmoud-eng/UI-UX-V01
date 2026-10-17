# DESIGN.md — Enterprise Medusa Admin design language

## Mission
A unified enterprise management experience for وَرْد وَخَشَب (temporary concept name; replace with approved brand). The dashboard visual concept is **not** a claim of built-in Medusa support. Custom enterprise modules require actual backend implementation and permissions. Arabic RTL by default; English LTR available.

## Tokens
- App canvas `#F7F7F5`; surface `#FFFFFF`; sidebar walnut `#322924`; hover `#EEEDE9`; primary `#4B312B`; secondary sage `#688478`; accent rose `#BF8594`; text `#242424`; border `#E5E3DE`.
- Status colors: success `#2E6A55`, warning `#A96A15`, danger `#AE3B42`, info `#4167A1`; communicate states with label and icon, never color alone.
- Arabic body IBM Plex Sans Arabic (fallback system sans), figures tabular aligned; title 24–30, table 14–15.

## Layout
- Persistent RTL right sidebar grouped by domain; expandable first/second/third-level nav with active highlight, favorite shortcuts, global search, role switcher, notification center, organization selector.
- Page header: breadcrumbs (at least 3 levels when applicable), title, contextual permissions, key actions and secondary action menu.
- Show date/time with Asia/Riyadh timezone; SAR values, VAT label, immutable IDs and operation provenance.
- Data grids with search, filter chips, sort, column selector, bulk tools, pagination, exports with role checks, details drawer.
- Forms: 2-column on desktop, inline validation, dirty-state warning, audit reason for sensitive edits, preview before save.
- Responsive to 1024px; provide mobile companion only for warehouse scanners, couriers and POS.

## Interaction & risk
- Configure views only; do not show false success on financial, tax, bank, inventory or authorization actions.
- Dangerous actions require confirmation and approval/audit trail; sensitive fields masked; permissions tested per action.
- States: empty, loaded, loading, partial success, validation error, integration unavailable, permission denied, offline where appropriate.
- Tooltips link to mock policy docs; make mock data clearly illustrative.
