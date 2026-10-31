---
name: ai-design-input
description: 将已确认的设计需求硬逻辑、现有页面上下文和用户采纳的竞品参考，统一生成或更新 ai-design-input-[需求名].md。适用于用户要求生成、更新、合并、补全或检查 AI Design Input，也作为 design-req-organizer、feature-benchmarking-skill 与 design-definition 的唯一 AI Input 写入入口。
---

# AI Design Input

生成给 AI 设计稿、交互 demo 和后续设计生成使用的精简硬逻辑底稿。输出为 `ai-design-input-[需求名].md`；同一需求更新同名文件，不创建副本。

## 输入与职责

- 原始会议、聊天或转写材料：直接提取经确认的硬逻辑。
- `design-requirement-brief-[需求名].html`：补充已整理的范围、设计对象、约束和待确认项。
- `design-definition-[需求名].html`：只同步其中已确认的逻辑变化，不复制评审叙述。
- `02_design_reference_checklist.html` 或用户明确采纳的内容：只将已勾选、复制或明确确认的竞品参考写入设计生成指令。

不写需求背景、目标、普通用户描述、设计问题、评审结论、完整约束摘要、接口、埋点、验收标准、后端算法、研发排期或实现细节。

## 写入规则

1. 必须先读取 `templates/ai-design-input.md`，以它的章节结构更新文件。
2. 第一阶段从原始材料提取硬逻辑；后续更新完整继承既有 Scope、Page / Container Map、Logic Model、User Flow、States / Rules、Content Requirements 和 Existing Surfaces，只更新已确认变化。
3. 同一规则只能写入唯一章节：范围 / 角色归 Scope，容器职责归 Page Map，对象关系与操作粒度归 Logic Model，顺序归 User Flow，条件与结果归 States，字段与反馈归 Content，复用边界归 Existing Surfaces。
4. 如果包含「现有页改造」，更新前必须确认用户提供对应截图；截图只补充 Existing Surfaces 中的布局、模块和承载上下文，不得推导新需求。
5. 未确认的竞品 Insight 不得写入；有 Checklist 但未获用户选择时，保留为待选择，不视为已采纳。
6. Blocking Open Questions 只保留会改变页面范围、流程、对象关系、权限、状态或操作粒度的问题；新发现的阻塞问题先向用户澄清，不能自行写成答案。

## 调用关系

- `design-req-organizer` 需要 AI Input 时，将原始材料和 Requirement Brief 交给本技能。
- `feature-benchmarking-skill` 只生成用户选择用的 Checklist；用户确认后，将确认内容交给本技能。
- `design-definition` 只生成评审 HTML；完整流程或需要同步硬逻辑时，由本技能在其后更新 AI Input。

## 输出前检查

- 删除本文件后，Brief / Design Definition 仍能独立说明背景与评审判断；删除 Brief 后，本文件仍能恢复页面、对象、关系、流程、状态和操作粒度。
- 没有重复章节或同一规则的换写法复述。
- Page / Container Map 已区分新设计、现有页改造、现有页复用和未来扩展。
- 现有页面、竞品参考和待确认问题均符合上述写入边界。

