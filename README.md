# Design Research Skill

一组面向设计师的设计前置流程 Skill：把会议纪要、聊天记录、语音转写等原始需求材料，整理成可评审的 Design Definition；可按需插入竞品调研，并为后续 AI 生成设计稿准备 AI Design Input。

## 能力

| Skill | 作用 | 主要产物 |
|---|---|---|
| `design-prephase` | 完整流程总入口，默认终点为 Design Definition | — |
| `design-req-organizer` | 从原始材料中提取设计相关信息 | `design-requirement-brief-[需求名].html` |
| `feature-benchmarking-skill` | 竞品与功能对标，来源可回链、截图本地化 | `00_source_pack.html` → `01_canvas_benchmark.html` → `02_design_reference_checklist.html` |
| `design-definition` | 生成面向 PM / 设计评审的设计说明 | `design-definition-[需求名].html` |
| `ai-design-input` | 汇总硬逻辑，供 AI 生成设计稿 / demo 使用 | `ai-design-input-[需求名].md` |

默认流程：

```text
原始材料 → design-req-organizer → (可选) feature-benchmarking-skill → design-definition → ai-design-input
```

竞品调研只在明确要求时执行，并在 Source Pack 之后等待用户选择产品，再进入 Canvas Benchmark。

## 安装

本仓库按 Codex Plugin 结构组织（`.codex-plugin/plugin.json` + `skills/`）。每个 `skills/*/SKILL.md` 也是标准的 Agent Skill，可以单独复制到 Claude Code 等支持 Skill 的工具中使用，例如：

```bash
cp -r skills/* ~/.claude/skills/
```

## 本地校验脚本

随 Skill 打包的 Python 脚本只依赖标准库，不需要 MCP server：

- `skills/feature-benchmarking-skill/scripts/validate_source_pack.py`：校验 Source Pack 结构、本地图片和来源。
- `skills/design-definition/scripts/validate_design_definition.py`：校验 Design Definition 模板骨架与章节顺序。

## 测试

```bash
python3 -m unittest discover -s tests -v
```

变更记录见 [CHANGELOG.md](CHANGELOG.md)。

## License

[MIT](LICENSE)
