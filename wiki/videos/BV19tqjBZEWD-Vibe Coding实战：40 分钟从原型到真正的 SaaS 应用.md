---
type: video
bv: BV19tqjBZEWD
title: "Vibe Coding实战：40 分钟从原型到真正的 SaaS 应用"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV19tqjBZEWD
date: 2026-04-30
duration: 39:00
tags: [Vibe Coding, SaaS开发, AI工程安全, 全栈开发, 数据库迁移]
concepts: [Vibe Building, 驾驭工程, 原型优先开发]
entities: [Easonlee的AI笔记, Colin Matthews]
topics: [LLM-Agent工程实践, 技术人创业与产品思维]
---

# Vibe Coding实战：40 分钟从原型到真正的 SaaS 应用

## 一句话摘要
用 SaaS 模板 + Claude Code 将 Vibe Coded 原型升级为生产级全栈应用的完整实操演示，核心洞见：原型和产品的差距不在 AI 生成能力，而在认证、支付、安全、数据库迁移等"无趣但关键"的基础设施层。

## 核心观点

- 原型（客户端）和产品（全栈）的核心差距是服务器端：认证、数据库、第三方集成（Stripe、邮件、文件存储）、分析——这些 AI 不擅长一次性生成正确的部分
- Lovable/Bolt 等工具默认使用 Supabase 且 RLS 规则完全开放，导致安全漏洞——这是当前 AI 编程最大的安全隐患
- 数据库变更必须通过 migration 文件而非让 AI 直接写 SQL，因为代码可以 undo，数据库不能
- SaaS 模板的价值不是代码本身，而是让 AI 代码生成遵循已有的正确模式——模板比从零开始更容易 one-shot 成功
- AI 编程的核心工作流：plan mode 先规划 → 实现 → 读错误信息 → 补充文档 → 再实现，而非一次性放手让它跑

## 详细笔记

### 原型 vs 全栈应用：差距在哪里

原型通常只跑在客户端。全栈应用 = 客户端 + 服务器 + 数据库 + 第三方集成：

- **认证**：不自己造轮子，用 Google/GitHub OAuth
- **支付**：Stripe 集成
- **邮件**：如 Resend
- **文件存储**：如 Firebase Storage
- **产品分析**：如 PostHog
- **错误日志**：如 Sentry

视频中的原型是 Peter 用 Gemini + NanoBanana 做的 AI 职业头像生成器，有前端和本地后端，但缺少以上所有生产级组件。代码中还包含典型的 AI 生成错误：base64 编码的预览图占位符、`localhost:3001` 硬编码 URL（部署后会直接失败）。

### SaaS 模板方法

Colin 的模板（Next.js + React）预置了 Stripe 支付、Google OAuth、AI 聊天、邮件偏好、PostHog 分析、错误监控，以及完整的数据库访问模式。

**迁移流程**：
1. 将原型的组件文件拖入模板的 `components` 目录
2. 用 Claude Code 基于原型代码生成 `.md` spec 文件（需求文档），AI 自动提取了提示词等关键信息
3. 清理 spec 中的冗余内容（原始 800 行精简到核心需求）
4. 让 Claude Code 基于 spec + 模板已有模式实现

模板的核心价值：AI 会推断和遵循已有代码模式（认证检查、数据库访问、API 路由），因此比从零开始更可靠。

### Vibe Coding 工具的安全隐患

Lovable 和 Bolt 使用 Supabase 作为后端。Supabase 通过自动生成 API 端点来代替手写服务器代码，但 RLS（Row Level Security）规则默认完全开放——任何用户可以访问任何数据。

关键问题：
- 使用这些工具的人大多不知道 RLS 规则的存在
- Lovable 发布时会弹出警告，但需要用户自己通过 prompt 让 AI 配置 RLS
- 把安全配置交给 AI 来生成，本身就是风险
- Bolt 宣传的"自有云后端"实际上是白标 Supabase，功能和直接集成 Supabase 完全相同

Colin 的观点：与其依赖 RLS 规则，不如自己掌控服务器代码——安全边界更清晰，出错后定位问题更容易。

