# F02 — First end-to-end independent Medusa custom Module
**Prerequisite:** F00 and F01 signed PASS.

## Objective
Demonstrate safe modular expansion by implementing ONLY one optional domain: Reviews (preferred) OR Wishlist (if signed decision). Never both in this phase.

## Scope
- Create Medusa documented module data model + service, isolated migrations; Module Link to product/customer where appropriate; official Query and Workflow for cross-module operation.
- Expose validated routes with authenticated ownership or moderation permissions; no direct privileged access from browser.
- Add small storefront component/interaction and optional Admin moderation widget, including loading/error states.
- Add isolated moduleIntegrationTestRunner test, workflow/API integration tests, Playwright E2E, negative BOLA/XSS/replay cases.
- Feature flag should hide entry when disabled; document that it is not hot uninstallation and data persists until deliberate migration.
- Clean upgrade migration and restart; existing F01 checkout/order regression remains PASS.

## Exit
Module contract filled per docs/08, complete E2E evidence, test and security report, rollback plan, ledger updated, no Medusa core modification.
