---
type: video
bv: BV1phndzwEs7
title: "如何用AI做出高颜值的原型设计？"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1phndzwEs7
date: 2026-04-30
duration: 44:00
tags: [AI设计, 原型设计, 提示工程, 设计品味, Landing Page]
concepts: [设计曝光, 微交互设计, 原型优先开发]
entities: [Easonlee的AI笔记]
topics: [技术人创业与产品思维]
transcript: .b2t/transcripts/original/如何用AI做出高颜值的原型设计-*.txt
---

# 如何用AI做出高颜值的原型设计？

## 一句话摘要
AI 单提示词生成的设计必然趋同，突破"通用 AI 审美"的关键是：用结构化提示词构建器替代随意描述，用模板/参考替代从零开始，用人工定制完成 AI 做不好的最后 10%。

## 核心观点

- **单提示词陷阱**：所有 AI 设计工具（v0、Lovable、Aura）对同一提示词的输出都趋同——Inter 字体、紫色主题、超大标题、白色背景。这是基线，不是终点。
- **资源 > 提示词**：关键不是"怎么写提示词"，而是"你给了 AI 什么参考"。name-drop 优秀设计（Arc、Comet、Perplexity、Apple）、提供代码片段、使用模板——这些比提示词技巧有效得多。
- **90/10 法则**：AI 做到 90%，人做最后 10%。字体切换、图片替换、阴影微调、按钮样式——这些细节 AI 反复重生成既慢又不稳定，不如手动微调。
- **品味是新时代的差异化**：当人人都能用 AI 生成网站，"知道什么是好的"比"知道怎么做"更重要。品味决定你选什么工具、什么参考、什么字体。
- **工具组合而非单一依赖**：Aura 做设计细节 → Lovable/v0 做全站 → Cursor 做编码。没有全能工具，只有最佳组合。

## 详细笔记

### Level 0 → Level 1：通用 AI 审美的困境

Men 用同一提示词在 v0、Lovable、Aura 上生成 landing page，结果高度趋同：Inter 字体、紫色渐变、超大粗体标题、白底卡片布局。这不是 bug，而是 AI 训练数据中"标准 web 设计"的统计平均。当亿万人用同一工具生成网站，基线会越来越拥挤，通用感会越来越强。

标杆对照：Arc 的 Comet 浏览器 landing page——自定义字体、3D 动画背景（Spline）、Midjourney 生成的抽象图、精心设计的阴影和间距。这是 Level 10，但方向清晰。

### 突围方法一：结构化提示词构建器

随意写"做一个漂亮的 landing page"是最低效的方式。Prompt Builder 把设计决策拆解为可选项：

1. **内容类型**：hero section / feature section / testimonial / settings
2. **布局配置**：sidebar / bento layout / full screen / card
3. **展示方式**：full screen / card / browser frame
4. **样式风格**：glass / liquid glass / light mode / dark mode
5. **配色**：primary color / background color
6. **字体**：这是最被低估的维度。AI 默认用 Inter，但 Instrument Serif、Playfair、Manrope 等字体能瞬间拉开差距。字体权重、字间距、字号比例同样重要

每个选择自动追加到提示词文本中，组合出结构化的完整提示词。本质是把设计词汇量从"漂亮"扩展到"bento layout + glass style + Instrument Serif + light mode"。

### 突围方法二：从模板 Remixed 而非从零开始

最高效的路径不是从空白提示词开始，而是：

1. 浏览社区模板（Aura 有 1500+，Framer 社区也有大量资源）
2. 找到接近目标的设计
3. Remixed + 微调（改字体、改颜色、改图片）
4. 也可以从 CodePen、21st.dev、React Bits 等资源站复制 HTML/组件代码，粘贴到 AI 工具中作为起始点

这和"站在巨人肩膀上"是同一逻辑——AI 已经在优秀设计上训练过，你给它具体参考比给它抽象描述有效得多。

### 突围方法三：手动定制完成最后 10%

AI 做不好的事情（或做得很慢的事情）：

