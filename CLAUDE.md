# Sharkbase — CLAUDE.md

## 项目概述

Sharkbase 是一个面向 AI 时代超级个体的知识发动机。

它将高价值信息源转化为：可追溯知识 → 能力地图 → 代表性任务 → 实践项目 → 评估标准 → SOP/Prompt/Skill 复利资产。

核心理念：不是收藏更多信息，而是把信息转成能力。不是生成更多文章，而是生成可实践、可评估、可复用的个人生产系统。知识库是持久化、复利增长的产物，每纳入一个新视频，知识库变得更丰富，能力地图变得更清晰。

## 七层架构

```
00_raw          原始材料层 — bili2text 输出，不可修改
01_sources      信源管理层 — 注册表、队列、信源分类
02_curation     策展与筛选层 — 质量评分、分级、相关性判断
03_knowledge    知识沉淀层 — wiki 视频页、概念页、主题页、实体页
04_capability   能力地图层 — 9 项一级能力、知识-能力映射、掌握等级
05_practice     实践任务层 — 代表性任务、项目实践、实验、复盘
06_assets       复利资产层 — Prompt、SOP、Skill、模板、Checklist
07_evals        评估校准层 — 质量标准、评分规则、评估报告
```

### 目录映射

```
sharkbase/
├── config/           # 配置文件（local.yaml, pipeline.yaml）
├── sources/          # 01_sources: registry.json, queue.md, series 分类
├── raw/              # 00_raw: 转录文件在 E:\bili2text\.b2t\，不在此目录
├── wiki/             # 03_knowledge: videos/, concepts/, topics/, entities/, tutorials/
├── capabilities/     # 04_capability: map.md, 能力页
├── practice/         # 05_practice: tasks/, projects/, experiments/, reviews/
├── assets/           # 06_assets: prompts/, sops/, skills/, templates/, checklists/
├── evals/            # 07_evals: rubrics/, samples/, judge_prompts/, reports/
└── scripts/          # 处理脚本
```

## 核心操作

### ingest — 纳入新视频

当用户提供视频 URL 或从 queue.md 取任务时：

1. **转录**: `cd E:\bili2text && uv run bili2text tx "BV号或URL" --provider sensevoice --model "E:\bili2text\models\sensevoice-onnx\iic\SenseVoiceSmall-Onnx"`
2. **读取转录**: 从 `E:\bili2text\.b2t\transcripts\original\` 找到对应的 .txt 文件
3. **读取元数据**: 从 `E:\bili2text\.b2t\metadata\` 找到对应的 .json 文件
4. **创建视频页面**: 在 `wiki/videos/` 创建该视频的深度整理页面
5. **更新实体页面**: 识别视频中的 UP 主、人物、组织，更新或创建 `wiki/entities/` 下的页面
6. **更新概念页面**: 识别视频中的核心概念，更新或创建 `wiki/concepts/` 下的页面
7. **更新主题页面**: 如果视频涉及已有主题，更新对应 `wiki/topics/` 页面；如果是新主题方向，创建新页面
8. **能力归位**: 将新知识挂到能力地图，更新 `capabilities/` 下的能力页
9. **更新 index.md**: 在知识目录中添加新条目
10. **追加 log.md**: 在活动日志中追加此次纳入记录
11. **更新 registry.json**: 在主注册表中记录此视频已处理

也可以使用 `python scripts/ingest.py "BV号"` 来执行步骤 1-3 和 11 的自动化部分。

### tutorialize — 生成教学文章

将视频转录稿提交给 Kimi API，生成课程化的教学文章。输出保存在 `wiki/tutorials/` 目录。

```
python scripts/tutorialize.py BV1D9ojBzEAd           # 生成教学文章
python scripts/tutorialize.py BV1D9ojBzEAd --force   # 覆盖已有文章
```

前提：视频必须已经 ingest（有转录文件和 registry 记录）。

API 配置：
- 端点：`https://api.kimi.com/coding/`
- 模型：`moonshot-v1-auto`
- API Key 通过 `KIMI_API_KEY` 环境变量配置（必需）

### operationalize — 知识转能力资产

将教程文章转化为可训练、可实践、可评估、可复用的能力资产。

```
python scripts/operationalize.py BV1VczqBREQ8           # 处理单个教程
python scripts/operationalize.py BV1VczqBREQ8 --force   # 覆盖已有输出
python scripts/operationalize.py --all                   # 处理所有已有教程
```

