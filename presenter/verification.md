# Verification record

Prepared 2026-09-23. This document distinguishes static checks from rehearsal.

## Source and assets

- Original three-glyph Workshop Demo source, one Regular master, 1000 UPM.
- H and O widths: 600; bounds x=80…520; expected LSB/RSB 80/80.
- Reporting APIs checked against the installed Glyphs 4 development corpus:
  GSFont.selectedLayers, GSLayer.width, GSLayer.LSB and GSLayer.RSB.
- Corpus SDK revision: `0f5422db727b78cb42abfb386f33ae0b382b0c4d`.
- Installation screenshot: actual Glyphs MCP Beta 6, build 48, Setup component
  and connection cards. Sidebar hidden; unrelated project/task details excluded.
- Beta 6 DMG and release links verified through GitHub's release API.

## Qualification status

- PASS: seven offline unit tests (TSV formatting, escaping, no attribute writes,
  empty selection, no font, checkpoint identity, project structure).
- PASS: development skill script validator (syntax, menu title, placeholders).
- PASS: actual app Add Local Template → Use Template → Preview → Create Project.
  The independent rehearsal copy contains all participant files. AGENTS.md has
  the requested project name, configured server name and endpoint substituted.
- PASS: corrected source opens cleanly in Glyphs 4.1 build 4107. One Regular
  master; H and O selected; native fields show width 600 and sidebearings 80/80.
- PASS: supplied reference script run in a new macro, guarded to the disposable
  workshop path. Native output: H/Regular/600.0/80.0/80.0 and
  O/Regular/600.0/80.0/80.0. Before/after tuples of every glyph layer's ID, width,
  LSB and RSB were equal. No font save, install or production-font mutation.
- Native empty/no-font script cases are not separately exercised; offline tests
  cover their logic. The test used a newly created Macro 6; existing macros were
  not overwritten. The rehearsal project remains local for presenter review.
- Initial source-format check exposed obsolete string node/Unicode encoding;
  corrected to v3 tuples, integer Unicode and metricValues, then rechecked natively.
- Pending: actual AI-client inspection and preview/apply/undo rehearsal, final
  client/build selection, fresh-machine setup, updated captures and recordings.

The local rehearsal project sits inside an existing checkout, so the app can
display its parent repository's Git state. For participants, choose a standalone
local project folder; initialize its own Git history only when desired.

AI-client rehearsal and final-build qualification remain gates in
`rehearsal-checklist.md`. These checks do not certify every client or beta.

Do not describe initial expected output illustrations as live MCP results.
