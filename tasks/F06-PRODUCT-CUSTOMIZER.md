# F06 — Reusable product personalization (first real vertical: cake builder)
Prereqs F00-F05 PASS.
1. Define customizer domain model: schema/option/version, allowed combinations, assets, customer configuration, preview, price adjustments via server-owned rules, line item snapshot.
2. Prove one cake size, flavor, filling, inscription and uploaded reference artwork through real Next.js wizard; retrieve matching Medusa product variant, stock and pricing. Preview is presentation, NOT checkout authority.
3. Implement validation and atomic price/stock rechecks before order; customer-supplied price ignored. Storage safe and content scan; protect customer image privacy.
4. Persist configuration to real cart/order; Admin staff views specification and attachments; guard draft schema migration and product changes.
5. E2E: success, tamper price, invalid combination, oversized/malicious file, simultaneous stock update, retry idempotency, empty/cancel, mobile/RTL.
Gate: order details prove customization persisted; isolated module tests, auth/asset tests, existing store unaffected. Stop.
