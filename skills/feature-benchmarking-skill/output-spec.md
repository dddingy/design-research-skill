# Feature Benchmarking Output Spec

本文件说明交付物应该包含什么内容，不是实际 HTML 模板。Source Pack HTML 优先使用 `templates/source-pack.html`；Canvas Benchmark HTML 优先使用 `templates/canvas-benchmark.html`。

## 1. Source Pack：`00_source_pack.html`

用途：给设计师快速看候选样本、证据来源和粗略分析，并决定是否继续做 Canvas Benchmark。

默认行为：

- 用户第一次调用本技能时默认只产出 Source Pack。从零开始的调研不支持跳过 Source Pack 直接进入 Canvas；如果当前任务没有可承接的 Source Pack，先补 Source Pack。
- Source Pack 不是纯素材列表，必须包含轻量判断：为什么相关、适合参考什么、不适合照搬什么、建议是否进入 Canvas。
- 如果已有 `design-req-organizer` 输出，必须承接其中的推荐调研点；用户可确认全部、选择其中一部分，或纠正调研点。

页面结构：

```text
Title：{功能名} Source Pack
Subtitle：{DATE} · 本步提供{对象/页面}样本与证据索引，用于选择产品并进入下一步 Canvas 深拆

1. Executive Summary
   - 本次调研范围
   - 已确认/推荐调研点
   - 用户点名产品覆盖情况
   - 样本池整体观察

调研范围区：
   - 问题、目标、参考类型各写 1 个短句或信息完整的短语

2. Candidate Navigation
   - 产品 A / 产品 B / 产品 C ...

3. Product Cards
   每个产品一张卡片：
   - 产品名
   - 标签：2–4 个关键交互或页面特征，放在标题同行
   - 产品介绍：说明“这个产品是什么、服务什么场景”
   - 推荐理由：为什么值得看、适合参考什么
   - 预览图：2–3 张，本地 `assets/` 引用，不热链
   - 注意/取舍：适合参考和不适合照搬的边界
   - Sources

4. Canvas 深拆推荐
   - 放在“下一步：生成 Canvas Benchmark”模块上方
   - 使用功能点维度表展示「功能点 → 下一步看什么 → 重点参考产品」
   - 这里帮助用户决策下一步优先深拆哪些产品，并解释这些产品会覆盖哪些功能点；不承担最终产品选择确认

5. 下一步：生成 Canvas Benchmark
   - 明确说明不会自动进入下一步，并告诉用户下一步需要从上方候选产品里选择要深拆的产品；用户只回复“继续”或“按推荐继续”时，默认按推荐产品生成“调研点 × 产品”的横向对比画布
   - 不再放产品推荐表，避免和上方候选产品卡片重复
   - 提供可编辑、可复制的确认文本，列出默认产品和调研点
   - 结尾明确请用户确认是否继续做 Canvas Benchmark
```

Source Pack HTML style baseline：

- 卡片扁平：使用 border + background，不加阴影。
- 卡片结构固定：产品名 + tags 同行 → 产品介绍 → 推荐理由 → gallery → 小字注意 → Sources。
- Gallery 默认 3 列，移动端变 1 列；图片默认 16:9 填充裁切，必要时用 contain 保完整。
- 图下只写图片内容描述，不放链接；来源链接放 Sources 区。
- 截图资产放在当前调研输出目录的 `assets/` 中，例如 `{research-name}/assets/`。

## 2. Canvas Benchmark：`01_canvas_benchmark.html`

用途：在用户确认继续后，做进一步画布式横向分析，帮助设计师比较同一个调研点在不同产品里的做法。

触发条件：

- 用户看完 Source Pack 后要求继续深入。
- 用户说“按你推荐做 Canvas / 做横向对比 / 深入画布 / 只看某几个调研点”。
- 用户要求横向矩阵 / 深入画布 / Canvas 时，只有当前任务已有可承接的 Source Pack 才进入 Canvas；否则先生成 Source Pack。

固定形式：

