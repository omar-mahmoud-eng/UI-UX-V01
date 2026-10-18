# 17 — Quality attributes, budget policy and measurable performance

## Attributes (ranked)
Correctness, transaction safety, data security/privacy, uptime/recovery, operability, maintainability, runtime performance, feature delivery velocity.

## Policies
Set route-specific latency SLOs for browse/cart/checkout/Admin reports once first end-to-end system works. Baselines report p50/p95/p99, actual error %, SQL active connections, CPU, memory, heap/GC, worker backlog, DB cache/IO and total host specs. Mobile page performance measured via Web Vitals separately from API latency.

## Candidate qualification tests (NOT measured yet)
- F00: smoke across backend/Admin/storefront after cold boot and reboot.
- F01: concurrency simulation for stock/order with controlled dataset.
- F04: 30-minute host test, 50 users (provisional), <1% unexpected errors, no restart, target p95 <1000ms for defined browse/cart path. Separate throughput number and hardware spec.
- F12: ramp (50, 100, 200 VU) + 60-minute soak and controlled process/Redis fault; document observed breaking point. **Do not claim massive scaling when database/host not measured**.

## Anti-collapse design
Bounded queues and concurrency; idempotent retries; backpressure; circuit-breaker when justified; pagination; Postgres pool sizing; index-backed queries; CDN media; predictable cache TTL/invalidation; graceful shutdown; worker and API limits; health/readiness; async export/report generation. Avoid polluting hot checkout path with CRM/analytics.

## Nonfunctional release block
If latency or crash regresses from agreed baseline, no launch until investigated. Perf claims attached to tested hardware, workloads and dataset. Security fixes prioritized over raw throughput.
