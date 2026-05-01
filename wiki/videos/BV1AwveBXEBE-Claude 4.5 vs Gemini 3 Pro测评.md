---
type: video
bv: BV1AwveBXEBE
title: "Claude 4.5 vs Gemini 3 Pro：测评"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1AwveBXEBE
date: 2026-04-30
duration: 59:00
tags: [AI模型测评, Vibe Coding, Claude Skills, 转化优化, 产品原型]
concepts: [Vibe Building, Claude Skill, 转化文案架构, 垂直整合]
entities: [Easonlee的AI笔记]
topics: [LLM-Agent工程实践]
transcript: .b2t/transcripts/original/BV1AwveBXEBE.txt
---

# Claude 4.5 vs Gemini 3 Pro：测评

## 一句话摘要

通过同题竞速（落地页 + 可点击原型）实测 Opus 4.5 与 Gemini 3 Pro，并展示 Claude Skills 如何让非工程师一次提示就产出接近生产级的前端和文案。

## 核心观点

- **Opus 4.5 在产品思考深度上胜出**：同样的"遗产清"概念，Opus 的落地页和原型更贴近真实 SaaS——时间线前置、功能层级清晰、审美克制；Gemini 3 Pro 的输出更像社交信息流，AI 功能植入大胆但产品逻辑偏浅。
- **Claude Skills 是被严重低估的杠杆**：frontend design skill 两行命令安装，能把 AI 默认的"紫渐变+emoji"审美直接压制；品牌 voice skill + 转化架构 skill 叠加后，一次提示就能产出可上线的落地页。
- **Gemini 的差异化价值在生态整合**：AI Studio + Antigravity + Nano Banana Pro + Google Workspace，垂直整合度无人能及——Antigravity 甚至能自动调用 Nano Banana 生成高保真视觉稿再写代码。
- **文案才是转化率的决定变量**：多数人 vibe coding 只关注视觉，忽视 copy；用"提升型直接回应"(Elevated Direct Response) 思路写文案，即使设计朴素也能转化。
- **多模型协作比单模型死磕更实际**：用 Claude 做主力工作马，用 Gemini/GPT 做外部顾问获取不同视角，遇到深层 bug 时调 ultrathink 或启动 subagent。

## 详细笔记

### 实测设计：同题竞速

目标产品：**Estate Clear**——遗产执行人的家庭仪表盘，解决执行人反复接电话、家属信息黑箱的问题。

- 两模型使用**完全相同的提示词**（来自 Idea Browser 的每日创意描述）
- Opus 4.5 附加 frontend design skill；Gemini 3 Pro 在 AI Studio 原生运行
- 评判维度：设计美学、产品逻辑深度、功能完整性

### 第一轮：落地页

**Opus 4.5 输出**：
- 克制审美，不使用典型 AI 紫渐变和 emoji
- 核心卖点前置，无需滚动即可获取关键信息
- 动效细节到位（卡片微动）
- 社会证明、定价卡齐全
- 一句话判断：**可直接用作 MVP 落地页**

**Gemini 3 Pro 输出**：
- "Keep the family united" 标语更有情感冲击
- 主动植入了 AI 功能："Let AI write the update"——Gemini 倾向在产品中加入 AI-first 特性
- 视觉更"人性化"，带插图和 emoji 风格
- 信息布局需要更多滚动才能获取全貌
- 一句话判断：**功能创意有亮点，视觉略逊于 Opus**

双方共识：Opus 美学更优，Gemini 的 AI 功能植入思路值得借鉴。

### 第二轮：可点击原型

**Opus 4.5 输出**：
- 完整仪表盘布局：进度时间线、近期活动、家庭成员列表
- 子视图齐全：更新发布、文档存储、里程碑追踪
- 审美从落地页到原型保持一致，字体和色彩贯穿
- 部分子页面未完成，但整体可导航

**Gemini 3 Pro 输出**：
- 偏社交/信息流风格，而非传统仪表盘
- AI 功能内嵌：更新时可用 AI 润色文案
- 文档存储和设置页面存在，但产品逻辑不如 Opus 深入
- 时间线功能存在但不如 Opus 前置突出

结论：**两轮测试后 Opus 4.5 在产品深度上领先**，但 Gemini 3 Pro 绝对达到 MVP 水准。

### 第三轮：Antigravity（Google 的 Agent IDE）

- 同一提示词放入 Antigravity 中的 Gemini 3 Pro
- Antigravity 自动调用 **Nano Banana Pro** 先生成高保真视觉稿（mockup 图片），再基于此写 HTML
- Chrome 扩展集成：可访问 DOM 和开发者工具数据，减少调试来回
- 输出的落地页嵌入了 Nano Banana 生成的仪表盘图片，视觉真实感强
- 但整体设计偏基础，不如 AI Studio 直接输出的精致

关键洞察：**Antigravity 的价值不在单次输出质量，而在工作流——先生成 mockup 确认方向，再写代码**，模拟了真实团队的设计-开发流程。

### Google 垂直整合的优势与边界

