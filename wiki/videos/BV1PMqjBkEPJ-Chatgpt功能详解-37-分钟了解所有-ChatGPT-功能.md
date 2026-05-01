```markdown
---
type: video
bv: BV1PMqjBkEPJ
title: "Chatgpt功能详解：37 分钟了解所有 ChatGPT 功能"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1PMqjBkEPJ
date: 2026-04-30
duration: 36:00
tags: [ChatGPT, AI工具, OpenAI生态, AI应用实践, 产品功能]
concepts: [ChatGPT全功能解析, AI Agent模式, 深度研究]
entities: [Easonlee的AI笔记, OpenAI]
topics: [AI工具实践]
---

# Chatgpt功能详解：37 分钟了解所有 ChatGPT 功能

## 一句话摘要

系统性梳理 ChatGPT 全部功能模块——从基础对话、语音模式到 Agent 模式和 Codex，帮助用户建立对 ChatGPT 能力边界的完整认知。

## 核心观点

- ChatGPT 的真正优势不在搜索式问答，而在创意生成和个性化输出——同样的问题，不同的引导方式能产出截然不同的结果
- 语音模式是最被低估的功能，不仅是输入方式，更是一个"思维陪练"工具，但存在情感依赖风险
- Agent 模式标志着 ChatGPT 从"对话工具"到"执行工具"的转变——可以直接生成代码、部署到 GitHub Pages
- 深度研究（Deep Research）能自主完成多轮搜索和信息综合，适合需要文献综述式输出的场景
- ChatGPT 的可视化能力（Canvas/Dashboard）可用但不是最强，Claude 在这方面明显更优

## 详细笔记

### 基础对话与搜索

默认使用 GPT-5（设为 Auto 模式）。多数人把 ChatGPT 当搜索引擎用（如"最流行的键盘是什么"），这虽然可行，但浪费了它的核心能力。ChatGPT 的真正价值在于创意任务——例如要求它从历史故事出发为跑鞋写营销文案，它能产出结构化的广告脚本，并持续迭代优化。

### 多模态能力

- **图片识别**：拍冰箱让 ChatGPT 识别食材并推荐菜谱；拍坏掉的马桶问如何修理——实用性强
- **移动端实时视觉**：打开摄像头让 ChatGPT 识别眼前物体（键盘型号、鼠标类型），识别准确度中等，能识别类别但难精确到具体型号

### 语音模式

UP主自认为最爱的功能。使用场景包括：
- 项目思考的角色扮演和推演
- 困难对话的预演练习
- 情感确认和自我对话

**风险警告**：提到 TikTok 上有人因与 ChatGPT 语音功能过度互动而产生情感依赖（命名为"AI psychosis"）。语音模式体验过于真实，容易让人放松警惕。

### 数据分析与可视化

演示了将文章、CSV 文件和 PDF 文档同时喂给 ChatGPT，让它生成数字游民趋势 Dashboard。Code Interpreter 在后台生成代码，Canvas 弹出预览窗口。结论：**Dashboard 质量可用但不如 Claude**——ChatGPT 胜在通用性，不在专业深度。

### Canvas 与 Vibe Coding

Canvas 可用于编辑文本和代码。演示了让 ChatGPT 根据网站改进建议直接生成新网站 mockup（HTML），然后进一步要求部署到 GitHub Pages——ChatGPT 通过 GitHub 集成完成了整个流程。

### Projects 项目管理

Projects 功能用于组织对话：可以创建项目、添加文件作为知识源、设定项目级指令。演示了投资主题项目，添加黄金投资 PDF 作为知识源，要求回答时始终列出优缺点，并支持项目内跨对话引用。

### GPTs 自定义助手

GPTs 是带有特定指令、额外知识和技能组合的自定义 ChatGPT 版本。已有大量社区 GPT（学者、占星、数据分析、写作等）。演示了创建一个"创意键盘构建师" GPT，指定预算和偏好后获取个性化键盘方案。创建自定义 GPT 需要付费计划。

### 定价体系

| 层级 | 价格 | 核心差异 |
|------|------|----------|
| Free | $0 | GPT-5 基础访问，语音模式（无视频/屏幕共享） |
| Plus | $20/月 | GPT-5 Sonnet 限额、高级语音（含视频/屏幕共享）、Agent 模式、深度研究、自定义 GPT、Sora 有限访问 |
| Pro | $200/月 | 无限 GPT-5 Pro、更高级语音限额、Pro Access、Codex Agent |
| Team/Enterprise | 更高 | 管理控制、训练数据排除、协作功能、安全合规 |

### 深度研究（Deep Research）

让 ChatGPT 自主完成多轮网络搜索并生成结构化报告。演示：约会趋势研究，ChatGPT 先通过追问明确范围（地区、年龄段、定性/定量偏好），然后耗时 7 分钟、搜索 18 个来源、执行 98 次检索，最终输出包含趋势分析、数据支撑和专家观点的综合报告。

### Agent 模式

从"建议"到"执行"的跃迁。演示：将网站改进建议加入 Project → 开启 Agent 模式 → 要求生成网站 mockup → ChatGPT 输出 HTML 文件 → 要求部署到 GitHub Pages → 通过 GitHub 集成完成部署。整个流程无需手动写代码。

### 隐藏功能

- **定时任务（Schedules）**：可设置定时提醒或周期性任务（每小时/每天/每周/每月/每年），如"每天早上 7 点发送趋势摘要"
- **记忆（Memories）**：ChatGPT 会主动保存用户信息，可查看"你知道我什么"来审计
- **个性化指令**：可设定职业、偏好等，但 UP主认为对善用提示词的用户意义不大
- **数据控制**：可选择是否允许数据用于模型训练、管理共享链接、导出/删除数据
- **安全设置**：多因素认证、登录日志

### Codex

面向代码的专用工具，可连接 GitHub 仓库。演示：
- 让 Codex 解释代码库结构（识别出 Streamlit 应用、OpenAI wrapper、PubMed 工具等模块）
- Codex 主动发现硬编码凭证（API Key 和 WordPress 密码）——UP主承认这是不好的实践
- 可用于 Vibe Coding（如生成 Pomodoro 应用），代码自动推送到 GitHub
- 支持 IDE 集成和代码审查

### Sora 视频生成

通过 ChatGPT 界面访问，可生成视频和图片。支持编辑提示词、混音（remix）、生成连续剧情。UP主评价：模型在快速进步，未来几个月会有显著提升。

### OpenAI Playground

不属于 ChatGPT 本身，但属于 OpenAI 生态。提供更细粒度的控制：
- 模型选择、消息结构编辑
- API Key 管理和应用测试
- Vector Store（向量存储）
- Batch 操作（批量处理）

### Agents SDK

面向开发者的 Agent 框架，用于构建生产级 Agent。需要编程能力。配合 OpenAI Platform 使用，包含向量存储和 Agent 评估（Evaluations）工具。

## 我的评注

- **赞同**：视频对 ChatGPT 功能的覆盖非常全面，从基础到高级都有涉及。特别有价值的是对"搜索式用法 vs 创意式用法"的区分——大多数人确实低估了 ChatGPT 在创意任务上的潜力。语音模式的风险警告也很诚实。
- **质疑**：视频本质是功能巡展，缺乏深度批判。对每个功能都是"这个很好"的态度，没有系统性地对比竞品（除了提到 Claude 可视化更好这一个点）。Agent 模式和 Codex 的演示偏浅——生成了 HTML mockup 和部署，但没展示失败场景和调试过程。深度研究的 7 分钟等待时间和 98 次检索也缺乏成本讨论。
- **关联**：Agent 模式和 Codex 直接呼应 [[Agent原生架构]] 的趋势——ChatGPT 正在从对话界面演变为 Agent 执行平台。Projects 功能体现了 [[上下文工程]] 的实践——通过文件注入和指令设定来控制输出质量。语音模式的情感依赖问题则与 [[AI设计美学]] 相关——OpenAI 刻意塑造"温暖安全"的交互人格，这既是产品优势也是伦理隐患。

## 与其他知识的关联

- 相关概念：[[Agent原生架构]]、[[上下文工程]]、[[AI设计美学]]、[[Vibe Coding]]
- 相关实体：[[Easonlee的AI笔记]]、[[OpenAI]]
- 相关主题：[[AI工具实践]]、[[LLM-Agent工程实践]]

## 待深入问题

- Agent 模式的可靠性边界在哪里？演示的是简单场景，复杂任务的失败率如何？
- ChatGPT 的记忆系统如何处理冲突信息？用户画像是否会"固化"导致输出偏见？
- 深度研究的成本效益比——7 分钟等待换来的报告质量是否优于手动搜索 30 分钟？
- 语音模式的情感依赖问题是否需要产品设计层面的干预（如使用时长限制）？
- Codex 与专业代码 Agent（如 Cursor、Claude Code）的定位差异是什么？
```
