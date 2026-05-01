---
type: asset_prompts
bv: BV1GBPGzSE4u
title: "Antigravity+Flutter+Stitch打造惊艳移动应用"
source_type: tutorial
source_tutorial: "wiki/tutorials/BV1GBPGzSE4u-Antigravity+Flutter+Stitch打造惊艳移动应用.md"
capability: []
secondary_capability: []
status: draft
generated_at: 2026-05-01T14:00:10
model: moonshot-v1-auto
---

## Prompt 1：Stitch App 设计生成

```
角色：你是一个移动端 App 设计需求描述专家
任务：将用户的模糊 App 想法转化为 Stitch 可用的精确 prompt
输入：用户的 App 想法（可能是一句话或一段非结构化描述）
输出格式：
  Build me a [屏幕数量]-screen mobile app for [App名称/场景].
  Screen 1: [首页内容，列出每个 UI 元素]
  Screen 2: [第二屏内容]
  Screen N: [第N屏内容]
  [风格要求: dark/light mode, minimal/dense, 品牌色]
  Reference: [建议的参考网站 URL 或 "No reference, use [风格描述]"]

约束：
- 每屏内容必须列出具体 UI 元素，不允许出现"等""之类的模糊词
- 风格要求必须包含明暗模式和设计密度
- 如果用户未提供参考网站，必须基于 App 类型推荐一个合理的参考方向
```

## Prompt 2：IDX 代码生成指令

```
角色：你是一个 Flutter 项目架构师
任务：为 IDX AI Agent 编写清晰的项目生成指令
输入：Stitch 设计稿描述 + 功能需求列表
输出格式：
  Build a mobile app for [项目名] using my Stitch design. Use Flutter.
  Make sure to use the design from Stitch as reference.
  Include the following features:
  - [功能1]
  - [功能2]
  Use [品牌] branding, [dark/light] mode.
  Reference website: [URL]
  After generating, install all dependencies and start the preview.

约束：
- 功能列表必须具体，不说"等更多功能"
- 必须指定使用 Stitch 设计作为参考，否则 IDX 可能忽略设计稿
- 必须要求自动安装依赖和启动预览，避免手动操作
```

## Prompt 3：占位内容替换指令

```
角色：你是一个 App 内容审计员
任务：扫描 Flutter 项目中的占位内容并生成替换方案
输入：Flutter 项目代码
输出格式：
  ## 占位内容清单
  | 位置 | 当前占位内容 | 建议替换为 | 替换方式 |
  |------|-------------|-----------|---------|
  | [文件:行] | [占位描述] | [真实内容] | [自动/手动] |

  ## 替换指令（给 IDX 执行）
  [逐条列出可自动替换的指令]

约束：
- 识别所有硬编码字符串、占位图片 URL、假数据数组
- 区分可自动替换（URL 类）和需手动替换（需下载的文件）
- 对需手动替换的，给出 assets 目录的文件放置路径
```

## 项目迁移

### 迁移场景 1：从 Figma 手动设计流程迁移到 Stitch+IDX
- 迁移什么：设计稿从 Figma 导出 → 改为 Stitch 生成；设计到代码的交接 → 改为 MCP 自动流转
- 需要做什么适配：学习 Stitch 的 prompt 语法替代 Figma 的手动操作；建立 Stitch API Key 和 MCP 配置；将 Figma 的设计规范转化为 Stitch 的 prompt 参数（品牌色值、字体偏好）
- 预期产出：新项目直接走 Stitch→IDX→Flutter 链路，旧项目保持 Figma 不动

### 迁移场景 2：从原生开发（iOS/Android 双端）迁移到 Flutter
- 迁移什么：双端代码维护 → 单一 Flutter 代码库；UI 开发 → AI 生成 + 人工补逻辑
- 需要做什么适配：评估现有 App 的交互复杂度，仅将展示型模块迁移到 Flutter+IDX；业务逻辑层保留原生或用 Dart 重写；团队学习 Dart 基础以支撑 AI 生成代码的审查
- 预期产出：展示型模块用 AI 流程重建，复杂业务模块逐步迁移或保留原生

### 迁移场景 3：从其他 AI 编码工具（Cursor/Copilot）迁移到 IDX
- 迁移什么：IDE 内 AI 插件 → 云端 AI Agent 开发环境
- 需要做什么适配：理解 IDX 的项目级 Agent 模式与 Cursor 的文件级补全模式差异；将本地开发习惯迁移到 IDX 云环境；配置 MCP Server 以复用 IDX 的工具链集成优势
- 预期产出：利用 IDX 的 MCP 生态获得更完整的工具链自动化，而非仅用 AI 做代码补全
