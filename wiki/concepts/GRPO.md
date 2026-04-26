---
type: concept
name: GRPO
tags: [强化学习, 优化算法, 语言模型训练]
first_seen: 2026-04-27
---

# GRPO

## 定义
Group Relative Policy Optimization (GRPO) 是一种强化学习优化算法，是PPO的简化改进版本。其核心机制是：从同一初始状态采样一组rollout，计算组内平均奖励作为基线，将优于基线的轨迹正向强化，差于基线的轨迹负向调整。

## 核心要点
- GRPO由DeepSeek团队提出，用于DeepSeek-R1的训练
- 相比PPO更简单——不需要单独的价值网络(critic)，降低了训练复杂度
- 核心操作：从同一初始状态产生多个rollout → 评估每个rollout的奖励 → 计算组内平均 → 与平均比较决定强化方向 → 更新模型参数
- 在井字棋实验中，GRPO配合Verifiers Trainer使用，2块GPU（1推理+1训练）即可运行
- 对batch size敏感：低于256会导致训练不稳定甚至模型崩溃

## 在以下视频中出现
- [[BV1D9ojBzEAd-将小模型训练成特定领域大师]]（作为RLVR训练的核心算法被讲解和应用）

## 与其他概念的关系
- [[强化学习与可验证奖励]] — GRPO是RLVR训练中常用的优化算法
- [[Verifiers库]] — 内置支持GRPO训练
- [[语言模型强化学习环境]] — GRPO需要环境提供奖励信号

## 相关主题
- [[LLM强化学习训练]]
