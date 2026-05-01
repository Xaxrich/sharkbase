---
type: video
bv: BV1hRndz1E4v
title: "用Claude Code搭建Life OS"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1hRndz1E4v
date: 2026-04-30
duration: 25:00
tags: [Claude Code, 个人操作系统, 工作流自动化, 子Agent, 内容创作]
concepts: [个人操作系统, 任务即子Agent, 驾驭工程, 复利工程]
entities: [Easonlee的AI笔记]
topics: [AI与生产力, LLM-Agent工程实践]
transcript: .b2t/transcripts/original/用ClaudeCode搭建LifeOS-*.txt
---

# 用Claude Code搭建Life OS

## 一句话摘要
用 Claude Code 的斜杠命令和子 Agent 系统，把日常重复任务（newsletter 研究、brain dump 分析、每日简报、目标追踪）编码为可一键触发的自动化工作流。

## 核心观点

- Claude Code 本质上是 AI Agent，不只是代码工具——它可以执行任何你能描述的任务
- 斜杠命令（slash command）+ 子 Agent（subagent）是构建个人自动化系统的核心架构
- 让 AI 自己写提示词——Claude Code 的创造力可以补全你没想到的子任务和边界条件
- "每天做事时问自己：怎么把 AI 接入这个任务？"——这是 2025 年最重要的技能
- AI 输出仍需人工审计，当前不能直接 copy-paste 发布

## 详细笔记

### Claude Code 超越编码

Claude Code 被定位为代码构建工具，但本质上是通用 AI Agent。Alex 的核心发现：它能力远超编码，只是大多数人还没意识到。他在 Cursor 的终端内运行 Claude Code，兼顾 IDE 的代码可视化和 Claude Code 的智能。

### Life OS 架构

整个系统是一个本地文件夹，内含：

- **brain dumps/** — 每日随意笔记和想法
- **newsletter/** — 竞品 newsletter 链接 + AI 生成的草稿
- **斜杠命令** — Claude Code 的 `.claude/commands/` 目录，每个命令是一个 markdown 文件
- **子 Agent** — `.claude/subagents/` 目录，每个子 Agent 有自己的角色设定和提示词

所有内容都是 markdown 文件，人可读、AI 可处理、Obsidian 可渲染。

### 四个核心命令

#### 1. Newsletter Researcher

流程：读取 `newsletter_links.md` 中的竞品 URL → 子 Agent A 抓取并分析竞品最新内容 → 子 Agent B 基于 A 的研究 + Alex 的历史文风写草稿 → 输出到 `newsletter/drafts/`。

关键细节：Alex 并未手写子 Agent 的提示词——他只给 Claude Code 一个主 prompt，Claude Code 自行拆分为研究者和写作者两个子 Agent，并自动分析 Alex 的历史 newsletter 来提取他的写作风格。

#### 2. Brain Dump Analysis

扫描最近 30 天的 brain dump 文件，寻找：洞察和模式、反复出现的主题、想法的演化轨迹、关键问题和突破、隐藏的思想联系。目标是为内容创作发现新的支柱（pillar）——Alex 认为好的创作者有 5-10 个支柱，反复强化。

#### 3. Daily Check-in

每晚回答一组问题（今天做了什么、心情如何、挑战是什么），系统追踪并生成每周仪表盘。在 Obsidian 中渲染为结构化的目标进度视图。

#### 4. Daily Brief

每日自动搜索互联网最新新闻（AI、科技、创业、创意领域），生成优先级排序的简报，包含来源、为何重要、内容创作角度建议。

### 设置方法

1. 在电脑上创建一个文件夹
2. 放入你想要的初始内容（如 newsletter 链接、brain dump 文件）
3. 打开 Claude Code，粘贴主 prompt
4. Claude Code 自动构建命令目录、子 Agent 目录、各自的提示词
5. 之后持续迭代：每天做事时发现新需求 → 让 Claude Code 建新命令

### 核心心法

Alex 的建议不是"规划一个完美系统然后实施"，而是"每天花时间实验，看 Claude Code 能做什么"。所有命令和子 Agent 都是从日常工作中自然长出来的——做一件事时想"能不能让 AI 替我做"，然后建一个命令。

## 我的评注

- **赞同**："让 AI 自己写提示词"是本视频最有价值的洞见。大多数人写提示词受限于自己的想象力边界，而 Claude Code 的创造力可以补全你没想到的子任务、边界条件、风格描述。这是一种元提示（meta-prompting）实践——用 AI 来对齐 AI。
- **赞同**：文件夹 + markdown + 斜杠命令的架构极其简洁。没有数据库、没有 API、没有前端——一个文件夹就是一个完整的个人操作系统。这与 [[个人操作系统]] 中三人各自的实现异曲同工，再次证明"上下文管理"的抽象需求在寻找最简实现。
- **质疑**：视频对"AI 生成内容需要审计"的讨论过于轻描淡写。Alex 说"我 pretty much gut the draft"，这意味着他实际投入的编辑时间和从零写可能差不多——系统的真正价值可能不是节省时间，而是克服"空白页恐惧"和提供结构化框架。这个区分很重要：如果你的 gut rate 是 95%，系统节省的不是写作时间，而是启动时间。
- **质疑**：30 天 brain dump 分析假设了持续输入的自律性——和 [[个人操作系统]] 中指出的可维护性问题一样。一旦你一周没写 brain dump，分析就基于过时数据。
- **关联**：这个 Life OS 和 [[BV1GAzqBWEWx-AI产品经理如何用AI做原型设计战略和个人OS]] 中三人展示的系统本质相同，但 Alex 的版本更强调"斜杠命令作为触发器"——每次执行是一个确定的流程，而非自由对话。这接近 [[Claude Skill]] 的"标准操作手册"定位，而非 [[第二大脑]] 的"开放探索"定位。两种模式（确定性流程 vs 开放对话）各有适用场景，Life OS 偏向前者。

## 与其他知识的关联

- 相关概念：[[个人操作系统]]、[[任务即子Agent]]、[[驾驭工程]]、[[复利工程]]、[[Claude Skill]]、[[第二大脑]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[AI与生产力]]、[[LLM-Agent工程实践]]

## 待深入问题

- 斜杠命令 + 子 Agent 的架构与 Claude Skill 的关系是什么？两者是否在功能上重叠？未来会统一吗？
- "让 AI 写提示词"的元提示实践有没有边界？什么时候 AI 生成的提示词比人写的差？
- Life OS 的可扩展性如何？当命令和子 Agent 超过 20 个时，管理和调试成本是否线性增长？
