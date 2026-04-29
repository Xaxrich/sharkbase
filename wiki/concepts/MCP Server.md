---
type: concept
name: MCP Server
tags: [AI协议, 工具互操作, Agent工具系统, 动态加载]
first_seen: 2026-04-26
---

# MCP Server

## 定义
Model Context Protocol Server，一种让 AI Agent 连接和调用外部工具的标准协议。MCP 定义了工具的描述、发现和调用规范，让 Agent 能按需获取外部能力。

## 为什么重要
MCP 解决的是 Agent 工具系统的核心矛盾：你需要给模型足够的工具才能完成任务，但工具描述本身占用上下文，工具太多反而让模型决策质量下降。MCP 的动态加载机制——不预加载所有工具描述，按需通过 description 让 Agent 发现——是"克制式设计"在工具层的具体落地。这个思路和 Skills 系统完全一致：延迟加载、按需暴露。

MCP 远未过时。虽然社区讨论热度有所下降，但 Claude Code 依然大量使用 MCP——沙箱功能本身也通过 MCP 实现。对于任何需要连接外部系统的 Agent 架构，MCP 仍然是最成熟的互操作协议。

## 我的判断
- **赞同**：动态加载是正确方向。静态地把所有工具描述塞进 system prompt 的做法，在工具数量增长后必然撞墙。MCP 的 description-based discovery 机制优雅地解决了这个问题。
- **质疑**：MCP 当前最大的问题是身份认证。Agent 写代码访问外部接口时无法带上用户身份信息——所有基于 MCP 的 Agent 系统都面临这个难题。目前只有阿里的悟空系统通过沙箱+请求拦截+固定认证头部分解决了这个问题。
- **补充**：MCP 服务器挂掉时，对应的指令不会被添加到 system prompt——这个容错设计看似简单，实则体现了 Harness 设计的基本原则：任何外部依赖的失败都不应导致 Agent 崩溃，只应导致能力降级。

## 深层联系
- [[驾驭工程]] — MCP 是 Harness 工具系统的核心互操作层。Claude Code 的 MCP 实现体现了"克制"哲学：只给模型它当前需要的工具信息，而非全部预加载。
- [[MVP思维]] — MCP 的动态加载和 MVP 的"先验证核心再迭代"是同一思路：不给（模型/用户）它不需要的东西，只在真正需要时才暴露。
- [[Google AI零代码工具链]] — Google 的 Stitch MCP + Flutter MCP 是 MCP 在零代码开发场景的早期实践，相对简单但展示了协议的基本价值。

## 来源
- [[BV1GBPGzSE4u-Antigravity-Flutter-Stitch打造惊艳移动应用]] — 作为连接三大工具的关键桥梁被演示
- [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]] — 作为 Claude Code 工具系统的核心组件被深入解析，展示了动态加载机制和容错设计

### Claude Code 中的 MCP 实现
- 沙箱功能本身通过 MCP 实现
- 动态加载：不预加载所有已注册 MCP 工具描述到 system prompt，按需通过 description 让 Agent 发现
- 服务器挂掉时对应指令不添加到 system prompt
- 与 Skills 系统的动态加载思路完全一致

### Google 工具链中的 MCP
- Stitch MCP Server：让 Antigravity 直接调用 Stitch 的项目和设计资源
- Flutter MCP Server：让 Antigravity 获得构建 Flutter 应用的知识和能力
- 配置流程：获取 API Key → 在 AI 平台配置 → 重启确认

## 相关主题
- [[LLM-Agent工程实践]]
