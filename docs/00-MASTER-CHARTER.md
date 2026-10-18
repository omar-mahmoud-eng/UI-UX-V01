# 00 — Product charter, non-goals, governing constraints

## Product
CommerceOS is a **self-hostable single-business e-commerce operating system**: customer storefront, Medusa commerce backend, complete administrative experience, configurable store design, and optional domain modules (CRM, automation, finance, operations, B2B, POS, analytics, etc.). Installation per client with their own hosting, database, assets and business configuration. Optional multi-store features only if proven need; no centralized SaaS control plane in v1.

## Success measures
- Actual repeatable install, upgrade, backup/restore on documented supported Linux environment.
- Successful real browser flows with persisted test records and no live payment or carrier calls until approved.
- Functional access control and secure defaults; evidence-based assurance, not zero-risk guarantees.
- High maintainability: minimal Medusa customizations, stable public contracts, strict ownership boundaries and explicit migrations.
- Horizontal application and worker scaling where architecture supports it; database and storage bottlenecks recognized and measured.
- Feature growth by independent domain modules with contract/version tests and backward-compatible changes.

## Scope
Phase 0-1: runnable backend+Admin+storefront+catalog/cart/simulated order, single SAR store default ar-SA with en support planned.
Later: administration, design system, CMS/page builder, personalization, marketing, CRM, inventory logistics, accounting, helpdesk, reports, B2B, automation, wholesale, subscriptions, POS, extensibility, integrations.
SaaS billing, cross-tenant shared DB, universal ERP parity and guaranteed massive throughput are **NOT** initial deliverables.

## Key decisions
- Platform: official Medusa v2 app, Next.js storefront, TypeScript strict mode; Postgres and Redis.
- Pattern: Medusa-native domain modules and workflows; plugins only for reusable bundles; background workers; modular monolith.
- Source of truth: Medusa for built-in commerce facts; avoid shadow orders/pricing/inventory/payment states.
- Single PostgreSQL logical database per store, module-owned models; enforce relationships via supported Module Links/Query/Workflows. Object storage for media with safe policies.
- Use existing Medusa Admin first; customize via documented Admin Extensions, not wholesale replacement.
- Prefer native OS services or containers based on host support; do not require Docker for local development; no vendor-specific hosting dependency.
- Architecture decisions must have ADR with rationale, proof of need and rollback impact.
- Keep all secrets outside repo; public repository.

## Principles
Working software over agent promises; small reversible PRs over giant generated rewrites; correctness and transaction safety over premature performance optimization; measurable SLOs over slogans; proven provider integration over inventing core primitives.

## Milestone honesty
Planning files are requirements, not implementation; future feature descriptions are backlog, not demonstrated functionality. As of this file creation, none of the application gates is passed.
