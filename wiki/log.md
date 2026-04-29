# 活动日志

> 按时间倒序排列，最新在前。格式：`## [日期] 操作类型 | 标题`

## 2026-04-29

### [tutorialize] 生成教学文章
- **时间**: 2026-04-29
- **变更**: 使用 Kimi API (moonshot-v1-auto) 通过 claude CLI 生成课程化教学文章
- **生成文章** (4): BV1SqDcBCEwW、BV1GBPGzSE4u、BV1D9ojBzEAd、BV1Y4oLBuEu6
- **输出目录**: `wiki/tutorials/`
- **新增脚本**: `scripts/tutorialize.py` + `scripts/tutorialize_prompt.md`
- **原理**: Kimi coding API 只允许 Coding Agent 访问，通过 claude CLI --print 模式设置 Kimi 的 Anthropic 兼容端点来调用

### [refactor] Wiki 深度重构
- **时间**: 2026-04-29
- **变更**: 模板重写 + 概念合并 + 主题重写 + 视频页加评注 + index.md 重建
- **删除概念** (10): GRPO、强化学习与可验证奖励、语言模型强化学习环境、Verifiers库、Google Stitch、Antigravity、Flutter、ReAct循环、Claude-Code架构、一人公司
- **新建概念** (2): RLVR训练范式（合并4个RL相关概念）、Google AI零代码工具链（合并3个Google工具概念）
- **重写概念** (4): 驾驭工程（吸收ReAct循环+Claude-Code架构）、MVP思维（吸收一人公司+跨领域共振）、MCP Server（加深判断和深层联系）
- **删除主题** (2): AI驱动移动应用开发、LLM强化学习训练
- **重写主题** (2): LLM-Agent工程实践（跨视频综合论证）、技术人创业与产品思维（环境偏见类比）
- **视频页更新** (4): 全部新增"我的评注"部分
- **index.md**: 从学术式空壳分类重建为实际维度（AI工程/创业与认知/核心概念）
- **概念数**: 13 → 6
- **主题数**: 4 → 2
- **核心改进**: 概念页从"百科词条"改为"思考笔记"（加"为什么重要"+"我的判断"+"深层联系"）；主题页从"视频摘要堆叠"改为"综合分析文章"（有核心主张+跨视频论证+开放分歧+我的立场）；视频页新增个人评注

## 2026-04-27

### [ingest] BV1Y4oLBuEu6 吃透Claude Code核心源码-架构设计与工程细节全解析
- **时间**: 2026-04-27
- **转录引擎**: sensevoice (chunk script)
- **创建页面**: `wiki/videos/BV1Y4oLBuEu6-吃透Claude-Code核心源码.md`
- **创建实体**: [[小韩]]（新建）
- **创建概念**: [[驾驭工程]]、[[ReAct循环]]、[[Claude-Code架构]]
- **更新概念**: [[MCP Server]]（追加Claude Code中的MCP实现细节）
- **创建主题**: [[LLM-Agent工程实践]]
- **备注**: 无metadata JSON，转录通过chunk脚本完成，视频约110分钟，内容极为丰富

### [ingest] BV1SqDcBCEwW 关于一人公司-也就是OPC的一些业务思考
- **时间**: 2026-04-27
- **转录引擎**: sensevoice
- **创建页面**: `wiki/videos/BV1SqDcBCEwW-关于一人公司也就是OPC的业务思考.md`
- **更新实体**: [[云途的AI之路]]（新建）
- **创建概念**: [[MVP思维]]、[[一人公司]]
- **创建主题**: [[技术人创业与产品思维]]
- **备注**: 视频约7分钟，核心探讨MVP思维、C端用户画像、营销驱动与一人公司运营

### [ingest] BV1D9ojBzEAd Deepset工程师-将小模型训练成特定领域大师
- **时间**: 2026-04-27
- **转录引擎**: sensevoice (chunk script)
- **创建页面**: `wiki/videos/BV1D9ojBzEAd-将小模型训练成特定领域大师.md`
- **更新实体**: [[Deepset]]（新建）
- **创建概念**: [[强化学习与可验证奖励]]、[[GRPO]]、[[Verifiers库]]、[[语言模型强化学习环境]]
- **创建主题**: [[LLM强化学习训练]]
- **备注**: 无metadata JSON，转录通过chunk脚本完成

## 2026-04-26

### [ingest] BV1GBPGzSE4u Antigravity+Flutter+Stitch打造惊艳移动应用
- **时间**: 2026-04-26 20:41
- **转录引擎**: sensevoice
- **创建页面**: `wiki/videos/BV1GBPGzSE4u-Antigravity-Flutter-Stitch打造惊艳移动应用.md`
- **更新实体**: [[GoldenSpiderAI]]（新建）
- **创建概念**: [[Google Stitch]]、[[Antigravity]]、[[Flutter]]、[[MCP Server]]
- **创建主题**: [[AI驱动移动应用开发]]
- **字符数**: ~5000
