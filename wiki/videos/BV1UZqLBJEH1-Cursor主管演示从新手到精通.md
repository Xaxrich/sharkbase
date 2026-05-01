---
type: video
bv: BV1UZqLBJEH1
title: "Curosr主管演示：50分钟从新手到精通Cursor"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1UZqLBJEH1
date: 2026-04-30
duration: 50:00
tags: [Cursor, AI编程, 开发者体验, Agent, Vibe Coding]
concepts: [AI Agent自验证循环, Cursor Rules, Vibe Coding与工程实践的边界]
entities: [Lee Robinson, Cursor, Vercel]
topics: [LLM-Agent工程实践]
transcript: .b2t/transcripts/original/
---

# Curosr主管演示：50分钟从新手到精通Cursor

## 一句话摘要

Cursor 主管 Lee Robinson 通过现场构建一个完整应用，演示了 AI Agent 辅助开发的全流程，并划清了"vibe coding"与"真正的软件工程"之间的界限。

## 核心观点

- **测试不是可选项，是 Agent 的自验证回路**：测试让 Agent 能运行代码、读取失败输出、自动修复，形成闭环。没有测试，Agent 只能靠你反复说"这不对"。
- **Prompt 即 PRD，但要补上技术地基**：给 Agent 的需求文档比传统 PRD 更需要技术判断——你得知道为什么选 PostgreSQL 而不是 MongoDB，为什么需要 OAuth 而不是自定义登录。
- **Vibe coding 是第一天，不是第一天之后**：快速原型没问题，但维护和迭代需要你理解自己构建的东西。不懂 API key 为什么不能放客户端的人，迟早会出安全事故。
- **Cursor Rules 是编码化工作习惯**：当你发现自己重复说同一句话，就该把它写成规则——测试必须跑、提交必须早、包管理器用 pnpm。
- **有经验的工程师才是 AI 最大的受益者**：Agent 放大的是你已有的判断力，不是替代你缺乏的知识。

## 详细笔记

### 嘉宾背景

Lee Robinson，前 Vercel 开发者体验负责人，参与构建 v0，近期加入 Cursor。他半年前从 AI 编程的怀疑者转变为深度使用者，触发点是背景 Agent 能从 Slack 消息直接修复 bug——让他意识到软件构建方式正在根本性改变。

### 从零到一：用 Cursor 构建应用

#### 结构化需求文档

Lee 现场演示构建一个 Last.fm 风格的音乐追踪应用。他的做法不是直接让 Agent 开写代码，而是先写一份结构化的需求文档，包含：

- **产品需求**：Google OAuth 登录、Spotify API 集成、数据存储到数据库
- **测试策略**：业务逻辑测试 + 端到端测试——关键是让 Agent 拥有自验证能力
- **技术栈选择**：React、Tailwind、shadcn/ui、ESLint、Git、pnpm
- **设计方向**：minimal、functional、intentional use of color
- **开放问题**：数据同步频率、核心统计指标——留给 Agent 提问

他强调：你不是在写 PRD，你是在给一个不知上下文的协作者提供足够的判断依据。

#### Agent 工作流程

1. Agent 读取需求，生成分阶段计划，包含每阶段的交付物和验证标准
2. 人工审核计划，调整顺序（把测试提前）、补充细节、回答开放问题
3. Agent 按阶段执行：安装依赖、配置工具、编写代码、运行测试
4. Agent 遇到测试失败时自动定位问题并修复——"I can see the issue, the default page doesn't have a main element"
5. 每阶段完成后自动 commit、更新计划中的 TODO 状态

#### 前台 Agent 与后台 Agent

- **前台 Agent**：实时观看，逐条审批文件变更，随时打断修正
- **后台 Agent**：从 Slack 或其他入口触发，处理独立的小任务（修复 typo、UI bug），适合低风险、低上下文的工作
- 多个前台 Agent 同时操作同一代码库时需谨慎——可能产生冲突

### Cursor Rules：把工作习惯编码化

当你发现自己在多个对话中重复相同指令，就应该写成 Cursor Rule。例如：

- 总是运行测试
- 总是使用特定包管理器
- 提交信息要描述性、提交频率要高

