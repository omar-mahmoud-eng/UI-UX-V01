# 01 — Reference architecture and technical boundaries

## Deployment topology
Browser storefront -> CDN/reverse proxy -> Next.js web process -> authenticated Medusa Store API
Medusa API+Admin -> PostgreSQL, Redis, object storage; background Medusa Worker -> queue/jobs and outbound sandboxed integrations.
For initial local stage one Medusa process per official starter is acceptable. Production: documented server/worker modes as appropriate to measured traffic. Separate Postgres and Redis persistence, backups, TLS and log aggregation. One installed stack per customer.

## Domain ownership
Medusa Commerce Modules own product/catalog, carts, customers, identity, orders, pricing, tax abstractions, promotions, inventory, fulfillment and payment state as supported. Read official docs before writing any gap.
Custom domain modules own only their own models. Cross-module association via Module Links; data projection via Query; multi-step business operations via Medusa Workflows (with compensation when appropriate). No private foreign keys into other modules; avoid modifying Medusa migrations directly.

## Layering
- apps/backend: official Medusa app + src/modules, src/links, src/workflows, src/api, src/subscribers, src/jobs, src/admin.
- apps/storefront: official Next.js starter plus theme/page renderer and interactive features; server-first access, scoped publishable key.
- packages/ (when truly reused): contracts, UI primitives, standalone plugins, lint/test configs. Do not create package per tiny function.
- ops/: reproducible local/production setup, migration and disaster recovery scripts as they are implemented.
- docs/, tasks/: authoritative gates and architecture.
**Starter-generated layout has precedence over hypothetical folder tree.**

## Architectural invariants
1. No direct DB reads/writes between domain owners; no circular imports.
2. Custom shared contracts are versioned, request/response validated, documented and backward compatible.
3. Order total, taxes, promotions and inventory checks use Medusa workflow/state and source of truth, never duplicate custom services.
4. Transaction-bound operations favor DB atomicity and official workflow tools; external effects are after-commit where possible with retries/idempotency. Implement outbox only when a proven reliability need arises.
5. Read-only analytics projections may be eventually consistent; checkout stock/payment/order state cannot rely on stale cache.
6. Authorization enforced on server at every route/actor and object; frontend hiding is insufficient.
7. Cache invalidation and key namespacing documented; no sensitive PII in public cache.
8. Workers designed for retry, dead-letter observation and cancellation; duplicate deliveries must not duplicate billing/order side effects.
9. Every schema change migration-tested on clean and upgrade paths, including rollback/recovery plan.
10. Architecture lint and dependency checks are blocking gates after introduced.

## Extension boundaries
Modules: domain models+service, isolated according to Medusa. Plugins: reusable packaging of Modules/API/Workflows/Admin Extensions. Big features (Analytics, Page Builder, CRM) can be one coherent bounded-context Module with internal subfeatures; no microservice required. May scale read replicas, application/worker processes and external object storage before considering service extraction.

## Evolution thresholds
Only move to separate service when profiling confirms isolation need (CPU bound tasks, independent compliance/security boundary, separate deploy cadence, conflicting resource requirements) and impact analysis demonstrates interface stability. Introduce sharding or cells only on measured capacity and after explicit design/testing.

## ADR template
Problem | Alternatives (incl. reuse Medusa) | Decision | Trade-offs | Security/data impacts | Scalability evidence | Rollback/migration | Owner/date.
