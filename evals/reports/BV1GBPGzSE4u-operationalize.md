---
type: eval_report
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

## 最低掌握等级

**L2**：能理解 Stitch、IDX、Flutter、MCP 各自的角色和协作关系，能复述全链路流程，能在指导下完成一次完整的 App 构建走通

## 建议掌握等级

**L3**：能独立完成从需求描述到真机安装的全流程，能根据 App 类型判断是否适合使用 AI 流程，能自行排查 MCP 配置和构建中的常见问题

## 各等级具体表现

| 维度 | L1 了解 | L2 理解 | L3 应用 | L4 熟练 | L5 精通 |
|------|---------|---------|---------|---------|---------|
| 工具角色理解 | 知道 Stitch/IDX/Flutter 大概是做什么的 | 能准确区分三者的能力边界和协作关系 | 能向他人清晰解释全链路价值和局限 | 能根据项目需求选择性地使用部分工具组合 | 能评估新工具加入链路的可行性和 ROI |
| Prompt 工程 | 能写出基本的 App 描述 | 能按模板写出结构化的 Stitch prompt | 能根据生成结果迭代优化 prompt，控制输出质量 | 能建立不同 App 类型的 prompt 模板库 | 能设计 prompt 策略让 AI 输出接近生产级 |
| MCP 配置 | 知道 MCP 是什么 | 能按步骤配置 Stitch/Flutter MCP | 能独立排查 MCP 连接失败问题 | 能配置非标准 MCP Server | 能开发自定义 MCP Server 扩展工具链 |
| 代码质量把控 | 能在预览中判断"像不像" | 能识别 AI 生成代码中的占位内容 | 能完成占位替换并修复简单代码问题 | 能审查 AI 生成代码的结构和安全性 | 能优化 AI 生成代码至可上生产的质量 |
| 流程判断力 | 知道不是所有 App 都适合 | 能区分展示型和业务逻辑型应用 | 能为具体需求选择合适的开发路线 | 能设计混合策略（AI 做原型+人工做核心逻辑） | 能建立团队级的 AI 开发流程规范 |

## 是否建议进入 practice

**是**。本文内容高度实操，仅靠阅读无法形成能力。核心技能（prompt 撰写、MCP 配置、代码审查）必须通过动手才能真正掌握。建议至少完成任务 1-3 走通一次全链路。

## 下一步行动：30 分钟最小实践任务

1. 打开 Google Stitch，用以下 prompt 生成一个 2 屏 App 设计："Build me a 2-screen mobile app for a personal reading list. Screen 1: homepage with a greeting, book count, scrollable book list with cover thumbnails and titles. Screen 2: book detail with cover image, title, author, reading progress bar. Dark mode, minimal design. Reference: https://literal.club"
2. 在 Stitch 中预览移动端效果，用 annotation 修改一处不满意的地方
3. 记录：你的原始 prompt、生成结果截图、修改指令、最终效果——这三者之间的对应关系就是你后续优化 prompt 的经验数据

**预期产出**：一套个人阅读清单 App 设计稿 + 一份 prompt 迭代笔记（记录什么措辞导致了什么结果）
