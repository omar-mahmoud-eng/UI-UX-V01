# AG02 Source Register: Authoritative Knowledge & Version Audit

**Project**: CommerceOS (`UI-UX-V01`)  
**Stage**: `AG02 — Source Literacy & Architecture Competence`  
**Date of Audit**: 2026-10-18  
**Auditor**: Principal Software Engineer (CommerceOS Engineering)  

---

## 1. Primary Source Inventory

| Category | Primary Official Source | Version / Release / Tag | Verified Capabilities (Facts) | Assumptions / Limitations (Explicitly Flagged) | Access / Audit Date |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Commerce Framework** | [Medusa Documentation](https://docs.medusajs.com/) | Medusa v2 (`@medusajs/framework` v2.x) | Modular Architecture, `@medusajs/framework` Service Factory, `createWorkflow`, `createStep`, `defineLink`, `RemoteQuery`, Admin Extensions via React components, Medusa Next.js starter integration, Medusa Worker mode (`medusa worker`). | Medusa v2 APIs differ fundamentally from v1 (e.g. Services are replaced by Modules with Data Models and Query Engine; no TypeORM entities). API signatures must strictly follow v2 documentation. | 2026-10-18 |
| **Medusa Workflows** | [Medusa Workflows Guide](https://docs.medusajs.com/learn/fundamentals/workflows) | Medusa v2.x Workflows Engine | Two-phase transaction compensation (`createStep` with rollbacks), idempotent execution steps, step input/output validation, workflow execution hooks, async step timeouts. | Workflows handle orchestration, not distributed two-phase commits across external non-transactional SaaS. Compensation steps must be idempotent. | 2026-10-18 |
| **Medusa Module Links** | [Medusa Module Links Guide](https://docs.medusajs.com/learn/fundamentals/module-links) | Medusa v2.x Remote Link & Remote Query | Inter-module loose coupling via Link definitions (`defineLink`), cross-module relational querying through `RemoteQuery` without foreign key schema dependencies. | Module Links maintain logical consistency; cascading deletes require explicit workflow orchestration rather than DB foreign key `ON DELETE CASCADE`. | 2026-10-18 |
| **Medusa Admin** | [Medusa Admin Guide](https://docs.medusajs.com/learn/fundamentals/admin) | Medusa v2.x Admin Extensions | Vite-based admin extensions, Custom UI widgets, nested settings routes, `@medusajs/ui` component library. | Core admin views cannot be arbitrarily rewritten; extension points are UI Widgets, UI Routes, and Setting Pages. | 2026-10-18 |
| **Medusa Testing** | [Medusa Testing Tools](https://docs.medusajs.com/learn/debugging-and-testing/testing-tools) | `@medusajs/test-utils` v2.x | Real PostgreSQL test runner, in-memory/isolated database instances, integration test harness for modules and workflows. | Integration tests require live Postgres connection; unit tests with mocks do not prove Medusa module link integrity. | 2026-10-18 |
| **Type System** | [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) | TypeScript v5.x (Strict Mode) | `strict: true`, `noImplicitAny`, `strictNullChecks`, Discriminated Unions, Template Literal Types, Branded/Nominal Types, `satisfies` operator. | Compile-time typing does not protect runtime I/O; Zod/Valibot runtime schema parsing is required at all API and network boundaries. | 2026-10-18 |
| **Specification Tool** | [Spec Kit](https://github.com/github/spec-kit) | v1.2.1 (Commit `9dca9bf42a031765ee5e5f2371137f2f26967e11`) | Markdown-based SDD pipeline (`speckit-specify`, `speckit-clarify`, `speckit-plan`, `speckit-tasks`, `speckit-analyze`), cross-artifact inconsistency detection. | Spec Kit analyzes specification artifacts; it does not generate production code directly without engineer/agent implementation. | 2026-10-18 |
| **Process Skills** | [Superpowers](https://github.com/obra/superpowers) | v7.0.0 (Commit `v7.0.0`) | TDD (`RED-GREEN-REFACTOR`), Systematic Debugging (4-phase scientific root-cause analysis), Verification Before Completion. | Auto-invocation hooks for Claude Code were safely pruned; skills run via Antigravity progressive disclosure in IDE. | 2026-10-18 |
| **Relational Database** | [PostgreSQL 17 Documentation](https://www.postgresql.org/docs/17/) | PostgreSQL 17.x | ACID transactions, MVCC, Row-Level Security (RLS), Isolation levels (`READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`), `EXPLAIN (ANALYZE, BUFFERS)`. | Default isolation level `READ COMMITTED` allows non-repeatable reads and phantom reads; concurrent checkout operations require pessimistic row locks (`SELECT ... FOR UPDATE`) or advisory locks. | 2026-10-18 |
| **Cache & Queue** | [Redis Documentation](https://redis.io/docs/latest/) | Redis 7.x | In-memory key-value store, atomic transactions (`MULTI`/`EXEC`), Pub/Sub, Lua scripting, BullMQ underlying message transport. | Redis is ephemeral by default unless configured with AOF/RDB; cannot be used as sole persistent storage for critical business orders. | 2026-10-18 |
| **Application Security** | [OWASP ASVS v4.0.3](https://owasp.org/www-project-application-security-verification-standard/) & [OWASP API Top 10 (2023)](https://owasp.org/API-Security/) | 2023 / 2024 Standards | Broken Object Level Authorization (BOLA/IDOR), Broken Authentication, SSRF, Unrestricted Resource Consumption, Injection, Security Misconfiguration. | Frontend access checks are purely visual; server-side authorization must verify object ownership on every single query/mutation. | 2026-10-18 |
| **Reliability & SRE** | [Google SRE Handbook](https://sre.google/sre-book/table-of-contents/) | Site Reliability Engineering Book | Service Level Objectives (SLOs), Error Budgets, Cascading Failure Mitigation, Graceful Degradation, Circuit Breakers, Bounded Retries with Exponential Backoff + Jitter. | 100% availability is impossible and economically irrational; error budgets must govern feature velocity and release gates. | 2026-10-18 |
| **Regional Regulation** | [Saudi ZATCA Fatoora Guidelines](https://zatca.gov.sa/) | Phase 2 (Integration Phase) | UBL 2.1 XML format, Cryptographic Stamp (ECDSA secp256k1), Invoice Hash (SHA-256), QR code generation (TLV structure), UUIDv4, sequential invoice counter. | Invoices cannot be modified or deleted once issued; credit notes / debit notes required for corrections. ZATCA clearance required for B2B; reporting within 24h for B2C. | 2026-10-18 |

---

## 2. Boundaries Between Verified Facts and Working Assumptions

### Confirmed Architectural Facts
1. **Medusa v2 Core Invariance**: Medusa v2 core packages (`@medusajs/medusa`, `@medusajs/framework`) are published npm libraries. Forking or patching core files in `node_modules` is strictly prohibited by Constitution Principle III.
2. **Modular Monolith Paradigm**: Medusa v2 runs in a single Node process (or dedicated API + Worker processes sharing the same codebase). Inter-module communication occurs in-memory via service resolution through the Medusa container, while data decoupling is enforced by separate database table prefixes and Module Links.
3. **No Direct Foreign Keys Across Bounded Contexts**: Foreign keys between Medusa core tables (e.g. `product`, `order`) and custom domain module tables (e.g. `cms_page`, `customizer_design`) are forbidden. All cross-module associations must use Medusa Module Links (`defineLink`) and be resolved via `RemoteQuery`.

### Explicitly Flagged Assumptions & Mitigations
* **Assumption 1**: Medusa v2 official Redis event bus handles all asynchronous events under expected production throughput.
  * *Verification/Mitigation*: If high event volume causes Redis stream lag, queue partitioning and dedicated BullMQ worker pools must be provisioned before considering an external Kafka/RabbitMQ cluster.
* **Assumption 2**: Single PostgreSQL database instance with connection pooling (`pgbouncer`) handles catalog reads and checkout writes up to 5,000 active concurrent shoppers.
  * *Verification/Mitigation*: Heavy read paths (CMS, Category browsing, Product details) must be cached via Next.js ISR/CDN and read-replicas. Checkout writes remain strictly transactional on the primary PostgreSQL node.
