# Feature Specification: Isolated Toy Order Processor

**Feature Identifier**: `003-toy-order-processor`  
**Stage**: `AG03 — Spec-Driven Drill`  
**Architecture Scope**: Isolated in-memory rehearsal module (Zero CommerceOS production code; Zero Medusa runtime).  
**Status**: `DRAFT (UNDER SPEC-KIT REVIEW)`  
**Created**: 2026-10-18  

---

## 1. Problem Statement & User Stories

### User Story 1: Valid Order Creation
As an API client,  
I want to submit a new order with line items, currency, and customer reference,  
So that the system validates the payload, assigns a unique order ID, and confirms the order in memory.

### User Story 2: Performance and Concurrency (Initial Unclarified Requirement - INJECTED AMBIGUITY)
> *Initial Draft*: The order processor must process requests fast and securely and handle high volume appropriately without delays.
> *(FLAGGED BY SPEC-KIT CLARIFY: Subjective, unquantifiable criteria lacking latency SLAs, concurrency limits, and error specifications).*

### User Story 3: Idempotent Request Handling
As an API client experiencing network blips or retries,  
I want to provide an `Idempotency-Key` header with my submission,  
So that duplicate submissions within 60 seconds return the cached response without creating duplicate orders.

---

## 2. Clarification Log (Via `speckit-clarify`)

To eliminate the ambiguity in User Story 2, the following clarification questions were resolved:

* **Question 1 (Latency & Throughput)**: What constitutes "fast" and "without delays"?
  * **Clarified Resolution**: The order processor must process valid order creation requests in-memory with $p95 \le 50\text{ ms}$ under concurrent load up to 100 requests, returning HTTP 201 Created.
* **Question 2 (Security & Boundary Validation)**: What constitutes "secure" processing for an in-memory toy processor?
  * **Clarified Resolution**: Strict runtime validation using schema assertions: `items` must be a non-empty array with positive quantities, `currency` must be an ISO 4217 code (`SAR`, `USD`), and `total_amount` must equal the sum of line items. Negative or non-numeric values must be rejected immediately with HTTP 400 Bad Request.
* **Question 3 (State Model)**: What are the allowable state transitions?
  * **Clarified Resolution**: The order state machine consists of `PENDING` $\rightarrow$ `CONFIRMED` (upon validation success) or `REJECTED` (upon validation failure). No intermediate states exist in this toy model.

---

## 3. Measurable Acceptance Criteria

* **AC-01 (Payload Validation)**:
  * Given a payload with valid `items` (array with `sku`, `quantity > 0`, `unit_price > 0`), valid ISO `currency`, and matching `total_amount`,
  * When the client submits `POST /orders`,
  * Then the processor returns HTTP 201 with `{ id: string, status: "CONFIRMED", total_amount: number, created_at: string }`.

* **AC-02 (Malformed Input Rejection)**:
  * Given a payload missing required fields, or having `quantity <= 0`, or an invalid currency,
  * When the client submits `POST /orders`,
  * Then the processor returns HTTP 400 with `{ error: "VALIDATION_FAILED", details: string[] }`.

* **AC-03 (Latency SLA)**:
  * Under a synthetic load of 100 sequential requests, $p95$ in-memory execution latency must not exceed $50\text{ ms}$.

* **AC-04 (Idempotency Key Deduping)**:
  * Given a client request containing `Idempotency-Key: <UUID>`,
  * When a second identical request is received within 60 seconds with the same key,
  * Then the processor returns HTTP 200 with the cached original response without creating a new order or mutating in-memory state.

---

## 4. Architectural Invariants (Constitution Aligned)

1. **Isolation**: The toy order processor is completely decoupled from Medusa v2 core and CommerceOS production modules.
2. **Persistence Boundary**: Pure in-memory execution. The processor stores order entities in an internal memory data structure (`Map<string, OrderRecord>`). No external disk, PostgreSQL, or Redis dependencies are permitted.
3. **Determinism**: State transitions are deterministic and synchronous.
