# Three experiments, one font

Working pattern: explain → prompt → demonstrate → try → review.
This is a draft exercise set; precise timing and client support will be rehearsed.

## 1. Does the assistant understand the font?

Open `sources/Workshop Demo.glyphs` (or `checkpoints/01-inspect.glyphs`).
Send the inspection prompts from `prompts.md`. Compare the family, path and
Regular master with Glyphs. Expected widths: H 600, O 600. No edits or saves.

Success: you can explain which font is being inspected and what has not changed.

## 2. Make one change you can inspect and reverse

Start from a fresh copy or `checkpoints/02-width-start.glyphs`. Close the previous
workshop document first; identify the new path in your conversation.

1. Ask for a preview of H's advance width +20, with outlines unchanged.
2. Review the proposal: only H Regular, 600 → 620; O stays 600.
3. Ask to apply. Inspect H's width field and unchanged outline in Glyphs.
4. Ask to read back the widths, then undo the current workflow.
5. Verify H and O are both 600 again. Save only if you explicitly want to.

Advance width includes sidebearings. It is not outline width. The expected H
outline spans x=80…520, so its outline width remains 440 while the advance grows.
The starting left/right sidebearings are 80/80. If the operation preserves the
outline coordinates, H's right sidebearing becomes 100.

If an edit times out, inspect the existing workflow; do not submit a duplicate.
If undo reports a conflict, stop and review it. A checkpoint is a separate clean
restart, not proof that an uncertain live edit was undone.

## 3. Turn a question into a small script

Use `checkpoints/03-report-start.glyphs` or the restored source. Ask for the script
before opening the reference solution in `scripts/Selection Report.py`.
Read the generated code and check that it is read-only. Open an Edit tab with
H and O and select both with the Text tool.

Open **Window → Scripting Window** in Glyphs 4. Click **+** beside Macros and
select the newly created empty macro so you do not overwrite another script.
Paste the reviewed script and run it using the window's Run control (⌘Return).
Use your text editor to copy the `.py` file's contents: Glyphs' File → Open does
not open Python scripts in the tested build. Consult the running app's menu if
the wording differs.
View output in the console / **Window → Floating Macro Console**. This is native
script execution, not an MCP arbitrary-code tool.

Expected baseline rows (numeric formatting may include decimals):

```text
Glyph	Layer	Width	LSB	RSB
H	Regular	600	80	80
O	Regular	600	80	80
```

Try an empty selection. The supplied solution prints a helpful message. It must
not save or modify the font. Repeated selected layers can produce repeated rows:
the report describes the selection, not a deduplicated glyph inventory.

## Optional: a Git checkpoint

The template does not create Git history. In your new project, explicitly
initialize Git with your editor or Git client, inspect the files and create a
starting commit. After a saved experiment, review the font diff before committing.
Avoid reset/checkout commands as a casual undo; they can discard unrelated work.
The Glyphs MCP app shows Git information but does not stage or commit for you.
