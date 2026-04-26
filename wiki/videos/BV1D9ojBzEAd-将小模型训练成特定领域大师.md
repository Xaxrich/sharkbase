---
type: video
bv: BV1D9ojBzEAd
title: Deepset工程师-将小模型训练成特定领域大师
uploader: Step Re (Deepset)
url: https://www.bilibili.com/video/BV1D9ojBzEAd
date: 2026-04-27
duration: 未知
tags: [强化学习, 语言模型训练, RLVR, GRPO, Verifiers, 小模型]
concepts: [强化学习与可验证奖励, GRPO, Verifiers库, 语言模型强化学习环境]
entities: [Deepset]
topics: [LLM强化学习训练]
transcript: .b2t/transcripts/original/Deepset工程师-将小模型训练-成特定领域大师-20260427-chunked.txt
---

# Deepset工程师-将小模型训练成特定领域大师

## 一句话摘要
Deepset工程师Step Re展示如何利用Reinforcement Learning with Verifiable Rewards (RLVR)和开源Verifiers库，将一个连井字棋都不会的小语言模型训练成超越GPT-5 mini的领域大师。

## 核心观点
- RLVR (Reinforcement Learning with Verifiable Rewards) 与监督微调(SFT)有本质区别：SFT是统计模仿，模型受限于人类示例质量；RLVR让模型通过试错探索不同轨迹，发现更高效的推理策略，不再被人类示例的天花板所限制
- 强化学习环境是LLM训练的新范式核心——从静态数据集转向动态交互系统，环境定义了任务、评分规则和交互逻辑，是实现RLVR训练的前提
- 训练超参数（尤其是batch size）对RL训练稳定性至关重要——batch size低于256会导致不稳定甚至模型崩溃，大batch size虽慢但稳定
- 更好的策略是从非推理模型出发，通过RL训练将其转化为推理模型，而非从已有的推理模型开始——推理模型会产生过长的思维链，在有限GPU资源下容易被截断
- 训练中不要持续监控loss曲线——RL训练需要时间才能看到进展，过度监控会导致过早停止

## 详细笔记

### 经典强化学习概念映射到LLM

经典RL中的核心概念可直接映射到语言模型领域：

| RL概念 | LLM映射 |
|--------|---------|
| Agent (智能体) | 语言模型 |
| Environment (环境) | 任务+数据+评分规则 |
| Action (动作) | 生成文本响应 |
| Reward (奖励) | 环境反馈信号（如+1胜，0负） |
| Trajectory (轨迹) | 完整的一次交互回合记录 |

智能体的目标是在时间上最大化累积奖励，需要平衡探索(exploration)与利用(exploitation)。

### LLM训练范式演进

标准LLM训练分三阶段：
1. **预训练(Pretraining)** — 海量互联网文本，模型学会文本补全，但不可用
2. **监督微调(SFT)** — 对话示例，模型学会遵循指令，本质是统计模仿
3. **RL对齐** — PPO等技术对齐人类偏好

关键转变：预训练的增长正在放缓，需要新的扩展方式。

#### DeepSeek-R1与OpenAI o1的启示

- OpenAI o1表明RL训练能让模型有效使用Chain-of-Thought (思维链)，且性能随RL训练计算量和测试时思考时间持续提升
- DeepSeek-R1揭示：用SFT教模型推理需要大量人工数据，成本过高；改用RLVR和GRPO算法，更简单且有效

### RLVR：强化学习与可验证奖励

核心范式：
1. 模型接收问题，生成推理过程(reasoning trace)和答案
2. 答案与正确答案比对验证
3. 奖励信号用于RL训练

更广义的理解：任何结果可自动验证的任务（正确答案、游戏胜利、工具调用成功）都可作为训练信号。

**RLVR与SFT的根本区别**：
- SFT：从精选示例中学习，输出贴近示例分布——受人类示例天花板限制
- RLVR：从预训练分布出发探索不同轨迹，学习最大化奖励的路径——可发现人类未知的策略

### Verifiers库详解

Verifiers是Trim Length团队开发的开源库，用于将RL环境构建为软件制品。

**提供的环境类型**：
- 单轮环境(Single-turn) — 如反转文本(reverse text)
- 多轮环境(Multi-turn) — 如双重检查数学(double check math)
- 工具环境(Tool) — 模型可调用Python函数定义的工具
- MCP环境 — 自动连接Model Context Protocol服务器
- 有状态工具环境(Stateful Tool) — 工具在rollout期间保持持久状态
- 递归LLM(Recursive LLM) — 语言模型可递归分解输入上下文

