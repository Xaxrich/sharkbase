---
type: video
bv: BV1Sef8BmEU3
title: "Vibe Code实战：8小时马拉松！顶级AI开发者现场演示"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1Sef8BmEU3
date: 2026-04-30
duration: 464分钟
tags: [Vibe Coding, Agent原生架构, 复利工程, AI编程工作流, 非技术者构建]
concepts: [复利工程, Agent原生架构, Vibe Coding, 自主循环开发]
entities: [Easonlee的AI笔记]
topics: [LLM-Agent工程实践]
---

# Vibe Code实战：8小时马拉松！顶级AI开发者现场演示

## 一句话摘要
Every 举办的8小时直播马拉松，汇聚全球顶级 vibe coder 现场演示 AI 原生开发工作流，揭示从"非技术者构建"到"自主循环开发"的范式跃迁。

## 核心观点

- **Vibe Coding 已跨越原型阶段，进入生产可用**：Portola 的 iOS 应用 Toin（数十万用户）核心功能完全由 Claude Code 编写，设计师甚至直接提交 PR
- **复利工程（Compound Engineering）是核心方法论**：规划→执行→审查→复利积累，每轮迭代都让 AI 更懂你的代码库和偏好
- **非技术者可以构建真正可用的软件**：Ben Tossel 用 766 条消息重建了完整的广告平台，关键不是编码能力而是"引导 Agent 的能力"
- **多 Agent 协作是效率倍增器**：Opus 做工程经理编排 Codex 做具体编码，比单 Agent 循环更高效
- **Voice-first 工作流正在取代打字**：Monologue 等语音工具让上下文输入的带宽提升数倍，更长的 prompt 意味着更好的输出

## 详细笔记

### 第一部分：Dan Shipper — Agent 原生应用 Proof

Dan 展示了他用 Claude Code 在两周内、会议间隙构建的 agent 原生 Markdown 编辑器 **Proof**：

- **人机共写归因**：文档中紫色代表 AI 写的内容，绿色代表人类写的，一眼看出谁写了什么
- **内置 Agent**：可以运行"every 风格指南审查"，Agent 自动按编辑规范修改文档
- **Agent Presence**：Claude Code 或 Codex 等外部 Agent 可以连接到 Proof，实时在文档中编辑，用户可以跟随 Agent 的光标滚动

Dan 同时展示了 **Anecdote**——一个 agent 原生健康应用，核心就是一个聊天 Agent 连接 Apple Health 数据。因为 agent 原生架构的**粒度性**，即使没有"清除所有评论"的功能，也能通过口头指令让 Agent 逐个操作 UI 完成任务。

### 第二部分：Ben Tossel — 非技术者的痛觉阈值

Ben 不会写代码，但构建了大量实际产品。核心洞见：

- **痛觉阈值是 vibe coding 的关键**：你愿意在挫折循环中待多久，决定了你能构建什么
- **"这是我的错，不是 Agent 的"**：当卡住时，反思自己给 Agent 的指令是否足够清晰，而非抱怨 Agent 笨
- **验证策略**：让 Agent 自己使用浏览器测试、写测试、检查数据库连接，而不是人工复制粘贴控制台日志
- **从 no-code 到 vibe coding 的延续**：Webflow 是前端、Zapier 是路由、Airtable 是后端——概念模型相同，只是抽象层变了

他用 766 条消息重建了 Ben's Bites 的整个广告平台（原为 Bubble 构建），包括 Supabase 实时数据库、订单系统等。

### 第三部分：Ash Mals — 关系智能与个人 Agent 套件

Ash 展示了 **ash.ai**——一个个人 Agent 生态系统：

- 所有项目、模板、目标追踪都整合在一个 Next.js 站点中
- Agent 通过 Slack webhook 接收信息，可以添加引用、追踪目标完成情况
- 贡献图（contribution graph）可视化每日习惯追踪
- 神经树突式的关系网络可视化——2D 网络图很难做好，3D 可能是未来
- 尝试用 Remotion（视频生成框架）将网络可视化做成动画视频

### 第四部分：Ryan Carson — Compound Product 自主产品循环

Ryan 在直播当天早上构建了 **Compound Product** 开源框架，核心思想：

- **Phase 0**：每日 cron job 从数据库拉取用户数据，让 Opus 写一份"VP 产品"报告
- **Phase 1**：Bash 脚本自动分析报告，生成 JSON 格式的改进建议
- **Phase 2**：Agent 自动创建 feature branch，写 PRD，分解为原子级用户故事
- **Phase 3**：Ralph Loop 循环执行——挑任务→实现→质量检查→失败则修复→通过则提交→更新进度
- **三级记忆系统**：长期记忆（训练进模型）、中期记忆（AGENTS.md）、短期记忆（progress.txt，当前循环的陷阱和教训）

核心洞察：人类团队本质上也是循环——起床、看数据、决定做什么、执行、睡觉。Agent 团队也应该如此。

### 第五部分：Every 内部团队 — 从 PPT 到编辑工作流