前提：视频必须已经 tutorialize（有 `wiki/tutorials/BVxxx-*.md`）。

流程：
1. 读取 `assets/prompts/operationalize_prompt.md`
2. 将教程文章内容替换 `{tutorial}` 占位符
3. 调用 Kimi API 生成含 XML 标签的结构化输出
4. 解析 5 个 XML 块：`<practice_task>` `<prompts>` `<sop>` `<checklist>` `<eval_report>`
5. 写入对应文件：
   - `practice/tasks/BVxxx-task.md` — 代表性任务
   - `assets/prompts/BVxxx-prompts.md` — 可复用 Prompt
   - `assets/sops/BVxxx-sop.md` — 标准操作流程
   - `assets/checklists/BVxxx-checklist.md` — 检查清单
   - `evals/reports/BVxxx-operationalize.md` — 评估报告
6. 更新 `sources/registry.json`（`operationalized_at` + `operationalize_outputs`）

重复执行默认跳过，`--force` 时覆盖。

### query — 知识查询

当用户提出问题时：

1. 搜索相关 wiki 页面（视频页、概念页、主题页、实体页）
2. 搜索能力地图（capabilities/）和实践任务（practice/）
3. 综合多个来源的信息，给出有引用的回答
4. 如果回答质量高，归档为新的主题页面或能力页

### lint — 健康检查

定期或按需执行：

1. 检查矛盾：不同页面间是否有互相矛盾的论断
2. 检查孤立页面：没有被任何 wikilink 引用的页面
3. 检查缺失引用：概念被提及但没有对应概念页面
4. 检查过时信息：注册表中的视频是否都有对应的 wiki 页面
5. 检查交叉引用：相关概念/主题之间是否已有 wikilink 连接
6. 检查能力归位：概念页是否有 capability 字段，是否挂到能力地图
7. 检查实践缺口：高价值教程是否有对应的实践任务
8. 检查资产沉淀：教程是否已提取可复用资产

## 文件命名规范

- 视频页面: `BV号-简短标题.md`（例: `BV1kfDTBXEfu-量子计算入门.md`）
- 实体页面: `人物或频道名.md`（例: `罗翔.md`）
- 概念页面: `概念名.md`（例: `因果推断.md`）
- 主题页面: `主题名.md`（例: `AI与法律.md`）
- 实践任务: `BV号-task.md`
- 能力页面: `序号_能力名.md`（例: `04_AI辅助开发与Agent调度.md`）
- 资产文件: `BV号-类型.md`（例: `BV1xxx-prompts.md`、`BV1xxx-sop.md`）

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
capability: [一级能力名]
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
（按视频逻辑结构整理的关键内容，不是逐字转录，是提炼和重组）

### 第一部分
...

### 第二部分
...

## 我的评注
（必须包含以下四类内容中的至少两类：）

- **赞同**：哪个观点特别有洞见？为什么？
- **质疑**：哪个观点值得商榷？遗漏了什么？逻辑哪里不成立？
- **关联**：这个视频和知识库中已有知识有什么深层联系？
- **待深入**：看完这个视频后，想进一步探索什么？

## 能力归位
这个视频主要补强哪项能力？学完后应该能做什么？

## 代表性任务
学完后应该做什么任务证明掌握？

## 可沉淀资产
这个视频能产出什么 Prompt / SOP / Skill / 模板？

## 与其他知识的关联
- 相关概念：[[概念1]]、[[概念2]]
- 相关实体：[[UP主名称]]
- 相关主题：[[主题1]]
- 相关能力：[[04_AI辅助开发与Agent调度]]

## 待深入问题
- 这个领域还有哪些未解答的问题？
```

### 概念页面模板

概念页不是百科词条，是思考笔记。核心区别：百科回答"它是什么"，概念页回答"为什么要在意它"。

```markdown
---
type: concept
name: 概念名
tags: [标签1, 标签2]
first_seen: 2026-04-25
capability: [一级能力名]
---

# 概念名

## 定义
1-2句话的简明定义。不要写成维基百科。

## 为什么重要
不是"它是什么"，而是"为什么要在意它"。它解决了什么问题？它改变了什么认知？
它和常识有什么冲突？

## 我的判断
（必须包含以下之一：）
- 赞同这个概念的理由
- 质疑或补充这个概念的理由
- 这个概念在实践中的局限或边界条件

