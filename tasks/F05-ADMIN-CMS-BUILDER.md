# F05 — Real Medusa Admin extension + secure page editor
Prereqs F00-F04 PASS; use Admin UI Routes, Widgets, Medusa UI and permitted package exports checked for pinned version.
1. Proof-of-concept Puck React editor vs alternative in ADR. Review license/version/Next.js and Admin integration, accessibility and iframe/content security. Prefer Puck if compatibility proven; never bespoke editor without justification.
2. CMS domain model: Page, PageRevision, PublishedPointer, Locale, Template, MediaRef, Redirect; snapshots, owner/permissions, audit. Medusa integration via documented module/link.
3. Draft preview token short-lived, publish/rollback atomic, SEO fields and approved React component registry; no arbitrary JS/HTML/script execution.
4. Staff RBAC for create/edit/publish/admin; safe file uploads with limits, MIME/extension/content inspection and private asset rules. Harden against XSS, URL/SSRF, preview token abuse, CSRF.
5. Render two production-like page types in Next.js: home and content landing; verify RTL/mobile and SEO. Integrate design tokens without rebuilding Checkout.
Gate: actual Admin editor and storefront publish+rollback browser trace, XSS negative tests, audit, migration tests and F01 regression. Stop.
