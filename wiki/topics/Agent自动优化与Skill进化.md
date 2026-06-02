---
type: topic
title: Agent自动优化与Skill进化
tags: [Agent自动优化, Skill进化, Harness优化, Agent强化学习]
updated_at: 2026-06-02T02:52:26
---

# Agent自动优化与Skill进化

这个主题页汇总 `Agent智能体深度研究院` 的 12 集 Agent 自动优化论文系列。核心问题是：Agent 的进化到底发生在哪里？这组视频给出的答案不是单一的，而是分布在模型外壳、技能库、经验表示、在线轨迹、训练数据和参数内化多个层面。

## 视频索引

- [[BV1rQ9JBoECh-Meta-Harness自动发明模型外壳]] — [Harness自动优化]01期-Meta-Harness-斯坦福爆火论文-别只卷模型，来“自动发明模型外壳”（简介附原文链接）
- [[BV1dFd9B7EvW-SkillX分层技能库]] — [基于skill的Agent进化]01期-将强Agent的成功轨迹构建为分层Skill库，实现可迁移的泛用性进化
- [[BV1YndDBTEpm-EvoMap策略基因]] — [基于经验的Agent优化]01期-EvoMap和清华的合作论文-把经验编码成控制信号，让进化真正生效（简介附原文链接）
- [[BV1BU5E6pEBL-Trace2Skill轨迹补丁合并]] — [基于skill的Agent进化] 阿里Qwen新论文-Trace2skill-分层整合从不同轨迹中得到的修改建议
- [[BV1dC5268Eja-SkillClaw多用户轨迹进化]] — [基于skill的Agent进化]阿里DreamX团队论文-SkillClaw-聚合多用户轨迹得到稳定进化方向，夜间验证保证有效性
- [[BV1XM526WEY6-Skill0把技能内化到参数]] — [基于skill进行ICRL]-美团论文-skill0-把skill逐步内化进模型参数
- [[BV1qS586HEdg-Skill1统一训练选用写技能]] — [skill进化]-美团新论文-skill1-一个信号拆三份，同时学习skill使用全流程
- [[BV1n9Gd6oEUK-AHE可观测Harness自进化]] — [Harness自动优化]02期 | 复旦爆火论文-AHE-可观测体系驱动Harness自进化
- [[BV1NTG26MEGv-Continual-Harness宝可梦长程自改]] — [Harness自动优化] 03期 | 谷歌×普林斯顿新论文-一边玩宝可梦，一边自动改写Agent Harness
- [[BV11vG669EyX-Ctx2Skill从上下文提技能]] — [skill进化] 清华爆火论文-Ctx2Skill-零标注自博弈，从文档提取技能
- [[BV1paVJ6FEZe-CoEvolve数据分布共同进化]] — [Agent强化学习] ACL26-CoEvolve-让Agent与数据分布共同进化
- [[BV1geVD6FETm-MUSE-Autoskill技能生命周期]] — [Skill进化] 06期 | 字节MUSE-Autoskill：给Agent装上Skill生命周期管理，自动创建、测试、维护Skill

## 路线图

- **Harness 路线**：Meta-Harness、AHE、Continual Harness 关注模型外部系统如何自动改写。
- **Skill 路线**：SkillX、Trace2Skill、SkillClaw、Skill1、MUSE-Autoskill 关注技能如何生成、选择、维护、测试与沉淀。
- **内化路线**：Skill0 关注外部技能如何从运行时上下文迁移到模型参数。
- **上下文路线**：Ctx2Skill 关注如何从陌生资料中零标注提取可复用技能。
- **数据路线**：CoEvolve 关注强化学习训练数据如何随 Agent 当前弱点动态演化。

## 总判断

这组视频共同指向一个趋势：Agent 工程正在从“写一个更好的 prompt”走向“构建可观测、可训练、可验证、可回滚的能力系统”。真正的复利不在单次调用结果，而在系统能否把失败、成功和用户反馈转化为下一轮更好的 harness、skill 或数据。