## 深层联系
（跨视频的思想共振——不是"出现在同一视频"，而是思想层面的连接）
- [[概念A]] — 关系说明：为什么这两个概念在深层是相通的或对立的？

## 能力归位
这个概念补强哪项能力？

## 代表性任务
学完这个概念后，应该做什么任务证明掌握？

## 可沉淀资产
这个概念最终能变成什么 Prompt / SOP / Skill / 模板？

## 实践记录
我是否已经用它做过真实项目？

## 来源
- [[BVxxx-视频标题]] — 简述该视频对这个概念的贡献

## 相关主题
- [[主题1]]
```

**概念页的质量标准**：如果删掉这个概念页，知识库会失去什么？如果答案是"什么都不会失去"（因为内容在视频页里都有），那这个概念页不该存在。

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

### 主题页面模板

主题页不是视频摘要的堆叠，是跨视频的综合分析文章。它应该有论点、论据、论证。

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

## 核心主张
一句话概括这个主题经过综合分析后得出的核心判断。

## 综合分析
（真正的跨视频论证。引用具体视频中的具体观点来支撑论点。
不是"视频A说了X，视频B说了Y"的并列，而是"视频A的X结合视频B的Y，说明Z"的综合。）

### 子论点1
...

### 子论点2
...

## 仍然开放的分歧
（不同视频之间的矛盾或张力，目前无法得出结论的争议点）

## 我的立场
（基于综合分析后的个人判断，不是"各有道理"的和稀泥）

## 来源视频
- [[BVxxx-视频标题]] — 简述贡献
- [[BVyyy-视频标题]] — 简述贡献

## 相关概念
- [[概念1]]、[[概念2]]

## 开放问题
- 尚未解答的问题？
```

**主题页的质量标准**：能否让一个没看过任何原始视频的人理解这个主题的核心洞见？如果不能，说明主题页只是目录索引，不是知识综合。

### 实践任务模板

```markdown
---
type: practice_task
source: BVxxx
capability: 一级能力名
status: todo
level: L3
created: 2026-05-01
---

# 任务名称

## 来源知识
- [[BVxxx-视频标题]]
- [[概念名]]

## 能力归位
这个任务训练哪项能力？

## 任务目标

## 输入材料

## 执行动作
1.
2.
3.

## 产出物

## 验收标准
- [ ]
- [ ]

## 常见失败

## 复盘记录
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
2. **可以合并和删除 wiki 页面** — 当概念页内容能被视频页一句话替代时，合并到父概念或删除
3. **log.md 只追加，不修改历史条目**
4. **index.md 可以重新组织结构，但不删除条目**
5. **每次操作后必须更新 log.md**
6. **每次 ingest 后必须更新 index.md**
7. **概念页采用"综合式更新"** — 新视频纳入后重新综合该概念的跨视频洞察
8. **主题页采用"综合式更新"** — 新视频纳入后重新综合该主题的跨视频分析
9. **每个概念页必须能回答"删掉它知识库会失去什么"** — 如果答案是"什么都不会失去"，说明不该独立存在
10. **每个主题页必须能让没看过原始视频的人理解核心洞见** — 如果做不到，说明只是目录索引
11. **高价值内容必须能力归位** — 每个概念必须挂到能力地图
12. **S/A 级内容必须生成实践任务** — 知识不进入实践就不算消化
13. **API Key 不硬编码** — 通过环境变量配置，本地用 .env

## 处理链路

```
collect → normalize → score → transcribe → curate → tutorialize → knowledgeize → capability_map → task_generate → asset_extract → eval_quality → practice_review

采集  → 标准化   → 评分 → 转录     → 策展   → 教程化      → 知识化       → 能力归位     → 任务生成      → 资产提取    → 质量评估    → 实践复盘
```

## bili2text 工具参考

- 安装位置: `E:\bili2text\`
- 运行方式: `cd E:\bili2text && uv run bili2text tx "BV号或URL" --provider sensevoice --model "E:\bili2text\models\sensevoice-onnx\iic\SenseVoiceSmall-Onnx"`
- 工作区: `E:\bili2text\.b2t\`
- 输出转录: `E:\bili2text\.b2t\transcripts\original\[安全标题]-[时间戳].txt`
- 输出元数据: `E:\bili2text\.b2t\metadata\[安全标题]-[时间戳].json`
- 元数据内容: source(bv/url/kind)、engine、model、download(title/author/duration)、language、generated_at
