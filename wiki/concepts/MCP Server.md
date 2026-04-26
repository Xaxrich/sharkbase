---
type: concept
name: MCP Server
tags: [AI协议, 工具互操作, 谷歌]
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

## 与其他概念的关系
- [[Google Stitch]] — 通过 Stitch MCP Server 接入 Antigravity
- [[Antigravity]] — 作为 MCP 客户端调用外部工具
- [[Flutter]] — 通过 Flutter MCP Server 让 Antigravity 获得构建能力

## 相关主题
- [[AI驱动移动应用开发]]
