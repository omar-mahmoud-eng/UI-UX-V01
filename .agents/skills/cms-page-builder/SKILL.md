# Secure CMS/Puck exploration
## When to invoke
Admin visual editing, reusable themes, landing pages and customer configurators.
## Required context
Read AGENTS.md, docs/11-AGENT-OPERATING-SYSTEM.md, docs/14-OFFICIAL-REFERENCES.md, the active tasks/Fxx file and relevant pinned official reference. Check that current stage is allowed.
## Execution protocol
Compare Puck documented APIs/version; design safe component registry, validated JSON schema, versioned pages, previews, publish/rollback. Test XSS, authorization, SSR and responsive RTL.
## Prohibited
Arbitrary script execution, unsupported iframe assumptions, replacing official checkout, publishing unsanitized assets.
## Evidence
Editor-to-store browser trace, draft/publish snapshot, negative XSS/SSRF tests, compatibility ADR.
## References
https://puckeditor.com/docs
