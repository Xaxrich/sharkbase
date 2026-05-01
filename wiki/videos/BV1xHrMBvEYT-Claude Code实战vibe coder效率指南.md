---
type: video
bv: BV1xHrMBvEYT
title: "Claude Code 实战：如何成为一名10倍效率的vibe coder？"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1xHrMBvEYT
date: 2026-04-30
duration: 33:00
tags: [Claude Code, Cursor, Vibe Coding, AI编码工作流, MCP Server]
concepts: [智能体分工, 微交互设计, 驾驭工程, 思考模式]
entities: [Easonlee的AI笔记]
topics: [LLM-Agent工程实践]
---

# Claude Code 实战：如何成为一名10倍效率的vibe coder？

## 一句话摘要
Chris 展示了他的双工具工作流（Claude Code + Cursor 并行）和六条实战技巧——plan mode、ultrathink、后台任务、MCP 服务器、代码审查工具、语音输入——将 AI 编码从"用一个工具做所有事"升级为"根据任务特性选最合适的工具和模式"。

## 核心观点

- **双工具并行而非择一而从**：Claude Code 和 Cursor 有不同的强项，同时使用比执着于"选一个"效率更高
- **Plan mode 是最被低估的功能**：让 AI 先规划再执行，输出质量至少提升 20%，且提前暴露问题方向
- **`ultrathink` 是 Claude Code 的隐藏关键词**：输入后模型会"更用力地思考"，对复杂问题效果显著，且似乎不显著增加 token 消耗
- **MCP 服务器是给 AI 赋能的正确方式**：Context7 提供最新文档，Supabase MCP 让 AI 直接操作数据库——比手动配置更安全也更快
- **独立开发者的安全网**：Bugbot 和 Cursor 代码审查工具（$40/月）替代了人力 code review，是 solo dev 的"能睡好觉"投资

## 详细笔记

### 工具配置：Claude Code + Cursor 并行

Chris 的工作界面：Cursor 编辑器左侧打开项目文件，右侧终端运行 Claude Code。两个工具同时可用，根据任务切换。

**分配逻辑**：
| 场景 | 选择 | 原因 |
|------|------|------|
| 非常复杂的 Bug | Cursor Plan Mode | 跟进追问能力更强，适合复杂调试 |
| 大规模架构（3-4 个 prompt 搭建整个 app） | Claude Code (Opus) | 长上下文理解能力更好 |
| UI / 动画 / 交互 | Claude Code (Sonnet) | 设计审美略优 |
| 小改动 | 任意 | 两者差异不大 |

### 模型选择策略

- **Claude Code**：Opus 4.1 用于极复杂问题，但用量极其有限（每周额度 3-4 小时即可耗尽）；Sonnet 4.7 用于日常执行
- **Cursor Plan Mode**：GPT-5.1 High 做规划 + Sonnet 4.7 做执行——反直觉的组合。Chris 的假设：GPT-5.1 High 本质上是写作模型而非编码模型，而规划恰恰需要的是"写清楚步骤"的能力，因此写作模型反而优于编码模型

### 实战演示：用 Claude Code 构建动画

Chris 现场演示了用 Claude Code 复刻 Amy 卡路追踪 app 的搜索动画。关键观察：

1. **语音输入生成长提示**：用 WhisperFlow 口述需求，包含完整的动画时序、状态转换、视觉细节——比手写详细 3-5 倍
2. **第一轮输出不完美但可用**：两个 prompt 后动画已基本可运行，继续迭代 10-20 次达到生产级
3. **同模型不同工具输出不同**：Claude Code (Sonnet 4.7) 和 Cursor Plan Mode (Sonnet 4.7 执行) 使用相同模型，但因为 Cursor 先做了规划步骤，首次输出质量反而更高

### 六条实战技巧

#### 1. 始终使用 Plan Mode
- Cursor：切换 Plan Mode，AI 生成详细步骤计划，人工审核后再执行
- Claude Code：按 Shift+Tab 切换到 Plan Mode，同样先规划后执行
- Chris 的判断：Cursor 的 Plan Mode 比 Claude Code 的更成熟——计划更详细、更善于追问
- 效果估计：输出质量至少提升 20%

