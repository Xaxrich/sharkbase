---
type: video
bv: BV1rQ9JBoECh
title: "[Harness自动优化]01期-Meta-Harness-斯坦福爆火论文-别只卷模型，来“自动发明模型外壳”（简介附原文链接）"
uploader: "Agent智能体深度研究院"
url: https://www.bilibili.com/video/BV1rQ9JBoECh
date: 2026-06-02
duration: 18:32
series: "Agent自动优化（Agent进化） [论文]"
series_index: 1
tags: ["Harness自动优化", "Agent工程", "上下文管理", "评估驱动优化"]
concepts: ["Model Harness", "Harness优化", "完整轨迹检索", "模型外壳"]
entities: ["Agent智能体深度研究院"]
topics: ["Agent自动优化与Skill进化"]
capability: ["Agent架构与工作流设计", "AI辅助开发与Agent调度"]
transcript: .b2t/transcripts/original/Harness自动优化-01期-Meta-Harness-斯坦福爆火论文-别只卷模型-来-自动发明模型外壳-简介附原文链接-20260602-023751.txt
---

# [Harness自动优化]01期-Meta-Harness-斯坦福爆火论文-别只卷模型，来“自动发明模型外壳”（简介附原文链接）

## 一句话摘要
Meta-Harness 把模型外部的检索、上下文组织、工具编排和状态管理视为可优化代码，让系统不只卷模型权重，而是自动改进模型真正工作的外壳。

## 核心观点
- 模型能力不是只由权重决定，harness 决定信息如何存储、检索、呈现和执行。
- 优化对象从 prompt 扩展到一整层系统代码，包括检索逻辑、状态管理和工具调用流程。
- 方法强调读取完整历史、失败日志和版本差异，而不是只看压缩摘要。
- 每一轮新 harness 的代码、分数和轨迹都会写回文件系统，形成可检索经验。
- 价值在于把工程师调参式的 harness engineering 变成可评估、可追溯、可迭代的闭环。

## 详细笔记
### 问题背景：为什么不能只优化模型
- 落地系统的效果取决于模型与 harness 的共同作用。模型给出能力上限，harness 决定能否把能力稳定释放出来。
- 很多失败并不是模型不会，而是上下文、检索、工具顺序或状态边界设计不当。

### 机制：把 harness 当成可搜索的工程对象
- 系统保留不同 harness 版本、运行轨迹、分数变化和失败案例。
- 优化器不是只读一个总结，而是像工程师查事故档案一样检索历史，定位哪个设计导致退化。
- 新版本 harness 会再次评测，并把结果写回历史，供下一轮优化使用。

### 工程启发
- Agent 项目应把 prompt、检索策略、工具描述、状态守卫和校验逻辑都文件化。
- 每次改动都应配套评测与失败样本，否则无法知道 harness 变强还是只是在某组题上过拟合。

## 与本系列的关系
这条视频属于 `Agent自动优化（Agent进化）` 系列的一环。它和同系列其他视频共同回答一个问题：Agent 的能力提升不只来自更强模型，还来自 harness、skill、memory、数据分布、测试反馈和训练课程等外部系统的持续演化。本条的重点是 `Meta-Harness自动发明模型外壳`，适合和主题页 [[Agent自动优化与Skill进化]] 联读。

## 我的评注
这期把“模型外壳”提升为一等工程对象，是后续 AHE 和 continual harness 的基础。需要警惕的是，自动优化如果只追单一 benchmark，可能学到脆弱的评测技巧。

## 待深入问题
- 如何给 harness 改动设计最小可回滚单元？
- 哪些运行日志必须保留，哪些可以摘要化？
- 怎样区分真实能力提升和 benchmark 过拟合？

## 关联
- [[Agent自动优化与Skill进化]]
- [[Agent原生架构]]
- [[智能体分工]]
- [[Claude Skill]]
- [[AI Agent自验证循环]]
