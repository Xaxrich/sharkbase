---
type: video
bv: BV1LfmHBuEzt
title: "Claude Skill实战：创建一个AI团队"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1LfmHBuEzt
date: 2026-04-30
duration: 33:00
tags: [Claude技能, AI工作流, 提示工程, 上下文管理, AI代理]
concepts: [Claude Skill, 上下文工程, 子代理, 确定性输出]
entities: [Easonlee的AI笔记]
topics: [LLM-Agent工程实践]
transcript: .b2t/transcripts/original/
---

# Claude Skill实战：创建一个AI团队

## 一句话摘要
Claude Skills 是 Anthropic 推出的可编程工作流机制，通过约束指令、引用文件和脚本代码，让 AI 输出从"大概对"变为"确定地对"。

## 核心观点

- **Skill 的本质是"可编程的 AI 员工"**：不是给 AI 一个模糊指令让它自由发挥，而是像培训初级同事一样——写清楚步骤、给好参考资料、设定行为边界
- **上下文不是越多越好，而是越准越好**：过多无关上下文反而导致幻觉；Skill 只在任务需要时按需加载相关上下文
- **脚本让 Skill 从"建议"变成"计算"**：用 Python 脚本处理数据分析任务，取代让 LLM 自行解读数据——前者确定性执行，后者每次结果不同
- **Skill 解决了 AI 采用率下降的根本问题**：企业 AI 粘性不足，问题不在 AI 本身，而在缺乏结构化的提示和上下文工程

## 详细笔记

### 三层概念：Projects → Subagents → Skills

**Projects（项目）**：Claude.ai 中的工作空间，包含系统指令、上下文文件、工具连接和对话记忆。适合团队协作，但需要持续手动更新上下文文件。

**Subagents（子代理）**：Claude Code 中的能力，可在一个对话中启动多个专用代理（如前端代理、后端代理），上下文隔离在各自对话窗口中。

**Skills（技能）**：全局、项目级或个人级可用的自动化工作流。核心优势：
- 按需加载上下文（只在任务相关时拉取）
- 可嵌入脚本代码执行确定性计算
- 可引用外部参考文件（品牌指南、术语表等）
- 可调用 MCP 工具（如 Firecrawl 爬取网页）

### Skill 的文件结构

一个 Skill 由三部分组成：
1. **Markdown 主文件**：定义技能概述、任务步骤和输出格式
2. **引用文件（References）**：品牌指南、指标定义、术语表等，按需加载
3. **脚本（Scripts）**：Python 代码，用于确定性数据处理，替代 LLM 的非确定性推理

### 实战演示

#### 1. UTM 链接生成器（Artifact Builder Skill）
使用预置的 Artifact Builder Skill，一句话指令生成可分享的 Web App——UTM 链接生成工具。Skill 提供了构建 Artifact 的规范和约束，确保输出是功能性完整的应用而非粗糙原型。

#### 2. A/B 测试想法生成器
- 输入网站 URL
- Skill 通过 Firecrawl MCP 爬取页面内容
- 按预设框架输出实验方案：控制组、变体、假设、影响/信心/实施难度评分（ICE）
- 实际价值：视频作者根据 Skill 建议将社交证明模块上移，正在跑 A/B 测试

#### 3. 营销数据分析器
- 上传 CSV 数据文件（广告投放数据）
- Skill 内嵌 Python 脚本进行确定性计算（总花费、收入、利润、各渠道对比）
- 关键洞察：同样的数据如果只靠 LLM 自由解读，容易产生幻觉数字；脚本计算确保数据准确

#### 4. 现场创建：推文转长文 Skill
- 使用 Skill Creator（用 Skill 创建 Skill）生成
- 提供参考文件：已有推文 + 已有 Newsletter 作为风格样本
- 一轮对话即生成符合风格的 Newsletter 长文
- 改进方向：导出全部推文建立完整风格指南，实现自动化

### AI 采用率的深层问题

引用 Ramp 报告：企业 AI 工具订阅出现下降，粘性不足。视频结论：
- 问题不是 AI 不行，而是**人们不会用**——缺乏结构化提示和上下文工程
- Skills 的出现恰好填补了这个缺口：把专家的隐性知识编码为显式指令和脚本

## 我的评注

- **赞同**：Skill 内嵌脚本的设计是关键洞见。数据分析任务中 LLM 的非确定性推理是真实痛点——让模型"看一下数据然后给洞察"，结果每次不同且难以验证。脚本把"AI 理解需求"和"代码执行计算"分离，各自做擅长的事
- **赞同**："AI 员工"的类比精准。Junior 同事需要明确的操作手册和参考资料，而非一堆散乱的背景信息。Skill 就是这个操作手册的数字化版本
- **质疑**：视频对 Skill 与 Plugin 的区别含糊带过（"don't quote me on this"）。作为教程，这是重要遗漏——用户需要清楚何时用 Skill、何时用 Plugin
- **质疑**：营销数据分析器的"确定性"声明需要验证。脚本计算数据指标确实确定，但"哪些指标值得看"和"如何解读趋势"仍然是 LLM 的非确定性输出。视频把这两层混在一起了
- **关联**：与 [[LLM-Agent工程实践]] 直接相关——Skill 本质上是 Agent 的"技能模块"，把通用能力分解为可组合的专用工作流。这个思路与 Agent SDK 中的 tool definition 和 system prompt 的组合一脉相承

## 与其他知识的关联
- 相关概念：[[上下文工程]]、[[确定性输出]]、[[Claude Skill]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题
- Skill 的脚本执行环境有什么安全边界？能否访问文件系统或网络？
- Skill 与 MCP 的交互模式——何时用 Skill 内嵌脚本、何时调 MCP 工具，选择标准是什么？
- 多个 Skill 组合使用时的上下文冲突如何解决？
- Skill 的版本管理和团队共享机制如何运作？
