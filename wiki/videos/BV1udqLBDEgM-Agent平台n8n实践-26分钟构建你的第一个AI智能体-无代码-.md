```markdown
---
type: video
bv: BV1udqLBDEgM
title: "Agent平台n8n实践：26分钟构建你的第一个AI智能体（无代码）"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1udqLBDEgM
date: 2026-04-30
duration: 26:00
tags: [AI Agent, n8n, 无代码, 工作流自动化, Agent评估]
concepts: [AI Agent六组件, 护栏机制, Agent评估]
entities: [Easonlee的AI笔记, n8n, Perplexity]
topics: [LLM-Agent工程实践]
---

# Agent平台n8n实践：26分钟构建你的第一个AI智能体（无代码）

## 一句话摘要

用 n8n 从零搭建一个完整的 AI Agent，覆盖六组件理论、护栏机制和评估部署，是少有的"不仅教搭 Demo，还教上线"的实践教程。

## 核心观点

- AI Agent 由六个组件构成：Model（模型）、Tools（工具）、Knowledge/Memory（知识与记忆）、Audio/Speech（语音）、Guardrails（护栏）、Orchestration（编排），缺一不可
- 大多数教程只覆盖前四项就收工，护栏和编排才是 Agent 从 Demo 走向生产的关键分水岭
- 护栏至少需要两类：内容安全审核（防止输出违规内容）和错误处理（工具调用失败时工作流不能崩）
- 编排的核心是评估（Evaluation）：用测试用例批量跑 Agent，量化指标，基于数据迭代 prompt，"不可测量则不可改进"
- Meta Prompt 是快速生成 Agent prompt 的实用技巧——描述角色、输入、任务、输出、约束，让 LLM 替你写 prompt

## 详细笔记

### AI Agent 六组件理论

| 组件 | 作用 | 示例 |
|------|------|------|
| Model | Agent 的大脑，驱动推理 | GPT-4、Gemini、小模型 |
| Tools | 执行任务的能力 | 日历 API、搜索引擎 |
| Knowledge/Memory | 记忆与知识库 | 对话历史、法律案例库 |
| Audio/Speech | 自然语言交互 | TTS/STT |
| Guardrails | 安全机制 | 内容审核、错误处理 |
| Orchestration | 编排与运维 | 部署、监控、评估 |

六组件齐全才能称为完整的 Agent，缺了任何一个都会在真实使用中暴露问题。

### 实战：AI Research Agent

**目标**：用户输入主题+时间范围 → Agent 自动搜索、生成摘要 → 转音频 → 发邮件。

#### 步骤1：触发器 — 表单提交

在 n8n 创建表单节点，包含两个字段：
- `topic`（搜索主题）
- `time_period`（时间范围，如"过去6个月"）

两个字段均为必填。

#### 步骤2：AI Agent 节点

- **Model**: OpenAI（需配置 API Key 凭证）
- **Prompt**: 使用 Meta Prompt 生成——在 ChatGPT 中输入描述（角色、输入、任务、输出、约束、可用工具），让 LLM 生成完整 prompt
- **Tools**: Perplexity API（sonar 模型），用于搜索信息
- **Memory**: Simple Memory，存储会话历史
- **关键细节**: prompt 中用变量引用表单字段（`{{ $json.topic }}`），让 Agent 知道用户输入了什么

执行后可通过日志查看 Agent 的决策链：OpenAI 判断需要搜索 → 调用 Perplexity → 结果回传 OpenAI → 编译摘要 → 存入 Memory。

#### 步骤3：文本转音频

添加 OpenAI TTS 节点，输入为 Agent 输出的摘要文本，生成音频文件。

#### 步骤4：邮件发送

Gmail 节点，将音频文件作为附件发送。需配置 Google OAuth 凭证。

### 护栏（Guardrails）实现

视频强调这是多数教程跳过的部分。

#### 内容安全审核

- 在 Agent 输出后添加 OpenAI **文本审核**节点（Text Moderation）
- 自动检测：骚扰、自残、性内容、暴力等类别，返回各维度的 flag 和置信分数
- 正常内容 flag=false，违规内容 flag=true 并标注类别

#### 条件分支 — Switch 节点

- flag=false → 继续正常工作流（转音频、发邮件）
- flag=true → 截断工作流，发送警告邮件，提示文本违规

这种设计是一种保守策略：宁可中断也不让违规内容通过。其他策略包括：重新让 Agent 生成、在邮件中标注风险等——取决于业务场景。

### 编排（Orchestration）— 评估体系

#### 评估流程

1. 在 Google Sheets 维护测试用例表（不同 topic + time_period）
2. 在 n8n 添加 **Evaluation Trigger** 节点，连接 Google Sheets 作为数据源
3. 通过"Do Nothing"节点合并两个触发器（表单 + 评估）到同一条 Agent 工作流
4. 添加 **Set Output** 节点，将 Agent 输出写回 Google Sheets
5. 添加 **Set Metrics** 节点，用 LLM 评估输出质量（如 helpfulness 1-5 分）

#### 评估指标

- 内置指标：correctness、helpfulness、string similarity
- 可自定义指标：关键词覆盖率、结构规范性、长度等
- 核心原则：基于评估数据迭代 prompt，而不是凭感觉调参

#### 部署

- 将工作流从 Inactive 切换为 Active
- 使用 Production URL 发布表单，用户即可直接使用

## 我的评注

- **赞同**：六组件框架是很好的思维模型，尤其是把护栏和编排提到与模型、工具同等的地位。多数人确实只关注"能让它跑起来"就停了，而这两项才是生产环境真正吃功夫的地方。
- **赞同**：Meta Prompt 的思路实用——用 LLM 生成 prompt 本身就是一种 bootstrapping，比手写 prompt 效率高很多。
- **质疑**：视频对"评估"的展示偏浅。helpfulness 1-5 分这种用 LLM 打 LLM 的评估方式（即 LLM-as-Judge），本身的信效度存疑。分数都接近满分时，区分度几乎为零，容易产生"一切正常"的虚假安全感。
- **质疑**：护栏只做了输出端审核，没有输入端审核。如果用户在表单中注入恶意 prompt，Agent 可能被诱导执行非预期行为。
- **关联**：这个视频展示的架构——触发器→Agent→审核→分支→输出——与 [[Agent原生架构]] 中讨论的 "Agent as Pipeline" 模式高度一致。n8n 本质上是把 Agent 编排可视化为节点流，降低了编排层的技术门槛，但也带来了调试和可观测性的新挑战。
- **关联**：评估部分与 [[LLM-as-Judge]] 概念直接相关，视频中的 helpfulness 评分就是一种 LLM-as-Judge 实践。

## 与其他知识的关联

- 相关概念：[[AI Agent六组件]]、[[护栏机制]]、[[AI评估体系]]、[[LLM-as-Judge]]
- 相关实体：[[Easonlee的AI笔记]]、[[n8n]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题

- n8n 这类可视化编排平台在复杂 Agent 场景下的可观测性如何？日志和调试体验是否足以支撑生产级 Agent？
- 输入端的 prompt injection 防御在 n8n 中如何实现？表单输入是否需要做清洗？
- LLM-as-Judge 评估的信效度如何提升？单一 helpfulness 分数之外，什么样的评估矩阵更有实际价值？
- 从无代码到低代码的边界在哪里？n8n 构建的 Agent 在什么复杂度下会遇到平台瓶颈？
```

页面已生成。核心提取了三点：

1. **六组件框架**是视频最有价值的理论贡献——Model/Tools/Memory/Speech/Guardrails/Orchestration
2. **护栏和编排**被强调为多数教程遗漏但生产必需的部分
3. **评估体系**的搭建流程有参考价值，但 LLM-as-Judge 的信效度问题值得警惕

如果你需要我继续创建相关的概念页（如"AI Agent六组件"、"护栏机制"）或更新实体页、主题页，告诉我。
