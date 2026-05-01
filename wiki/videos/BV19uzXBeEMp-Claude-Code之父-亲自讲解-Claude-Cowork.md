---
type: video
bv: BV19uzXBeEMp
title: "Claude Code之父：亲自讲解 Claude Cowork"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV19uzXBeEMp
date: 2026-04-30
duration: 42:00
tags: [AI Agent, Claude Code, 人机协作, 自动化办公, 生产力工具]
concepts: [AI Agent, 复利工程, 技能系统]
entities: [Boris, Anthropic]
topics: [LLM-Agent工程实践]
---

# Claude Code之父：亲自讲解 Claude Cowork

## 一句话摘要

Claude Cowork 创造者 Boris 亲自演示了如何用 Agent 操作文件、浏览器和邮件，并分享了他使用 Claude Code 的核心方法论——并行派发任务、投资 CLAUDE.md、让模型自验证输出。

## 核心观点

- **Agent 的本质是"能行动的 AI"**，不是聊天，不是搜索，而是能操作你电脑上的工具、文件和浏览器
- **并行任务 > 深度单任务**：新工作流的核心是同时派发多个任务，在它们之间跳转、答疑、放行，而非自己埋头做一件事
- **Opus 4 + thinking 是当前最佳选择**——虽然更贵更慢，但因为更聪明、需要更少 steering，最终反而更快更省
- **CLAUDE.md 是复利工程的基础设施**：团队共享、持续更新、永不对同一问题评论两次
- **给模型验证自身输出的途径**，结果会显著变好——如同摘掉画家的眼罩

## 详细笔记

### Cowork 产品定位

- Cowork 是 Claude Code 的 UI 化版本，底层用的是同一套 SDK（Claude Agent SDK）
- 目标用户：不想用终端的非技术人群——Anthropic 内部的销售、设计、产品经理已在日常使用 Claude Code
- 安全设计：默认不可访问任何文件，用户必须 opt-in 授权特定文件夹；底层运行虚拟机隔离；新增删除保护，操作前会确认
- 仅 macOS 可用，Windows 即将推出

### Agent 真正的含义

- Boris 强调 "agent" 一词已被过度使用，失去了原本的含义
- 真正的 Agent = 能**使用工具**并**采取行动**的 AI，区别于 chat/search 类产品
- Anthropic 从早期就在模型层面投入 tool use 和 computer use 能力
- 反向询问（reverse solicitation）：模型不确定时会主动问用户，而非自行假设

### 演示场景

1. **文件整理**：授权 receipts 文件夹，让 Cowork 根据收据上的日期重命名文件——发现缺日期的文件时主动询问
2. **生成电子表格**：将收据数据整理进 spreadsheet
3. **操作浏览器**：打开 Google Sheets 创建在线表格，演示 computer use——模型能看到屏幕、点击、输入
4. **发邮件**：打开 Gmail，搜索联系人 Amy，起草邮件——全程通过浏览器操作完成
5. **Slack 自动化**：Boris 分享自己每周用 Cowork 检查团队工作表，自动给未填状态的工程师发 Slack 消息

### 并行工作流

- 核心转变：从"自己做一件事"到"同时派发 N 件事，在它们之间切换"
- Boris 的习惯：同时开多个 tab/任务，一个在跑时切到另一个
- "现在是多线程并行主义的时代——不再是深度钻一个东西，而是做个通才、照看你的 quas"

### 技能系统（Skills）

- Skill = 可复用的操作模板，让模型知道如何处理特定工具/格式
- Cowork 内置了 Excel 等 skill；用户可以为 AutoCAD、Salesforce 等自定义 skill
- 建议：起步时不要过度定制，先用简单功能，等发现模型不擅长某类任务时再写 skill

### Boris 的 Claude Code 工作流（原帖 990+ bookmarks）

1. **并行任务**：开多个 tab，轮流检查，一旦 plan 可行就开 auto-accept edits
2. **跨平台使用**：终端、Web、iOS 多端切换；Boris 约 50% 的编码在手机上完成
3. **始终用 Opus 4 + thinking**：更聪明的模型反而更省 token、更快、更便宜
4. **团队共享 CLAUDE.md**：check into git，全员贡献，看到 Claude 犯错就补一条——这是"复利工程"（compounding engineering）的核心
5. **GitHub Action 集成**：`claude install github-action`，在 PR/Issue 中 @claude 让它自动修改——最常见的用途就是更新 CLAUDE.md
6. **Plan Mode 先行**：先在 plan mode 反复对齐，plan 好了再切 auto-accept——"once the plan is good, the code is good"
7. **让模型自验证**：用 Chrome 扩展让模型看到自己的输出、运行测试、启动 dev server——"摘掉眼罩"

### 提升性能的三件事

Boris 推荐的 Claude Code 性能优化三板斧：
1. 用 Opus 4 with thinking
2. 维护好 CLAUDE.md
3. 给模型验证自身输出的方式

### 未来展望

- 指数增长难以直觉预测——半年前 Dario 预测年底没人写代码，Boris 起初不信，但过去两个月 Claude Code 写了 100% 的代码而他自己一行没写
- 对 Cowork 的预测：枯燥的连接型任务（app A → app B、数据搬运）将被 Agent 自动化
- 类比 iPhone：没人预见 Uber，但 GPS 使其成为可能；Agent 时代也会出现类似的意外应用

## 我的评注

- **赞同**："once the plan is good, the code is good" 这个判断非常精准。Plan mode 被严重低估——很多人跳过规划直接让模型写代码，结果反复修改反而更慢。这本质上是把"架构决策"和"代码执行"解耦了。
- **赞同**：自验证的观点极具洞察。模型写代码却看不到运行结果，就像盲人画画——这不是能力问题，是反馈闭环缺失。给模型 Chrome 扩展让它"看见"自己的输出，是一个被低估的工程实践。
- **质疑**："50% 编码在手机上完成"这个说法更像是展示产品能力而非真实生产力指标。手机适合轻量级 steering（review plan、approve edit），但复杂架构决策仍然需要大屏和深度思考。
- **质疑**：Boris 对安全性的讨论过于乐观。虚拟机隔离和删除保护是好的，但 prompt injection 攻击面（模型操控浏览器访问恶意页面）是一个真实且未解决的问题，他承认了这一点但未深入讨论风险量化。
- **关联**：Cowork 的 Skill 系统与 [[Agent原生架构]] 中讨论的"工具层"设计高度一致——Agent 的能力边界由可用工具定义，而非模型能力本身。这也呼应了 [[MVP思维]] 中"先跑通最小闭环"的理念。

## 待深入问题

- Skill 系统的编写规范和最佳实践是什么？如何写出一个高质量的 skill？
- CLAUDE.md 的组织结构如何避免膨胀？当条目达到数百条时，模型是否还能有效利用？
- prompt injection 在 browser use 场景下的攻击面具体有多大？有哪些已知的防护策略？
- "复利工程"（compounding engineering）的量化效果如何？CLAUDE.md 的投入产出比能否测量？
- 当多个并行任务之间有依赖关系时，如何协调？Cowork 是否支持任务间通信？
