import json
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]


class PluginContractTests(unittest.TestCase):
    def test_manifest_exposes_skills_without_custom_mcp_servers(self) -> None:
        manifest = json.loads(
            (PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
        )

        self.assertEqual(manifest["name"], "design-research-skill")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertNotIn("mcpServers", manifest)
        self.assertFalse((PLUGIN_ROOT / ".mcp.json").exists())
        self.assertIsInstance(manifest["interface"]["defaultPrompt"], list)

    def test_all_independent_skills_and_default_entry_exist(self) -> None:
        expected = {
            "design-prephase",
            "design-req-organizer",
            "feature-benchmarking-skill",
            "design-definition",
            "ai-design-input",
        }
        actual = {
            path.parent.name
            for path in (PLUGIN_ROOT / "skills").glob("*/SKILL.md")
        }

        self.assertEqual(actual, expected)
        self.assertFalse((PLUGIN_ROOT / "skills" / "skill-audit").exists())

    def test_packaged_skills_do_not_reference_a_personal_install_path(self) -> None:
        offenders = []
        for skill_file in (PLUGIN_ROOT / "skills").glob("*/SKILL.md"):
            if "/Users/" in skill_file.read_text(encoding="utf-8"):
                offenders.append(skill_file.relative_to(PLUGIN_ROOT).as_posix())

        self.assertEqual(offenders, [])

    def test_default_entry_contract_reaches_design_definition(self) -> None:
        content = (
            PLUGIN_ROOT / "skills" / "design-prephase" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("默认终点", content)
        self.assertIn("design-definition", content)
        self.assertIn("明确要求竞品", content)
        self.assertIn("单独调用", content)

    def test_requirement_brief_preserves_decision_context_and_filters_candidates(self) -> None:
        organizer_root = PLUGIN_ROOT / "skills" / "design-req-organizer"
        skill = (organizer_root / "SKILL.md").read_text(encoding="utf-8")
        rules = (organizer_root / "rules.md").read_text(encoding="utf-8")
        template = (
            organizer_root / "templates" / "requirement-brief-html.md"
        ).read_text(encoding="utf-8")

        self.assertIn("适合 PM / 设计师快速阅读", skill)
        self.assertIn("待确认问题闭环扫描", skill)
        self.assertIn("不能仅因存在多个方案就写成设计重点关注", skill)
        self.assertIn("具体对象 / 场景 + 设计难点或矛盾", rules)
        self.assertIn("每条末尾标注来源（说话人或角色）", rules)
        self.assertGreaterEqual(rules.count("每条末尾标注来源"), 2)

    def test_requirement_brief_uses_readable_goal_nesting_and_compact_benchmark_prompt(
        self,
    ) -> None:
        organizer_root = PLUGIN_ROOT / "skills" / "design-req-organizer"
        rules = (organizer_root / "rules.md").read_text(encoding="utf-8")
        template = (
            organizer_root / "templates" / "requirement-brief-html.md"
        ).read_text(encoding="utf-8")

        self.assertIn("只有一句话因包含多个明确模块 / 能力而难以阅读时", rules)
        self.assertIn("外部入口、来源场景和返回路径不属于页内模块", rules)
        self.assertIn("用 feature-benchmarking-skill 调研", template)
        self.assertIn("重点：[1-2 个可横向比较的设计维度]", template)
        self.assertNotIn("目标用户：[", template)
        self.assertNotIn("调研主路径：[", template)

    def test_requirement_brief_uses_original_section_roles_without_global_fact_ownership(self) -> None:
        organizer_root = PLUGIN_ROOT / "skills" / "design-req-organizer"
        rules = (organizer_root / "rules.md").read_text(encoding="utf-8")
        template = (
            organizer_root / "templates" / "requirement-brief-html.md"
        ).read_text(encoding="utf-8")

        self.assertNotIn("## 事实唯一归属", rules)
        self.assertNotIn("关键取舍只进入设计相关结论", rules)
        for required_section in (
            "<h2>设计目标</h2>",
            "<h2>用户与影响范围</h2>",
            "<h2>设计重点关注</h2>",
            "<h2>设计约束条件</h2>",
            "<h2>设计相关结论</h2>",
        ):
            self.assertIn(required_section, template)
        self.assertNotIn("<h2>设计要求</h2>", template)


if __name__ == "__main__":
    unittest.main()