Cursor Rules 有两种形式：
- `.cursorrules` 单文件（旧版，仍支持）
- `.cursor/rules/` 目录下多文件（新版），可按需引入、可打标签（如 `@web` 搜索网络、`@docs` 引入文档）

### 上下文管理

- 对话历史是 Agent 的工作记忆，会累积消耗 context window
- 当已有 commit 保存了当前状态，应开新对话避免旧上下文干扰
- 接近 context 上限时出现"大海捞针"问题——Agent 在海量信息中难以定位相关内容

### Vibe Coding 与软件工程的分野

Lee 对 vibe coding 的态度很明确：

- **适合**：快速原型、个人项目、一次性的代码实验
- **不适合**：需要长期维护的产品、团队协作的代码库、生产环境

核心区别不在工具，在知识。"第一天之后"才是真正的挑战——你构建的应用出了问题，你能否定位、修复、迭代？如果不懂循环语句，你看 Agent 生成的 for loop 就只是一段神秘文本。

### 对产品经理和新手的建议

- 边做边学，同时学习计算机科学基础——数据结构、算法、客户端/服务端的区别
- 善用 AI 解释代码：在 Cursor 中选中不理解的部分，直接提问
- 不要把 AI 当"快速致富"工具，把它当"我想学软件工程"的加速器
- 不懂 API key 的人不会知道该问"为什么 API key 不能放在客户端"——这是真正的风险

### Cursor vs Vercel 的工作方式对比

- **Vercel**：成熟公司，成熟的产发流程，专职产品经理
- **Cursor**：工程师即产品经理，极高的自主权，快速试错，至今只有一位 PM
- 趋势：产品型工程师（product-minded engineer）正在成为主流

Lee 分享了在 Cursor 第一周的观察：工程师 Eric 用脚本（而非 SaaS 工具 UI）处理批量退款和邮件发送——自动测试、dry run、失败状态记录、提交到内部脚本仓库。这是 Agent 放大有经验工程师能力的典型案例。

## 我的评注

- **赞同**：测试作为 Agent 自验证回路这个观点非常有洞见。传统上测试是给人看的质量保障，现在测试同时是给 Agent 看的反馈信号——这个视角转换解释了为什么"AI 时代测试更重要而非更不重要"。TypeScript、ESLint、编译器同理：都是向 Agent 输出信号的工具。
- **赞同**：Vibe coding 和软件工程的二分法比"AI 取代程序员"的叙事诚实得多。关键不是 AI 能不能写代码，是你能不能理解 AI 写的代码。
- **质疑**：演示中的应用仍然非常简单（Hello World + 设置页），Agent 自动修复的问题也都是浅层的（缺少 HTML 元素、缺少类型定义）。当遇到运行时逻辑错误、跨服务状态不一致、性能瓶颈时，Agent 的自验证循环是否还能闭环，视频没有涉及。
- **质疑**：Lee 对"学习基础"的呼吁是对的，但他没有回答一个现实问题：很多用 vibe coding 构建第一个版本的人，根本没有耐心回过头学基础。这不是意愿问题，是激励结构问题——vibe coding 给你的即时反馈太强了。
- **关联**：这与[[上下文工程]]的核心主张一致——Agent 的输出质量取决于你提供的上下文质量。Lee 的需求文档本质上就是在做上下文工程。

## 与其他知识的关联

- 相关概念：[[AI Agent自验证循环]]、[[上下文工程]]、[[Vibe Building]]、[[驾驭工程]]
- 相关实体：[[Lee Robinson]]、[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题

- Agent 在复杂代码库中的表现：当项目有数千文件、微服务架构、多个数据库时，Agent 的上下文管理策略是什么？
- Cursor Rules 的最佳实践：规则过多是否会增加 context 负担、降低 Agent 灵活性？规则之间冲突怎么处理？
- 从 vibe coding 到工程实践的过渡路径：有没有结构化的方法帮助新手在获得即时反馈的同时逐步建立基础知识？
- Agent 的安全边界：Lee 提到 API key 泄露风险，但 Agent 本身执行终端命令时是否有沙箱机制？误操作的生产数据破坏如何防范？
