```markdown
---
type: video
bv: BV1Q9ndzjEer
title: "Claude Code实战：15分钟开发Youtube Research Agent"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1Q9ndzjEer
date: 2026-04-30
duration: 15:00
tags: [Claude Code, AI Agent开发, 自动化工作流, Slash命令, 规格驱动开发]
concepts: [Claude Skill, 乘风策略, 上下文工程]
---

# Claude Code实战：15分钟开发Youtube Research Agent

## 一句话摘要

演示了用 Claude Code 从零到一构建 YouTube 频道分析 Agent 的完整流程，核心方法论是"先规划后编码"——通过探索方案、写规格、列清单三步前置规划，让编码变成最简单的一步。

## 核心观点

- Claude Code 不仅是编码工具，更是"everything agent"，可以自动化任何任务
- 开发 AI Agent 的正确顺序：探索方案 → 写规格 → 列待办 → 编码，编码是最后一步也是最容易的一步
- Plan Mode 是项目起步的关键——先在计划模式下头脑风暴，避免走弯路
- Spec（规格文档）中最重要的部分是理想输出格式的定义，这直接决定 Agent 能否一次生成正确结果
- Slash 命令是复用 AI 工作流的核心机制，一次定义、反复使用

## 详细笔记

### 六步开发流程

#### 第一步：在 Plan Mode 下探索方案

- 进入 Plan Mode（Shift+Tab），让 Claude 探索不同实现路径
- 本例中 Claude 给出三种方案：YouTube Data API（官方但需 API Key 和配额）、网页爬虫（不可靠）、第三方工具 yt-dlp（开源免费无需 API Key）
- 选定 yt-dlp 方案后，Claude 想立即开始编码——**此时应拒绝**，因为还需大量前置规划

#### 第二步：配置权限自动审批

- 输入 `/permissions` 创建本地权限配置文件
- 允许的工具：文件读写、npm、localhost、yt-dlp、Web Search 等
- 目的：让 Claude 无需逐次请求许可，可以"放手干"

#### 第三步：编写 Spec

- Spec 是 Slash 命令的蓝图，定义命令的行为和输出格式
- 关键内容：命令名（youtube）、输入（频道 handle）、数据源（yt-dlp）、输出结构
- **理想输出格式是 Spec 中最重要的部分**——包括 Key Insights（5条性能模式分析）、Your Next Video（3个标题建议）、Top 10 Videos（含链接和播放量）
- 仔细审查和修改 Spec，删掉不需要的字段（如上传日期），确保格式符合预期

#### 第四步：将 Spec 转为详细待办清单

- 提示 Claude 基于规格生成实施清单
- 本例生成 12 个步骤，作者选择先实施前 7 步（核心功能），错误处理和缓存暂缓
- 清单需审查和裁剪，避免过度工程化

#### 第五步：编码实现并测试

- 基于前四步的充分规划，Claude 一次性成功生成代码
- 测试：`/youtube peteryangyt` 生成分析报告，验证链接有效
- 发现小问题：标题被截断，需后续反馈修正

#### 第六步：添加批处理

- 需求：一次分析多个频道而非逐个运行
- 实现：创建 `youtube-channels.md` 文件列出频道列表，命令无参数时自动读取该文件并批量处理
- 测试成功：一次性输出 5 个频道的完整分析报告

### 可复用的模式

Slash 命令的模式可推广到多种研究场景：
- 每日简报：聚合多个博客的 AI 行业新闻
- Newsletter 摘要：总结订阅的 Newsletter
- 市场研究：分析某主题的行业趋势

## 我的评注

- **赞同**："探索方案→写规格→列清单→编码"的流程确实比直接让 AI 写代码有效得多。规格和清单的作用是压缩不确定性——把"AI 该做什么"的模糊地带在编码前全部消除。这个方法论对任何 AI 辅助开发都有参考价值。
- **质疑**：视频中跳过了 yt-dlp 的安装和配置细节，对新手不够友好。批处理中 5 个频道串行请求 yt-dlp 数据，没有提及速率限制和错误处理的实际影响。标题截断的 bug 在演示中被轻描淡写，但这类输出质量问题在 Agent 场景下很常见，恰恰说明"一次成功"的理想需要更多迭代。
- **关联**：这个流程本质上是 [[Claude Skill]] 的手工构建过程——Spec 即 Skill 的 prompt 定义，待办清单即实施步骤，Slash 命令即 Skill 的触发入口。与 [[乘风策略]] 的关系：先用 Plan Mode 快速试错找到正确方向，再投入编码资源，正是乘风的体现。整个流程也是 [[上下文工程]] 的实践——Spec、待办清单都是在管理 AI 的上下文，确保编码时 Claude 拥有足够且精准的信息。

## 待深入问题

- yt-dlp 的速率限制和反爬机制在实际批量使用中会带来什么影响？
- Slash 命令的 Spec 如何版本管理和迭代？随着需求变化，Spec 的维护成本如何？
- 从 Slash 命令到 MCP Server 的演化路径是什么？当 Agent 需要被其他系统调用时，Slash 命令的局限性在哪里？
- 输出质量问题（如标题截断）是否有通用的后处理或校验策略？
```

页面已生成。三个概念页的关联依据：

- **Claude Skill**：Slash 命令本质上就是手工构建的 Skill，Spec 即 prompt 定义
- **乘风策略**：Plan Mode 先试错再编码，正是先乘后造
- **上下文工程**：Spec 和待办清单都是上下文管理手段
