# CommerceOS — Agent-Qualified Medusa-First Engineering Blueprint
**Status: AGENT TRAINING BLUEPRINT ONLY — AG00 NOT_STARTED, AG07 NOT CERTIFIED, F00 LOCKED. No Medusa application is installed.**  
**Repository:** UI-UX-V01 (reused by explicit owner request)  
**Reset date:** 2026-10-18  
**Authoritative language:** Architecture and rules in English; operational handoff also in Arabic.  
**Deployment shape:** One independent store + Admin per client/hosting; extensible, not a global multi-tenant SaaS in v1.

## Mission
Build an actually running, maintainable, secure-by-design, production-operable e-commerce platform on top of the official Medusa v2 app and official bundled Next.js starter. Integrate future modules progressively without modifying Medusa's internals. Do not declare zero vulnerabilities, unlimited capacity, or readiness without evidence.

## Starting points — AGENT FIRST, then application only after certification
1. Read [AGENTS.md](AGENTS.md), [.specify/memory/constitution.md](.specify/memory/constitution.md), [START_AGENT_AR.md](START_AGENT_AR.md) and [Agent OS v2](docs/agent-os/README.md).
2. Read [docs/01-ARCHITECTURE.md](docs/01-ARCHITECTURE.md), [docs/02-SOURCE-OF-TRUTH.md](docs/02-SOURCE-OF-TRUTH.md), [docs/03-MODULE-CATALOG.md](docs/03-MODULE-CATALOG.md).
3. Read [docs/04-ROADMAP-AND-GATES.md](docs/04-ROADMAP-AND-GATES.md), [docs/05-TEST-STRATEGY.md](docs/05-TEST-STRATEGY.md), [docs/06-SECURITY-BASELINE.md](docs/06-SECURITY-BASELINE.md).
4. Begin ONLY AG00 (agent environment inventory) using [specs/000-agent-readiness/tasks.md](specs/000-agent-readiness/tasks.md), [training gate requirements](docs/agent-os/04-CERTIFICATION-GATES.md) and [live state](docs/agent-os/STATUS.md). F00 implementation explicitly LOCKED until AG07 is human-approved.

## Non-negotiable rules
- Prefer existing, documented Medusa modules/providers/workflows; build only real gaps.
- No blanket rewrites, fake endpoints, hard-coded success, placeholders passing as completed work, or tests asserted without execution.
- One vertical slice at a time, runnable and tested in an actual browser. Preserve known-good commits.
- No payments or shipping provider live credentials in early stages. No production customer data in tests.
- Do not over-architect: single deployable Modular Monolith initially; optional separate worker process for jobs. No Kubernetes, Kafka, CQRS, sharding, event sourcing or microservices without measured necessity and an approved ADR.
- Database changes: migrations only, with recovery procedure, no destructive changes by default.
- Block merge on security critical/high findings, startup errors, broken checkout, unsafe access control, or unverified migrations.
- Public repository: **NO credentials, private data, .env, tokens or sample real secrets.**

## Documentation index
- docs/00-MASTER-CHARTER.md — purpose, constraints and outcomes.
- docs/01-ARCHITECTURE.md — concrete module boundaries, dependencies, data, extension strategy.
- docs/02-SOURCE-OF-TRUTH.md — use Medusa rather than duplicating features.
- docs/03-MODULE-CATALOG.md — complete long-term functional map.
- docs/04-ROADMAP-AND-GATES.md — sequential executable stages.
- docs/05-TEST-STRATEGY.md — tests and measurable gates.
- docs/06-SECURITY-BASELINE.md — threat model and assurance.
- docs/07-DEPLOYMENT-SRE.md — VPS, scale, monitoring, backup, release.
- docs/08-CONTRACTS-AND-EXTENSIONS.md — module contract & lifecycle.
- docs/09-SAUDI-LOCALIZATION.md — Saudi deployment requirements.
- docs/10-UI-ADMIN-BUILDER.md — storefront, admin, CMS, customization.
- docs/11-AGENT-OPERATING-SYSTEM.md — control protocol for Antigravity.
- docs/12-REQUIREMENTS-MATRIX.md — traceability and acceptance.
- docs/13-RELEASE-AND-RISK.md — risk, rollback and change management.
- tasks/F00-BASELINE.md — first agent task, stop point.
- tasks/F01-COMMERCE-SMOKE.md — actual seeded storefront/cart/checkout.
- tasks/F02-CUSTOM-MODULE.md — first extension end to end.
- docs/14-OFFICIAL-REFERENCES.md — source links.
- docs/15-CHANGE-LOG.md — actual execution ledger.
- .github/pull_request_template.md — review checklist.

## Definition of success
Not number of features or files. Success is repeatably booting the whole system, an actual transaction through the UI against PostgreSQL, secured API paths, verifiable automated tests, a deployable documented release and recovery, and modular growth without regression.

## Current state
Planning package written; legacy UI/UX prompts removed from main branch via replacement tree. Old content retained on archive/pre-commerceos-reset-2026-10-18. **No application baseline is installed yet. No runtime/security/load checks have been performed.**

## Advanced execution package (also planning only)
- tasks/F03-KSA-FOUNDATION.md through tasks/F12-CAPACITY-SECURITY-GO-LIVE.md: later gates, executable only after predecessors pass.
- .agents/skills/*/SKILL.md: 12 controlled local Antigravity playbooks; see .agents/README.md.
- docs/19-EXECUTION-PRIMER.md and docs/20-DOMAIN-BOUNDARIES.md and docs/21-COMPATIBILITY-AND-REUSE.md: implementation protocol, complete domain map and known Medusa version traps.

## Agent OS v2: Superpowers + Spec Kit integration (primary workflow)
The first task is to qualify Antigravity, NOT to build the store. The v2 package includes 20 project-specific local skills under .agents/skills, a nine-competency curriculum, 8 mandatory practical gates AG00-AG07, threat-model and reliability labs, a ratified engineering constitution, a canonical Spec Kit-compatible feature-000 spec/plan/tasks, an installer review guide and structural CI. Official Superpowers (obra/superpowers v7.0.0) and Spec Kit (github/spec-kit v1.2.1) have been studied and integrated at PROCESS level; executable upstream plugins are NOT installed in the user's Antigravity environment yet. AG01 installs and tests them with explicit review. See docs/agent-os/README.md and START_AGENT_AR.md. F00 remains blocked until AG07. 
