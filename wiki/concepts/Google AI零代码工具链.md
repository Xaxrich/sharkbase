---
type: concept
name: Google AI零代码工具链
tags: [谷歌, AI应用开发, 零代码, 移动应用, MCP]
first_seen: 2026-04-26
---

# Google AI零代码工具链

## 定义
Google 提供的三款免费 AI 工具组合——Stitch（设计）、Antigravity（开发）、Flutter（构建）——通过 MCP Server 互连，实现从文字描述到可安装手机 App 的全流程零代码开发。

## 为什么重要
它展示了一种新的软件生产方式：AI 作为不同工具间的"粘合层"，MCP 作为工具互操作协议。重要的不是单个工具的能力，而是工具链的编排方式——这和 [[驾驭工程]] 中 Claude Code 用 MCP 动态加载工具的思路是同一方向。

## 我的判断
- **价值**：演示效果好，门槛低，对非技术人员有真实的赋能作用
- **局限**：视频演示的是极简场景（活动页 App），复杂应用（后端 API、数据库、权限系统）的可行性存疑。目前更像"AI 版 PPT"而非"AI 版工程师"
- **真正值得关注的**：MCP 协议本身。Stitch MCP Server 让 Antigravity 直接调用设计资源，Flutter MCP Server 让它获得构建知识——这种"AI 平台通过 MCP 按需获取外部能力"的模式，才是长期有生命力的东西

## 深层联系
- [[MCP Server]] — 工具链的核心连接层，MCP 协议的动态加载机制在 Claude Code 中被更深度地使用
- [[驾驭工程]] — Antigravity 本质上是一个简化版 Agent，它的工具系统（Stitch MCP + Flutter MCP）是 Harness 中工具层的缩影

## 来源
- [[BV1GBPGzSE4u-Antigravity-Flutter-Stitch打造惊艳移动应用]] — 完整演示了三大工具的协作流程

### 工具分工

**Google Stitch** — AI 设计工具，输入文字描述或参考网站 URL 生成 App 界面设计，集成 Imagen 图像生成，支持注释修改和移动端预览。

**Antigravity** — Google AI 代码平台，通过 MCP 连接 Stitch 和 Flutter，描述需求即可自动生成和构建应用。

**Flutter** — Google 跨平台移动应用框架（Google Pay、阿里巴巴等使用），开源，配合 Antigravity 可直接生成 APK。

## 相关主题
- [[LLM-Agent工程实践]]
