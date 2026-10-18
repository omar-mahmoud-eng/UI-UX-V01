# Agent Bootcamp and CommerceOS stage status (source of truth)
**Last planning update: 2026-10-18. This is a proposal/pack, NOT real training evidence.**

| Stage | Description | Status | Evidence |
| --- | --- | --- | --- |
| AG00 | Tool/source inventory | PASS | Windows 11 NT 10.0.26300; Git 2.53.0 (SHA 82c467b); Node v22.15.1; Python 3.13.14; uv 0.13.0; Docker 29.8.1 (Postgres 17 + Redis 7 up); specify 1.1.4.dev0; agy CLI absent; verify_agent_os PASS |
| AG01 | Controlled Superpowers + Spec Kit install | PASS | Live Antigravity verification verified: Superpowers v7.0.0 active in IDE (15 skills in ~/.gemini/config/plugins/superpowers); Spec Kit v1.2.1 active (10 speckit-* skills in .agents/skills); Live speckit-specify + speckit-analyze detected contradiction INC-001 in specs/002-token-bucket-limiter; Live systematic-debugging verified on config_merger defect (RED->GREEN); Constitution v2.0.0 and 20 local skills preserved 100%; PR #4 updated |
| AG02 | Source literacy / architecture research | IN_REVIEW | Factual patch applied: ASVS v5.0.0 stable ratified; Medusa inventory reservations confirmed inside completeCartWorkflow; Admin auth separated from Staff RBAC gap with fail-closed security; Curriculum E1-E9 mapped with practical competences NOT_VERIFIED pending katas; PR #6 updated; verify_agent_os PASS |
| AG03 | SDD drill | IN_REVIEW | Live Spec Kit v1.2.1 drill on isolated 003-toy-order-processor; Constitution->Specify->Clarify->Plan->Checklist->Tasks->Analyze flow executed; Caught & remediated 3 injected defects (ambiguity, plan/spec DB contradiction INC-002, and AC-04 task coverage gap); 100% requirements-to-tests traceability matrix verified; PR pending human review |
| AG04 | TDD drill | NOT_STARTED | No scratch code test |
| AG05 | Root cause debug drill | NOT_STARTED | No runtime diagnostics |
| AG06 | Security + reliability drill | NOT_STARTED | No authorized sandbox |
| AG07 | Holdout board + human certification | NOT_STARTED | No reviewer approval |
| F00 | Official Medusa/Next baseline | LOCKED | Must pass AG07 first |
| F01-F12 | CommerceOS feature execution | LOCKED | Must pass preceding gates |

### Transition
Only a genuinely executed gate can be marked PASS and cited with command outputs, host versions, SHA and reviewer. All later stages require explicit human go/no-go. Planning CI success is not agent qualification, security clearance or production readiness.
