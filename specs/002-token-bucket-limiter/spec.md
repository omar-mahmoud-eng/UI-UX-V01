# Feature Specification: In-Memory Token Bucket Rate Limiter

**Feature Branch**: `002-token-bucket-limiter`
**Created**: 2026-10-18
**Status**: Draft
**Input**: User description: "High-performance in-memory token bucket rate limiter for synthetic agent qualification"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Request Admission within Capacity (Priority: P1)

As an API client, I want to submit requests within my allocated token quota so that all requests are admitted without delay.

**Why this priority**: Core functional capability for traffic regulation.

**Independent Test**: Send 10 concurrent requests with capacity 10 and assert all 10 are admitted.

**Acceptance Scenarios**:

1. **Given** a bucket with 10 available tokens, **When** a request consumes 1 token, **Then** the request is allowed and remaining tokens count is 9.

---

### User Story 2 - Traffic Throttling (Priority: P1)

As an API defender, I want requests exceeding capacity to be throttled with HTTP 429 so that system resources remain protected.

**Why this priority**: Protective backpressure mechanism.

**Independent Test**: Send request when tokens=0 and assert HTTP 429 Too Many Requests with Retry-After header.

**Acceptance Scenarios**:

1. **Given** an empty token bucket (0 tokens), **When** an incoming request arrives, **Then** return HTTP 429 and do not execute downstream logic.

## Requirements *(mandatory)*

### Functional Requirements

- FR-001: The rate limiter must refill tokens at a configurable continuous rate per second.
- FR-002: Token bucket state MUST be stored exclusively in-memory using local process data structures. External storage or Redis is strictly forbidden.
- FR-003: Throttled requests must receive HTTP 429 with standard Retry-After header.

### Non-Functional Requirements

- NFR-001: In-memory token acquisition must complete in under 1 millisecond.
- NFR-002: Zero external network or database round-trips.

## Success Criteria *(mandatory)*

- SC-001: 100% of requests within quota are admitted.
- SC-002: 100% of excessive requests return HTTP 429.

## Out of Scope

- Distributed multi-node synchronization, Redis clusters, or database persistence.