### 数据库迁移的正确做法

AI 编程工具的默认行为是直接修改数据库（写 SQL），这是危险的。正确做法是生成 migration 文件，经确认后再 apply。原因：
- 代码变更可以 git revert，数据库变更不能 undo
- migration 文件让代码和数据库始终同步
- 可以先审查变更内容，确认无误后再执行

实操中：AI 生成了新的 `headshots` 表（存储用户 ID 和生成历史），通过 migration 文件应用到已有数据库。

### 实操中的典型问题与修复

1. **模型版本错误**：Claude Code 使用了过时的 Gemini 模型名（`gemini-2.0-flash-exp`），因为训练数据截止日期后 API 已更新。修复方式：复制官方文档，粘贴给 Claude Code，让它用正确的模型和 API
2. **Plan Mode 工作流**：Colin 几乎从不跳过 plan mode——先让 AI 规划，审查后再执行，避免"放手让它跑"导致不可控变更

### AI 编程工具对比

- **Lovable / Bolt**：适合原型，但后端依赖 Supabase 且 RLS 默认开放，安全风险高
- **Claude Code / Codex**：适合在已有代码库上构建，能遵循已有模式。Codex 在大型代码库上表现更好
- **核心差异**：不是哪个工具"更好"，而是哪个工具让你犯不可逆错误的概率更低

### 部署与建议

部署方式：GitHub → Render（自动同步部署），或 Vercel。Colin 的课程重点不是证书，而是"学会技能，做出能产生收入的 side project"。

三条建议：
1. 使用 SaaS 模板——模板已有的模式引导 AI 做出更正确的决策
2. 用 VS Code + Claude Code 或 Codex
3. 配置好所有 API Key（Stripe、Google OAuth、文件存储等），不要只追求速度而忽略理解底层原理

## 我的评注

- **赞同**：模板方法比从零 vibe coding 更靠谱，和 [[驾驭工程]] 的核心逻辑一致——约束产生聚焦。模板中的已有模式就是约束，让 AI 在约束中发挥比在空白中发挥更有效。视频也验证了这一点：AI 在模板上 one-shot 成功率远高于从零开始。
- **赞同**：plan mode 的工作流是当前 AI 编程的最佳实践。先规划再执行、交替进行而非一次性放手，这和 [[Vibe Building]] 中"系统化在前，构建在后"的判断完全吻合。
- **质疑**：视频对 RLS 安全问题的讨论有误导性。Supabase RLS 本身不是问题，问题在于默认开放。这更像是产品设计的取舍（降低入门门槛 vs 安全默认值），而非 Supabase 架构的缺陷。自己写服务器代码也并不意味着安全——手动实现的认证逻辑同样可能有漏洞，只是更容易 code review。
- **质疑**：视频暗示"用模板就能避免 AI 编程的安全问题"，但模板本身的安全性取决于模板作者的水平。如果模板有漏洞，所有基于它的应用都有漏洞——这是单点故障的风险。
- **关联**：这个视频和 [[原型优先开发]] 形成完整闭环：原型优先解决了"如何快速验证方向"，这个视频解决了"验证之后如何变成产品"。两步之间的鸿沟——认证、支付、安全、数据库——正是 [[Vibe Building]] 中"瓶颈从执行转移到判断"的具体体现。

## 与其他知识的关联
- 相关概念：[[Vibe Building]]、[[驾驭工程]]、[[原型优先开发]]
- 相关实体：[[Easonlee的AI笔记]]、[[Colin Matthews]]
- 相关主题：[[LLM-Agent工程实践]]、[[技术人创业与产品思维]]

## 待深入问题
- RLS vs 自建服务器的安全模型，哪种在 AI 辅助开发场景下实际出错率更低？需要实证数据而非直觉判断
- SaaS 模板方法是否会形成"模板依赖"——当需求超出模板覆盖范围时，重构成本是否比从零构建更高？
- AI 编程工具的 plan mode 是否能被系统化为一种可复用的 harness 模式，而非依赖个人习惯？
