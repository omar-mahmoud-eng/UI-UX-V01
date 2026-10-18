# Tasks: In-Memory Token Bucket Rate Limiter

**Feature**: `002-token-bucket-limiter`
**Status**: Ready for Execution

## Phase 1: Setup

- [ ] T001 Setup rate limiter test harness in tests/limiter/

## Phase 2: User Story 1 (P1) - Request Admission

- [ ] T002 [P] [US1] Write failing test for in-memory token consumption
- [ ] T003 [US1] Implement in-memory Map structure for token tracking
- [ ] T004 [US1] Connect rate limiter to external Redis cluster using ioredis and persist token counters in Redis key rate:limit:{id}

## Phase 3: User Story 2 (P1) - Throttling

- [ ] T005 [P] [US2] Write failing test for 429 throttling response
- [ ] T006 [US2] Implement HTTP 429 response formatting with Retry-After header
