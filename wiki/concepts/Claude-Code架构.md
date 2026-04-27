---
type: concept
name: Claude-Code架构
tags: [Claude Code, Agent架构, 源码解析, Anthropic]
first_seen: 2026-04-27
---

# Claude-Code架构

## 定义
Anthropic 的 Claude Code 开源源码所展现的 Agent 工程架构，被视为 Harness Engineering（驾驭工程）的最佳参考实现。其核心设计哲学是"克制"——通过约束和精简工程功能来激发模型自身能力。

## 核心要点

### Query Engine（神经系统）
- **ReAct 循环**：State 维护 message list + tools list + 压缩状态，循环执行 推理→工具调用→结果追加→压缩→再推理
- **Context Engineering**：`buildEffectiveSystemPrompt` 动态组装；静态分割符策略（静态内容前置、动态后置，最大化 Token 缓存命中，成本降至1/10）
- **Token 管理**：三层压缩——默认剪裁（裁掉10轮以前的 tool result）、异步磁盘重建（后台压缩、到达阈值时从磁盘加载）、全量摘要压缩
- **记忆管理**：克制策略——system prompt 声明可写记忆但触发不明确；Extended Memory（stop hook 后提取记忆，需开关）；Auto Dream（24小时闲时整理，需内部开关）

### Tool System（手脚）
- 52个内置工具，三层过滤后仅约20个可见：Feature Flag → 权限模式 → 项目规则
- 基础工具以 Shell/Bash 为核心，文件系统 Read/Write，搜索仅用 grep（无 RAG）
- MCP 工具动态加载（按 description 发现，不预加载全部描述）
- Skills 系统按优先级加载（项目 `.claude/skills` > 用户目录 > `/etc/`）

### Agent 协作（团队协作）
- 五种模式：通用 SubAgent（空白起点）、专用 SubAgent（预定义角色+工具+模型）、ForkAgent（克隆全上下文+利用 Token 缓存）、协调者模式（主Agent只编排不执行）、Team 模式（独立数字员工协作）
- 异步执行基于 `createTask` 工具，结果通过队列在 stop hook 时消化

### Security（基础设施）
- 六原则：纵深防御、最小权限、安全默认、零信任模型输出、TOCTOU防御、企业可控
- 权限漏斗：企业规则 > Ask 规则 > Auto 规则 > 权限模式
- 沙箱：网络隔离、目录限制、配置文件隔离
- 提示注入防控：Key 清除、Skill 路径随机化、路径遍历防御
- 审计日志：决策日志、分布式链路追踪、精确成本追踪

### 设计哲学：克制
- 工具过滤保持精简而非全部暴露
- 记忆宁可少记也不乱记
- 协调者模式做减法而非加法
- 安全默认全部拒绝

### 不足
- 开发 Harness 缺失（如何用 Claude Code 开发自身）
- 评估体系缺失（Agent 执行质量如何量化）
- 工程基建缺失（CI/CD、版本管理、安全测试）

## 在以下视频中出现
- [[BV1Y4oLBuEu6-吃透Claude-Code核心源码]]（全程深度解析）

## 与其他概念的关系
- [[驾驭工程]] — Claude Code 是该概念的最佳参考实现
- [[ReAct循环]] — Claude Code 的核心循环机制
- [[MCP Server]] — Claude Code 工具系统中的远端工具接入方式

## 相关主题
- [[LLM-Agent工程实践]]
