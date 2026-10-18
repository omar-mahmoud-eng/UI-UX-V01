# 18 — Architecture decisions and review log

## ADR-001: Medusa-first modular monolith (ACCEPTED, planning)
Context: multiple earlier AI-generated builds were not runnable. Decision: official Medusa v2+official bundled Next.js starter; extend using Medusa Module Links/Workflows/Plugins; no core fork, no ERP rewrite. Consequence: constraints from Medusa API, but lower initial integration and operational complexity. Validation: F00-F02 runtime gate.

## ADR-002: one independent client installation (ACCEPTED)
Decision: client-owned hosting/database and assets, optional modules, single deployment unit; no shared multitenant SaaS core in v1. Validation: clean-install portability.

## ADR-003: avoid premature distributed infrastructure (ACCEPTED)
Decision: no Kubernetes/Kafka/microservices/sharding/cells until profiling and independent operational capacity justify. Scale stateless processes, queries, cache, workers and DB first. Validate F04/F12.

## ADR-004: page builder selection (PENDING)
Candidate Puck; evaluate official release/license, compatibility with Next/React/Medusa Admin, schema validation and security sandbox. Choose by F05 proof; never assert Puck is chosen merely because name appears in past plans.

## ADR-005: package manager/Node and exact Medusa version (PENDING, F00)
Check verified official supported engines and framework starter, select one package manager and lock toolchain, pin reproducible versions. No hardcoded latest release claim. Store actual Node/Postgres/Redis versions and decision.

## ADR-006: CMS and media persistence (PENDING, F05)
Compare local and S3-compatible storage; choose off-host data protection, SSRF/file threat model, rollback and portability.

## ADR-007: payments/shipping implementation (PENDING, later)
Use documented Medusa providers with sandbox and risk review; real KSA integration after explicit approval.

## ADR template for new decisions
Number/date/status/owner | problem | alternatives | documented Medusa reuse | decision | compatibility | data migration | security | perf evidence | rollback | follow-up.
