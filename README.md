# Controlling Glyphs with an MCP Server

Preparation draft for Thursday **8 October 2026, 13:00–15:00 BST / 14:00–16:00 CEST**.
Presented in English by Thierry Charbonnel and Rainer Erich Scheichelbauer.

One font. Three experiments. Inspect a font, make a controlled change, and build
a useful reporting script. The agenda and teaching client remain provisional.

## Install as a Glyphs MCP project

1. Open Glyphs MCP's project start screen and find the workshop in **Templates**.
2. Choose **Refresh** if the list needs updating.
3. Choose **Use Template**, name your project, choose a local parent folder,
   review its contents and choose **Create Project**.
4. Open your new project's `sources/Workshop Demo.glyphs` in Glyphs 4.
5. Start with `documentation/setup.md`, then `documentation/exercises.md`.

**No workshop ZIP download is required.** The workshop will be added to the app's
template list before the session. The catalog entry is not published yet.

### Presenter setup while private

Use an authenticated local checkout. On the project start screen, choose
**Add Local Template…** and select this repository's **template/** folder, not
the repository root. It then appears in Templates for **Use Template**.
This registration is for preparation; participants will use the listed template.
The ZIP remains an optional manual fallback, not the normal setup path.

The app copies files; it does not execute scripts, clone Git history or configure
an AI client from this template. Project instructions are guidance, not a skill
installer. Install the matching Glyphs MCP skills through the app separately.

## Downloads and status

- [Glyphs MCP Beta 6 DMG](https://github.com/thierryc/Glyphs-mcp/releases/download/v2.0.0-beta.6/Glyphs-MCP-2.0.0-beta.6.dmg)
- [Release and checksums](https://github.com/thierryc/Glyphs-mcp/releases/tag/v2.0.0-beta.6)
- [Optional repository ZIP](https://github.com/thierryc/glyphs-mcp-workshop/archive/refs/heads/main.zip)

The repository is private during preparation. GitHub links require collaborator
access until the owner explicitly makes it public. The remote app catalog cannot
download private repositories; use a local template during rehearsal.
Beta 6 is the available download used for these initial screenshots, **not a
promise of the final workshop version**. See `presenter/verification.md`.

## What's here

- `template/`: participant project, original demo font, prompts, script and checkpoints.
- `presenter/`: provisional running order, rehearsal and publication gates.
- `assets/`: actual application screenshots with provenance.
- `tools/`: repeatable packaging and offline validation.
- `LICENSES/`: original-material license and upstream script scaffold notice.

Create the participant ZIP with `python3 tools/package.py`; run offline checks
with `python3 -B -m unittest discover -s tests -v`. Native and AI-client rehearsals
are separate from those checks. No GitHub Actions or Pages deployment is enabled.

Keep fallback recordings outside this repository so the app's archive download
stays below 20 MB compressed / 64 MB expanded. Never commit client credentials,
private fonts or unrelated project screenshots.
