# Publish the full design pack

1. Download `UI-UX-V01_GitHub_Ready_760_Screens.zip` from the Drive link in `SOURCE_ARCHIVE.md`.
2. Clone `https://github.com/omar-mahmoud-eng/UI-UX-V01.git`.
3. Extract the archive at the root of the clone (preserve directories and hidden `.github`).
4. Run `python scripts/verify_pack.py` and confirm 638 admin + 122 storefront screen prompts.
5. `git add . && git commit -m 'feat: import 760 Stitch screen specifications' && git push origin main`.
6. Verify all files on GitHub before beginning Stitch design.

Never claim the prompts are implemented UI designs until each Stitch screen is actually created and reviewed.
