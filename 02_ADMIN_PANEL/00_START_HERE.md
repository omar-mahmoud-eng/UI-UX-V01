# START HERE — Google Stitch / Enterprise Admin

## Goal
Create a unified operational UX design comprising **all 23 functional groups from the supplied 2026 enterprise checklist**, 150 named submodules, deep detail/configuration screens, plus artisan workshops and flower operations extensions. This is a DESIGN PACK; it does not imply that Medusa v2 already provides all the modules.

## Steps
1. Create a **separate Stitch project** named `Wood & Flowers — Enterprise Admin` and import/reference `DESIGN.md`.
2. Apply `00_MASTER_STITCH_PROMPT.md`. Use `01_ADMIN_NAVIGATION_AND_ROLES.md` for sidebar IA, shared shells, role-based views.
3. Generate in batches shown in `03_STITCH_BATCHES.md`; DO NOT ask Stitch to generate 500 screens at once.
4. Each screen has an individual paste-ready prompt under `SCREEN_PROMPTS/`. Each module also has a combined file under `MODULE_PROMPTS/`.
5. Prototype workflows from `02_OPERATIONAL_JOURNEYS.md`, and verify with `04_UX_ACCEPTANCE_TESTS.md`.
6. Integrate backend later using Medusa v2 official custom modules, routes and workflows, and dedicated enterprise services only where required.

## Disclaimer
Requirements taken from user-provided 23-section list. Backend capabilities and ZATCA/GDSN/GDSN Data Pool, payment escrow, telecom, WMS algorithms, IFRS15 and GDPR/PDPL must be implemented and validated separately. These are UX concepts, not certified ready-to-use functions.