#### 2. Claude Code 中使用 `ultrathink`
- 输入 `ultrathink` 后关键词变色，表示模型正在"更用力地思考"
- Chris 在 90% 的消息中使用，未发现显著增加 token 消耗
- 推测使响应时间翻倍，但复杂问题收益远大于时间成本

#### 3. 后台任务
- Claude Code 可在后台运行开发服务器：`run the server in the background for me`
- AI 获得服务器日志访问权——调试时无需手动复制粘贴错误信息
- 近一个月新增的功能

#### 4. MCP 服务器
- **Context7**：免费 MCP，提供最新版本的压缩文档，比让 AI 自己爬取 URL 更可靠
- **Supabase MCP**：让 AI 直接操作数据库（创建表、配置安全规则、设索引）。Chris 认为反而可能比手动配置更安全——AI 配置的安全规则比他自己写的更严格。生产环境仍需谨慎

#### 5. 代码审查工具
- Bugbot 和 Cursor 内置审查：对 PR 自动做安全审查和 Bug 检查
- 专门训练用于识别安全问题，比在编辑器里手动让 AI 审查效果更好
- $40/月，Chris 认为是独立开发者最好的投资之一

#### 6. Deep Research 做技术预研
- Claude Desktop（聊天应用）中的 Deep Research 功能：付费 Claude Code 用户有更高额度
- 用法：描述技术问题，AI 搜索 12 分钟文档后给出最佳实践总结
- 用途：新手学习架构方案，有经验者验证实现是否正确
- 研究结果可直接喂给 Claude Code / Cursor 执行

### 给新手的建议

不建议新手直接上 Claude Code / Cursor，推荐先从 Create Anything、v0、Bolt 等低门槛平台开始。等遇到平台能力上限再"毕业"到专业工具——此时已对 AI 协作和 prompt 技巧有基本认知。Create Anything 在移动端设计上目前领先于 Vibe Code 和 Roc。

## 我的评注

- **赞同**：双工具并行的策略比"选一个工具死磕"更务实，与知识库已有的 [[智能体分工]] 思路一致。Chris 的实证方法（让两个工具做同一任务、比较结果）比凭印象选工具更可靠
- **赞同**：Plan Mode 的价值被严重低估。它本质上是在执行前增加了一个"思考"步骤，与 [[思考模式]] 中"不让 AI 直接写成品"的逻辑相通——但 Plan Mode 是工具内建的结构化实现，比在 prompt 里说"先别写"更可靠
- **质疑**：`ultrathink` 的效果描述过于依赖主观感受。"似乎不增加 token 消耗""可能思考时间翻倍"——这些都是猜测而非测量。Claude Code 的 extended thinking 机制确实会在系统层增加推理 token，对 Max 订阅的用量限制有实际影响，Chris 的经验可能不具普遍性
- **关联**：此视频与 [[BV1FgveB7Ebx-Claude Code实战如何将个人产出提高15倍]] 互补——后者强调"AI 做一切非编码工作"和"在最低价值阶段干预"，此视频补充了具体的工具配置、模型选择和六条操作技巧。两期合在一起，构成了从策略到操作的完整图谱

## 与其他知识的关联
- 相关概念：[[智能体分工]]、[[微交互设计]]、[[驾驭工程]]、[[思考模式]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]
- 相关视频：[[BV1FgveB7Ebx-Claude Code实战如何将个人产出提高15倍]] — 同系列，策略层面；本视频是操作层面

## 待深入问题
- `ultrathink` 在 Claude Code 中的实际机制是什么？是触发 extended thinking 还是改变 system prompt？对 Max 订阅用量限制的实际影响如何？
- Plan Mode 的"规划质量"差异（Cursor vs Claude Code）是模型差异还是 prompt engineering 差异？能否通过自定义 prompt 在 Claude Code 中复现 Cursor 的规划深度？
- MCP 服务器在生产环境中的安全边界——Supabase MCP 能做到只读模式吗？如何防止 AI 执行破坏性操作？
- 语音输入的 prompt 质量是否真的系统性优于手写？还是仅因为"说得多所以写得多"？
