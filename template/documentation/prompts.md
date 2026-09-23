# Workshop prompt sheet

Use each prompt separately. Read the result before sending the next one.
Formula: **context + target + action + constraints + expected result**.

## 1 — Inspect

> Check Glyphs MCP status and identify my Workshop Demo font, including its file
> path and masters. Do not change anything. Summarize what you can inspect.

> In that font's Regular master, report the advance widths of H and O. Do not
> change anything. Tell me if either glyph is missing.

Expected starting widths: H = 600; O = 600.

## 2 — Preview, apply, inspect, undo

> In that Workshop Demo font, preview an increase of 20 font units to the advance
> width of H only. Show which layers would change and their before/after widths.
> Keep outlines unchanged. Wait before applying. Do not save without asking me.

Expected proposal: H Regular, 600 → 620. O stays 600. This changes advance width,
not the width of H's outline. Check the actual proposal rather than assuming it.

> Apply the preview.

> Read back H and O's advance widths so I can compare them with Glyphs. Do not
> make another change or save.

> Undo these changes.

> Verify that H and O are back to 600 units. Do not save.

## 3 — Build a reusable reporting script

> Create a Glyphs 4 Python script that reports the glyph name, layer name,
> advance width, and left and right sidebearings for each selected layer. It
> must not modify the font, change selection, write files or make network
> requests. Explain how to run it in Glyphs. Handle an empty selection clearly.

> Format the report as tab-separated text so I can paste it into a spreadsheet.

## Better prompts and reusable guidance

Instead of “Improve the spacing,” try:

> In Workshop Demo, inspect the spacing of H and O in the Regular master.
> Explain any suggested changes with measurements. Do not apply changes yet.

MCP provides access to tools; a skill provides reusable guidance for using them.
Ask a code-capable client to draft a short read-only inspection checklist in
your project. Review it before installing it as a host-specific skill. A local
Markdown checklist is not automatically an installed skill in every client.
