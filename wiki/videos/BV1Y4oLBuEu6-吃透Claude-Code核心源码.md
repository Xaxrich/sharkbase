---
type: video
bv: BV1Y4oLBuEu6
title: 吃透Claude Code核心源码-架构设计与工程细节全解析
uploader: 小韩
url: https://www.bilibili.com/video/BV1Y4oLBuEu6
date: 2026-04-27
duration: 110:00
tags: [Claude Code, Agent架构, 驾驭工程, 源码解析, 工具系统, 安全, ReAct循环, 记忆管理, Agent协作]
concepts: [驾驭工程, ReAct循环, Claude-Code架构, MCP Server]
entities: [小韩]
topics: [LLM-Agent工程实践]
transcript: .b2t/transcripts/original/吃透-Claude-Code-核心源码-架构设计与工程细节全解析-20260427-chunked.txt
---

# 吃透Claude Code核心源码-架构设计与工程细节全解析

## 一句话摘要
以驾驭工程(Harness Engineering)的视角，从同心圆架构出发，深度剖析 Claude Code 开源源码的 Query Engine、工具系统、Agent协作和安全机制，揭示其"克制式"设计哲学与工程最佳实践。

## 核心观点
- Claude Code 不只是一个 AI 编码工具，而是 Harness Engineering（驾驭工程）的最佳参考实现——它展示了如何构建一个完整的 Agent 工程架构
- Claude Code 的核心设计哲学是"克制"：52个内置工具经三层过滤后仅约20个可见给模型；五种Agent协作模式大部分被 feature flag 隐藏；宁可少记也不乱记——与竞争对手的"做加法"策略形成鲜明对比
- System Prompt 采用静态分割符(Static Separator)策略——将不变内容前置、动态内容后置，最大化利用模型端 Token 缓存机制，成本可降至原来的十分之一
- Agent协作存在五种模式：通用SubAgent（空白起点）、SubAgent（专有角色）、ForkAgent（克隆全上下文）、协调者模式（做减法）、Team模式（数字员工协作）；目前仅前两种开放
- 安全没有"一招先"，只能在每个可能的漏洞点层层设防——Claude Code 在工具可见、工具执行、工具结果三个阶段都做权限检查，体现了纵深防御原则

## 详细笔记

### 一、Claude Code 的本质与 Harness Engineering 语义演变

小韩开篇强调 Claude Code 不是 AI 编码工具，而是一套完整的工程架构。理解它的关键是 Harness Engineering（驾驭工程）这个概念，但该概念的语义经历了多次演变：

1. **测试领域起源**：Harness 最初指测试领域的测试桩(test harness)
2. **AI领域扩展**：被 Anthropic、OpenAI、LangChain 等引入 AI 领域
3. **OpenAI 三大支柱**：OpenAI 第一篇论文定义 Harness 的三大支柱——Engineering（工程）、Constraints（约束）、Garbage Collection（垃圾回收）
4. **概念泛化与混乱**：后来业界将 "Agent = Model + Harness" 泛化，Harness 变成了"模型以外的一切"——引擎、工具、记忆、约束、管控全都包进去，概念极为混乱
5. **Claude Code 作为最佳实践**：不管概念多混乱，Claude Code 就是 Harness 的最佳参考实现，看懂它的架构就能理解 Harness

### 二、同心圆架构：从 Harness 视角看 Claude Code

小韩的架构图不是按代码结构画的，而是按 Harness 的同心圆逻辑画的：

| 层次 | 名称 | 比喻 | 核心组件 |
|------|------|------|----------|
| 核心 | Model API | 大脑 | LLM 本身，被驾驭的对象 |
| 第一圈 | Query Engine | 神经系统 | ReAct循环、Prompt工程、记忆管理、Token管理 |
| 第二圈 | Tool System | 手脚 | 基础工具、MCP工具、Skills系统、Agent工具 |
| 第三圈 | Agent Collaboration | 团队协作 | SubAgent、ForkAgent、协调者模式、Team模式 |
| 外围 | Security | 基础设施 | 权限机制、沙箱、防注入、审计日志 |

### 三、Query Engine 详解

#### 3.1 ReAct 循环

Claude Code 的核心循环基于 ReAct (Reasoning + Acting) 模式：

**State 结构体**维护的全局状态：
- `message list` — 最终发给模型的消息列表，随循环不断追加
- `tools list` — 所有可用工具列表
- `turn count` — 当前对话轮次
- `compression status` — 是否需要压缩、压缩失败次数
- `termination flags` — 是否有人终止等

**循环流程**：
1. 构建初始 system prompt + user prompt → message list
2. 发送请求给模型
3. 判断模型返回结果类型：
   - **文本响应** → 直接退出循环，返回结果
   - **工具调用** → 进入工具执行
