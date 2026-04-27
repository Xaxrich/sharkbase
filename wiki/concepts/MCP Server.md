---
type: concept
name: MCP Server
tags: [AI协议, 工具互操作, 谷歌, Agent工具系统]
first_seen: 2026-04-26
---

# MCP Server

## 定义
Model Context Protocol Server，一种让 AI 代理（如 Antigravity）连接和调用外部工具的协议服务器。

## 核心要点
- 允许 AI 平台直接操作外部工具和数据源
- 在本工作流中有两个关键 MCP Server：Stitch MCP（连接设计工具）和 Flutter MCP（提供构建知识）
- 配置流程：获取 API Key → 在 AI 平台配置 → 重启确认
- 是 AI 工具链互操作的关键基础设施

## 在以下视频中出现
- [[BV1GBPGzSE4u-Antigravity-Flutter-Stitch打造惊艳移动应用]]（作为连接三大工具的关键桥梁）
- [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]]（作为 Claude Code 工具系统的核心组件被深入解析）

### Claude Code 中的 MCP 实现（来自 [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]]）
- Claude Code 在 MCP 上有大量使用，MCP 依然是很强的工具组件，远未过时
- 沙箱功能本身也通过 MCP 实现
- **动态加载机制**：不再将所有已注册 MCP 工具描述预加载到 system prompt，而是按需通过 description 让 Agent 发现——解决了 MCP 工具描述过长占用上下文的问题
- 与 Skills 系统的动态加载思路完全一致，都是延迟加载、按需暴露
- MCP 服务器挂掉时，对应的指令不会被添加到 system prompt 中

## 与其他概念的关系
- [[Google Stitch]] — 通过 Stitch MCP Server 接入 Antigravity
- [[Antigravity]] — 作为 MCP 客户端调用外部工具
- [[Flutter]] — 通过 Flutter MCP Server 让 Antigravity 获得构建能力

## 相关主题
- [[AI驱动移动应用开发]]
