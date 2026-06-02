---
type: concept
name: Harness自动优化
tags: [Agent自动优化, Agent工程]
updated_at: 2026-06-02
capability: [Agent架构与工作流设计]
---

# Harness自动优化

Harness 自动优化把模型外部的 prompt、工具、检索、状态、记忆、子代理和校验逻辑视为可编辑、可评估、可回滚的工程外壳。

## 要点

- 核心判断：模型权重给出能力上限，harness 决定能力能否稳定释放。
- 优化不应只依赖压缩摘要，而要保留可追溯的轨迹、失败日志、版本差异和评测结果。
- 成熟路径包括离线版本搜索、可观测文件化、自评估变更记录，以及在线连续轨迹中的自我修补。

## 相关视频

- [[BV1rQ9JBoECh-Meta-Harness自动发明模型外壳]]
- [[BV1n9Gd6oEUK-AHE可观测Harness自进化]]
- [[BV1NTG26MEGv-Continual-Harness宝可梦长程自改]]
