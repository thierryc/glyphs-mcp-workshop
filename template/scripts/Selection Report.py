# MenuTitle: Selection Report
# encoding: utf-8

__doc__ = 'Read-only TSV report for the selected Glyphs layers.'

from GlyphsApp import Glyphs
import csv
import io


def selection_report(layers):
    """Return TSV without changing layers, selection, clipboard or files."""
    output = io.StringIO()
    writer = csv.writer(output, delimiter="\t", lineterminator="\n")
    writer.writerow(["Glyph", "Layer", "Width", "LSB", "RSB"])
    for layer in layers:
        glyph = layer.parent
        if glyph is None:
            continue
        writer.writerow([glyph.name, layer.name, layer.width, layer.LSB, layer.RSB])
    return output.getvalue()


def main():
    font = Glyphs.font
    if font is None:
        raise RuntimeError("Open a font in Glyphs before running this script.")

    layers = list(font.selectedLayers or [])
    if not layers:
        print("Select H and O in an Edit tab, then run the script again.")
        return
    print(selection_report(layers), end="")


if __name__ == "__main__":
    main()
