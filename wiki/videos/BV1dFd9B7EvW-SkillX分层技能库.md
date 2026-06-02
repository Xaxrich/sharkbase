---
type: video
bv: BV1dFd9B7EvW
title: "[基于skill的Agent进化]01期-将强Agent的成功轨迹构建为分层Skill库，实现可迁移的泛用性进化"
uploader: "Agent智能体深度研究院"
url: https://www.bilibili.com/video/BV1dFd9B7EvW
date: 2026-06-02
duration: 24:09
series: "Agent自动优化（Agent进化） [论文]"
series_index: 2
tags: ["Skill进化", "经验复用", "分层技能库", "Agent迁移"]
concepts: ["Planning Skill", "Functional Skill", "Atomic Skill", "成功轨迹抽取"]
entities: ["Agent智能体深度研究院"]
topics: ["Agent自动优化与Skill进化"]
capability: ["Agent架构与工作流设计", "AI辅助开发与Agent调度"]
transcript: .b2t/transcripts/original/BV1dFd9B7EvW-20260602-chunked.txt
---

# [基于skill的Agent进化]01期-将强Agent的成功轨迹构建为分层Skill库，实现可迁移的泛用性进化

## 一句话摘要
SkillX 的核心是让强 Agent 的成功轨迹沉淀成 planning、functional、atomic 三层技能库，再让弱 Agent 通过检索和分层调用复用高手经验。

## 核心观点
- 弱 Agent 自己反思只能产出弱经验，强 Agent 的成功轨迹可以作为迁移源。
- 经验不是原始轨迹，也不是一句总结，而是可检索、可组合、可执行的技能文档。
- 三层技能分别解决任务规划、子任务执行和单工具注意事项。
- 技能库需要 refinement，合并重复、过滤低质条目，并覆盖未探索区域。
- 使用时先检索规划技能，再按计划逐步检索功能技能和原子技能。

## 详细笔记
### 三层技能结构
- Planning skill 像路线图，定义任务步骤、依赖关系和分支判断。
- Functional skill 像可复用操作段，描述一个子任务如何稳定完成。
- Atomic skill 贴近单个工具，记录参数约束、常见失败和调用注意事项。

### 从轨迹到技能
- 系统从成功轨迹中抽取可复用动作，过滤探索、回退和错误调用。
- 长环境反馈会被摘要为紧贴任务进展的状态信息，避免噪声污染技能。

### 迁移价值
- 不同模型缺的能力不同：有的缺规划，有的缺工具细节，有的缺子任务模板。
- 分层技能让帮助粒度可调，比一次性塞入完整轨迹更可迁移。

## 与本系列的关系
这条视频属于 `Agent自动优化（Agent进化）` 系列的一环。它和同系列其他视频共同回答一个问题：Agent 的能力提升不只来自更强模型，还来自 harness、skill、memory、数据分布、测试反馈和训练课程等外部系统的持续演化。本条的重点是 `SkillX分层技能库`，适合和主题页 [[Agent自动优化与Skill进化]] 联读。

## 我的评注
这期把技能从 memory 中剥离出来，强调技能的结构化与可迁移性。真正落地时，难点在于如何判断哪些轨迹动作是“成功原因”，哪些只是偶然过程。

## 待深入问题
- 强 Agent 轨迹如何避免把隐含偏差传给弱 Agent？
- 技能检索失败时是否需要 fallback 策略？
- 技能库规模变大后怎样维护层级索引？

## 关联
- [[Agent自动优化与Skill进化]]
- [[Agent原生架构]]
- [[智能体分工]]
- [[Claude Skill]]
- [[AI Agent自验证循环]]
