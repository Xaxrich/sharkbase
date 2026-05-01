```markdown
---
type: video
bv: BV1bJndzzELm
title: "Anthropic官方教程：30分钟掌握Claude Code"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1bJndzzELm
date: 2026-04-30
duration: 28:00
tags: [Claude Code, AI编程, Agent工作流, 开发者工具, 提示工程]
concepts: [Claude Code, AI Agent工作流, 上下文工程, 工具集成]
entities: [Anthropic, Easonlee的AI笔记]
topics: [LLM-Agent工程实践]
---

# Anthropic官方教程：30分钟掌握Claude Code

## 一句话摘要

Anthropic 工程师亲授 Claude Code 的实操技巧：从代码问答入门，到编辑代码、集成团队工具、配置上下文、SDK 管道化，层层递进地展示了如何把 Claude Code 用成一个真正的工程搭档。

## 核心观点

- **先用 Claude Code 做代码问答，再做代码编辑**——这是 Anthropic 内部教新人的第一条规则，问答是零风险的上手路径
- **让 Claude 先想再做**——直接让它"实现一个300行功能"往往翻车，要求它先 brainstorm、做计划、跑给你确认，效果天差地别
- **给 Claude 反馈工具，它就能自我迭代**——单元测试、截图、Puppeteer，任何能让 Claude 看到自己输出的工具都行，迭代2-3轮后结果接近完美
- **CLAUDE.md 是性价比最高的上下文投资**——写一次，全团队受益，从项目级到企业级分层管理
- **Claude Code 是完全多模态的**——终端里可以拖拽、粘贴图片，只是不容易被发现

## 详细笔记

### Claude Code 是什么

不是逐行补全的 AI 助手，而是完全 Agent 式的——能写整个功能、整个文件、修整个 bug。工作在你现有的终端里，不需要换 IDE 或换工作流。VS Code、Xcode、JetBrains、Vim 用户都能用。

### 初始设置

- `claude terminal-setup`：开启 Shift+Enter 换行，告别反斜杠
- `claude theme`：切换亮/暗主题
- `claude /install-github-app`：安装 GitHub App，可在 issue/PR 里 @claude
- 自定义权限：把常用工具加入白名单，避免每次确认
- macOS 辅助功能里的听写：双击听写键，语音输入 prompt，大幅减少打字

### 第一步：代码问答（最重要的建议）

Anthropic 内部新人 onboarding 的标准流程：装好 Claude Code 后，第一件事就是问代码库问题。

典型问题类型：
- "这段代码怎么用的？"——Claude 不做文本搜索，会找实例、找调用模式，给出文档级回答
- "为什么这个函数有15个参数？"——Claude 会翻 git 历史，追溯每个参数何时引入、关联的 issue 和 commit
- "我这周 ship 了什么？"——结合 git log 和 GitHub，周一 standup 直接用

**效果**：Anthropic 的技术 onboarding 从 2-3 周缩短到 2-3 天。

**隐私**：不做索引，不上传代码，不训练模型，零设置即可使用。

### 第二步：编辑代码

Claude Code 内置工具集很小：编辑文件、运行命令、搜索文件。但它能自主串接这些工具完成任务，不需要你指定用什么工具。

**关键模式**：
- 先让 Claude brainstorm / 做计划，确认后再写代码——不需要 plan mode，直接说"先做计划，确认后再写"
- `think with this, commit, push`——常用咒语，Claude 会自动建分支、写 commit message、推送
- 给 Claude 反馈工具让它自我迭代：写单元测试、跑 Puppeteer 截图、iOS 模拟器截图——有了反馈循环，迭代2-3轮后结果几乎完美

### 第三步：集成团队工具

两类工具：
- **Bash 工具**：告诉 Claude 某个 CLI 怎么用（如 `--help`），频繁使用可写入 CLAUDE.md
- **MCP 工具**：添加 MCP server，Claude 自动学会使用

Anthropic 内部案例：apps 仓库配置了 Puppeteer MCP server，所有工程师都能用 Claude 自动操控浏览器和截图迭代，不用各自安装。

### 第四步：配置上下文

CLAUDE.md 的分层体系：

| 层级 | 位置 | 检入版本控制 | 加载时机 |
|------|------|-------------|---------|
| 项目根目录 | `./CLAUDE.md` | 是，团队共享 | 每次会话自动 |
| 用户本地 | `./CLAUDE.local.md` | 否，个人偏好 | 每次会话自动 |
| 子目录 | `./src/CLAUDE.md` | 视情况 | Claude 工作到该目录时按需加载 |
| 企业级 | 企业策略路径 | 管理员统一管理 | 所有项目自动 |

CLAUDE.md 内容建议：常用命令、代码风格、核心文件、架构决策。**保持简短**——太长浪费上下文。

其他上下文机制：
- **Slash Commands**：可放 home 目录或项目里，支持自动化工作流（如自动给 issue 打标签）
- **`#remember`**：告诉 Claude 记住某事，可选择写入哪个 memory 文件
- **`/memory`**：查看所有被加载的 memory 文件