4. 框架（非模型）执行具体的 tool call
5. 工具结果作为 `tool result` 追加到 message list
6. 检查是否需要 Token 压缩，若需要则执行压缩
7. 回到步骤2，再次请求模型（此时模型已知道上一轮工具结果）

**关键认知**：所有模型本身没有工具能力，模型唯一能做的是"吐出"工具调用的指令，真正的工具执行由工程框架完成。

#### 3.2 Context Engineering（上下文工程）

与过去做 Prompt Engineering 不同，Agent 时代的上下文工程有两个可控点：

1. **进入循环前的 System Prompt** — 工程上完全可控
2. **Hook 机制** — 在循环中的任意步骤插入 Hook，可以修改 message list

**System Prompt 的动态组装**（`buildEffectiveSystemPrompt` 函数）：
- 不是简单读一个 system 文件，而是一个庞大的构造器，从各处拉取片段拼接
- 有优先级概念：某些模式会完全替换 system prompt，SubAgent 也会替换
- 用户可在工程中自定义追加

**静态分割符(Static Separator)策略** — 极具工程智慧的缓存优化：

组装顺序从最静态到最动态：
1. **最静态**：身份信息、系统规则、执行安全（写死在不同文件中）
2. **中间层**：Agent 工具列表（取决于当前模式）、Skill 加载、CLAUDE.md、Memory、MCP 服务器指令（服务挂了就不添加）
3. **最动态**：Git 状态、日期、用户消息

**原理解释**：大模型推理是线性结构——从前往后依次处理。模型端会做 Token 缓存：前面相同的部分可以命中缓存，只需计算新增部分。将静态内容前置，意味着每次请求的前缀高度一致，缓存命中率高。缓存命中的 Token 价格仅为原来的十分之一。

#### 3.3 Token 管理（三层压缩机制）

| 层次 | 机制 | 说明 |
|------|------|------|
| 第一层 | 默认剪裁 | 每轮执行，把十轮以前的 tool result 直接裁掉，大幅控制 token 增长 |
| 第二层 | 基于磁盘重建的异步压缩 | 当 token 使用超过一定比例时，异步将上下文存盘并后台压缩；真正到达阈值时从磁盘重建，发现已压缩好的内容直接加载，大大节省等待时间 |
| 第三层 | 全量摘要压缩 | 如果磁盘重建时后台未压缩好，则同步进行全量摘要压缩——非常慢，因为需要大量输出 Token 生成摘要 |

**结构化压缩**：压缩不是让模型自由总结，而是要求遵循特定 JSON 结构——用户问题、任务清单、澄清内容等标准化字段，使压缩高效且可解析。

#### 3.4 记忆管理

Claude Code 的记忆体系体现了"克制"原则：

**当前开放的记忆能力**：
- 在 system prompt 中声明"你拥有持久化记忆系统，可以用 write 工具写记忆"
- 触发条件：随时间推移主动写（但模型遵从度低）、用户明确要求记住/删除时立即执行
- 不足：触发条件不明确，模型很少主动记忆

**Extended Memory（需特殊开关）**：
- 每次 React 循环完成后的 stop hook 触发
- 将当前 agent 全部 message list 交给后台程序进行记忆提取
- 更主动的记忆提取，但可能记错或记无关内容

**Auto Dream（实验性，需内部开关）**：
- 仿生学机制：模仿人类睡眠时大脑整理记忆的过程
- 每24小时触发一次，在闲时执行
- 扫描工作空间所有 memory 和 CLAUDE.md
- 识别需合并的内容、整合上下文、去重、提炼精华、抽象
- 清理噪声、解决冲突、删除不需要的内容
- 对应 OpenAI 论文三大支柱中的 Garbage Collection
- 决定项目空间能否持久使用而不劣化的核心能力

### 四、工具系统详解

#### 4.1 三层过滤机制

Claude Code 内置 **52个工具**（含实验性），但经三层过滤后 agent 可见不到20个：

| 过滤层 | 机制 | 效果 |
|--------|------|------|
| 第一层 | Feature Flag 过滤 | 隐藏实验性功能（Auto Dream、ForkAgent等），过滤掉约30个 |
| 第二层 | 权限模式过滤 | 根据当前运行模式（read-only、plan等）过滤工具 |
| 第三层 | 项目规则过滤 | 企业/项目自定义策略过滤 |

即使工具通过三层过滤可见，最终调用时还要过权限检查。

#### 4.2 工具分类

