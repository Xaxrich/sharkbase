```markdown
---
type: video
bv: BV1G9ndzjEtc
title: "Claude Code实战教程：15分钟开发一个电影APP"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1G9ndzjEtc
date: 2026-04-30
duration: 16:00
tags: [Claude Code, AI编程, 计划模式, CLAUDE.md, 前置规划]
concepts: [计划模式, CLAUDE.md, AI编程工作流]
entities: [Easonlee的AI笔记]
topics: [LLM-Agent工程实践]
---

# Claude Code实战教程：15分钟开发一个电影APP

## 一句话摘要
Claude Code 实战入门教程——核心教训是：前置规划（spec、CLAUDE.md、todo list）比直接让 AI 写代码更能保证一次成功。

## 核心观点
- **前置规划决定成败**：写 spec、建 CLAUDE.md、审查 todo list，这些"不写代码"的步骤才是 Claude Code 用好的关键
- **Plan Mode 是隐藏利器**：Shift+Tab 进入计划模式，让 Claude 只做研究不写代码，先生成 spec 再审查
- **CLAUDE.md 是持久记忆**：每个 session 自动加载的项目上下文，包含代码库理解和最佳实践约束
- **审查 spec 再动手**：AI 倾向过度设计，必须人工砍掉不需要的功能并分阶段实施
- **让 AI 解释代码库是最好的学习方式**：非工程师通过让 Claude 逐文件解释，能快速建立代码阅读能力

## 详细笔记

### 安装 Claude Code

两种方式：
- **终端安装**：复制官方文档的一行命令，粘贴到终端即可，输入 `claude` 启动
- **在 Cursor 中使用**：在 Cursor 项目中打开终端，输入 `claude`。好处是可以直接在 IDE 中查看和编辑文件

### 克隆并理解项目

1. 用 `git clone` 将一个 TMDB 电影发现应用克隆到项目中
2. 用自然语言让 Claude Code 解释代码库结构——"告诉它我是 PM，不是工程师"来调整解释深度
3. Claude 会分析技术栈（TypeScript + Tailwind CSS）、数据来源（TMDB API）、架构逻辑

### 让应用跑起来

1. 让 Claude 安装依赖并启动本地服务
2. 遇到 API Key 缺失问题——Claude 主动创建了 `.env` 文件模板
3. 去 TMDB 注册免费 API Key，让 Claude 写入 `.env`
4. 应用成功加载电影数据

### 用 Plan Mode 写 Spec

这是教程的核心步骤：
1. **Shift+Tab 进入 Plan Mode**——Claude 只做研究和规划，不修改代码
2. 给出简短的 spec 方向："添加 watchlist 功能，保存想看的电影，创建 spec 文件夹，写设计文档，保持简单以便逐步测试"
3. **关键指令**："keep simple so can test along the way"——防止 AI 过度设计
4. Claude 生成包含实现阶段（phase 1/2/3）的 spec
5. **必须审查 spec**：砍掉不需要的功能（如通知、批量操作），确保分阶段可测试

### 创建 CLAUDE.md

- `CLAUDE.md` 是每次 Claude Code session 自动加载的持久化上下文
- 用 `/init` 命令让 Claude 基于代码库自动生成
- 内容包含：项目环境、架构说明、组件模式、开发规范
- 手动补充最佳实践：写测试、小步提交、遵循现有模式

### 实现 Watchlist 功能

1. 让 Claude 先生成 todo list，审查后再开始编码
2. Claude 逐步实现：创建存储 → 添加 watchlist 按钮 → watchlist 页面 → 从详情页添加
3. 因为 CLAUDE.md 中写了"写测试"，Claude 会自动编写测试验证自己的实现
4. 最终功能一次通过：添加/移除电影、TV 剧集支持、详情页操作均正常

## 我的评注

- **赞同**：教程清晰展示了"规划 > 编码"的工作流。Plan Mode + CLAUDE.md + todo list 的三重前置准备，是真正有实战价值的最佳实践，而不是泛泛的"提示词技巧"
- **赞同**："keep simple so can test along the way"这条指令非常实用——AI 确实倾向过度设计，必须显式约束范围
- **质疑**：教程标题说"15分钟开发一个APP"，但实际是克隆一个已有项目并加一个功能。标题有误导性，对初学者可能造成不切实际的期望
- **质疑**：教程中多次说"我比较懒就全部同意权限了"——这不是好的示范，权限审查是安全底线
- **关联**：这个视频的工作流和 [[代码即最高保真]] 的理念一致——CLAUDE.md 本质上就是把项目约束"代码化"，让 AI 的行为可预测、可复现

## 与其他知识的关联
- 相关概念：[[Claude Skill]]、[[代码即最高保真]]、[[Vibe Coding]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题
- Plan Mode 生成的 spec 质量如何量化评估？什么样的 spec 算"足够好"？
- CLAUDE.md 的最佳实践清单有没有社区共识版本？不同项目类型的差异在哪？
- 当 spec 和实际实现出现偏差时，应该更新 spec 还是调整实现？这个反馈循环怎么管理？
- 对于已有大型代码库（非从零克隆），CLAUDE.md 的初始化策略有何不同？
```
