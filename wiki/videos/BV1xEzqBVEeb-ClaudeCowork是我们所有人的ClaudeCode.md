---
type: video
bv: BV1xEzqBVEeb
title: "Claude Cowork : Claude Cowork 是我们所有人的 Claude Code"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1xEzqBVEeb
date: 2026-04-30
duration: 92:00
tags: [AI产品, 异步Agent, 人机交互, Agent原生架构, Claude生态]
concepts: [异步Agent范式, Agent原生架构, Skills系统]
entities: [Every, Anthropic, Dan Shipper, Felix]
topics: [AI工程实践]
transcript: .b2t/transcripts/original/BV1xEzqBVEeb.txt
---

# Claude Cowork : Claude Cowork 是我们所有人的 Claude Code

## 一句话摘要

Claude Cowork 把 Claude Code 的异步 Agent 能力带给非技术用户，标志着一个核心范式转移：从"等 AI 回复"到"把任务交给 Agent，过会儿来看结果"。

## 核心观点

- **Claude Cowork = Claude Code 的非技术版**：底层是同一套 Agent 基础设施（甚至报错信息都来自 Claude Code），但 UI 更友好，面向非程序员
- **异步是关键心智转换**：非技术用户习惯了"发 prompt → 等回复 → 再发下一个"的同步模式；Cowork 让你"交办任务 → 去做别的事 → 回来看结果"，这是根本性的交互范式变化
- **Skills 是最核心的可定制面**：比起 MCP 工具或硬编码功能，Skills（Markdown 描述文件 + 可选脚本）是当前最灵活的扩展方式，也是 Opus 4.5 擅长遵循的指令格式
- **Agent 原生架构四原则**：Parity（Agent 能做用户在 UI 上能做的一切）、Granularity（工具粒度低于功能，功能留给 prompt/skill）、Composability（工具可自由组合）、Emerging Capability（用户会发现你没想到的用法，然后你为之构建）
- **先发再迭代，而不是闭门做完美品**：Felix 团队用一周半做出 Cowork，刻意放在独立 Tab 作为"施工现场"，邀请用户一起探索

## 详细笔记

### 产品定位与核心差异

Claude Cowork 是 Anthropic 在 Claude 应用内新增的第三个 Tab（Chat / Code / Cowork）。它本质上是 Claude Code 的 UI 包装——运行在用户本地电脑上，有文件系统访问权限，可以长时间运行任务。与普通 Claude Chat 的核心区别：

1. **异步交互**：可以在 Agent 工作时继续发送消息，不需要等它完成
2. **长时间运行**：任务可以跑几十分钟甚至一小时，不会像 Chat 那样几个回合就停止
3. **本地执行**：直接操作用户的电脑，有 Chrome 浏览器控制、文件系统访问等能力
4. **任务导向**：界面概念是"Task"而非"Chat"，鼓励交办复杂工作

### 实际使用场景演示

- **竞品分析**：让 Cowork 去 Every 网站找 5 个竞争对手并分析定位，它会长时间浏览和整理
- **邮件起草**：连接 Gmail 后，根据邮件上下文起草回复，生成的文本风格接近用户本人
- **日历审计**：分析一个月的日历数据，对比个人目标，评估时间分配是否合理（跑了一个多小时）
- **书籍分类**：读完整本书，对人物和观点做分类整理
- **数据分析**：在 PostHog 中查找特定按钮的点击数据，替代了需要找数据团队手动查询的工作
- **Chrome 浏览器操控**：连接 Chrome 后可以浏览网页、读取 Twitter 信息流、操作 Google Docs
- **Google Docs 抄写编辑**：使用 Skills 中的校对规则，在 Google Docs 中逐条查找并建议修改（演示不太成功，但展示了方向）

### 与 Anthropic 团队的对话

Felix（Anthropic 技术团队成员）分享了几个关键设计决策：

**为什么是独立 Tab？**
- 这是一个"施工现场"，允许粗糙、快速迭代
- 让用户明确知道这是实验性功能，预期不同
- 当前运行在本地，与 Chat 的云端架构不同

