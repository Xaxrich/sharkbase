---
type: video
bv: BV1n9Gd6oEUK
title: "[Harness自动优化]02期 | 复旦爆火论文-AHE-可观测体系驱动Harness自进化"
uploader: "Agent智能体深度研究院"
url: https://www.bilibili.com/video/BV1n9Gd6oEUK
date: 2026-06-02
duration: 9:28
series: "Agent自动优化（Agent进化） [论文]"
series_index: 8
tags: ["AHE", "Harness工程", "可观测性", "Agent自进化"]
concepts: ["组件可观测性", "经验可观测性", "决策可观测性", "Change Log"]
entities: ["Agent智能体深度研究院"]
topics: ["Agent自动优化与Skill进化"]
capability: ["Agent架构与工作流设计", "AI辅助开发与Agent调度"]
transcript: .b2t/transcripts/original/BV1n9Gd6oEUK-20260602-chunked.txt
---

# [Harness自动优化]02期 | 复旦爆火论文-AHE-可观测体系驱动Harness自进化

## 一句话摘要
AHE 的主张是：让 harness 自进化的关键不是让 Agent 盲目改 prompt，而是把组件、经验和决策都变成可观测对象。

## 核心观点
- Harness 包含 system prompt、工具描述、工具实现、中间键、技能、子代理、记忆、日志和校验。
- 组件可观测性把可编辑部分文件化，便于失败归因到具体组件。
- 经验可观测性把海量轨迹整理成概览、单题报告和原始 trace 的渐进披露结构。
- 决策可观测性要求每次编辑写明证据、根因、预计修复和潜在回归。
- 下一轮评测会验证预测是否成立，不成立的修改可以按文件粒度回滚。

## 详细笔记
### 人工调 harness 为什么会成为瓶颈
- 开发者通常看失败轨迹、改几句 prompt、再跑评测；任务变长后人类注意力跟不上。
- 原始轨迹可能有千万级 token，粗暴总结会丢证据，直接改 prompt 无法稳定归因。

### 三层可观测性
- 组件可观测性：让 prompt、工具、中间状态和记忆都有固定文件与挂载点。
- 经验可观测性：从概览 drill down 到单题报告和原始轨迹。
- 决策可观测性：每次改动都必须绑定可验证预测。

### 典型改动
- 例如 agent 生成正确交付物后又清理删除，AHE 可演化出 publish state guard，保护已验证文件。
- 这类改动不是模型权重变化，而是 harness 层的工程守卫变强。

## 与本系列的关系
这条视频属于 `Agent自动优化（Agent进化）` 系列的一环。它和同系列其他视频共同回答一个问题：Agent 的能力提升不只来自更强模型，还来自 harness、skill、memory、数据分布、测试反馈和训练课程等外部系统的持续演化。本条的重点是 `AHE可观测Harness自进化`，适合和主题页 [[Agent自动优化与Skill进化]] 联读。

## 我的评注
AHE 是 Meta-Harness 的工程化后续：它把自动改外壳这件事从搜索问题推进到可观测系统设计。

## 待深入问题
- 哪些 harness 组件应该先文件化？
- change log 的预测应细到任务级还是行为级？
- 自动回滚策略怎样避免丢掉长期有益改动？

## 关联
- [[Agent自动优化与Skill进化]]
- [[Agent原生架构]]
- [[智能体分工]]
- [[Claude Skill]]
- [[AI Agent自验证循环]]
