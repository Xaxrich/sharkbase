---
type: video
bv: BV1cMveBUEc1
title: "我作为设计师测试了 Gemini 3。它好得令人恐惧。"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1cMVEc1
date: 2026-04-30
duration: 28:00
tags: [AI设计, Gemini3, VibeDesigning, 产品原型, 参考图像]
concepts: [Vibe Designing, 参考图像驱动设计, 迭代式AI设计]
entities: [Easonlee的AI笔记]
topics: [AI驱动产品设计]
---

# 我作为设计师测试了 Gemini 3。它好得令人恐惧。

## 一句话摘要

用三个真实设计场景实测 Gemini 3 Pro 在 Google AI Studio 中的设计能力，证明 AI 辅助设计已从"勉强能用"进入"令人惊叹"的阶段。

## 核心观点

- Gemini 3 Pro 在 Google AI Studio 中能从单条提示词生成高质量、可交互的完整应用界面，不再是早期 Vibe Coding 时代的"紫色 Tailwind 模板"
- 参考图像是产出质量的关键杠杆——给好的参考图，产出大幅提升；给模糊描述，产出明显下降
- AI Studio 的标注（Annotation）功能支持视觉化迭代反馈，降低了非设计师获取好结果的门槛
- 设计品味（taste）比技术能力更重要——AI 是执行层，人有决定"什么算好"的判断力

## 详细笔记

### 测试一：个人网站 — Windows XP 风格重设计

**输入**：截图 + 简短描述——"像 Windows XP 体验的个人网站"，域名 eisenberg，要求更多色彩和新鲜感。

**产出**（约 110 秒）：生成了完整可交互的 Windows XP 风格个人网站——桌面图标对应 About、Newsletter、Guides 等功能模块，内容从原网站自动抓取，移动端也能正常显示。

**迭代**：
- 要求修正应用图标（图标不够像真实 Windows 应用图标）→ 修正后图标质量明显提升
- 用标注功能在白色背景上标注"无聊，应该用 XP 经典蓝天绿地"→ 背景改为蓝天但山脉未出现，图标被破坏。**教训**：应直接提供 XP 壂墙纸参考图而非文字描述

**评分：9/10**

### 测试二：SaaS 仪表盘 — Teenage Engineering 风格

**输入**：Dribbble 上的 SaaS Dashboard 截图 + Teenage Engineering 产品照片 + 描述"餐厅 AI 分析 SaaS，按钮要有实体感"。

**产出**：生成带有 Teenage Engineering 旋钮风格的仪表盘界面，包含 AI 助手"Chef O"、实时数据（活跃桌数、平均客单价等）、可点击但不可拖拽的组件。

**评分：8.5/10**（单条提示词的产出，缺少拖拽交互）

**补充说明**：若提供 PRD（产品需求文档）而非模糊描述，产出会更好。可借助 Idea Browser Pro 生成 PRD，或使用 Lenny's Newsletter 的 PRD 模板。

### 测试三：移动应用 — Brainrot 风格健身 App

**输入**：Brainrot App Store 预览图 + 描述"设计一个让人去健身的 Brainrot，吉祥物、游戏化、暖色调"。

**产出**：React 应用"Gains"——健身吉祥物响应锻炼习惯，包含目标维护模式、活动日历、热门贡献者等模块。点击交互部分功能缺失（无法记录、无设置页）。

**评分：8.3/10**（设计质量高，交互完整性不足）

### 关于 Antigravity

Google 发布的 Cursor 竞品 Antigravity 也支持 Gemini 3 设计，但测试者在其中获得的设计质量不如直接使用 Google AI Studio。

## 我的评注

- **赞同**：三个测试从低到高复杂度递进，覆盖了个人项目、商业 SaaS、移动端三类真实场景，说服力强。参考图像作为质量杠杆的论点非常实用——这是很多人忽略的关键输入。
- **质疑**：评分偏乐观。9/10 的个人网站缺少内容完整性验证（如 Blog 页面是否可用），8.5 的 SaaS 缺少核心交互（拖拽、数据绑定），这些在实际交付中是硬伤。评分更像是"视觉冲击分"而非"可用产品分"。背景迭代失败（文字描述不如参考图）恰好说明了当前 AI 设计的局限：语义理解与视觉模仿之间仍有差距。
- **关联**：这和 [[Vibe Coding]] 的演进一致——从"能跑就行"到"设计也行"。核心模式相同：**用品味和参考图替代编码/设计技能，AI 做执行**。与 [[AI驱动产品工作流]] 中的 PRD→设计→原型流程高度吻合。

## 待深入问题

- 当需求从"单页原型"升级到"多页完整产品"时，Gemini 3 的上下文窗口和设计一致性是否能维持？
- 标注（Annotation）反馈循环的效率如何？多次迭代后是收敛还是发散？
- 与 Cursor/Windsurf 等 IDE 内设计能力相比，AI Studio 的纯设计场景优势在哪里？劣势在哪里？
- 非设计师用 AI 做设计，最大的瓶颈是品味判断力还是提示词能力？
