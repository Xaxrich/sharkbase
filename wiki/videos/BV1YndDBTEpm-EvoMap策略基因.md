---
type: video
bv: BV1YndDBTEpm
title: "[基于经验的Agent优化]01期-EvoMap和清华的合作论文-把经验编码成控制信号，让进化真正生效（简介附原文链接）"
uploader: "Agent智能体深度研究院"
url: https://www.bilibili.com/video/BV1YndDBTEpm
date: 2026-06-02
duration: 17:25
series: "Agent自动优化（Agent进化） [论文]"
series_index: 3
tags: ["经验表示", "Strategy Gene", "Agent优化", "测试时控制"]
concepts: ["Procedural Skill", "Strategy Gene", "经验编码", "测试时进化"]
entities: ["Agent智能体深度研究院"]
topics: ["Agent自动优化与Skill进化"]
capability: ["Agent架构与工作流设计", "AI辅助开发与Agent调度"]
transcript: .b2t/transcripts/original/BV1YndDBTEpm-20260602-chunked.txt
---

# [基于经验的Agent优化]01期-EvoMap和清华的合作论文-把经验编码成控制信号，让进化真正生效（简介附原文链接）

## 一句话摘要
EvoMap 的关键判断是：经验复用的难点不是存更多经验，而是把经验编码成能在测试时直接约束模型行为的高密度控制信号。

## 核心观点
- 面向人阅读的完整 skill 文档不一定适合作为模型的即时控制上下文。
- strategy gene 是短小的作战卡片，包含任务匹配信号、摘要、策略、失败警告和验证约束。
- 许多科学代码失败来自单位、参数语义和输出转换等细节，gene 用极短文本提醒模型避坑。
- 实验把任务输入和控制表示分开，变化只来自经验表示本身。
- 核心贡献是把经验表示从“文档化”推进到“控制化”。

## 详细笔记
### Skill 文档的问题
- 完整文档适合教学、审查和维护，但进入上下文时会稀释真正影响行为的信号。
- 模型测试时最需要的是能立刻改变决策的边界条件和错误警告。

### Strategy Gene 的形态
- 它不是普通摘要，而是按任务匹配、策略动作、失败风险组织的控制对象。
- 典型内容包括单位转换、函数参数含义、验证步骤和不要做什么。

### 对 Agent 经验库的启发
- 同一经验可以保留两个版本：给人看的 skill 文档，以及给模型执行时看的 gene。
- 经验库不应只追求完整性，还要评估进入上下文后的控制强度。

## 与本系列的关系
这条视频属于 `Agent自动优化（Agent进化）` 系列的一环。它和同系列其他视频共同回答一个问题：Agent 的能力提升不只来自更强模型，还来自 harness、skill、memory、数据分布、测试反馈和训练课程等外部系统的持续演化。本条的重点是 `EvoMap策略基因`，适合和主题页 [[Agent自动优化与Skill进化]] 联读。

## 我的评注
这期补上了“经验怎么重新进入模型”的问题。它提醒我们，知识库不是越长越好，模型执行场景需要低噪声、高约束的经验表示。

## 待深入问题
- 哪些经验适合保留为长 skill，哪些应压缩为 gene？
- gene 过短时如何避免丢失关键边界？
- 能否自动评估一条经验的控制强度？

## 关联
- [[Agent自动优化与Skill进化]]
- [[Agent原生架构]]
- [[智能体分工]]
- [[Claude Skill]]
- [[AI Agent自验证循环]]