- **Natalia & Natesh**：构建了 Every PPTX 插件，将制作演示文稿从数天压缩到15分钟。Claude Code 直接生成带 Every 设计规范的 PPT，包括 AI 生成的插图
- **Katie Parrott**：作为非技术写作者，用 Claude Code Desktop App 的下拉菜单替代终端导航。使用 compound engineering 插件进行代码审计，让 Agent 用"五岁小孩能懂"的语言解释技术问题

### 第六部分：Nat Eliason — Teagan 与 24/7 Agent 编排

Nat 展示了 **Teagan**——一个 AI 原生内容营销 Agent，以及他的完整工作流：

- **Conductor**（GUI 替代终端）：管理多个 worktree，一键启动 dev server，Opus 审查 Codex 的工作
- **Claudebot**：通过 Telegram 与 Mac Mini 上的 Claude Code 对话，可以语音发指令。Opus 做工程经理，Codex 做具体编码
- **自动 PR 审查循环**：Claude 审查自己的审查，创建后续 issue，实现需要实现的部分，关闭 PR 时自动处理后续 issue
- **夜间用户行为报告**：凌晨 2 点拉取用户对话记录，分析痛点，自动修复 bug，改进建议写进 Google Doc

### 第七部分：Tina He — Vibe Coding 作为创意实践

Tina 的核心论点：**vibe coding 不只是工具，更是自我表达和创造乐趣的新方式**。

- 构建了一个仿古 Mac OS 风格的个人操作系统网站，含交易应用、图像增强、数据标注等小工具
- "Corporate Translator"——将职场愤怒翻译成得体的商业语言
- 主张 90% 的 AI 用于工作，10% 用于创造快乐——成本低于一杯咖啡，却能让人微笑
- 推荐使用 Context7（MCP 服务器）了解最流行的技术栈

### 第八部分：Paola — 生产级 Vibe Coding

Portola 的 iOS 工程师 Paola 挑战了"vibe coding 只能做原型"的偏见：

- **Toin**（AI 伴侣应用，数十万用户）的核心功能——商店系统、星球自定义、Token 动画——全部由 Claude 编写
- SpriteKit 动画从 prompt 到生产级只用了5分钟，效果甚至超过了 Figma 中的原型
- **关键设置**：13 个 Skills（领域知识）、Hooks（自动护栏）、MCP 集成（GitHub/Linear/Sentry/Figma/PostHog）
- **Agent 分工**：Opus 做逻辑审查，Sonnet 做模式审查；Agent 自动 shepherd PR 直到工程师审查时已是良好状态
- **设计师也能提交 PR**——非工程师也能向生产环境推送代码

### 第九部分：CJ (10x) — Flowy 可视化规划工具

CJ 构建了 **Flowy**——一个本地图表工具，JSON 文件直接存于项目目录：

- 在 Claude Code 规划时用可视化流程图替代 ASCII 图，大幅提升 Agent 理解准确度
- 流程图和 UI 模型图作为 Skills 提供给 Claude，让它直接读取 JSON 生成对应界面
- 偏好 Skills 而非 MCP——上下文膨胀更少，同等能力
- 主张 mono repo 架构：全栈开发避免前后端协调瓶颈

### 第十部分：Google AI Studio — 从截图到可交互应用

Logan 和 Amar 展示了 Google AI Studio 的新能力：

- **Figma 到可交互原型**：截图粘贴 + Figma 插件导出 JSON，一键生成可交互的实时原型
- **CSV 到交互式可视化**：上传 YouTube Shorts 数据，自动生成交互式仪表盘，甚至可以一键生成同类视频
- **多人协作 Figma Jam 克隆**：一张截图 one-shot 生成可多人使用的白板应用
- 目标用户：非终端用户和轻度构建者，与 Cursor/Cloud Code 互补

### 第十一部分：Jeffrey Lit (Notion) — Notion 作为 Agent 看板

Jeffrey 展示了用 Notion 管理多个 Claude Code 实例的工作流：

- 任务卡片驱动：从 Notion 看板拉取任务 URL，Claude Code 自动规划、构建
- **红卡机制**：Agent 需要人类决策时将卡片标红，人类在评论区回复后 Agent 继续
- 语音笔记→结构化任务：在手机上录语音，Notion AI 自动填充看板
- **Quiz 自测**：每个 PR 完成后生成理解测试题，确保人类真正理解了变更内容——防止"AI 生成→人类盲审"的陷阱
- 核心原则：AI 向人类输出应该是"总统每日简报"级别的高质量、高信息密度

### 第十二部分：Kevin Rose & Ken — 复利工程深入

Ken（Cora GM）和 Kevin Rose 对谈复利工程：

- **复利部分**是多数人忽略的关键：从每次错误中提取教训，自动生成 markdown 文档存入 docs/ 目录，后续规划和审查时自动检索相关教训
- Kevin 的工作流：用 Deep Wiki 理解 GitHub 仓库→生成 NotebookLM 播客→2 倍速收听→7 分钟掌握一个工具
- **v0 先行**：Kevin 先在 v0 中原型化 UI 感觉，确认"这东西必须存在"后再进入 Claude Code 正式构建
- **DHH 审查员**：Ken 的插件中有模拟 DHH 风格的审查 Agent——强烈观点的"桌上导师"

