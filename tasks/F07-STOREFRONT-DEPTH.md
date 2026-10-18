# F07 — Customer experience and content expansion
Prereqs F00-F06 PASS; split into small sub-PRs with individual acceptance.
A. Faceted search with pagination and relevance; SEO/structured data/sitemap, canonical/redirects; no duplicate catalog.
B. Catalog import/export and bulk actions as queued work with dry-run and rollback; authorization.
C. Wishlist/reviews/compare and merchandising via modules when native gap; independent links, tests.
D. Fully responsive accessible templates for product, collection, content, account, checkout and error flows; improve LCP/CLS/INP with measured Web Vitals.
E. Real user journeys in Arabic/English; protected account/order and file scopes.
Gate per slice: Admin/storefront actual API, E2E, no fake screens, security and perf regression, no broken F01 checkout.
