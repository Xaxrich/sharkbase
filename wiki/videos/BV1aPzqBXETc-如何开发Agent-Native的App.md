---
type: video
bv: BV1aPzqBXETc
title: "如何开发Agent-Native的App？"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1aPzqBXETc
date: 2026-04-30
duration: 22:00
tags: [Agent架构, Vibe Coding, AI原生应用, 变革管理, Claude工程实践]
concepts: [Agent-Native架构, Vibe Coding, AI驱动组织运营]
entities: [Easonlee的AI笔记, Compound Engineering]
topics: [LLM-Agent工程实践]
---

# 如何开发Agent-Native的App？

## 一句话摘要

两位 AI 从业者通过展示实际构建的应用，讨论了 Agent-Native 架构如何解决传统 AI 应用的准确性问题，以及 AI 原生思维如何渗透到公司运营的每个环节。

## 核心观点

- Vibe Coding 能在两小时内做到 95%，但最后 5% 会让你无限循环——根本原因是架构不够 Agent-Native
- Agent-Native 架构的核心区别：传统应用是"调用 AI 填一个字段"，Agent-Native 是"AI 知道这个字段必须填，会主动搜索直到找到答案"
- AI 原生运营不是技术问题，是变革管理问题——组织越大越难推动，但 Agent 可以绕过人的阻力
- 高自主性的人（high agency）在 AI 时代获得了指数级优势——从步行到骑自行车到开直升机
- 正确的初期投入（日志、调试工具、自我修复能力）决定了 Vibe Coding 项目的生死

## 详细笔记

### Demo 1: 公司分析应用（Deal Hunter）

一个用于投资尽职调查的应用，输入公司名后自动抓取背景信息、财务数据、管理层信息、法律风险，生成评估报告和交易备忘录。

- 技术栈：Claude API + Amplify（拉取财务数据）+ Firecrawl（网页抓取）
- 核心痛点：设计很快就到位，但数据准确性迟迟无法解决——幻觉、数据缺失、字段未填充
- 典型表现：对非上市公司的分析基本失败，因为 Agent 不会主动去搜公开信息，只是返回"信息不可用"

### Vibe Coding 的 95% 陷阱

- 前 95% 极快完成，后 5% 无限循环
- 本质原因：没有给 AI 足够的工具和架构去自我调试、自我修复
- 解决方向：初期就建立 guardrails、proper logging、调试工具，让 AI 能 self-heal

### Agent-Native 架构 vs 传统 AI 应用

- **传统架构**：界面先设计好，AI 被当作填字工具——"这个字段空了，调 API 填一下"
- **Agent-Native 架构**：AI 理解整个任务的完整性——"这个字段必须填，我主动搜索直到找到答案"
- Compound Engineering 提供的 Agent Native Review 工具可以审查应用是否符合 Agent-Native 原则
- Compound Engineering 插件还支持"让它自己测试自己"——不断循环直到功能正常

### Demo 2: 人格分析应用

- 30 分钟问卷 → 生成约 100 页的完整人格分析文档
- 支持创建自定义 AI（ChatGPT GPT / Claude Project），基于人格评分生成 prompt
- 支持伴侣对比、生成临床版 PDF、生成沟通风格卡等
- 设计质量远超典型 Vibe Coding 产物——不像 Lovable 模板，看起来像真正的产品
- 但数据完整性问题依然存在：用户偶尔遇到结果损坏

### AI 原生公司运营

用 Notion Agent 做 2026 年战略规划：

1. CEO 写出顶层战略（人机协作完成）
2. Notion Agent 逐个访谈每个部门负责人：上季度表现、本季度计划、如何对齐公司战略
3. Agent 会追问、挑战假设、帮助校验逻辑
4. 结果：20 人公司的运营流程变得极其高效

延伸应用：
- AI 自动扫描 Discord 对话，发现有趣话题并推送选题建议
- AI 读取会议记录（Granola），主动向 CEO 汇报需要关注的事项
- 文化建设：将"会议默认录音"设为团队规范，为后续 AI 利用铺路

### 变革管理的现实

- 大组织（如拥有 30 个 CEO 的集团）推动 AI 转型极难
- Agent 的潜在价值：为不同人定制不同激励话术——销售听"翻倍营收"，设计师听"拿设计奖"
- 领导者没有时间和每个人一对一，Agent 可以补上这个缺口

### Claude Code 工作流技巧

- **Happy Cloud**（happy.engineering）：在 Claude Code 线程中写 `mobile`，手机和电脑会话同步，可以随时离开
- **Cloud Island**：将所有 Claude 会话放入 iPhone 动态岛，方便监控
- **移动端工作流**：在手机上用 Claude 修 bug → 回家后有多个 PR 分支 → 合并到一个测试分支 → 手机测试 → 确认后合并
- **模型选择策略**：`/model` 设为 Opus，Claude Code 会自动在 Opus（规划）和 Sonnet（代码审查）之间切换，既快又聪明
- **Sonnet 1M 上下文窗口**：处理大型代码库时使用

## 我的评注

- **赞同**：Agent-Native vs 传统的区分切中要害。很多 AI 应用的失败不是因为模型不够好，而是架构把 AI 当"被动工具"而非"主动执行者"——这解释了为什么同一个模型在不同应用里效果天差地别
- **赞同**：Vibe Coding 的 95% 陷阱描述极其精准。前 95% 是确定性工作（UI、流程），后 5% 是不确定性工作（数据准确性、边界情况），后者恰恰需要 Agent 式的主动搜索和自我修复
- **质疑**：对话对"Agent-Native 架构"的具体技术实现描述不足——只说了"AI 主动搜索直到找到答案"，但没有展开 prompt 设计、工具编排、错误恢复等关键细节。视频标题是"如何开发"，但"如何"的部分偏浅
- **质疑**：对变革管理的讨论过于乐观——"Agent 可以绕过人的阻力"这个判断忽略了信任和授权问题。如果员工不信任 Agent 的判断，Agent 再聪明也推不动
- **关联**：与 [[Agent原生架构]] 直接相关，但这个视频更多是从实践者视角补充了"为什么传统架构会卡在最后 5%"的具体机制

## 与其他知识的关联

- 相关概念：[[Agent原生架构]]、[[Vibe Coding]]、[[上下文工程]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题

- Agent-Native 架构的具体技术模式是什么？如何设计 prompt 和工具链让 AI 真正"主动"？
- 在数据准确性要求高的场景（尽职调查、医疗），Agent-Native 如何与人类审核流程结合？
- Notion Agent 访谈部门负责人的 prompt 是如何设计的？如何避免信息失真？
- Compound Engineering 的 Agent Native Review 具体审查哪些维度？
