# 10 — Storefront, Admin and site-builder architecture

## Baseline UI philosophy
Run the official Medusa Admin and Next.js storefront unchanged first. After F01, define design tokens and consistent primitives (typography, spacing, motion budget, forms, navigation, error states, accessibility). Arabic and English, desktop/mobile/tablet, keyboard and screen readers. Avoid rebuilding commerce/state controls already in Medusa.

## Storefront functional map
Home; menus/search; collection; product details/variants; favorites; compare optional; filters; cart; mini cart; checkout address/shipping/payment/review; result states (success/failure/out-of-stock); account login/register/password reset where supported; addresses; orders/status/returns; customizer pages; gift cards and codes; CMS pages, blog, FAQ, policy, contact; notifications, content marketing, SEO and error/offline-friendly states.
Functional coverage is incremental; no inert screens or pretend backend API.

## Admin functional map
Core Medusa product/prices/orders/customers/inventory/payments/fulfillment staff routes FIRST. Add dashboard KPIs, saved views, bulk actions, advanced reports, CMS/pages/themes, media, marketing, customer lifecycle, supplier/inventory forecasting, finance exports, task approvals, support and integrations only after real domain API exists. Route-level and object-level RBAC; stable UX conventions; actual loading/empty/error/permission states.

## Visual page builder ADR hypothesis
Evaluate Puck or comparable React JSON-based editor by source/version/license/security/SSR integration and localization; choose after runnable spike. DO NOT build a bespoke drag-drop editor before proof. Content storage in owned CMS Module: pages, versions, slots, approved component schema, translation, draft and published pointers, revision/audit, redirects, preview tokens with short expiry. Render via allowlisted component registry. Never execute customer-provided JS, CSS URL exfiltration or unsafe HTML by default.

## Extensibility
Each installed extension can register allowed storefront components/sections and Admin navigation/widgets through explicit reviewed capability manifest: extension ID, version, permissions, schema, data source, assets, migration and uninstall impact. Dynamic install/update/reload is *not* presumed feasible without restart/migration; mark rollout type.

## Advanced customization
Reusable "configuration engine" powering cake personalization and future flowers/gifts/engraving: input schema, validation/price rules computed on server, media uploads, preview, versioned result and order snapshot. Distinguish render-only options from price-affecting options. Detect malicious prices, out-of-stock customization and size/weight limits.

## UI acceptance
Every clickable affordance has defined real action or intentionally disabled explanation; tests cover keyboard, RTL/LTR, mobile viewport, screen reader landmarks, error states, saved/published CMS state and XSS tests. UI screenshots alone do not prove end-to-end functionality.
