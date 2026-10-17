# Mandatory instructions for any UI-UX-V01 design agent

- User objective: produce actual high-fidelity Google Stitch UI/UX designs for a Saudi wood-and-flowers gifting storefront (122) and enterprise Medusa-powered administration panel (638); do not confuse design prompts with built screens.
- Admin starting point: [`agent/START_ADMIN_STITCH_GITHUB.md`](agent/START_ADMIN_STITCH_GITHUB.md). Do not shortcut it.
- Storefront starting point: [`agent/START_STOREFRONT_STITCH_GITHUB.md`](agent/START_STOREFRONT_STITCH_GITHUB.md).
- Do not guess file existence or repository state; inspect actual local files and run `python scripts/verify_pack.py`.
- `DESIGN.md`, module instructions, and per-screen prompts must be read before each screen. Each screen prompt is authoritative for its own screen.
- Work screen-by-screen; keep a durable, accurate `tracking/*_execution_ledger.json` with real Stitch project IDs, screen IDs, URLs, QA state and any blockers. Use statuses PENDING/IN_PROGRESS/QA_FAILED/BLOCKED/COMPLETED.
- After interruptions, reconcile ledger with actual Stitch screens and continue unfinished ones; never silently skip or duplicate.
- Keep Git commits coherent; only commit actually updated ledger and source content; never commit tokens or credentials.
- Respect actual tool/API session limits: when automation or access is unavailable, report BLOCKED and leave reproducible continuation instructions, rather than claiming background work.
