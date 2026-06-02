---
type: video
bv: BV11vG669EyX
title: "[skill进化] 清华爆火论文-Ctx2Skill-零标注自博弈，从文档提取技能"
uploader: "Agent智能体深度研究院"
url: https://www.bilibili.com/video/BV11vG669EyX
date: 2026-06-02
duration: 9:48
series: "Agent自动优化（Agent进化） [论文]"
series_index: 10
tags: ["Ctx2Skill", "上下文学习", "自博弈", "零标注"]
concepts: ["复杂资料", "Challenger", "Reasoner", "Rubric Judge"]
entities: ["Agent智能体深度研究院"]
topics: ["Agent自动优化与Skill进化"]
capability: ["Agent架构与工作流设计", "AI辅助开发与Agent调度"]
transcript: .b2t/transcripts/original/BV11vG669EyX-20260602-chunked.txt
---

# [skill进化] 清华爆火论文-Ctx2Skill-零标注自博弈，从文档提取技能

## 一句话摘要
Ctx2Skill 关注模型面对一份陌生复杂资料时，能否零标注地通过自博弈把资料里的规则、流程和约束提炼成可复用技能。

## 核心观点
- 这里的 context 是外部复杂资料，不只是聊天窗口。
- 目标不是从资料中找答案，而是先学习资料里的新规则，再解决后续任务。
- Challenger 根据资料出探测任务和 rubrics，Reasoner 带当前技能答题，Judge 按 rubrics 判分。
- 失败题用于更新 Reasoner 技能，成功题用于提升 Challenger 出题能力。
- 技能是自然语言操作手册，不更新参数。

## 详细笔记
### 普通总结为什么不够
- 复杂资料中包含格式约束、流程顺序、例外条件和角色规则，单次总结不知道漏了什么。
- 没有反馈，模型写出的技能是否能支撑任务无法验证。

### 自博弈闭环
- Challenger 负责出有区分度的任务，不只是把题变难。
- Reasoner 使用当前技能答题，暴露资料理解缺口。
- Judge 只按 rubric 严格判定，失败再反推缺失技能。

### 适用场景
- 产品手册、游戏规则、实验记录、网页材料、报告和复杂对话都可以视作资料源。
- 它适合把一次性上下文变成后续可重复使用的资料专属技能。

## 与本系列的关系
这条视频属于 `Agent自动优化（Agent进化）` 系列的一环。它和同系列其他视频共同回答一个问题：Agent 的能力提升不只来自更强模型，还来自 harness、skill、memory、数据分布、测试反馈和训练课程等外部系统的持续演化。本条的重点是 `Ctx2Skill从上下文提技能`，适合和主题页 [[Agent自动优化与Skill进化]] 联读。

## 我的评注
Ctx2Skill 把 skill generation 的数据源从运行轨迹扩展到文档上下文，很适合知识库与 Agent 能力系统结合。

## 待深入问题
- Challenger 如何避免出偏题或伪难题？
- Rubric 自动生成的可靠性如何校准？
- 资料更新后技能如何失效和重建？

## 关联
- [[Agent自动优化与Skill进化]]
- [[Agent原生架构]]
- [[智能体分工]]
- [[Claude Skill]]
- [[AI Agent自验证循环]]
