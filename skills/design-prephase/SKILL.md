---
name: design-prephase
description: Use when the user invokes the Design Prephase plugin, asks to process design inputs end-to-end, or expects raw requirements to finish as a review-ready Design Definition.
---

# Design Prephase

## 默认契约

直接调用本 Plugin 或要求“处理完 / 走完整流程”时，默认终点是
`design-definition-[需求名].html`，随后由 `ai-design-input` 生成或更新
`ai-design-input-[需求名].md`。

## 路由

1. 先检查已有产物，禁止重复执行已经完成的阶段。
2. 只有原始会议、聊天或转写材料时，先执行 `design-req-organizer`。
3. 用户明确要求竞品、benchmark、参考案例或“别人怎么做”时，在需求整理后执行
   `feature-benchmarking-skill`。遵守该 Skill 的确认节点；完成后继续
   `design-definition`，最后执行 `ai-design-input`。
4. 已有用户确认采纳的竞品材料时，直接把它作为 `design-definition` 输入。
5. 未明确要求竞品且没有已确认竞品材料时，跳过竞品分析，执行
   `design-definition`，最后执行 `ai-design-input`。

## 单独调用

用户明确点名 `design-req-organizer`、`feature-benchmarking-skill`、
`design-definition`、`ai-design-input`，或明确只要某一阶段产物时，只执行该能力；
不要强行补齐完整链路。

## 本地校验脚本

各阶段按对应 Skill 的说明运行随插件打包的本地 Python 校验脚本。Design Definition 校验错误必须修复；重复内容 warning 触发一次跨章节压缩复查，但不得把 warning 解释成固定条数上限。脚本只负责确定性检查，不替代 Skill 的需求判断、竞品洞察或设计定义，也不需要 MCP server。

## 最终输出

完整调用只返回实际生成或更新的产物路径。若因材料歧义、业务规则未定或竞品确认节点
暂停，按对应 Skill 的规则向用户说明当前阻塞点。
