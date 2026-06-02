---
type: video
bv: BV1NTG26MEGv
title: "[Harness自动优化] 03期 | 谷歌×普林斯顿新论文-一边玩宝可梦，一边自动改写Agent Harness"
uploader: "Agent智能体深度研究院"
url: https://www.bilibili.com/video/BV1NTG26MEGv
date: 2026-06-02
duration: 11:31
series: "Agent自动优化（Agent进化） [论文]"
series_index: 9
tags: ["Continual Harness", "长程Agent", "自改系统", "Google DeepMind"]
concepts: ["连续轨迹", "Refiner", "Subagent", "Skill Memory"]
entities: ["Agent智能体深度研究院"]
topics: ["Agent自动优化与Skill进化"]
capability: ["Agent架构与工作流设计", "AI辅助开发与Agent调度"]
transcript: .b2t/transcripts/original/BV1NTG26MEGv-20260602-chunked.txt
---

# [Harness自动优化] 03期 | 谷歌×普林斯顿新论文-一边玩宝可梦，一边自动改写Agent Harness

## 一句话摘要
Continual Harness 研究在不可重置的长程任务中，Agent 能否一边行动一边修改自己的 prompt、子代理、技能和记忆。

## 核心观点
- 宝可梦被用作长程、部分可观测、反馈稀疏、不能随便 reset 的具身任务。
- Harness 包含 system prompt、subagents、skills 和 memory，不只是 prompt。
- Refiner 根据最近轨迹窗口识别导航循环、工具失败、目标停滞和探索遗漏。
- 修改会立即进入下一步行动上下文，而不是等一轮完整 run 结束后重置。
- 它把人类直播调试 harness 的流程自动化，保留在同一条连续轨迹里。

## 详细笔记
### 为什么不能总是 reset
- 很多失败只在任务深处暴露，重置会让系统很难稳定到达这些状态。
- 真实编程或操作 Agent 也常常没有免费重置，必须在当前状态上修复。

### Refiner 修改什么
- 改写 prompt 的策略指导。
- 新增或修正战斗、解谜、自反思等 subagent。
- 把成功序列固化为 skill，或修复报错代码。
- 更新 memory，降低已探索区域的重要性，修正过时记忆。

### 与前几期的关系
- Meta-Harness 和 AHE 更偏离线/轮次优化，Continual Harness 强调在线连续轨迹内的自我修补。
- 它把 harness evolution 推向更接近真实长程 Agent 的状态管理问题。

## 与本系列的关系
这条视频属于 `Agent自动优化（Agent进化）` 系列的一环。它和同系列其他视频共同回答一个问题：Agent 的能力提升不只来自更强模型，还来自 harness、skill、memory、数据分布、测试反馈和训练课程等外部系统的持续演化。本条的重点是 `Continual Harness宝可梦长程自改`，适合和主题页 [[Agent自动优化与Skill进化]] 联读。

## 我的评注
这期最重要的是“连续性”。长程 Agent 的 harness 不是赛后总结文档，而是行动中持续被改写的系统状态。

## 待深入问题
- 在线修改如何避免把短期补丁污染长期策略？
- memory 更新如何处理过时事实？
- 连续任务中的安全边界如何设计？

## 关联
- [[Agent自动优化与Skill进化]]
- [[Agent原生架构]]
- [[智能体分工]]
- [[Claude Skill]]
- [[AI Agent自验证循环]]
