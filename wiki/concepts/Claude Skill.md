---
type: concept
name: Claude Skill
tags: [Claude, 工作流自动化, MCP, 提示工程]
first_seen: 2026-04-30
---

# Claude Skill

## 定义
Anthropic 推出的可编程工作流机制：由 Markdown 指令文件、引用文件和脚本代码组成，可全局、项目级或个人级加载，用于自动化重复性任务。

## 为什么重要
它解决了 Projects + LLM 自由发挥的核心痛点：在 Claude Project 中上传数据、写系统指令，LLM 自行决定如何分析——每次结果不同，且经常不是用户想要的。Skill 的三层结构（指令+引用+脚本）把专家的隐性知识编码为显式规则，同时用脚本替代 LLM 的非确定性推理。类比：Project 是给 AI 一个办公室和一堆资料，Skill 是给 AI 一份标准操作手册。

## 我的判断
Skill 是"约束中激发能力"在产品层面的落地。它和 [[MCP Server]] 互补：MCP 解决"AI 能调用什么工具"，Skill 解决"AI 用什么流程调用这些工具"。但视频未说清 Skill 与 Plugin 的区别，这是当前文档的空白。风险在于：Skill 的质量完全取决于编写者对任务的拆解能力——糟糕的 Skill 和糟糕的提示词一样无济于事。

Felix 的补充让 Skill 的定位更清晰：它是通用工具和确定性脚本之间的中间路线——用 Markdown 描述意图（通用），用脚本处理确定性部分（可靠）。而且 Skills 的"可分享"特性使其不只是个人效率工具，而是团队和组织对齐 AI 行为的标准方式——"不是一切都该即时生成，有些事你要和一群人用同一种方式反复做"。

## 深层联系
- [[驾驭工程]] — Skill 是驾驭工程在 Claude 产品生态中的标准化载体
- [[MCP Server]] — MCP 提供工具能力，Skill 定义使用流程；两者组合 = 可重复的自动化工作流
- [[上下文工程]] — Skill 的按需加载机制是上下文工程的工程化实现
- [[Vibe Building]] — Skills 把 vibe building 从随意变为系统化：前期构建 Skill 的投入在每次产出中复用

## 来源
- [[BV1LfmHBuEzt-Claude Skill实战创建AI团队]] — 完整介绍 Skill 的概念、结构与四个实战案例
- [[BV1AwveBXEBE-Claude 4.5 vs Gemini 3 Pro测评]] — 补充 frontend design skill 的安装与效果，以及品牌 voice skill + 转化架构 skill 的构建路径
- [[BV1G3zXBPEUk-ClawdBot席卷硅谷最新AI工具]] — 补充内部 Skill 用法（品牌文档 skill、写作 skill 去 AI 味），以及"个人笔记文件夹作为隐性记忆替代 Skills"的观点——当 Co 能持续读取你的笔记文件夹时，对显式 Skill 的需求降低
- [[BV1xEzqBVEeb-ClaudeCowork是我们所有人的ClaudeCode]] — Felix（Anthropic）确认 Skills 是当前最核心的可定制面，Cowork 自动加载 Claude Code 的 Skills；Opus 4.5 极擅长遵循 Skill 指令；Ken 演示了 Deep Research → Skill 创建工作流和 Swiss Design + 3D Print 双 Skill 组合
- [[BV1QeZ2BZEFZ-Claude Code实战复合工程让AI越用越懂你]] — Karel 对 Skills 的定位是"即时上下文注入"——当 AI 需要某领域知识时才加载，避免一次性灌入所有信息杀死上下文；Skills 内可包含脚本扩展 Claude Code 本身不具备的能力（如图片生成）；Compound Engineering 插件会读取项目级 Skills 并在规划中应用

## 相关主题
- [[LLM-Agent工程实践]]
