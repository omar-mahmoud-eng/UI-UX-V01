# 21 — Critical official compatibility traps and reuse policy (2026-10-18)

## Avoid old tutorials
Medusa v2 is not v1. Review pinned docs before using examples, especially modules vs services, scoped API keys, query, workflows, admin. In supported Medusa recent versions:
- The Next.js starter has an official combined monorepo generator. Favor it over separate manual scaffolding.
- Medusa Admin supports UI Routes and Widgets; it uses React Router, with React Router v7 starting Medusa v2.19.0. Avoid duplicate incompatible react-router-dom installs.
- The maintained @medusajs/dashboard exports of Admin components/hooks/utilities started v2.21.0; use exported maintained components where pinned package supports them, not old tutorials copying source.
- Some older Medusa Module Link examples refer to deprecated Remote Link. Match current Link API.
- Puck is a MIT-licensed React visual editor compatible with Next.js in principle; evaluate exact React/router/server integration before adopting it as an official decision.
- Each plugin isn't a full process-isolated sandbox or automatic runtime removable unit.

## F00 requirements
Actual framework version, Node engine compatibility, package manager exact version, PostgreSQL, Redis, Next, React and Admin SDK lock from official scaffold must be logged. If a new version conflicts with starter release, select a compatible documented pair and capture ADR, rather than forced upgrades.

## Security/performance consequence
Avoid two React Router majors, duplicate UI design libraries, parallel cart/payment state machines, direct DB writes across domains, unreviewed high-privilege plugins, or dynamic arbitrary code by page builder. These can cause the exact startup faults and security exposures the project must prevent.

## Real verification required
Fetch installed package versions; run dependency tree checks, cold-start Admin and storefront, open Admin through browser and navigate UI Route proof after F05. Source docs:
https://docs.medusajs.com/resources/nextjs-starter
https://docs.medusajs.com/learn/fundamentals/admin/routing
https://docs.medusajs.com/resources/admin-components
https://docs.medusajs.com/learn/fundamentals/module-links/link
https://puckeditor.com/docs