**核心架构**：
- `load_environment` — 环境入口，包含所有设置逻辑
- `XMLParser` — 解析模型响应中的特定标签
- `Rubric` — 加权奖励函数的集合
- 抽象模型服务，兼容OpenAI API端点（可用vLLM接入本地模型）

**训练集成**：内置trainer，同时集成Prime RL、SkyRL等框架。

**环境中心(Env Hub)**：社区共享RL环境的平台，旨在对抗环境碎片化——当前环境常被锁定在特定训练栈中，难以复用。

### 井字棋实验：从新手到大师

#### 初始设置
- 模型总是执X先手，在`<move>`标签内输出0-8的移动
- 对手随机下棋
- 简单的奖励函数：胜+1，负0，格式正确+0.2

#### 逐步改进环境设计
1. **交替先手** — 让模型有时先手有时后手，训练更全面
2. **可控对手技能** — 引入Minimax算法作为最优对手，但通过`random_move_prob`参数控制其随机走子概率；训练初期对手太强会导致模型永远赢不了，无法学习
3. **推理思维链** — 添加`<think>`标签，鼓励模型在给出最终答案前产生思考过程
4. **无效走子处理** — 不再立即判负，而是继续游戏并给予-0.1惩罚，确保小模型仍能获得学习信号

#### 噪声控制
- 确定性种子：每个数据集示例设固定种子选择先手，每回合派生特定种子，保证相同局面下对手行为一致
- 分层采样(Stratified Sampling)：确保每个batch包含均匀分布的对手技能水平，避免因随机采样导致的奖励方差过大

#### 模型评估

| 模型 | 格式遵循 | 棋力 |
|------|---------|------|
| GPT-5 mini | 优秀 | 良好但非完美 |
| LM2 (Liquid AI) | 困难，频繁无效走子 | 很弱，偶尔赢随机对手 |

#### 训练流程

**SFT阶段**：
- 用GPT-5 mini生成200局合成数据，过滤掉输掉的棋局
- 用Prime RL训练，仅需单GPU数分钟
- 结果：格式接近完美，无效走子大幅减少

**RL阶段（GRPO）**：
- 使用Verifiers Trainer，2块GPU（1推理+1训练）
- 对手随机走子概率20%-70%
- 关键发现：batch size >= 256是训练稳定的底线

**RL训练结果**：
- 模型碾压随机对手
- 对最优对手约70%胜率
- 无效走子降至接近零

#### 推向完美

进一步改进：
- 提高对手技能（随机走子概率0%-25%）
- 提高温度(temperature)鼓励探索新策略
- 经历探索期：初始奖励显著下降（模型尝试随机新策略），随后恢复并超越之前的高点
- 最终结果：**井字棋大师**，对最优对手的表现超越GPT-5 mini

### 关键经验教训

1. **Batch Size**：大=慢但稳定；小=不稳定，可能强化次优策略，甚至模型崩溃
2. **环境偏见**：Minimax算法在多个最优走法中总是选第一个——模型实际上在记忆特定对手，而非学习通用策略
3. **模型选择**：从非推理模型出发训练成推理模型，优于从已有推理模型开始（后者思维链过长，在有限资源下被截断）
4. **实际评估**：不要只看程序化指标，用模型实际完成任务来评估
5. **耐心训练**：开始时检查错误和稳定性，之后停止监控——RL需要时间，持续监控会让人过早终止

## 关键引用
> "In SFT, the model learns from curated examples and its completions tend to stay close to the distribution of those examples. In RLVR, the model explores different trajectories from its pretraining and learns to favor the ones that maximize rewards. The model is no longer limited by the quality of human examples — through trial and error, it can discover more efficient reasoning strategies."

> "Pretraining no longer seems to be enough to keep improving model quality at the same rate. We need a new way to scale."

> "If you can define a clear reward signal, you can build an environment and train a small specialized model to beat a large closed model on a specific task at a fraction of the cost."

> "We did not just show the model how to play — we gave it a space to play and guided it through reward."

## 与其他知识的关联
- 相关概念：[[强化学习与可验证奖励]]、[[GRPO]]、[[Verifiers库]]、[[语言模型强化学习环境]]
- 相关实体：[[Deepset]]
- 相关主题：[[LLM强化学习训练]]

## 待深入问题
- RLVR能否扩展到更复杂的博弈（如国际象棋、围棋）？计算成本如何？
- 环境偏见问题在更复杂任务中如何检测和消除？
- GRPO相比PPO在更大规模任务上的表现差异如何？
- 小模型在特定任务上击败大模型的边界条件是什么？
- Verifiers库的多工具环境和MCP环境的实际训练效果如何？
