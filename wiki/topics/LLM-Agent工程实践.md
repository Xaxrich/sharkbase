---
type: topic
name: LLM-Agent工程实践
tags: [Agent架构, 驾驭工程, 工程实践, Claude Code, LLM应用]
created: 2026-04-27
updated: 2026-04-27
video_count: 1
---

# LLM-Agent工程实践

## 主题概述
探讨如何以工程化方式构建 LLM 驱动的 Agent 系统——从核心循环设计、上下文管理、工具系统、Agent协作到安全机制，关注"驾驭工程"(Harness Engineering)这一核心方法论。

## 核心问题
1. 什么是 Harness Engineering？它与传统的 Prompt Engineering 有何本质区别？
2. 如何设计高效的 ReAct 循环和上下文管理策略？Token 缓存如何最大化利用？
3. Agent 的工具系统应该如何设计？是"多而全"还是"少而精"？
4. 多 Agent 协作有哪些模式？各自适用什么场景？
5. Agent 安全的纵深防御体系如何构建？企业级身份认证如何解决？
6. Agent 系统的评估体系和迭代基建缺失会带来什么问题？

## 综合梳理

### 从 Prompt Engineering 到 Harness Engineering
来自 [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]] 的观点认为，LLM 应用的工程化已从 Prompt Engineering 进入 Harness Engineering 阶段。传统 Prompt Engineering 关注的是单次对话的提示词优化，而 Harness Engineering 需要构建模型以外的完整工程体系——推理引擎、工具系统、记忆管理、安全约束、协作机制。

Harness 的语义本身也在快速演变：从测试领域的 test harness，到 OpenAI 三大支柱（Engineering + Constraints + Garbage Collection），再到泛化的 "Agent = Model + Harness"。Claude Code 是目前该概念的最佳参考实现。

### ReAct 循环与上下文管理
来自 [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]] 的解析揭示了 ReAct 循环作为现代 Agent 标准底层设计的工程细节：

- **State 驱动**：全局状态机维护 message list、tools list、轮次和压缩状态
- **工具执行在框架侧**：模型只产生调用指令，框架负责真正执行——这是 Agent 安全的基础
- **可控点**：system prompt 构造（循环前）和 Hook 机制（循环中）

**上下文管理的关键创新**：
- 静态分割符策略：静态内容前置最大化 Token 缓存命中，成本可降至1/10
- 三层压缩：剪裁（去旧 tool result）→ 异步磁盘重建（后台压缩避免阻塞）→ 全量摘要（最后手段）
- 结构化压缩：要求遵循 JSON 结构而非自由总结，保证压缩质量和可解析性

### 工具系统设计：克制 vs 扩张
来自 [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]] 的分析展现了 Claude Code "克制式"工具设计哲学：

- 52个内置工具经三层过滤后仅约20个对 Agent 可见——Feature Flag 隐藏实验功能、权限模式过滤不可用工具、项目规则按策略裁剪
- 核心工具以 Shell/Bash 为主，搜索仅用 grep——代码库场景不需要 RAG，但企业级文档场景仍需
- MCP 工具和 Skills 系统均采用动态延迟加载——只注册描述、使用时才加载，解决上下文占用问题

这与竞争对手"什么工具都暴露"的策略形成对比。克制设计的核心逻辑是：工具越少，模型的决策空间越集中，执行越可靠。

### Agent 协作的五种模式
来自 [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]] 的梳理呈现了从简单到复杂的协作层级：

1. **通用 SubAgent**：空白起点，新上下文，适合并行处理独立任务
2. **专用 SubAgent**：预定义角色+受限工具+轻量模型，适合专项任务（探索、规划、验证），其中验证 Agent 被故意设为"杠精"角色
3. **ForkAgent**：克隆主 Agent 全部上下文，利用服务端 Token 缓存降低输入成本，适合需前文上下文的子任务
4. **协调者模式**：做减法——主 Agent 只编排不执行，Worker 严格受限（无创建子 Agent 权、后台任务只有 read+grep）
5. **Team 模式**：每个成员是独立 Claude Code 实例，有独立工作空间/记忆/技能，通过"邮件信箱"通信——真正的数字员工协作

异步执行是协作的基础：`createTask` 创建子任务，结果通过队列在 stop hook 时消化。

### 安全：纵深防御而非一招先
来自 [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]] 的安全分析强调：安全没有万能方案，只能在每个可能的漏洞点层层设防。

- **六原则**：纵深防御（每件事多个检查点）、最小权限（默认无权限）、安全默认（默认全拒绝）、零信任模型输出、TOCTOU防御、企业可控性
- **权限漏斗**：企业规则 > Ask规则 > Auto规则 > 权限模式
- **提示注入防控**：针对具体攻击方法逐条设防——Key清除、路径随机化、路径遍历防御
- **企业级身份认证缺失**：所有基于 MCP 的 Agent 系统都面临此难题——Agent 写代码访问外部接口时无法带上身份信息。目前仅有阿里的悟空系统通过沙箱+请求拦截解决

### Harness 的空白
来自 [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]] 的反思指出，即使看完了 Claude Code 源码，仍有大量 Harness 能力不可见：开发 Harness（如何用 Agent 开发自身）、评估体系（Agent 执行质量如何量化）、工程基建（CI/CD、版本管理、安全测试）。这些是后续需要集中精力建设的方向。

## 相关视频
- [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]] — 小韩以 Harness 视角深度解析 Claude Code 架构，涵盖 Query Engine、工具系统、Agent协作和安全机制

## 相关概念
- [[驾驭工程]]、[[ReAct循环]]、[[Claude-Code架构]]、[[MCP Server]]

## 相关实体
- [[小韩]]

## 开放问题
- Agent 的评估体系应包含哪些维度？如何量化执行质量？
- 企业级身份认证在 Agent 场景下如何系统性解决？
- 协调者模式和 Team 模式在实际生产中的效果如何？
- "克制式"设计哲学是否在所有场景下都优于"扩张式"？
- 如何构建"开发 Harness"——用 Agent 开发和迭代 Agent 本身？
- RAG 与 grep/语法树在不同规模知识库场景下的边界在哪里？
