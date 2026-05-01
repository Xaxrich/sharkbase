---
type: video
bv: BV14HndzMEZ1
title: "Claude Code + Figma：Claude的设计主管这么用的"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV14HndzMEZ1
date: 2026-04-30
duration: 39:00
tags: [AI设计工作流, 设计师编程, Claude Code, Figma, 快速迭代]
concepts: [代码即最高保真, 设计-开发桥梁, 内部dogfooding]
entities: [Megan, Easonlee的AI笔记]
topics: [LLM-Agent工程实践]
---

# Claude Code + Figma：Claude的设计主管这么用的

## 一句话摘要

Anthropic 设计主管 Megan 展示设计师如何用 Claude Code 跨越设计-开发鸿沟：从理解代码库到提交 Draft PR，代码成为设计交付的最高保真载体。

## 核心观点

- **设计师可以并且应该 ship to prod**：Megan 用 Claude Code 定期将设计推上生产环境，不再依赖工程师翻译设计意图
- **代码是设计的最高保真形式**：比 Figma 原型更真实，比 spec 更精确——Megan 不再交付 Figma mock，而是交付 Draft PR
- **Claude Code 对设计师的核心价值在前端而非编码**：理解代码库、探索方案可行性、做最后 10% 的视觉打磨——这三件事占 Megan 90% 的 Claude Code 使用时间
- **避免 AI 生成的"默认紫"设计**：不给 AI 空白画布，而是提供现有设计或参考截图作为锚点
- **角色正在变得流动**：设计师、PM、工程师之间的边界模糊化，但最终决策权仍在专家手中

## 详细笔记

### 设计师用 Claude Code 的三大工作流

1. **零到一探索**（0→1 exploration）：在代码库内快速验证新想法，比 Figma 原型更真实，因为 AI 能理解代码上下文。Megan 个人项目用得多，工作中较少。
2. **理解代码库**：开始新功能前，先问 Claude 当前实现方式——系统提示怎么写的、架构怎么组织的、用例是什么。甚至问"你会怎么重新设计这个"。这是 Megan 最常做的工作流。
3. **最终打磨**（last 10% polish）：工程师搭好基础设施后，设计师进代码做像素级调整——对齐、间距、配色。这是 Megan 在 Claude Code 里花最多时间的地方。

### 完整设计流程中的 Claude Code 定位

传统双钻模型（探索→发现→设计→原型→打磨→交付）中，大多数人认为 Claude Code 只在最后两步有用。Megan 认为前三步（探索方案、理解历史、规划排序）才是 Claude Code 对非技术人员的超能力——因为它让你在代码这个 source of truth 里工作，而不是在 Figma 的象牙塔里。

### 设计交付方式的根本转变

- **旧方式**：交付 Figma mock + spec 文档
- **新方式**：交付 Draft PR，附描述说明设计意图，工程师直接在此基础上完成
- 好处：Megan 能立刻看到实现与设计的差距，不需要反复找工程师改像素
- 前提：公司文化允许设计师 push 代码。Megan 说在 Anthropic "anyone can code"，入职时与工程师 pair programming 一天来搭环境

### 实战演示：ClaudeCafe 打磨流程

1. 用 Claude Code 启动 dev server（`Ctrl+R` 后台运行，不阻塞对话）
2. 对照 Figma 设计发现实现差异：图片对齐、header 左对齐等细节
3. **方法一**：导出 Figma 截图为 PNG，拖入 Claude Code，说"按这个 mock 更新"。Megan 更常用这种方式而非 Figma MCP——因为 MCP 切换 dev mode 繁琐
4. **方法二**（进阶）：在浏览器 Web Spec 模式看 CSS class，直接指引 Claude Code 修改特定组件
5. **关键习惯**：先进 planning mode，让 Claude 列出修改计划和步骤，审查后再执行——尤其对非技术者，这是理解软件架构思维的学习机会

### CLAUDE.md：设计师的个性化指令

Megan 创建了一份全局 CLAUDE.md，将 Claude Code 调教为"设计师友好"模式：

- 要求更多解释（因为设计师不是软件工程师）
- 要求 Claude 在最终确定实现方案前先查看现有组件库，遵循设计系统最佳实践
- 标记"高风险"修改（push 到 prod 的代码需特别谨慎——Megan 因此触发过一次 incident）
- 这份文件持续迭代，Megan 不断调整以优化自己的工作流

### 避免 AI 默认设计风格的策略

AI 从零生成的设计容易千篇一律（"紫色渐变背景"问题）。Megan 的做法：

