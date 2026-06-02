---
type: video
bv: BV1XM526WEY6
title: "[基于skill进行ICRL]-美团论文-skill0-把skill逐步内化进模型参数"
uploader: "Agent智能体深度研究院"
url: https://www.bilibili.com/video/BV1XM526WEY6
date: 2026-06-02
duration: 10:31
series: "Agent自动优化（Agent进化） [论文]"
series_index: 6
tags: ["Skill0", "ICRL", "技能内化", "强化学习"]
concepts: ["Skill Internalization", "动态课程", "helpfulness", "技能脚手架"]
entities: ["Agent智能体深度研究院"]
topics: ["Agent自动优化与Skill进化"]
capability: ["Agent架构与工作流设计", "AI辅助开发与Agent调度"]
transcript: .b2t/transcripts/original/BV1XM526WEY6-20260602-chunked.txt
---

# [基于skill进行ICRL]-美团论文-skill0-把skill逐步内化进模型参数

## 一句话摘要
Skill0 反过来问：如果 Agent 永远依赖运行时技能说明书，它到底学会了技能，还是只会照着提示做题？答案是把技能作为训练脚手架，最终推理时撤掉。

## 核心观点
- 训练时给技能，推理时不给技能，让程序性能力从上下文进入模型参数。
- 技能库不是被否定，而是从推理外挂变成训练脚手架。
- helpfulness 指标通过“带技能 vs 不带技能”的子任务差值判断技能是否仍有帮助。
- 动态课程从满技能逐步减少到零技能，避免模型突然失去支架。
- 推理成本下降，因为运行时不再携带长技能文本。

## 详细笔记
### 外挂技能的结构性成本
- 检索可能带来错误指导，技能文本消耗 token，模型还可能只学会读说明书。
- Skill0 的目标是训练时借助技能探索，后期逐步撤掉支架。

### 动态课程如何撤技能
- 系统周期性比较当前策略在有/无某技能时的子任务表现。
- 差值大说明技能仍有帮助，差值小或负说明模型可能已内化或该技能是噪声。
- 预算分阶段下降，使上下文变化平滑而不是断崖式。

### 位置：从会调用技能到学会技能
- SkillX、Trace2Skill、SkillClaw 解决技能如何生成和维护。
- Skill0 解决技能能否被模型吸收，形成更轻、更便宜的推理 Agent。

## 与本系列的关系
这条视频属于 `Agent自动优化（Agent进化）` 系列的一环。它和同系列其他视频共同回答一个问题：Agent 的能力提升不只来自更强模型，还来自 harness、skill、memory、数据分布、测试反馈和训练课程等外部系统的持续演化。本条的重点是 `Skill0把技能内化到参数`，适合和主题页 [[Agent自动优化与Skill进化]] 联读。

## 我的评注
这期给技能路线补上“闭卷考试”目标。风险在于它高度依赖初始技能库和验证子任务质量，训练成本也不低。

## 待深入问题
- 哪些技能适合内化，哪些必须保留为外部工具说明？
- helpfulness 子任务如何自动生成？
- 撤掉技能后如何监控能力遗忘？

## 关联
- [[Agent自动优化与Skill进化]]
- [[Agent原生架构]]
- [[智能体分工]]
- [[Claude Skill]]
- [[AI Agent自验证循环]]
