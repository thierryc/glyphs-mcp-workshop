import ast
import importlib.util
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import io
import contextlib

ROOT = Path(__file__).resolve().parents[1]


class WorkshopTests(unittest.TestCase):
    def module(self, font=None):
        spec = importlib.util.spec_from_file_location("report", ROOT / "template/scripts/Selection Report.py")
        module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"GlyphsApp": SimpleNamespace(Glyphs=SimpleNamespace(font=font))}):
            spec.loader.exec_module(module)
        return module

    def test_tsv_and_no_mutation(self):
        layer = SimpleNamespace(parent=SimpleNamespace(name="H"), name="Regular", width=600, LSB=80, RSB=80)
        before = vars(layer).copy()
        self.assertEqual(self.module().selection_report([layer]), "Glyph\tLayer\tWidth\tLSB\tRSB\nH\tRegular\t600\t80\t80\n")
        self.assertEqual(vars(layer), before)

    def test_tsv_escaping(self):
        layer = SimpleNamespace(parent=SimpleNamespace(name="H"), name="Tab\tname", width=600.125, LSB=80, RSB=80.125)
        self.assertIn('"Tab\tname"', self.module().selection_report([layer]))

    def test_empty_selection(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.module(SimpleNamespace(selectedLayers=[])).main()
        self.assertIn("Select H and O", output.getvalue())

    def test_no_font(self):
        with self.assertRaisesRegex(RuntimeError, "Open a font"):
            self.module().main()

    def test_script_has_no_attribute_assignments(self):
        tree = ast.parse((ROOT / "template/scripts/Selection Report.py").read_text())
        self.assertFalse(any(isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Store) for node in ast.walk(tree)))

    def test_checkpoints_match_source(self):
        source = (ROOT / "template/sources/Workshop Demo.glyphs").read_bytes()
        for name in ["01-inspect", "02-width-start", "03-report-start"]:
            self.assertEqual((ROOT / f"template/checkpoints/{name}.glyphs").read_bytes(), source)

    def test_template_structure(self):
        for folder in ["sources", "exports", "proofs", "documentation", "scripts", "checkpoints", "LICENSES"]:
            self.assertTrue((ROOT / "template" / folder).is_dir())
        text = (ROOT / "template/AGENTS.md").read_text()
        for token in ["PROJECT_NAME", "SERVER_NAME", "ENDPOINT_URL"]:
            self.assertIn("{{" + token + "}}", text)


if __name__ == "__main__":
    unittest.main()