- **锚定现有设计**：说"看这个已有的设置页面，按同样的模式实现新设置"
- **参考外部设计**：像 Pinterest 一样收集喜欢的截图，丢给 Claude 说"做成类似这种风格"
- **绝对不给空白画布**：没有参照物的 AI 生成几乎一定落入默认审美

### Anthropic 内部的产品开发模式

以 Agents（子 Agent/并行 Agent）功能为例：

- 工程师 Sid 快速原型→内部发 demo→内部用户开始用→Megan 看到后提出设计改进→三方快速迭代→团队扩大反馈→发布
- **没有正式 spec 或设计文档**——对小功能来说是 organic 过程
- 判断"ready"的信号：内部反馈从密集转为稀疏（说明 bug 和问题已经修完），加上 adoption 数据上升、负面反馈下降
- **先发后修**：内部反馈用尽后直接对外发布，从社区获取更快反馈——不设 early preview 程序
- 大功能仍走传统流程，但"谁在起草、谁在贡献"非常流动

### Claude Code 快捷操作备忘

- **Shift+Tab**：切换 auto accept mode 和 plan mode——Megan 最常用
- **Ctrl+L**：连接 MCP server（Figma MCP、Playwright MCP 等）
- **Ctrl+R**：后台运行 dev server，不阻塞对话
- **Escape**：取消 Claude 正在做的事；**双击 Escape**：回到上一条 prompt 修改指令
- **--resume / -z**：恢复上一次会话
- **memory**：更新 CLAUDE.md，将重复性操作固化

### 对设计师角色演变的判断

- 设计师和 PM 之间的流动性已经存在（越资深越明显），现在设计师和工程师之间也在变得流动
- 关键区分：**技能在扩张，但决策权仍属专家**——工程师仍是代码的最终审查者和决策者
- 正向趋势：更多资深设计师选择继续做 builder 而非转管理——因为工具让 builder 的乐趣变得可及
- Megan 自己现在 Claude Code 和 Figma 各花一半时间

### 给想入行的设计师的建议

1. 从 Claude AI + artifacts 开始，理解 AI 生成代码的样子
2. 找一个工程师搭档 pair program——搭建环境、理解部署流程
3. 学一点 React 和 Tailwind 基础（不需要精通，但能帮你理解 AI 生成的代码）
4. 在 X 和 GitHub 上关注社区——现在是分享热情很高的时期
5. 让 Claude 解释它做了什么——这是从 AI 辅助编码中学到最多的方式
6. 学会判断 Claude 什么时候走错了方向——这需要对代码有基本理解

## 我的评注

- **赞同**：交付 Draft PR 而非 Figma mock 是一个范式级转变。Figma mock 的根本问题是"设计"和"实现"之间永远存在翻译损耗——设计师的意图在工程师实现时被压缩、丢失、误解。Draft PR 让设计师直接在实现层表达意图，消除了翻译环节。
- **赞同**："先理解代码库再做设计"的顺序比"先做设计再塞进代码"务实得多。很多设计之所以落不了地，是因为设计师不了解技术约束。Claude Code 让这个理解过程的成本趋近于零。
- **质疑**：Megan 反复强调"Anthropic 文化允许任何人写代码"，但这恰恰说明她的经验受限于一个极特殊的环境——小团队、强信任、高工程素养。在大公司或外包场景中，设计师 push 代码可能触发安全审计、代码质量门槛、权限管控等问题。这个工作流的泛化能力存疑。
- **关联**：与 [[BV1ohDzBwEJN-Claude设计主管Cowork揭秘]] 中 Jenny 的视角形成互补——Jenny 侧重 Co（非技术用户的 AI 原生产品设计），Megan 侧重 Code（技术化的设计师直接写代码）。两人共同指向同一个趋势：**设计师正在获得代码能力，但路径不同**——Jenny 的路径是通过 Co 降低门槛，Megan 的路径是通过 Code 提升能力。

## 与其他知识的关联

- 相关概念：[[代码即最高保真]]、[[设计-开发桥梁]]、[[内部dogfooding]]、[[AI设计美学]]、[[上下文工程]]
- 相关实体：[[Easonlee的AI笔记]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题

- CLAUDE.md 作为"设计师的 AI 个性化层"——这种模式能否推广到其他角色（PM、运营、QA）？每个角色的 CLAUDE.md 长什么样？
- "代码即最高保真"的设计审查模式，对远程团队和异步协作有什么影响？Figma 的评论和标注功能在代码审查中如何替代？
- 设计师 push 代码的安全和质量边界在哪？Anthropic 模式在更大规模组织中如何适配？
- 当设计师和工程师都能写代码时，代码审查的权责如何划分？设计师的代码审查标准是否应该和工程师不同？
