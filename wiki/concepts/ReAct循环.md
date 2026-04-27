---
type: concept
name: ReAct循环
tags: [Agent架构, 推理模式, 循环结构, LLM]
first_seen: 2026-04-27
---

# ReAct循环

## 定义
ReAct (Reasoning + Acting) 循环是现代 AI Agent 的核心运行模式：模型先推理(Reasoning)，再执行动作(Acting)，根据动作结果继续推理，循环往复直到产生最终答案。已成为业界公认的 Agent 底层设计标准。

## 核心要点
- **State 结构体**：维护循环全局状态——message list（消息列表）、tools list（工具列表）、turn count（轮次计数）、compression status（压缩状态）、termination flags（终止标志）
- **循环流程**：构建初始 prompt → 请求模型 → 文本响应则退出 / 工具调用则由框架执行 → tool result 追加到 message list → 检查压缩 → 再次请求模型
- **模型本身没有工具能力**：模型只能"吐出"工具调用指令，真正的工具执行由工程框架完成
- **两个可控点**：(1) 进入循环前的 system prompt（工程完全可控）；(2) Hook 机制（在循环任意步骤插入代码修改 message list）
- **Claude Code 的实现特点**：
  - System Prompt 采用动态组装 + 静态分割符策略，最大化 Token 缓存命中
  - 三层 Token 压缩：默认剪裁 → 异步磁盘重建 → 全量摘要
  - 记忆管理采用克制策略，宁可少记也不乱记

## 在以下视频中出现
- [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]]（作为 Query Engine 的核心循环被详细解析）

## 与其他概念的关系
- [[驾驭工程]] — ReAct 循环是 Harness 中 Query Engine 的核心组件
- [[Claude-Code架构]] — Claude Code 对 ReAct 的具体工程实现

## 相关主题
- [[LLM-Agent工程实践]]
