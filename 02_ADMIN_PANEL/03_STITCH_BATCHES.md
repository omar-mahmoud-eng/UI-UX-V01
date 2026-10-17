# Stitch batch plan — Admin

Do not ask Stitch to generate all modules at once. Start with shared chrome and 3 canonical views (dashboard, list, detail), then generate each **submodule triplet: workspace → record detail → configuration**, plus specialized scenarios.

**Batch 01** Shared shell + 00 general views + module 01 PIM.
**Batch 02** 02 Orders + 03 Warehouse + custom module 24 Wood Workshop + module 25 Florist & Gift Assembly.
**Batch 03** 08 CRM + 14 Contact Center + 21 CDP & marketing.
**Batch 04** 09 Pricing/CPQ + 07 B2B RFQ + 20 Supplier procurement.
**Batch 05** 10 Finance + 11 Fiscal/ZATCA + 04 Subscription.
**Batch 06** 22 Shipping + 05 Private fleet + 19 POS.
**Batch 07** 12 CMS + 13 Marketplace + 23 Affiliate.
**Batch 08** 06 Workflows + 15 AI + 16 IAM + 17 BI + 18 System Core.

Within each batch, use MODULE_PROMPTS/ for context and SCREEN_PROMPTS/ for one exact screen at a time. Mark each frame by ADM ID; link workflows, then test approval/denied and error states. Prioritize implemented business scope before optional full marketplace/TMS.
