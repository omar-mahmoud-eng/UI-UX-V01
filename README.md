# UI-UX-V01 — Wood & Flowers Enterprise Commerce Design Pack

**Design source files, not finished Stitch designs or a working Medusa implementation.**

This repository contains **760 individual UI screen prompts** for a wood-and-flowers gift retailer in Saudi Arabia: **122 storefront screens** and **638 enterprise admin screens**. The enterprise admin covers **23 requested original modules** plus **2 custom modules** for wood-workshop production and florist / gift-box assembly. There are **25 module-level prompt documents**. Placeholders such as «ورد وخشب», product prices and mock operational data are not legal or production facts.

## Structure

```text
UI-UX-V01/
├── 01_STOREFRONT/
│   ├── DESIGN.md, 00_START_HERE.md, 03_STITCH_BATCHES.md, SCREENS_INDEX.md
│   ├── SECTION_PROMPTS/         # 5 high-level journey files
│   └── SCREEN_PROMPTS/          # 122 unique screen prompts
├── 02_ADMIN_PANEL/
│   ├── DESIGN.md, 00_START_HERE.md, 03_STITCH_BATCHES.md, SCREENS_INDEX.md
│   ├── MODULE_PROMPTS/          # 25 module prompts
│   └── SCREEN_PROMPTS/          # 638 unique screen prompts
├── agent/
│   ├── START_ADMIN_STITCH_GITHUB.md    # Main autonomous admin agent prompt
│   ├── START_STOREFRONT_STITCH_GITHUB.md
│   └── ORIGINAL_DRIVE_ADMIN_EXECUTION_PROMPT.md
├── tracking/
│   ├── admin_execution_ledger.json
│   └── storefront_execution_ledger.json
└── scripts/verify_pack.py
```

## Start here

1. Run `python scripts/verify_pack.py` from the repo root, and only proceed if all validations pass.
2. For **admin**, read `agent/START_ADMIN_STITCH_GITHUB.md`, then all specified source files in the required order.
3. For **storefront**, read `agent/START_STOREFRONT_STITCH_GITHUB.md`.
4. Use **two independent Google Stitch projects** to keep administration and storefront styles distinct.
5. Generate **one screen at a time**, verify Stitch output visually, and record actual Project ID, Screen ID, URL and QA in the ledger.
6. Never label a screen `COMPLETED` unless it exists in Stitch and has passed review; never invent screen URLs or report that 760 designs were created merely because 760 prompts exist.

## Technologies and guardrails

Medusa v2 is a candidate backend for commerce. Screens mentioning finance, ZATCA, WMS, telematics or other enterprise functions describe requested **UX**, not verified implementation or compliance. Design in Arabic RTL first, English LTR secondary; SAR and Asia/Riyadh. Do not hard-code demo credentials or secrets in Git. Do not overwrite existing branch history.

The original user request and the master prompt references are preserved in the source documents. The previous Drive upload can be used as a fallback; this repository is intended as the primary source once uploaded and verified on GitHub.
