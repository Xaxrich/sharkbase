---
type: concept
name: Agent原生架构
tags: [Agent架构, 产品设计, 软件架构, 组合性]
first_seen: 2026-04-30
---

# Agent原生架构

## 定义
以 Agent 为核心而非确定性规则为核心构建软件应用。底层是一个 Agent（而非传统代码逻辑），Agent 连接到应用的 UI，用户操作通过 Agent 以 prompt 形式传递，Agent 自主决定调用哪些工具、如何组合、执行多少步。四条核心原则：Parity（对等性）、Granularity（粒度）、Composability（组合性）、Emerging Capability（涌现能力）。

## 为什么重要
它颠覆了传统软件"需求→设计→编码→测试"的确定性构建流程。传统软件中，每个功能都是开发者预定义的；Agent 原生架构中，功能由工具组合和 prompt/skill 催生，大量用户行为是开发者未预见的。这意味着：模型能力每提升一次，你的产品自动获得新能力——只要你做了足够通用的工具设计。

Felix 的关键洞察：**模型能力提升的速度远快于开发者产出工具的速度**。因此越通用、越可组合的工具设计，越能从模型进步中受益——这和做特化工具、等用户提需求再开发的模式是根本对立的。

## 我的判断
- **赞同**：四原则是经过 Claude Code 大规模验证的设计智慧。Parity 保证了 Agent 不被 UI 人为限制；Granularity 让工具层稳定、功能层灵活；Composability 让有限工具产生无限组合；Emerging Capability 则是验证你是否做对了前三条的标准。
- **质疑**：通用性和可靠性的张力被低估了。Google Docs 校对失败说明，在非结构化 UI 中操作时，Agent 的可靠性远低于在结构化 API 中操作。通用工具+prompt 在结构化场景（代码、数据库）中表现好，在非结构化场景（浏览器操控、视觉交互）中还有很大差距。
- **补充**：Skills 是通用性和确定性之间的中间路线——用 Markdown 描述意图（通用），用脚本处理确定性部分（可靠）。这不是最终答案，但当前的务实选择。

## 深层联系
- [[驾驭工程]] — Agent 原生架构是驾驭工程的"为什么"：Harness 的设计原则（约束中激发能力、工具过滤、安全默认）正是为了让 Agent 在自主运行时不失控
- [[MVP思维]] — 先发最小可组合单元，让涌现能力告诉你该构建什么，这和 MVP 的"不要等产品完美再上线"是同一逻辑
- [[复利工程]] — 通用工具设计是复利工程在架构层的体现：前期投入做通用工具，后期模型能力提升时自动受益
- [[乘风策略]] — 不和模型能力赛跑（做特化工具），而是搭模型能力提升的便车（做通用工具）——这是架构层的乘风策略

## 来源
- [[BV1xEzqBVEeb-ClaudeCowork是我们所有人的ClaudeCode]] — Every 团队总结的四原则与 Felix 的对话验证；Felix 补充了"模型能力提升速度 > 工具开发速度"的关键论据；Skills 作为通用工具与确定性脚本之间中间路线的实证
- [[BV1QeZ2BZEFZ-Claude Code实战复合工程让AI越用越懂你]] — Karel 以 Cora 产品演示 Agent Native 实践：目标是让 Agent 能做用户能做的一切（Parity），从而涌现新的工作流；审查阶段专门设置"Agent 原生程度"视角的审查者
- [[BV1Sef8BmEU3-VibeCode实战8小时马拉松]] — Dan Shipper 的 Proof（人机共写归因+Agent Presence）、Anecdote（粒度性涌现能力）、Jeffrey 的 Notion+Claude Code 集成（Parity 让 Notion 看板可直接驱动 Agent）

## 相关主题
- [[LLM-Agent工程实践]]
