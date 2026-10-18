# Agent Bootcamp and CommerceOS stage status (source of truth)
**Last planning update: 2026-10-18. This is a proposal/pack, NOT real training evidence.**

| Stage | Description | Status | Evidence |
| --- | --- | --- | --- |
| AG00 | Tool/source inventory | PASS | Windows 11 NT 10.0.26300; Git 2.53.0 (SHA 82c467b); Node v22.15.1; Python 3.13.14; uv 0.13.0; Docker 29.8.1 (Postgres 17 + Redis 7 up); specify 1.1.4.dev0; agy CLI absent; verify_agent_os PASS |
| AG01 | Controlled Superpowers + Spec Kit install | PASS | Live Antigravity verification complete: Superpowers v7.0.0 active in IDE (15 skills loaded from ~/.gemini/config/plugins/superpowers); Spec Kit v1.2.1 active (10 speckit-* skills in .agents/skills); live /speckit-specify and /speckit-analyze verified on 001-health-check-ping; live systematic-debugging verified on synthetic defect; constitution v2.0.0 and 20 local skills preserved 100%; PR #4 updated |
| AG02 | Source literacy / architecture research | NOT_STARTED | No agent study exam |
| AG03 | SDD drill | NOT_STARTED | No real CLI/skills run |
| AG04 | TDD drill | NOT_STARTED | No scratch code test |
| AG05 | Root cause debug drill | NOT_STARTED | No runtime diagnostics |
| AG06 | Security + reliability drill | NOT_STARTED | No authorized sandbox |
| AG07 | Holdout board + human certification | NOT_STARTED | No reviewer approval |
| F00 | Official Medusa/Next baseline | LOCKED | Must pass AG07 first |
| F01-F12 | CommerceOS feature execution | LOCKED | Must pass preceding gates |

### Transition
Only a genuinely executed gate can be marked PASS and cited with command outputs, host versions, SHA and reviewer. All later stages require explicit human go/no-go. Planning CI success is not agent qualification, security clearance or production readiness.
