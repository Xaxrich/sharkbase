---
type: video
bv: BV1paVJ6FEZe
title: "[Agent强化学习] ACL26-CoEvolve-让Agent与数据分布共同进化"
uploader: "Agent智能体深度研究院"
url: https://www.bilibili.com/video/BV1paVJ6FEZe
date: 2026-06-02
duration: 8:23
series: "Agent自动优化（Agent进化） [论文]"
series_index: 11
tags: ["Agent强化学习", "数据进化", "CoEvolve", "ACL26"]
concepts: ["遗忘信号", "边界信号", "稀有信号", "环境验证"]
entities: ["Agent智能体深度研究院"]
topics: ["Agent自动优化与Skill进化"]
capability: ["Agent架构与工作流设计", "AI辅助开发与Agent调度"]
transcript: .b2t/transcripts/original/BV1paVJ6FEZe-20260602-chunked.txt
---

# [Agent强化学习] ACL26-CoEvolve-让Agent与数据分布共同进化

## 一句话摘要
CoEvolve 的核心是让训练数据分布跟着 Agent 当前弱点一起变化，而不是反复训练一批早已静态生成的任务。

## 核心观点
- 训练越往后，旧数据可能变得不合适：有的任务已会，有的能力退化却没人发现。
- 系统从 rollout 中抽取遗忘、边界和稀有三类信号。
- 遗忘信号指最近曾成功、当前又失败的任务；边界信号指同题采样有成有败；稀有信号指低频但反复出现的动作模式。
- LLM 基于信号上下文重新探索环境，生成新的任务-解法对。
- 新任务必须经过环境验证，能执行成功才进入下一轮训练集。

## 详细笔记
### 静态数据的问题
- 人工轨迹贵且覆盖不了真实长尾，普通合成数据又不知道模型后来卡在哪里。
- 训练中期暴露的新短板需要动态数据，而不是继续刷旧题。

### 三类信号
- 遗忘信号覆盖能力回退。
- 边界信号覆盖策略不稳定。
- 稀有信号覆盖长尾探索不足。

### 从信号到新任务
- 系统把触发信号的完整轨迹、任务描述、动作和反馈交给 LLM 总结弱点。
- 再进入环境多轮、多步探索，把动作观察抽象为新任务与可能解法。
- 最终通过环境执行验证，过滤看似合理但不可执行的噪声。

## 与本系列的关系
这条视频属于 `Agent自动优化（Agent进化）` 系列的一环。它和同系列其他视频共同回答一个问题：Agent 的能力提升不只来自更强模型，还来自 harness、skill、memory、数据分布、测试反馈和训练课程等外部系统的持续演化。本条的重点是 `CoEvolve数据分布共同进化`，适合和主题页 [[Agent自动优化与Skill进化]] 联读。

## 我的评注
这期把 Agent 进化从 skill/harness 推到训练数据层。它提醒我们，数据集不是一次性资产，而应随策略状态动态演化。

## 待深入问题
- 信号阈值如何设置才能避免追噪声？
- 环境验证成本如何控制？
- 动态数据会不会放大模型短期偏好？

## 关联
- [[Agent自动优化与Skill进化]]
- [[Agent原生架构]]
- [[智能体分工]]
- [[Claude Skill]]
- [[AI Agent自验证循环]]
