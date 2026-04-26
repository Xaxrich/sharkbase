---
type: video
bv: BV1GBPGzSE4u
title: Antigravity+Flutter+Stitch打造惊艳移动应用
uploader: GoldenSpiderAI
url: https://www.bilibili.com/video/BV1GBPGzSE4u
date: 2026-04-26
duration: 19:10
tags: [AI应用开发, Flutter, 谷歌, 移动应用, MCP]
concepts: [Google Stitch, Antigravity, Flutter, MCP Server]
entities: [GoldenSpiderAI]
topics: [AI驱动移动应用开发]
transcript: .b2t/transcripts/original/Antigravity-Flutter-Stitch打造惊艳移动应用-新技能-20260426-204107.txt
---

# Antigravity+Flutter+Stitch打造惊艳移动应用

## 一句话摘要
演示如何用 Google 三大免费 AI 工具（Stitch 做设计、Antigravity 写代码、Flutter 构建应用）实现从描述到可安装手机 App 的全流程零代码开发。

## 核心观点
- Google Stitch 可将文字描述或参考网站转化为完整的 App 界面设计，支持注释修改和移动端预览
- Antigravity 是 Google 的 AI 代码平台，通过 MCP（Model Context Protocol）连接 Stitch 和 Flutter，实现自动编码
- Flutter 作为跨平台移动应用框架，配合 Antigravity 可直接生成 APK 安装到手机
- 三者组合形成完整工作流：Stitch（设计）→ Antigravity（开发）→ Flutter（构建+部署）
- 全部工具免费可用，MCP Server 是连接各工具的关键桥梁

## 详细笔记

### 第一部分：三大工具介绍

**Google Stitch** — AI 设计工具，输入文字描述或参考网站 URL 即可生成完整的 App 界面。集成 Imagen（Google 最强图像生成模型），可自动创建所需图片。免费使用。

**Antigravity** — Google AI 代码平台。不需要写代码、不需要连接模块，只需描述需求即可自动构建。可创建真实移动应用。

**Flutter** — Google 的跨平台移动应用框架，被 Google Pay、eBay、阿里巴巴、纽约时报等使用。完全开源。

### 第二部分：Stitch 设计流程

1. 访问 Google Stitch，输入参考网站 URL（如 Google Cloud Next 活动页）
2. 给出描述性 prompt：构建双屏移动应用，首页含 logo、活动名称、日期、议程 tabs，使用 Google Cloud 品牌色，暗色模式
3. Stitch 自动生成设计稿，包含真实场馆图片和议程数据
4. 可通过注释（annotate）功能精确修改设计中的特定区域
5. 支持移动端预览，查看实际滚动效果
6. 可导出设计文件到本地

### 第三部分：MCP Server 配置

- **Stitch MCP Server**：让 Antigravity 直接调用 Stitch 的项目和设计资源
- **Flutter MCP Server**：让 Antigravity 获得构建 Flutter 应用的知识和能力
- 配置步骤：在 Stitch 获取 API Key → 提供给 Antigravity → 自动配置 MCP → 重启 Antigravity 确认 MCP 已安装
- 配置完成后，Antigravity 可直接查询 Stitch 项目、创建新项目、调用设计资源

### 第四部分：完整应用构建演示

1. 在 Antigravity 中给 Stitch 下指令：为 Google Cloud Next 2026 设计移动应用
2. Stitch 生成设计 → Antigravity 读取设计 → 生成 Flutter 代码
3. 本地预览 → 安装依赖 → 构建应用
4. 替换占位图片：手动从参考网站下载真实图片，替换到项目文件
5. 构建 APK：Antigravity 生成 APK 文件，可直接安装到手机

## 关键引用
> "You can now design a full mobile app with AI and actually install it on your phone without writing a single line of code."

## 与其他知识的关联
- 相关概念：[[Google Stitch]]、[[Antigravity]]、[[Flutter]]、[[MCP Server]]
- 相关实体：[[GoldenSpiderAI]]
- 相关主题：[[AI驱动移动应用开发]]

## 待深入问题
- Antigravity 与其他 AI 代码平台（如 Cursor、Windsurf）相比的优劣？
- MCP 协议在更多工具间互操作的潜力有多大？
- 用此工作流构建复杂应用（如含后端 API、数据库）的可行性？