**关于未来 UI 趋势**
- "搜索框"式的输入会长期存在（类似 Chrome 地址栏或 Google 搜索框的泛化）
- 但不需要为每个场景建单独的输入框——更可能走向少量通用入口
- Excel 类比：通用工具会被 power user 发现深层工作流，这些工作流有时会独立成产品，但 power user 往往更愿意留在通用工具中

**关于 Skills 系统**
- Felix 个人正在从写 MCP 工具转向写 Skills
- Skills = Markdown 描述文件 + 可选的二进制脚本
- Opus 4.5 非常擅长遵循 Skills 指令
- 这是当前最核心的可定制面，Cowork 自动加载已安装的 Claude Code Skills

### Agent 原生架构原则

Every 团队总结的四条原则，Felix 表示认同：

1. **Parity**：用户在 UI 能做的，Agent 都应该能做。Cowork 中的体现——当用户请求访问某个文件夹时，Agent 自动模拟了文件选择器的操作
2. **Granularity**：工具应该比功能粒度更低，功能由 prompt/skill 定义。好处是模型智能提升时，不需要重写工具
3. **Composability**：低粒度工具可以自由组合出未预见的功能
4. **Emerging Capability**：用户会发明你没想到的用法，你观察后为之构建

**重要洞察**：模型能力提升的速度远快于开发者产出工具的速度。因此，越通用、越可组合的工具设计，越能从模型进步中受益。

### 工具与 Skills 的张力

当前存在一个设计张力：
- 高度特化的工具（如"搜索邮件"、"读取邮件"分别作为独立工具）更确定性、更可靠
- 极度通用的工具（如一个 "execute" 工具 + Skills 描述）更灵活但更不可预测
- Skills 是中间路线：用 Markdown 描述意图，用脚本处理确定性部分
- Felix 的做法：将工作流拆分为确定性部分（用工具/脚本）和非确定性部分（交给模型），但承认"完全不给工具、让模型从零开始"也不是不可能的未来

### 评价

- **想法（Green）**：给非技术用户 Claude Code 级别的 Agent 能力，是正确的方向
- **执行（Yellow）**：UI 还有很多粗糙之处——权限跳过逻辑混乱、本地/云端区分不清、任务状态不直观、移动端缺失

## 我的评注

- **赞同**：异步范式是非技术用户使用 AI 的下一个关键解锁。当前大多数人用 Chat 类产品还停留在"对话"模式，但真正的生产力来自"交办→审查"模式。Cowork 把这个范式显式化了
- **赞同**：Skills 作为核心扩展面非常聪明。它利用了 Opus 4.5 强大的指令遵循能力，同时保持了人类可读、可分享、可迭代的特性。比起 MCP 的工程化门槛，Skills 降低了定制 Agent 行为的门槛
- **质疑**：本地/云端的混淆是一个真实风险。用户在同一个应用内，一个 Tab 是云端执行，另一个 Tab 是本地执行，但 UI 没有清晰区分。这对安全意识和预期管理都是挑战
- **质疑**：Google Docs 抄写编辑的失败演示说明，浏览器操控类任务的可靠性还远未达到生产级别。Agent 在非结构化 UI 中的操作精度仍有很大差距
- **关联**：视频中讨论的 Agent 原生架构四原则与 [[MVP思维]] 和 [[原型优先开发]] 高度一致——先给用户最小的可组合单元，让涌现能力告诉你该构建什么。这也是 [[乘风策略]] 的体现：利用模型能力提升的速度，做更通用而非更特化的设计

## 与其他知识的关联
- 相关概念：[[异步Agent范式]]、[[Agent原生架构]]、[[Skills系统]]
- 相关实体：[[Every]]、[[Anthropic]]
- 相关主题：[[AI工程实践]]

## 待深入问题
- Skills 和 MCP 的边界在哪里？什么该用 Skill 描述，什么该用 MCP 工具实现？是否有明确的决策框架？
- 异步 Agent 在企业场景下的安全边界如何界定？本地执行意味着数据不经过 Anthropic 服务器，但 Agent 的行为本身如何审计？
- "搜索框泛化"假说——如果最终走向一个通用入口处理所有任务，那不同领域的上下文切换和权限隔离如何解决？
- Google Docs 操控失败是否说明 Computer Use 在生产力工具中的可靠性还不够？需要什么样的架构改进才能让 Agent 可靠地操作非结构化 UI？