配置层级也适用于权限管理：企业策略可以自动批准常用命令、屏蔽危险 URL，员工无法覆盖。

### 键位参考

| 键位 | 功能 |
|------|------|
| Shift+Tab | 切换自动接受编辑模式（命令仍需确认，编辑自动通过） |
| `#` + 内容 | 让 Claude 记住某事，写入 CLAUDE.md |
| `!` + 命令 | 临时切到 bash 执行命令，输出进入 Claude 上下文 |
| Escape | 中断 Claude 当前操作 |
| Escape 两次 | 结束当前会话 |
| `/resume` | 恢复上一个会话 |
| `/continue` | 继续当前会话 |
| `@` 文件夹 | 引用文件夹到上下文 |

### Claude Code SDK

`claude -p "prompt"` 就是 SDK 的核心。可传入 prompt、指定工具、选择输出格式（JSON / streaming JSON）。本质是一个 Unix 管道工具——可以 pipe 进、pipe 出。

典型场景：CI/CD、事件响应、日志分析（grep 巨大日志后 pipe 给 Claude 总结）。

### 并行工作

高级用户通常开多个终端 tab / tmux session，同时对多个仓库或同一仓库的不同 checkout 跑 Claude Code。这是提高吞吐量的关键模式。

### Q&A 精华

- **Bash 安全性**：静态分析判断命令是否只读，分级权限系统（allowlist / blocklist），不同层级可配置
- **多模态**：终端里可拖拽/粘贴图片，用于 UI 迭代时截图给 Claude
- **为什么做 CLI 不做 IDE**：一是团队用各种 IDE，终端是最大公约数；二是模型进步太快，年底可能不需要 IDE 了，不想过度投资 UI
- **ML 用途**：Anthropic 约 80% 技术人员每天用 Claude Code，包括研究员用 notebook 工具编辑和运行 Jupyter

## 我的评注

- **赞同**："先问答再编辑"的学习路径设计非常合理。零风险上手，让用户在问答中自然建立对 Agent 能力边界的直觉，比直接上手写代码安全得多。这也暗示了一个更深的原则——Agent 的信任是逐步建立的
- **赞同**：给 Agent 反馈工具让它自我迭代，这是目前 Agent 工程最实用的模式。不需要完美的 prompt，只需要一个反馈循环。这个洞见和 [[AI Agent自验证循环]] 的思路完全一致
- **质疑**："年底可能不需要 IDE"的说法过于激进。CLI 适合工程师，但 IDE 提供的视觉反馈（diff view、debugger、profiler）是纯文本交互难以替代的。更可能的未来是 CLI 和 IDE 深度融合，而非 CLI 取代 IDE
- **关联**：视频中"CLAUDE.md 分层体系"的设计，本质上是 [[上下文工程]] 的一个具体实现——把人类工程师脑中的隐式上下文显式化、结构化、分层管理。这与 [[Agent原生架构]] 中"Agent 需要结构化的环境配置"是同一个思路

## 与其他知识的关联

- 相关概念：[[Claude Skill]]、[[AI Agent自验证循环]]、[[上下文工程]]、[[Agent原生架构]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题

- CLAUDE.md 的最佳长度和内容结构有没有量化数据？多长开始明显影响效果？
- 企业级策略的权限分层在实际落地中，安全性和灵活性之间怎么平衡？
- Claude Code SDK 的管道模式在 CI/CD 中的具体集成方案和错误处理机制是什么？
- 多 session 并行工作时，对同一文件的冲突编辑如何处理？
- "先让 Agent 做计划"这个模式，在不同复杂度任务上的效果差异有多大？
```
