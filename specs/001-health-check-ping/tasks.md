# Tasks: Synthetic Health Check Ping Utility

**Feature**: `001-health-check-ping`
**Status**: Ready for Execution

## Phase 1: Setup

- [ ] T001 Setup project test harness in tests/ping/
- [ ] T002 Configure test runner

## Phase 2: User Story 1 (P1) - Ping Health Status

- [ ] T003 [P] [US1] Write failing test for GET /healthz returning 200 OK
- [ ] T004 [P] [US1] Write failing test for POST /healthz returning 405 Method Not Allowed
- [ ] T005 [US1] Implement route handler for /healthz in src/ping/handler.js

## Phase 3: User Story 2 (P2) - Memory Diagnostics

- [ ] T006 [P] [US2] Write failing test for GET /healthz/diagnostics
- [ ] T007 [US2] Implement diagnostics handler in src/ping/diagnostics.js

## Phase 4: Verification

- [ ] T008 Run full test suite and record exit codes
