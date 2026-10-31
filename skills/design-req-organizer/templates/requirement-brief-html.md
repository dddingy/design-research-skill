# Human Requirement Brief HTML Template

用于生成 `design-requirement-brief-[需求名].html`。这份文件是给 PM / 设计师快速阅读的需求整理页，不是设计定义页，也不是 AI 生成设计稿输入。

## 必须包含的内容结构

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[需求名] 需求整理</title>
  <style>
    :root {
      --bg: #ffffff;
      --text: #172033;
      --muted: #4f5f74;
      --line: #d8e0ec;
      --soft: #f7f9fc;
      --blue: #2457d6;
    }
    * { box-sizing: border-box; }
    body { margin: 0; font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: var(--text); background: var(--bg); }
    main { max-width: 1080px; margin: 0 auto; padding: 40px 36px 64px; }
    .hero { margin-bottom: 28px; padding-bottom: 22px; border-bottom: 2px solid var(--text); }
    .eyebrow { color: var(--blue); font-size: 13px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
    h1 { margin: 10px 0 12px; font-size: 36px; line-height: 1.18; letter-spacing: 0; }
    .summary { max-width: 980px; color: var(--muted); font-size: 17px; line-height: 1.7; }
    .grid { display: block; }
    .card { padding: 24px 0 18px; margin: 0; border-bottom: 1px solid var(--line); }
    .card h2 { margin: 0 0 14px; font-size: 22px; }
    .card h3 { margin: 20px 0 10px; font-size: 17px; font-weight: 800; }
    p, li { color: var(--muted); font-size: 16px; line-height: 1.68; }
    strong { color: var(--text); font-weight: 800; }
    ul { margin: 0; padding-left: 20px; }
    li { margin: 7px 0; }
    table { width: 100%; border-collapse: collapse; table-layout: fixed; }
    .w1h-table { table-layout: auto; }
    .w1h-table th { width: 112px; white-space: nowrap; }
    .w1h-table td { width: auto; }
    th, td { border: 1px solid var(--line); padding: 13px 14px; text-align: left; vertical-align: top; font-size: 14px; line-height: 1.5; }
    th { background: var(--soft); color: var(--text); }
    td { color: var(--muted); }
    .tag { display: inline-flex; padding: 4px 0; color: var(--muted); font-weight: 700; font-size: 13px; }
    .note { border-left: 3px solid var(--blue); background: var(--soft); padding: 12px 14px; margin: 14px 0 0; color: var(--muted); }
    .prompt-draft { margin-top: 18px; padding: 18px 20px; background: #f3f6fa; border: 0; border-radius: 8px; }
    .prompt-draft h3 { margin-top: 0; }
    .prompt-help { margin: 4px 0 12px; color: var(--muted); font-size: 13px; line-height: 1.5; }
    .copy-row { display: block; }
    .copy-output { width: 100%; min-height: 120px; resize: vertical; border: 1px solid var(--line); border-radius: 10px; padding: 10px 12px; color: var(--text); background: #fff; font: inherit; }
    .copy-button { margin-top: 12px; border: 1px solid #c8d6ff; border-radius: 10px; padding: 9px 12px; background: #fff; color: #1f3f9c; font-weight: 700; cursor: pointer; }
    .copy-status { margin-left: 10px; color: var(--muted); font-size: 12px; }
    @media (max-width: 860px) { main { padding: 28px 18px 52px; } h1 { font-size: 30px; } table { display: block; overflow-x: auto; } }
  </style>
</head>
<body>
  <main>
    <header class="hero">
      <div class="eyebrow">Requirement Brief</div>
      <h1>[需求名] 需求整理</h1>
      <p class="summary">[两句内说明产品 / 业务对象，以及本期要设计的具体功能、核心流程和不包含范围。]</p>
    </header>

    <section class="card">
      <h2>5W1H</h2>
      <table class="w1h-table">
        <tbody>
          <tr><th>Who</th><td>[用户 / 角色]</td></tr>
          <tr><th>Why</th><td>[问题 / 机会]</td></tr>
          <tr><th>What</th><td>[本需求做什么]</td></tr>
          <tr><th>Where</th><td>[入口 / 页面 / 容器]</td></tr>
          <tr><th>When</th><td>[功能发生时机 / 用户使用场景时机，不写项目排期]</td></tr>
          <tr><th>How</th><td>[系统和用户如何完成]</td></tr>
        </tbody>
      </table>
    </section>

    [仅在材料明确给出版本范围、复用边界或不做范围时，追加 Current Scope / Boundary；没有明确边界时省略]

    <section class="grid">
      <section class="card">
        <h2>设计目标</h2>
        <ul>[每条一个独立设计对象，可以是页面、容器、流程节点或页内模块。默认一句概括；只有一句话因包含多个明确模块 / 能力而难以阅读时，才在该条下用二级 bullet 展开真实组成部分。外部入口与返回路径不属于页内模块。]</ul>
      </section>
      <section class="card">
        <h2>用户与影响范围</h2>
        <p>[面向谁，覆盖哪些范围，权限和内测 / 排除范围。]</p>
      </section>
    </section>

    <section class="card">
      <h2>设计重点关注</h2>
      <ul>[只写材料明确指出的设计难点。每条包含具体对象 / 场景、难点或矛盾，以及对理解、判断、操作、流程或状态的影响；没有真实难点时省略或写「材料中未提及」。]</ul>
    </section>

    <section class="card">
      <h2>设计约束条件</h2>
      [按主题分组输出约束，每条为规则句并标注来源。]
    </section>

    <section class="card">
      <h2>设计相关结论</h2>
      [按页面 / 功能 / 模块分组，只写已拍板结论并标注来源。]
    </section>

    <section class="card">
      <h2>交付内容与时间节点</h2>
      <table>[交付物、负责人、截止时间；仅当材料明确时才加入格式 / 保真度。]</table>
    </section>

    <section class="card">
      <h2>待确认问题</h2>
      <ul>[只列需要 PM / 研发 / 业务给外部答案的问题。]</ul>
    </section>

    <section class="card">
      <h2>建议竞品调研关注点</h2>
      <p>[提炼 1 条最值得 benchmark 的主路径或关键设计问题，必须来自当前需求本身；不写竞品结论，不写外部产品名称。]</p>
      <ul>[列出建议优先调研点，默认 1 条，必要时 2 条，复杂需求最多 3 条；只有当调研主题明显不同、后续需要不同截图证据时才拆开。每条必须能作为 feature benchmarking 或 Canvas 的一行横向比较主题，写清要观察的页面/容器组合、用户动作、系统反馈、状态或信息结构；不按页面、字段、按钮逐项拆分。]</ul>

      <div class="prompt-draft">
        <h3>可选下一步：feature benchmarking</h3>
        <p class="prompt-help">可直接复制给 Feature Benchmarking Skill，后续由 Feature Benchmarking Skill 搜集和推荐调研样本。</p>
        <div class="copy-row">
          <textarea class="copy-output" id="benchmark-prompt-draft">用 feature-benchmarking-skill 调研「[页面 / 功能 / 流程]」设计。

重点：[1-2 个可横向比较的设计维度]。
输出：真实产品截图、来源和横向对比；不生成设计方案。</textarea>
          <button class="copy-button" type="button" data-copy-target="benchmark-prompt-draft">复制/选中</button>
          <span class="copy-status">如果浏览器拦截复制，会自动选中文本。</span>
        </div>
      </div>
    </section>
  </main>
  <script>
    document.querySelectorAll("[data-copy-target]").forEach((button) => {
      button.addEventListener("click", async () => {
        const target = document.getElementById(button.dataset.copyTarget);
        const status = button.parentElement.querySelector(".copy-status");
        const originalText = button.textContent;
        target.select();
        target.setSelectionRange(0, target.value.length);
        try {
          if (navigator.clipboard && window.isSecureContext) {
            await navigator.clipboard.writeText(target.value);
          } else if (document.execCommand("copy") === false) {
            throw new Error("copy failed");
          }
          button.textContent = "已复制";
          if (status) status.textContent = "已复制到剪贴板。";
        } catch (error) {
          button.textContent = "已选中，请按 Cmd+C";
          if (status) status.textContent = "浏览器拦截了自动复制，文本已选中，请按 Cmd+C。";
        }
        setTimeout(() => { button.textContent = originalText || "复制/选中"; }, 1600);
      });
    });
  </script>
</body>
</html>
```