### 第十三部分：Tori (Anthropic) — Claude Code 内部视角

Tori 分享了 Claude Code 团队的工作方式：

- **"解除模型束缚"**（unhobbling the model）是核心目标——模型本身有潜力，产品要释放它
- **Ask User Question Tool**：让模型在不确定时主动提问，而非猜测
- **Tasks 系统**（即将发布）：替代 TODO，支持跨会话、跨 Agent 的持久化任务，带依赖关系
- **删除代码是必要的修行**：模型每三个月就更强，曾经需要的复杂编排代码现在可以删除，让模型原生完成
- **赛跑至顶**（Race to the top）：不断设定更高的产品质量标准，因为竞争对手可以复制功能点但无法复制方向向量

### 第十四部分：Naveen — Monologue 语音优先工作流

Naveen 展示了 Monologue 的核心特性和即将发布的 iOS 版：

- **Modes**：按应用自动激活不同转录模式（Cloud Code 模式、消息模式等）
- **Auto-send**：录制完毕自动发送到光标位置，真正 hands-free
- **Paste last transcript**：快捷键粘贴上一次转录，解决 Cloud Code 和 Codex 同时使用的问题
- **iOS 版**（2月9日目标）：与 Mac 版 modes/scores 同步，widget 快速录制
- **Notes 功能**：录制→后台转写→生成摘要+转录
- **未来愿景**：Monologue 根据你的编辑自动学习，逐步适配你的语言习惯

关键数据：p90 用户平均每次输入 400 词，中位数 48 词——深度用户确实在"对 Agent 说话"。

### 第十五部分：Yash — 逆向工程学习法

Yash（Sparkle GM）分享了他的独特学习方法：

- **逆向工程 Mac 应用**：一个 prompt 就能拆解 ChatGPT/Spotify 等应用的架构、框架、API 端点
- 用 Claude Code 分析 .app 包内的文件结构，生成完整的"拆解报告"存为 markdown
- 学习十亿美元公司的工程决策：为什么 ChatGPT 用 LiveKit？为什么 Spotify 的音频框架用原生而 UI 用 Web？
- **Agent Watch**：自建工具监控多个 Agent 运行状态，保持 flow state
- 主张"导演方法论"：先拍摄（实现功能），后期再剪辑（打磨设计），不必一开始就追求完美

### 第十六部分：Brooker — Claude Code 作为研究助理

Brooker 展示了金融研究场景的 Claude Code 用法：

- 一个命令生成交互式 Streamlit 仪表盘（Meta 财报预览），包含收入指引、Beat/Miss 追踪、迷你 Excel 模型
- 数据来自 Daloopa MCP + 本地转录文件 + API
- 将 prompt 存储在 GitHub 仓库中，版本化管理，避免 ChatGPT 的 800 字符限制
- 过去5小时的工作现在20分钟完成，且输出是交互式的而非静态 PDF

## 我的评注

- **赞同**：这个直播清晰地展示了一个范式跃迁——从"AI 辅助编码"到"AI 作为工程团队"。Nat Eliason 的 Claudebot 设置（Opus 做经理、Codex 做程序员、夜间自动审查用户反馈）不再是概念验证，而是实际运行的工作流。Jeffrey 的"Quiz 自测"理念尤其重要——它是防止人类在 AI 产出面前自我欺骗的关键机制。
- **质疑**：几乎所有演示者都提到了"痛觉阈值"和"挫折循环"，但很少讨论**可持续性**。Katie 是唯一提到倦怠管理的人。当 Agent 可以 24/7 运行，人类的工作节奏是否会被反向绑架？另外，多人提到"我不看代码"，但 Yash 明确反对——"你需要对每一行代码负责"。这种张力尚未解决。
- **与 AI 工程实践的关联**：这个直播验证了知识库中已有的几个核心概念——[[复利工程]]的"从错误中学习并持久化"机制被反复提及，[[Agent原生架构]]的"对等性"和"粒度性"原则在 Proof 和 Notion 集成中体现得淋漓尽致。新增的重要概念是**自主循环开发**——从 Ralph Loop 到 Compound Product，Agent 不再只是工具，而是可以自主运行、自主修复、自主改进的系统。

## 与其他知识的关联

- 相关概念：[[复利工程]]、[[Agent原生架构]]、[[上下文工程]]、[[任务即子Agent]]、[[内部dogfooding]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题

- 当 Agent 可以 24/7 运行，人类如何设定健康的参与边界？"永远在线"是否会导致新型倦怠？
- Skills/Hooks/MCP 的最佳维护策略是什么？随着模型能力提升，哪些应该删除、哪些应该保留？
- "复利积累"的边际收益是否递减？100 个 lessons-learned 文件和 1000 个的区别有多大？
- 语音优先工作流对非英语用户的适配程度如何？中文语音转 prompt 的准确度能否支撑同样的工作流？
- 多 Agent 协作中，Opus→Codex 的编排模式是否是最优的？未来是否会出现更精细的 Agent 分工体系？