```text
Title：{功能名} Canvas Benchmark

1. Header
   - 简短说明调研范围和调研点

2. Canvas Matrix
   - 表头是产品
   - 每个产品名下面继承 Source Pack 的产品介绍和推荐理由；新增产品需补齐同等粒度说明
   - 左侧是调研点
   - 每个交叉格展示该产品在该调研点下的图片和文字总结
   - 没有对应截图或证据的格子留空，不放替代图

3. Reference Links
   - 作为 Canvas Matrix 的最后一行合并进大表
   - 左侧调研点列写 `Reference Links` 和说明，右侧每个产品列列出该产品在本次 Canvas 使用过的所有来源链接
   - 不要做成矩阵之外的独立区块或卡片
   - 包括 Source Pack 继承来源和 Canvas 追加来源
   - 链接数量必须多于 Source Pack，且必须包含 Canvas 阶段按「产品 × 调研点」追加的细证据链接
   - 格子内仍保留对应来源，Reference Links 用于审查和归档回链

4. Design Insights
   - 放在 Reference Links 下方
   - 将横向观察收束成设计启示，数量不设硬限制，按证据和设计问题自然分析
   - 必须使用表格呈现，每行 1 条 Insight，列为「Insight / 看到 / 说明 / 对你的启示」
```

Canvas cell 内容：

- 1–2 张对应截图或局部特写；必须本地 `assets/` 引用。
- 图片标题：说明画面中的关键控件/状态。
- 来源：直达 URL。
- 总结：1–3 条短句，只写该产品在该调研点下的做法和启示。

Canvas 追加调研要求：

- Canvas 的细证据与来源标准以 `rules.md` 为准。

Design Insights 内容：

- 必须来自 Canvas 中已经出现的证据，不新增无来源结论。
- 必须写成表格，不放进矩阵格子里，不再使用卡片或列表承载 Insight。
- 表格列固定为：
  - Insight：`Insight N｜{一句可执行设计判断}`，例如“把分组做成可配置规则，不是固定节点”。标题必须能直接指导设计取舍，不写“入口启示”“结果反馈”这类泛标题。
  - 看到：引用 Canvas 中哪些产品的具体做法，至少点名 1–3 个产品和对应机制。
  - 说明：解释这些做法背后的设计判断、适用条件或风险。
  - 对你的启示：转化成本需求可用的设计决策，必须出现本需求对象、默认规则、控件、布局或状态处理方式。
- 写法要像设计师给下一步设计的决策备忘，不像竞品综述；优先写“要怎么做”，少写抽象价值判断。
- 每条 Insight 必须包含至少一个明确的设计取舍、触发条件或边界规则，例如“低风险入口常驻，高风险动作进入确认卡”“未绑定对象时不能执行”。如果只是复述产品做法或写通用价值，不合格。
- Reference Checklist 可从这些 Design Insight 中挑选用户能够独立采纳的条目；数量按证据自然拆分。

## 3. Optional Product Appendix：`products/{product}.html`

默认不生成单产品页。

只有在以下情况才生成：

- 用户明确要求深拆某个产品。
- 某个产品在 Canvas 中承担了大量证据，需要单独展开。
- 某条流程跨多个页面，无法放进一个 Canvas cell。
- 评审或 design-definition 需要完整产品路径作为附录。

单产品附录应包含：

- 为什么值得看
- 入口 / 默认视图 / 关键状态
- 核心交互路径
- 可迁移模式与不适合照搬的点
- 来源链接与截图来源

## 4. Design Reference Checklist：`02_design_reference_checklist.html`

用途：仅在用户明确要筛选可采纳的竞品参考时使用。它提供具体参考做法、来源产品、对应调研点、可参考点和适配提醒；用户勾选后，页面生成可复制的确认摘要。

默认不在 Source Pack 后生成，也不作为普通 Canvas 交付自动生成。

生成时优先基于 `templates/design-reference-checklist.html`。

页面结构：

- 左侧逐条展示可独立采纳的参考：来源产品、对应调研点、可参考点、适配提醒与“采纳此参考”选择；不提供编辑字段，也不展示内部证据位置。
- 右侧提供可编辑 textarea，只汇总已采纳参考的确认摘要；不设单独备注字段，改写边界直接编辑最终文本。
- 勾选后自动生成只包含已采纳参考点的确认摘要；复制内容只包含布局 / 组件、触发规则、设计指令和约束，不夹带竞品分析过程。
