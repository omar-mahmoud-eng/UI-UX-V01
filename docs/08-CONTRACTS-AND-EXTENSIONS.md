# 08 — Medusa extension and module contract standard

## Naming & classification
Domain module: apps/backend/src/modules/<bounded-context>, using documented module service/data model patterns.
Cross-domain links: apps/backend/src/links; orchestration: src/workflows; APIs: src/api; admin widgets/routes: src/admin.
Reusable plugin: packages/plugins/<name> ONLY when extension needs to travel among installations or packages multiple Medusa customizations. Plugin shape follows official Medusa plugin docs; actual package structure vetted against pinned release.

## Contract for every custom module
ID & owner; purpose & boundaries; official Medusa features reused; owned entities; commands/queries; input/output schemas with validation; API routes & permission matrix; linked Medusa models; emitted/consumed events; workflow compensation; consistency requirement; idempotency key rules; file upload rules; data retention; explicit migrations; event/route version; feature flag semantics; health/metrics; test matrix; rollback/reinstall strategy.

## Evolution rules
- Use add-only contract evolution and expand/contract migrations; publish deprecation window and compatibility fixtures.
- Avoid importing other module private code or directly mutating another module's tables.
- No global singleton mutable state or process-local truth for inventory/order data.
- Plugin enable/disable means feature availability. Actual deinstallation can require data retention/migrations. Never silently drop schema.
- Extension cannot intercept/override sensitive price/payment flow without mandatory security review and provider idempotency proof.
- Admin/UI uses existing Medusa components and documented extension points; noncritical feature failure must fail gracefully if possible.

## First pilot: reviews
Create Reviews bounded context; customer reviews linked to purchased product as approved; secure moderation route and customer ownership; one module link, one workflow, one Admin widget or route, one store component, migrations and tests, clean fallback when disabled. Do not imply deployment hot-pluggability until measured.

## Plugin evaluation gate
Check package security, dependency risk, maintainership, compatibility, license, performance and rollback; avoid adding arbitrary third-party plugins to solve trivial problems.

## Contract test release
Every new module ships module isolated tests, HTTP/workflow tests and at least one real UI vertical E2E. Breaking changes require explicit major version and migration plan.
