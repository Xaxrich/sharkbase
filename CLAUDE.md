# Bilibili 知识库 — CLAUDE.md

## 项目概述

这是一个自进化的 Bilibili 视频知识库系统。用户观看深度视频后，系统将视频转为文字，
再由 AI（你）进行深度整理、分类、摘要、交叉引用，构建持续积累的知识网络。

核心理念：知识库是一个**持久化、复利增长的产物**。交叉引用已经存在、矛盾已标注、
综合分析已反映所有已读内容。每纳入一个新视频，知识库变得更丰富。

## 三层架构

1. **原始层** (`E:\bili2text\.b2t\`) — bili2text 工具的输出，不可修改
   - `transcripts/original/` — 原始转录文本 (.txt)
   - `metadata/` — 每个转录的元数据 (.json)，包含 BV 号、标题、UP主、引擎等
   - `audio/` — 提取的音频文件
   - `downloads/` — 下载的视频文件

2. **策展层** (`sources/`) — 人工管理的视频队列和注册表
   - `sources/queue.md` — 待处理视频的 URL/BV 号列表
   - `sources/registry.json` — 所有已处理视频的主注册表

3. **知识层** (`wiki/`) — 你负责维护的知识库，Obsidian 兼容的 Markdown 文件
   - 这是唯一的、持续积累的知识产物

## 核心操作

### ingest — 纳入新视频

当用户提供视频 URL 或从 queue.md 取任务时：

1. **转录**: 在 `E:\bili2text\` 目录下运行 `uv run bili2text tx "BV号或URL" --provider sensevoice --model "E:\bili2text\models\sensevoice-onnx\iic\SenseVoiceSmall-Onnx"`
2. **读取转录**: 从 `E:\bili2text\.b2t\transcripts\original\` 找到对应的 .txt 文件
3. **读取元数据**: 从 `E:\bili2text\.b2t\metadata\` 找到对应的 .json 文件
4. **创建视频页面**: 在 `wiki/videos/` 创建该视频的深度整理页面
5. **更新实体页面**: 识别视频中的 UP 主、人物、组织，更新或创建 `wiki/entities/` 下的页面
6. **更新概念页面**: 识别视频中的核心概念，更新或创建 `wiki/concepts/` 下的页面
7. **更新主题页面**: 如果视频涉及已有主题，更新对应 `wiki/topics/` 页面；如果是新主题方向，创建新页面
8. **更新 index.md**: 在知识目录中添加新条目
9. **追加 log.md**: 在活动日志中追加此次纳入记录
10. **更新 registry.json**: 在主注册表中记录此视频已处理

也可以使用 `python scripts/ingest.py "BV号"` 来执行步骤 1-3 和 10 的自动化部分。

### query — 知识查询

当用户提出问题时：

1. 搜索相关 wiki 页面（视频页、概念页、主题页、实体页）
2. 阅读相关页面内容
3. 综合多个来源的信息，给出有引用的回答
4. 如果回答质量高，可以将其归档为新的主题页面或追加到现有主题页面

### lint — 健康检查

定期或按需执行：

1. 检查矛盾：不同页面间是否有互相矛盾的论断
2. 检查孤立页面：没有被任何 wikilink 引用的页面
3. 检查缺失引用：概念被提及但没有对应概念页面
4. 检查过时信息：注册表中的视频是否都有对应的 wiki 页面
5. 检查交叉引用：相关概念/主题之间是否已有 wikilink 连接

## 文件命名规范

- 视频页面: `BV号-简短标题.md`（例: `BV1kfDTBXEfu-量子计算入门.md`）
- 实体页面: `人物或频道名.md`（例: `罗翔.md`）
- 概念页面: `概念名.md`（例: `因果推断.md`）
- 主题页面: `主题名.md`（例: `AI与法律.md`）

命名使用中文，不加空格。不使用英文命名除非概念本身就是英文。

## 页面模板

### 视频页面模板

```markdown
---
type: video
bv: BV1kfDTBXEfu
title: 视频标题
uploader: UP主名称
url: https://www.bilibili.com/video/BV1kfDTBXEfu
date: 2026-04-25
duration: 45:30
tags: [标签1, 标签2]
concepts: [概念1, 概念2]
entities: [实体1]
topics: [主题1]
transcript: .b2t/transcripts/original/标题-时间戳.txt
---

# 视频标题

## 一句话摘要
用一句话概括视频的核心价值。

## 核心观点
- 观点1
- 观点2
- 观点3

## 详细笔记
（按视频逻辑结构整理的关键内容）

### 第一部分
...

### 第二部分
...

## 关键引用
> "原文中特别有洞见的句子。"

## 与其他知识的关联
- 相关概念：[[概念1]]、[[概念2]]
- 相关实体：[[UP主名称]]
- 相关主题：[[主题1]]

## 待深入问题
- 这个领域还有哪些未解答的问题？
```

### 实体页面模板

```markdown
---
type: entity
kind: uploader
name: 实体名
tags: [标签1, 标签2]
---

# 实体名

## 简介
一句话介绍。

## 出现的视频
- [[BVxxx-视频标题]]

## 核心观点与风格
- ...

## 相关概念
- [[概念1]]

## 相关主题
- [[主题1]]
```

### 概念页面模板

```markdown
---
type: concept
name: 概念名
tags: [标签1, 标签2]
first_seen: 2026-04-25
---

# 概念名

## 定义
简明定义。

## 核心要点
- 要点1
- 要点2

## 在以下视频中出现
- [[BVxxx-视频标题]]（说明出现方式）

## 与其他概念的关系
- [[概念A]] — 关系说明

## 相关主题
- [[主题1]]
```

### 主题页面模板

```markdown
---
type: topic
name: 主题名
tags: [标签1, 标签2]
created: 2026-04-25
updated: 2026-04-25
video_count: 1
---

# 主题名

## 主题概述
一句话概括这个主题关注什么。

## 核心问题
1. 问题1
2. 问题2

## 综合梳理
（跨视频的知识综合，不是单视频摘要的堆叠）

### 子话题1
来自 [[BVxxx-视频标题]] 的观点认为...
来自 [[BVyyy-视频标题]] 的补充观点...

## 相关视频
- [[BVxxx-视频标题]] — 简述贡献

## 相关概念
- [[概念1]]、[[概念2]]

## 相关实体
- [[实体1]]

## 开放问题
- 尚未解答的问题？
```

## 中文处理规则

1. 所有页面内容使用中文，除非概念本身就是英文术语
2. 英文术语首次出现时附中文翻译: "Quantum Entanglement (量子纠缠)"
3. 标签使用中文: `tags: [量子计算, 物理学]`
4. Wikilink 使用中文: `[[量子比特]]`
5. 元数据 YAML 中的键名使用英文（便于程序化处理），值使用中文

## Obsidian 兼容规则

1. 所有文件使用 `.md` 扩展名
2. 使用 `[[wikilink]]` 语法进行交叉引用
3. YAML frontmatter 用于结构化元数据
4. 文件名可以包含中文和 BV 号
5. 不使用 Obsidian 特有插件功能，保持纯 Markdown 兼容

## 操作约束

1. **绝不修改原始层 `.b2t/` 下的任何文件** — 这是事实来源，不可变
2. **绝不删除 wiki 页面** — 只能标记为过时或合并
3. **log.md 只追加，不修改历史条目**
4. **index.md 可以重新组织结构，但不删除条目**
5. **每次操作后必须更新 log.md**
6. **每次 ingest 后必须更新 index.md**
7. **概念页和实体页采用"追加式更新"** — 新信息追加到现有内容，不覆盖
8. **主题页采用"综合式更新"** — 新视频纳入后重新综合该主题的跨视频分析

## bili2text 工具参考

- 安装位置: `E:\bili2text\`
- 运行方式: `cd E:\bili2text && uv run bili2text tx "BV号或URL" --provider sensevoice --model "E:\bili2text\models\sensevoice-onnx\iic\SenseVoiceSmall-Onnx"`
- 工作区: `E:\bili2text\.b2t\`
- 输出转录: `E:\bili2text\.b2t\transcripts\original\[安全标题]-[时间戳].txt`
- 输出元数据: `E:\bili2text\.b2t\metadata\[安全标题]-[时间戳].json`
- 元数据内容: source(bv/url/kind)、engine、model、download(title/author/duration)、language、generated_at