**基础工具（Base Tools）**：
- **Shell/Bash/PowerShell** — Claude Code 运行的核心，一切通过命令行执行
- **文件系统** — Read、Write 工具
- **搜索** — 仅用 grep（基于文件名和内容搜索），无向量数据库、无 RAG！
- **Web** — Web Search 和 Web Fetch（常有权限问题）
- **Agent 工具** — 用于 Agent 间协作

**MCP 工具**：
- 沙箱本身也通过 MCP 实现
- 动态加载：不将所有 MCP 工具描述预加载到 system prompt，而是按需通过 description 让 agent 发现
- 解决了 MCP 工具描述过长占用上下文的问题

**Skills 系统**：
- 作为 subprocess 注册到 system prompt
- 只注册 name 和 description，真正使用时才加载
- 优先级加载机制：项目 `.claude/skills` > 用户目录 > `/etc/` 下的配置

### 五、Agent 协作机制

#### 5.0 异步执行基础（Task 机制）

Claude Code 的异步基于 `createTask` 工具：
- 主 Agent 在 React 循环中调用 createTask，创建子任务（含 task ID、状态、描述）
- 分配给 SubAgent 后台执行，createTask 立即返回
- 主 Agent 继续 Loop 循环
- 子任务结果放入队列
- 主 Agent 在 stop hook（完成当前轮结果输出）后从队列读取子任务结果，触发下一轮处理
- 异步 Shell 命令也通过同样的 Task 机制执行

#### 5.1 五种协作模式

| 模式 | 状态 | 特点 | 上下文 | 适用场景 |
|------|------|------|--------|----------|
| 通用 SubAgent | 已开放 | 空白起点，新 system prompt | 全新构建 | 并行处理多文件、探索任务 |
| 专用 SubAgent | 已开放 | 专有 system prompt + 工具集 + 轻量模型 | 全新构建 | 代码探索、规划、验证等专项 |
| ForkAgent | 开开关可用 | 克隆主 Agent 全部上下文 | 继承完整历史 | 需要前文上下文的子任务 |
| 协调者模式 | 实验性 | 主 Agent 只编排不执行 | 新 system prompt | 大任务编排探索 |
| Team 模式 | 实验性 | 独立数字员工协作 | 完全隔离 | 多角色协作 |

**通用 SubAgent**：最常见的使用方式。创建全新的空白 Agent，需要重新生成 system prompt，上下文中只有任务描述。好处是不受前文影响，上下文成本低；缺点是从零开始。

**专用 SubAgent**：针对特定场景预定义角色的 Agent。Claude Code 内置了探索性 Agent（只读探索代码库）、Plan Agent（规划）、Query Agent（查询）、验证 Agent（只做验证，故意设为"杠精"角色不遵从主 Agent 的假设）等。它们有专有的 system prompt、受限的工具集（如探索 Agent 没有写权限）、切换到更轻量的模型——实现专项能力封装和成本节约。

**ForkAgent**：不是创建新 Agent，而是克隆主 Agent 当前的全部 message list，在末尾追加新任务让它在后台跑。好处是子 Agent 完全知道之前信息，可直接开工；且利用服务端 Token 缓存，输入 Token 只需花十分之一价格。缺点是上下文过长，不适合需要上下文隔离的场景（如验证 Agent）。

**协调者模式（Coordinator）**：做的是减法而非加法。主 Agent 被强制设置为"只能编排不能执行"，所有工具必须通过 Task 分发给 Worker 执行。Worker 也被严格限制：不能创建新 SubAgent；后台任务只有 read 和 grep 权限；只有前台任务才有文件编辑权限。体现了 Claude Code 的克制设计理念——与竞争对手不断做加法不同，Claude Code 一直在克制和收缩。

**Team 模式**：真正的"数字员工"协作，超越了传统 Agent 协作。每个 Team Member 是独立的 Claude Code 实例：有自己的工作空间、记忆、技能。协作方式：Team Leader（经理角色）接收整体任务并分配；给每个数字员工分配"信箱"；通过"邮件"方式通信（不再是内存/上下文传递）；建立通讯总线，有公共区域和私聊通道。但该模式目前连入口都没有，完全实验性。

### 六、安全机制详解

#### 6.1 六大设计原则

| 原则 | 说明 |
|------|------|
| 纵深防御 | 同一件事在多个点设防——工具可见时检查、工具执行时检查、工具结果返回时检查，任一点漏掉都不会被完全击穿 |
| 最小权限 | 默认无权限，每次使用必须授权，授权范围非常有限 |
| 安全默认 | 所有默认策略全是拒绝，必须有用户显式动作才开放权限 |
| 零信任模型输出 | AI 说的所有话都不信，AI 不能绕过安全直接执行 |
| TOCTOU 防御 | 防御时间线和并发下的检查时刻与使用时刻不一致的安全漏洞 |
| 企业可控性 | 严格的权限优先级，企业策略最高，下级无法覆盖 |