Google 的完整栈：
- 基础模型（Gemini）
- 应用层（Workspace：邮件、日历、文档）
- 开发工具（AI Studio、Antigravity）
- 创意工具（Nano Banana Pro）
- 硬件（Android 设备）
- 芯片（TPU，与 Broadcom 合作制造，成本低于竞品）
- 投资关系（持有 Anthropic 约 14% 股份）

优势：对 90% 的普通开发者来说，一站式解决从认证、存储、AI 集成到部署的全部需求，成本和速度都有竞争力。

局限：生态锁定风险；专业开发者仍倾向自由组合工具链。

### Claude Skills 实战方法论

Skills 本质：一组预定义指令，让模型在执行特定任务时自动参考。不是提示词模板，而是持久化的行为规范。

**三个核心 Skill 的构建路径**：

1. **品牌 Voice Skill**
   - 用 Perplexity MCP 研究领域内标杆人物（如 Cody Sanchez、Alex Hormozi）的文案策略
   - 提取共性：Cody 的"逆向教育者"钩子、Hormozi 的"无法拒绝的报价"价值堆叠
   - 喂入自己的写作样本（推文、视频转录、已有文案），让模型提炼个人语言风格
   - 合成为 voice skill：逆向教育者 + 直接回应 DNA + 系统化思维 + 创作者语言

2. **提升型直接回应 (Elevated Direct Response) Skill**
   - 融合直接回应营销的转化原则与克制表达
   - 不卖弄、不空洞品牌语、不过度推销，但精准击中痛点并推动行动

3. **Frontend Design Skill**
   - 安装：两条命令（添加 Anthropic 插件市场 → 安装 frontend-design 插件）
   - 效果：压制 AI 默认的"紫渐变+emoji+通用插画"视觉，输出接近生产级的设计
   - Anthropic 内部团队构建的指令集，避免典型 AI 审美

**落地页转化架构**：
1. Hero 区：核心转变/结果
2. 痛点激化（Problem-Agitate）：描述现状痛感
3. 解决方案 + 价值堆叠（Solution + Value Stack）
4. 社会证明（Social Proof）
5. 转变描绘（Transformation）：重新销售核心结果
6. 二次强 CTA
7. FAQ（如需）

核心原则：**前期做无聊的研究（建 Skills），后期一次提示就能产出高质量结果**。

### 调试策略

遇到深层 bug 时的分层策略：
1. `ultrathink` 关键词触发 Opus 4.5 的深度推理模式
2. 启动专项 subagent（QA 测试员、高级工程师），各自调查不同维度后综合分析
3. 仍未解决时，切换到 Cursor Agent 用 GPT/Gemini 获取外部视角
4. Opus 4.5 的预期改进：在大型代码库中更好地保持上下文，减少迷失

## 我的评注

- **赞同：Skills 作为持久化行为规范的设计**。将"研究标杆 → 提炼原则 → 喂入个人样本 → 合成 skill"这条路径标准化，比每次手动写长提示词高效得多。这本质上是在构建个人的"AI 操作系统"，值得在更多领域复制。

- **赞同：文案 > 设计的判断**。落地页转化率的核心瓶颈通常是 copy 而非视觉，这个洞察在 vibe coding 社区中被严重忽视。但视频没有提供任何转化率数据来支撑这一论断，仅凭"老式长文案信也能转化"的历史类比略显单薄。

- **质疑：测评方法的严谨性**。同题竞速有价值，但"一次提示定胜负"忽略了真实使用场景中迭代 25 次后的格局可能完全不同。Opus 的 frontend design skill 本质上是额外的上下文注入，Gemini 没有等量加持，这不算完全公平。视频对此有坦诚承认但未深究。

- **质疑：对 Opus 4.5 代码能力的结论过于乐观**。落地页和原型都是前端单文件，真正的 SaaS 需要后端、数据库、认证、支付集成。视频承认"还没用 Opus 4.5 构建过完整应用"，但结论已隐含"可以做到"——这是信念而非证据。

- **关联：与 [[Vibe Building]] 的深层共振**。视频中"vibe coding / vibe marketing / vibe designing 界限模糊化 → vibe building"的观察，指向一个更根本的趋势：当 AI 把执行成本压到接近零，创意和判断成为唯一稀缺资源。这与 [[MVP思维]] 中"最小可行产品"的理念形成张力——如果一次提示就能产出接近 MVP 的原型，MVP 的"最小"定义需要重新校准。

## 与其他知识的关联

- 相关概念：[[Vibe Building]]、[[Claude Skill]]、[[微交互设计]]、[[确定性输出]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题

- Skills 的维护成本如何？品牌 voice 会随时间漂移，skill 是否需要定期重训？
- Opus 4.5 在大型多文件代码库（100+ 文件）中是否真能保持上下文不迷失？视频只测了单文件场景。
- Gemini 3 Pro 的 AI-first 产品直觉（自动植入 AI 功能）是特性还是偏差？在非 AI 目标市场中是否反而增加复杂度？
- Antigravity 的 Chrome 扩展集成对调试效率的实际提升有多少？缺少对比基准。
- "垂直应用最难的是确定工作流"——这个判断如何系统化验证？是否有方法论可以在写代码前低成本试错工作流假设？
