# {{PROJECT_NAME}}

Your disposable workshop project for **Controlling Glyphs with an MCP Server**.

1. Read [Setup](documentation/setup.md).
2. Open `sources/Workshop Demo.glyphs` in Glyphs 4.
3. Follow [the exercises](documentation/exercises.md), using the
   [copyable prompts](documentation/prompts.md).

`sources/` contains an original teaching font with one Regular master and only
H, O and space. It is deliberately small, not a production typeface.
`exports/` and `proofs/` are yours for output. `scripts/Selection Report.py` is a
read-only reference solution; try writing your own before looking at it.

Each exercise can restart from its corresponding file in `checkpoints/`.
Close the previous disposable copy before opening a checkpoint, then have the
assistant identify the new path. Do not keep two same-named workshop fonts open.

The template is copied independently. It does not install or run scripts,
initialize Git, or modify your other fonts. To keep Git checkpoints, explicitly
initialize a repository in your new project using your editor or Git client;
review a diff before each commit. The app's Git view is read-only.

See `LICENSES/` for reuse terms and `documentation/troubleshooting.md` for help.
