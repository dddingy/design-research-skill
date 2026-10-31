# Feature Benchmarking 交付自检清单

本清单只核验产物；具体内容标准以 `rules.md` 和 `output-spec.md` 为准。

## Source Pack

- 是否承接已确认调研点、覆盖 P0 seed，并让扩展样本服务当前主题？
- 页面结构、范围区、产品卡片、Summary 与下一步确认区是否符合 `output-spec.md`？
- 来源、截图、本地 assets 与候选证据门槛是否符合 `rules.md`？
- 是否已运行 `scripts/validate_source_pack.py {输出目录}/00_source_pack.html` 且通过？
- 最终回复是否只引导用户选择是否进入 Canvas，并写清默认产品与覆盖调研点？

## Canvas Benchmark

- 是否在当前任务已有 Source Pack 且用户确认后才生成？
- 矩阵、Reference Links 行、非空格子与 Insight 表是否符合 `output-spec.md`？
- 细证据、来源回链、空格处理、新增样本和 Insight 判断是否符合 `rules.md`？
- 是否只在用户明确要求时生成 Checklist？

## 可选产物

- 单产品附录是否确有触发条件，且结构符合 `output-spec.md`？
- Checklist 是否仅按需生成，页面与确认摘要是否符合 `output-spec.md`？
- 未确认的 Insight 是否仍只留在竞品报告，未进入后续设计输入？
