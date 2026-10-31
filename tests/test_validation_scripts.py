import importlib.util
import tempfile
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str, relative_path: str):
    path = PLUGIN_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ValidationScriptTests(unittest.TestCase):
    def test_rejects_design_definition_without_template_skeleton(self) -> None:
        validator = load_script(
            "design_definition_validator",
            "skills/design-definition/scripts/validate_design_definition.py",
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact = Path(temp_dir) / "design-definition-test.html"
            artifact.write_text("<!doctype html><html><body><h2>User Flow</h2></body></html>", encoding="utf-8")
            errors, warnings = validator.validate(artifact)
        self.assertIn("Missing template class '.hero'.", errors)
        self.assertIn("Missing required section 'Materials'.", errors)
        self.assertEqual(warnings, [])

    def test_page_structure_requires_wireframe_page(self) -> None:
        validator = load_script(
            "design_definition_validator",
            "skills/design-definition/scripts/validate_design_definition.py",
        )
        html = """<!doctype html><html><body>
          <header class="hero"><div class="hero-inner"><div class="topline"></div>
            <span class="title-level">P1</span></div></header>
          <main><section><h2>Materials</h2><ul class="materials"></ul></section>
          <section><h2>Project Background</h2></section>
          <section><h2>Design Goal</h2></section>
          <section data-user-flow-type="page-structure"><h2>User Flow</h2><div class="flow-map"></div></section>
          <div class="section-group"><h2>Design Direction</h2></div></main></body></html>"""
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact = Path(temp_dir) / "design-definition-test.html"
            artifact.write_text(html, encoding="utf-8")
            errors, _ = validator.validate(artifact)
        self.assertIn("Page-structure User Flow must contain a '.wireframe-page' layout.", errors)

    def test_accepts_template_based_page_structure(self) -> None:
        validator = load_script(
            "design_definition_validator",
            "skills/design-definition/scripts/validate_design_definition.py",
        )
        html = """<!doctype html><html><body>
          <header class="hero"><div class="hero-inner"><div class="topline"></div>
            <span class="title-level">P1</span></div></header>
          <main><section><h2>Materials</h2><ul class="materials"></ul></section>
          <section><h2>Project Background</h2></section>
          <section><h2>Design Goal</h2></section>
          <section data-user-flow-type="page-structure"><h2>User Flow</h2>
            <div class="wireframe-page"></div></section>
          <div class="section-group"><h2>Design Direction</h2></div></main></body></html>"""
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact = Path(temp_dir) / "design-definition-test.html"
            artifact.write_text(html, encoding="utf-8")
            errors, warnings = validator.validate(artifact)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_design_definition_warns_on_cross_section_repetition(self) -> None:
        validator = load_script(
            "design_definition_validator",
            "skills/design-definition/scripts/validate_design_definition.py",
        )
        repeated = "查看对象的历史表现，帮助用户判断告警阈值。"
        html = f"""<!doctype html><html><body>
          <header class="hero"><div class="hero-inner"><div class="topline"></div>
            <span class="title-level">P1</span></div></header>
          <main><section><h2>Materials</h2><ul class="materials"></ul></section>
          <section><h2>Project Background</h2><p>{repeated}</p></section>
          <section><h2>Design Goal</h2><ul><li>{repeated}</li></ul></section>
          <section><h2>User Flow</h2><div class="flow-map"></div></section>
          <div class="section-group"><h2>Design Direction</h2></div></main></body></html>"""
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact = Path(temp_dir) / "design-definition-test.html"
            artifact.write_text(html, encoding="utf-8")
            errors, warnings = validator.validate(artifact)
        self.assertEqual(errors, [])
        self.assertIn("Repeated content appears in multiple review sections.", warnings)

    def test_source_pack_uses_packaged_validator(self) -> None:
        validator = load_script(
            "source_pack_validator",
            "skills/feature-benchmarking-skill/scripts/validate_source_pack.py",
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact = Path(temp_dir) / "00_source_pack.html"
            artifact.write_text("<html><body></body></html>", encoding="utf-8")
            errors = validator.validate(artifact)
        self.assertIn("Missing heading '调研范围'.", errors)


if __name__ == "__main__":
    unittest.main()