#### 6.2 四大安全机制

**权限漏斗**：
- 工具是否能用，取决于从上到下的优先级链：
  - 企业规则（最高优先级，不可覆盖）
  - Ask 规则（需用户确认）
  - Auto 规则（可自动放行，但必须用户显式设置）
  - 权限模式（默认全部禁用）
- 隐藏功能：内部小模型分类器判断哪些工具执行是安全的（未开放）
- 权限被拒时会给模型友好提示让其换方法，失败累积多次时弹出交互让用户确认

**沙箱**：
- 默认不开启，需手动安装环境并打开
- 网络隔离：在沙箱网络层直接拦截禁止的域名和网站（无法通过写 Python 脚本绕过）
- 目录限制：只允许修改指定目录（在操作系统级限制，无法通过 Node.js 逃逸）
- 配置文件隔离：安全配置文件在沙箱内不可见，操作系统级无权限
- 阻止仓库逃逸

**提示注入防控**：
- 没有通用的一招先方案，每个攻击方法都有对应的防御规则
- 环境变量 Key 清除：启动命令时直接清除环境中的 API Key，防止恶意代码获取
- Skill 路径随机化：加载 Skill 时路径后加随机串，防止攻击者预先在特定路径放置恶意 Skill 文件
- 路径遍历防御：专门防止 `..` 方式绕出限制目录
- 核心原则：永远不依赖模型判断来决定是否安全

**审计日志与可观测性**：
- 全功能使用日志、决策日志（每次权限通过/拒绝的完整记录）
- 分布式链路追踪（Agent 动作、子 Agent 动作、沙箱日志全链路追踪）
- 精确成本追踪（每个 Token、每个 Session、缓存命中 vs 压缩的成本分拆）

### 七、Claude Code 的不足（Harness 的空白）

小韩指出，即便看完了 Claude Code 的源码，Harness 仍有大量空白：

1. **开发 Harness 缺失**：Anthropic 如何用 Claude Code 开发 Claude Code 本身？他们的 Memory 记了什么？日常如何做定期清理？这些迭代流程完全不可见
2. **评估体系缺失**：Harness 第一篇研究论文的核心是评估——Agent 执行对错、稳定性、成本——但 Claude Code 中看不到评估体系
3. **工程基建缺失**：CI/CD、版本管理、安全测试、攻击模拟等构建它的基础设施仍是黑盒

**核心洞察**：Anthropic 给了我们一个切面，但如何构建出这个切面仍一无所知。只能推测，需要自己逐步建立这套东西。

### 八、Q&A 要点

- **RAG 在代码库场景是否需要？** Claude Code 不用 RAG，因为代码库用 grep + 语法树就够了。但企业级大量文档/数据场景下，RAG 仍然必要
- **Claude Code 有隐藏的 LSP 功能**：Language Server Protocol 解析代码结构后做检索，但未开放
- **记忆管理建议**：带时间戳、基于语义做结构化整理（知识用三元组、SOP 用步骤列表），而不是简单压缩
- **企业级身份认证缺失**：所有基于 MCP 的 Agent 系统都面临身份认证难题——Agent 写代码访问外部接口时无法带上身份信息。目前只有阿里的悟空系统通过沙箱+请求拦截+固定认证头解决了这个问题
- **设计哲学对比**：Claude Code 不断做克制和收缩，激发模型自身能力；竞争对手不断做加法、加功能——这是根本的设计思路区别

## 关键引用
> "Claude Code 并不只是一个 AI 的工具，它本身应该是一套非常好的一个工程架构。"

> "安全是没有一招先的。你只能基于已有的攻击手段，一条一条地去知道有哪些安全漏洞，才能去做防控。安全是一个你几乎没法抄作业的东西。"

> "Claude Code 在不断的去克制、不断的去收缩工程的功能，而更好的去激发模型或激发整个能力运行得更顺——这是与竞争对手根本的设计思路区别。"

> "Auto Dream 对应 OpenAI 论文三大支柱中的 Garbage Collection，它是决定项目空间能不能一直持久使用而不被劣化的核心能力。"

## 与其他知识的关联
- 相关概念：[[驾驭工程]]、[[ReAct循环]]、[[Claude-Code架构]]、[[MCP Server]]
- 相关实体：[[小韩]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题
- 协调者模式和 Team 模式何时开放？效果如何评测？
- Auto Dream 机制在实际项目中的效果如何？是否会导致关键信息丢失？
- 企业级身份认证问题如何系统性解决？
- Token 缓存策略在不同 API 代理环境下的可用性如何？
- 评估体系应包含哪些维度？如何量化 Agent 的执行质量？
