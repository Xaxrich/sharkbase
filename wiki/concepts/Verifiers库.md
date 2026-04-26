---
type: concept
name: Verifiers库
tags: [开源工具, 强化学习环境, 语言模型训练]
first_seen: 2026-04-27
---

# Verifiers库

## 定义
Verifiers是由Trim Length团队开发的开源Python库，用于将强化学习环境构建为可安装、可分发的软件制品。它提供模块化组件来创建LLM agent的RL环境，既可用于评估也可用于训练。

## 核心要点
- 提供多种环境基类：单轮(Single-turn)、多轮(Multi-turn)、工具(Tool)、MCP、有状态工具(Stateful Tool)、递归LLM
- 核心抽象：`load_environment`（环境入口）、`XMLParser`（解析模型响应中的标签）、`Rubric`（加权奖励函数集合）
- 抽象模型服务，兼容OpenAI API端点——可通过vLLM接入本地模型，或直接使用OpenAI
- 支持单次交互和并行轨迹(rollout)，让开发者专注于环境逻辑
- 训练集成：内置Trainer，同时集成Prime RL、SkyRL等框架
- 环境中心(Env Hub)：社区共享环境的平台，旨在对抗环境碎片化问题

### 环境类型示例
- **单轮环境**：如reverse text（反转文本），一次交互即完成
- **多轮环境**：如double check math（双重检查数学），模型回答后环境追问"你确定吗？"
- **工具环境**：模型可调用Python函数定义的工具，接收结果后继续推理
- **MCP环境**：自动连接Model Context Protocol服务器暴露工具
- **有状态工具环境**：工具在rollout期间保持持久状态（如数据库连接、会话ID）
- **递归LLM**：语言模型可递归分解和交互输入上下文，处理无限长度输入

## 在以下视频中出现
- [[BV1D9ojBzEAd-将小模型训练成特定领域大师]]（作为构建井字棋RL环境的核心工具被详细演示）

## 与其他概念的关系
- [[强化学习与可验证奖励]] — Verifiers是实现RLVR环境的基础设施
- [[GRPO]] — Verifiers内置支持GRPO训练
- [[语言模型强化学习环境]] — Verifiers是构建此类环境的具体实现
- [[MCP Server]] — Verifiers的MCP环境类型可连接MCP服务器

## 相关主题
- [[LLM强化学习训练]]