- **字体切换**：AI 重生成整个页面来换字体，耗时 30 秒到数分钟；手动改 CSS 变量即时生效
- **图片替换**：用 Midjourney 生成的高质量抽象图或 Unsplash 照片替换 AI 默认的通用图片
- **按钮样式**：从 uiVerse 复制 CSS 样式，粘贴到 AI 工具中应用，比让 AI 重新生成按钮更可控
- **3D 背景动画**：Spline 社区有大量免费 3D 场景，导出链接嵌入即可
- **图标替换**：维护自己的图标库，手动替换比 AI 重生成更快更准

Men 的核心比喻：AI 是从 0 到 50 或 80 的加速器，但永远不是 100。最后 20% 需要人的品味、经验和手艺。

### 工具生态与分工

| 工具 | 擅长 | 不擅长 |
|------|------|--------|
| Aura | 设计细节、字体/颜色/图片定制、模板库、提示词构建器 | 全站构建、复杂交互逻辑 |
| Lovable | 全站生成、功能完整性 | 样式微调、字体/图片替换 |
| v0 | 组件生成、React 生态 | 设计差异化 |
| Cursor | 代码编辑、迭代开发 | 从零设计 |
| Spline | 3D 动画背景 | 非 3D 场景 |
| Midjourney | 高质量图片生成 | UI 组件 |
| Framer | 无代码全站发布 | 深度定制 |

推荐工作流：Aura 设计组件 → 导出 HTML → 粘贴到 Lovable/Cursor → "用这个样式替换 testimonials" → AI 保持样式一致性生成全站。

### Claude 模型选择

- Claude Sonnet 3.5 (claude-4-7-sonnet)：更注重细节，但倾向使用 Inter + 紫色，需要更多约束
- Claude Sonnet 4 (claude-sonnet-4-6)：稍"懒"但更听从指令，风格上更容易引导

### 六个月后的展望

Men 判断：当前 AI 设计能力是 Level 1（五个月前是 Level 0），六个月后会到 Level 5，接近 Arc/Comet 的水准。工具和知识都需要持续进化。

## 我的评注

- **赞同**：90/10 法则精准描述了当前 AI 设计工具的能力边界。Men 没有陷入"AI 能做一切"的幻想，而是诚实展示 AI 的慢和不稳定——换个字体要等 30 秒，改个图标可能破坏布局。这种克制在 AI 宣传过剩的时代很可贵。
- **赞同**："品味是差异化"这个判断在 Vibe Coding 时代尤为重要。当执行成本趋近于零，判断力成了唯一的稀缺资源。但视频没有展开"如何培养品味"，只是说"用好的工具"——实际上 [[设计曝光]] 的方法（持续接触优秀设计）才是品味培养的核心路径。
- **质疑**：Men 作为 Aura 创始人，整个演示都在 Aura 平台内完成，对竞品的评价不够中立。他说 Lovable/v0 "样式难调"，但没有展示在那些平台上的定制能力上限。实际上 Lovable 的 edit 功能也在快速进步。
- **质疑**：视频过度聚焦 landing page。Landing page 是设计最容易出彩的产品类型（纯展示、无复杂状态），但大多数产品是 dashboard、表单、数据可视化——这些场景下 AI 设计工具的能力远不如 landing page。
- **关联**：这和 [[驾驭工程]] 的"约束中激发能力"同构——Prompt Builder 本质上是设计领域的 Harness：不直接生成设计，而是通过结构化选项约束 AI 的输出空间，让模型在更窄的范围内做出更好的决策。和 Claude Code 的工具过滤（52→~20）是同一思想。
- **关联**：和 [[原型优先开发]] 互补——视频侧重"原型怎么做得好看"，但没讨论"原型之后怎么变成产品"。Aura 当前定位是组件级设计工具（类似 Figma），全站能力还在路上。

## 与其他知识的关联
- 相关概念：[[设计曝光]]、[[微交互设计]]、[[原型优先开发]]、[[Vibe Building]]、[[驾驭工程]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[技术人创业与产品思维]]

## 待深入问题
- AI 设计的品味培养是否有更系统的方法论，而非"多看多用"？
- 当所有人都在用同一批模板和参考时，差异化如何持续？模板本身会不会也成为新的通用基线？
- Aura 的"组件级设计 → 全站"路径是否可行？Framer 已经在这条路上走了多年，AI 加持能突破什么瓶颈？
- 在 dashboard/表单/数据可视化等非 landing page 场景下，AI 设计工具的能力边界在哪里？
