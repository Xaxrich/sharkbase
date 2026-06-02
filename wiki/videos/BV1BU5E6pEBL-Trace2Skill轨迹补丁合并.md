---
type: video
bv: BV1BU5E6pEBL
title: "[基于skill的Agent进化] 阿里Qwen新论文-Trace2skill-分层整合从不同轨迹中得到的修改建议"
uploader: "Agent智能体深度研究院"
url: https://www.bilibili.com/video/BV1BU5E6pEBL
date: 2026-06-02
duration: 12:20
series: "Agent自动优化（Agent进化） [论文]"
series_index: 4
tags: ["Trace2Skill", "轨迹蒸馏", "技能补丁", "阿里Qwen"]
concepts: ["Skill Patch", "并行轨迹分析", "失败根因验证", "层级合并"]
entities: ["Agent智能体深度研究院"]
topics: ["Agent自动优化与Skill进化"]
capability: ["Agent架构与工作流设计", "AI辅助开发与Agent调度"]
transcript: .b2t/transcripts/original/BV1BU5E6pEBL-20260602-chunked.txt
---

# [基于skill的Agent进化] 阿里Qwen新论文-Trace2skill-分层整合从不同轨迹中得到的修改建议

## 一句话摘要
Trace2Skill 把成功与失败轨迹先拆成技能补丁，再通过并行分析和层级合并形成可迁移技能，避免顺序更新造成技能漂移。

## 核心观点
- 单条轨迹局部，但大量轨迹中反复出现的修复方式能反映任务域规律。
- 系统不直接把轨迹贴进文档，而是提炼插入、删除、更新等 skill patch。
- 成功轨迹侧重提取关键成功行为，失败轨迹需要多轮诊断和最小修复验证。
- 并行 patch 避免早期偶然错误污染后续更新。
- 层级合并用于去重、解冲突，并拒绝引用不存在文件或范围冲突的补丁。

## 详细笔记
### 为什么不是顺序更新
- 顺序更新会让后续分析看到已被前面案例改过的技能，容易围绕偶然版本继续修补。
- 并行分析让每条轨迹独立给出证据，最后再统一归纳。

### 成功与失败的不同价值
- 成功轨迹告诉系统哪些动作真正促成结果。
- 失败轨迹需要读日志、输入输出和标准答案，确认根因可复现，避免生成假补丁。

### 技能合并的工程约束
- 合并不只是让模型总结，还需要文件存在性、编辑范围冲突和格式校验。
- 这使 skill evolution 更像受约束的代码 review，而不是自由写作。

## 与本系列的关系
这条视频属于 `Agent自动优化（Agent进化）` 系列的一环。它和同系列其他视频共同回答一个问题：Agent 的能力提升不只来自更强模型，还来自 harness、skill、memory、数据分布、测试反馈和训练课程等外部系统的持续演化。本条的重点是 `Trace2Skill轨迹补丁合并`，适合和主题页 [[Agent自动优化与Skill进化]] 联读。

## 我的评注
这期的价值在于把“从轨迹学技能”落到编辑操作层。它比泛泛总结更工程化，但仍依赖分析 Agent 的根因判断能力。

## 待深入问题
- 失败根因验证能否完全自动化？
- 补丁合并时如何处理少数但关键的长尾案例？
- 技能补丁是否需要版本回滚机制？

## 关联
- [[Agent自动优化与Skill进化]]
- [[Agent原生架构]]
- [[智能体分工]]
- [[Claude Skill]]
- [[AI Agent自验证循环]]
