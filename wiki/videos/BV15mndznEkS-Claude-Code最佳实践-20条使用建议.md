---
type: video
bv: BV15mndznEkS
title: "Claude Code最佳实践：20条使用建议"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV15mndznEkS
date: 2026-04-30
duration: 35:00
tags: [Claude Code, AI编程, 工作流优化, 调试技巧, AI Agent]
concepts: [Plan Mode, Spec-Todo-Code流程, 上下文管理, 子代理]
---

# Claude Code最佳实践：20条使用建议

## 一句话摘要

以构建家庭活动查找器为实战案例，系统演示 Claude Code 的 20 条使用技巧，核心信息是：计划越多，AI 编码成功率越高。

## 核心观点

- **Plan Mode 是最重要的单条建议**——让 Claude 先规划再编码，否则它会像过度积极的工程师一样直接冲去写代码
- **Spec → Todo → Code 流程是核心方法论**——写规格说明、创建待办清单、再逐步编码，每步都要人工审核
- **上下文质量决定输出质量**——具体反馈、截图、控制台日志、文档链接，给的上下文越精确，调试越快
- **Claude 会过度构建**——你必须主动简化、审核、打断走偏的方向，不能放任不管
- **对话历史越长 AI 表现越差**——用 compact 清理上下文，用子代理隔离不同任务

## 详细笔记

### 规划与项目设置

#### 1. 使用 Plan Mode
按 Shift+Tab 切换到 Plan Mode。Claude 会反复请求开始编码，必须拒绝。"把 Claude 当作一个过度积极的工程师，你得一直拉着它。"

#### 2. 与 Claude 协作探索方案
在 Plan Mode 中先让 Claude 解释代码库，再提出需求，要求从最简单的方案开始探索。视频中 Claude 给出三种方案：静态数据库+客户端过滤、第三方 API、Claude Messages API + Web Search。选择了第三种。

#### 3. 遵循 Spec → Todo → Code 流程
选定方案后，让 Claude 创建 spec.md（需求、技术栈、设计准则、里程碑），人工审核并简化，再让它为第一个里程碑创建 todo 清单。关键：每一步都要审核，Claude 总是构建超出你要求的东西。

#### 4. 单独编写 Prompt 模板
如果使用 Claude API，提前写好 prompt.md 文件，明确系统提示词和输出格式要求。视频中补充了"timely"关键词，避免返回通用景点信息。

#### 5. 用 Output Style 边建边学
- `/output-style explanatory`——Claude 添加说明框解释架构决策
- `/output-style learning`——Claude 让你自己写代码片段来练习

#### 6. 用 CLAUDE.md 建立项目记忆
输入 `/init` 让 Claude 扫描代码库生成 CLAUDE.md。也可手动添加个人偏好（如"我是产品经理，请解释架构和变更"），该文件成为所有后续对话的记忆。

### 核心编码工作流

#### 7. 用语音输入提供上下文
使用 WhisperFlow、Morelo 等语音工具直接口述指令。自然说话比打字能提供更多细节，Claude 输出更好。

#### 8. 尽早让应用跑起来
第一个里程碑只做 UI + 假数据，不接 API。看到应用运行后，后续修改能实时观察效果。

#### 9. 按 Escape 阻止偏离方向
Claude 走偏时随时按 Escape 中断，不会丢失上下文。"不要害怕打断它。"

#### 10. 用 GitHub 做版本控制
每个里程碑完成后提交到 GitHub。AI 编码容易出错，版本控制让你能回退。也可用 `/install-github-app` 快速集成。

#### 11. 设置权限减少打断
创建 `.claude/settings.json` 自动授权读写和常见命令，拒绝删除类操作。不推荐 `dangerously-skip-permissions`。

#### 12. 每个里程碑都重新走 Spec → Todo → Code
在开始新里程碑前：更新 todo 清单（勾选完成的、添加新的），审核细节（如模型版本是否正确——视频中 Claude 试图用已弃用的 claude-3.5-sonnet，需纠正为 claude-4-sonnet）。

### 调试技巧

#### 13. 让 Claude 深度思考
- "think ultra hard"——让 Claude 用更多 token 思考
- "why do you think this happened"——让 Claude 回溯推理

#### 14. 提供精确上下文
具体描述问题、粘贴浏览器控制台错误、上传截图。"给 Claude 的上下文越多，它越可能找到问题。"

视频实战：应用显示空白页，检查控制台发现 Uncaught Error，粘贴错误信息给 Claude 后修复。

### 上下文管理

#### 15. 用 compact / clear 清理对话
- `/compact`——压缩对话历史但保留摘要
- `/clear`——完全清除对话历史
对话越长 AI 表现越差，优先用 compact。

### 高级功能

#### 16. 创建自定义命令
为重复工作流创建自定义斜杠命令。参见 UP 主专题教程。

#### 17. 使用子代理（Subagents）
让 Claude 创建专门的子代理（名称、描述、独立 prompt），每个子代理有独立上下文窗口，不污染主对话。Anthropic 内部用于文档更新、安全审计等。

#### 18. 设置 Hooks
Claude 完成特定操作后触发脚本，例如完成后发送 Slack 通知。直接让 Claude 帮你创建即可。

#### 19. 安装 MCP 服务器
- `claude mcp add <server>` 添加
- 推荐服务器：Serena（代码搜索）、Playwright（截图和 UI 测试）、Figma（设计稿接入）
- 注意：MCP 会加载大量上下文到 prompt，不要同时运行太多

#### 20. 并行运行多个 Claude 会话
用 worktree 同时在不同分支上构建前端和后端。需要工程经验，初学者慎用。

## 我的评注

- **赞同**：Spec → Todo → Code 流程是本视频最有价值的方法论。很多人直接让 AI 编码，结果反复修改。先花时间规划，后续效率反而更高。视频中反复强调"审核每一步"也是关键——Claude 不是执行者，是合作者，你必须充当技术评审。
- **赞同**："把 Claude 当作过度积极的工程师"这个比喻精准。AI 编码的核心问题不是能力不足，而是过度构建——它总想做更多。人类的价值在于判断"什么不需要做"。
- **质疑**：视频声称 30 分钟建完应用，但实际花 10 分钟调试 API 速率限制问题。这恰恰说明 AI 编程的瓶颈往往不在编码本身，而在调试和集成——视频对此着墨不够。
- **质疑**：对 MCP 和子代理等高级功能仅一笔带过，缺乏实操。对于目标受众（非技术背景），这些恰恰是最需要详细演示的部分。
- **关联**：视频的方法论与 [[驾驶工程]] 的核心主张高度一致——AI 编程中人仍然是驾驶员，不是乘客。也与 [[上下文工程]] 直接相关：Claude Code 的本质就是通过 prompt、CLAUDE.md、权限文件、MCP 等手段管理上下文，上下文质量决定输出质量。

## 与其他知识的关联
- 相关概念：[[上下文工程]]、[[驾驶工程]]、[[MVP思维]]、[[Claude Skill]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题
- Spec → Todo → Code 流程在不同规模项目中的适用性？小型脚本是否也需要？
- compact 压缩摘要后 Claude 的表现下降幅度有多大？有无量化数据？
- MCP 上下文膨胀问题的具体影响——加载多少 MCP 工具后性能开始明显下降？
- 子代理与主代理之间的信息隔离边界在哪里？子代理的结果如何可靠地回传？
