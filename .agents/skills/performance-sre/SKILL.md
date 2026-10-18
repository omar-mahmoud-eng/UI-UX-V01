# Performance, resilience & load testing
## When to invoke
After a stable functional path exists, before infrastructure scaling claims.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Choose documented load tool/hardware/data profile. Measure p95/p99, error %, DB, worker backlog, 15-min baseline, soak and fault injection; optimize measured hotspots before adding infrastructure.
## Prohibited
Invented throughput, load test against customer production, immediate Kubernetes/microservices.
## Evidence
Raw report with exact scenario, machine and resource metrics, regression delta.
## References
https://docs.medusajs.com/learn/deployment/general
