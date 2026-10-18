# Implementation Tasks: Toy Order Processor (Remediated — Complete Coverage)

**Feature**: `003-toy-order-processor`  
**Status**: `REMEDIATED & READY FOR VERIFICATION`  
**Date**: 2026-10-18  

---

## Task Breakdown

### Phase 1: Setup & Data Contracts
- [ ] **T-01**: Define TypeScript interfaces (`OrderPayload`, `OrderRecord`, `OrderStatus`) and Zod schema.
  - *Covers*: AC-01 input contract.
  - *Estimated Effort*: Small.

### Phase 2: Input Validation
- [ ] **T-02**: Implement `OrderValidator` function to validate line item counts, positive pricing, and ISO 4217 currency (`SAR`, `USD`).
  - *Covers*: AC-01, AC-02.
  - *Estimated Effort*: Small.

### Phase 3: State Management & In-Memory Storage
- [ ] **T-03**: Implement `InMemoryOrderStore` and `StateEngine` to manage deterministic state transitions (`PENDING` -> `CONFIRMED` or `REJECTED`).
  - *Covers*: AC-01.
  - *Estimated Effort*: Medium.

### Phase 4: Idempotency Subsystem (REMEDIATED — COVERS AC-04)
- [ ] **T-04**: Implement `IdempotencyManager` using `Map<string, { response: any, expiresAt: number }>` with 60-second TTL eviction and duplicate request short-circuiting.
  - *Covers*: AC-04.
  - *Estimated Effort*: Small.

### Phase 5: Verification Suite
- [ ] **T-05**: Implement automated test suite covering payload validation (AC-01), malformed inputs (AC-02), latency benchmarking $\le 50\text{ ms}$ (AC-03), and duplicate idempotency retries (AC-04).
  - *Covers*: AC-01, AC-02, AC-03, AC-04.
  - *Estimated Effort*: Medium.

---

## Acceptance Criteria Coverage Summary

| Acceptance Criterion | Description | Covering Task(s) | Status |
| :--- | :--- | :--- | :---: |
| **AC-01** | Valid payload -> HTTP 201 CONFIRMED | `T-01`, `T-02`, `T-03`, `T-05` | **100% Covered** |
| **AC-02** | Malformed input -> HTTP 400 Bad Request | `T-02`, `T-05` | **100% Covered** |
| **AC-03** | Latency SLA $p95 \le 50\text{ ms}$ under 100 requests | `T-05` | **100% Covered** |
| **AC-04** | Duplicate request within 60s returns cached response | `T-04`, `T-05` | **100% Covered** |
