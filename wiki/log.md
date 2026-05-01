# 活动日志

> 按时间倒序排列，最新在前。格式：`## [日期] 操作类型 | 标题`

## 2026-05-01

### [batch] "AI工具实践"系列批量处理
- **时间**: 2026-05-01
- **系列**: AI工具实践 (Easonlee的AI笔记)，73个视频
- **分类**: A级34个（深度技术/方法论）、B级29个（实战教程）、C级10个（短评，跳过）
- **转录**: 70/73 成功，2失败（BV19MzXBNESV、BV1G3zXBPEUk 超时），1跳过
- **Wiki页面**: 65个视频页面（去重后）
- **教学文章**: 63个教程文章
- **工具**: batch_ingest.py — 分块SenseVoice转录 + Kimi API生成wiki/教程
- **已知问题**: Kimi API部分调用失败（exit 1），部分wiki页面内容较短（200-500字符截断）

## 2026-04-30

### [ingest] BV162rNBDE26 "Nano Banana教程：15分钟内创建与您的品牌相符的精美信息图表"
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文视频，15分钟）
- **创建页面**: `wiki/videos/BV162rNBDE26-Nano Banana品牌信息图表教程.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，30→31视频，追加风格指南工程化关注点）
- **更新概念**: [[AI设计美学]]（追加风格指南来源和上下文工程深层联系）、[[AI驱动的产品工作流]]（追加品牌资产自动化深层联系）
- **更新主题**: [[AI与生产力]]（追加"风格指南：把隐性设计知识编码为显式提示词"章节，video_count 3→4）
- **更新**: index.md（视频总数 38→39）

### [ingest] BV1TRvYBtEfD "创作点子：快来抄作业！10款月收入超过5万美元的未知应用"
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文视频，33分钟）
- **创建页面**: `wiki/videos/BV1TRvYBtEfD-10款月入5万美元的未知应用.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，29→30视频，追加选品框架关注点）
- **创建概念**: [[AI微应用]]、[[高意图输入]]
- **更新概念**: [[AI原生商业模式]]（追加微应用实证来源）、[[乘风策略]]（追加ASO作为搜索意图便车来源）
- **更新主题**: [[技术人创业与产品思维]]（追加"从神经出发：选品的方法论化"章节，video_count 7→8）
- **更新**: index.md（视频总数 37→38，概念数 48→50）

### [ingest] BV1ZqBgBHEfM "没有AI我无法完成工作"：这位产品经理如何将Claude + ChatGPT作为他的第二大脑
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，38分钟）
- **创建页面**: `wiki/videos/BV1ZqBgBHEfM-AI第二大脑产品经理.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，28→29视频，更新风格描述）
- **更新概念**: [[第二大脑]]（追加多Project架构来源）、[[AI驱动的产品工作流]]（追加PM全链路工作流来源）、[[上下文工程]]（追加多Project上下文隔离和"一切皆文本"方法论来源）
- **更新主题**: [[LLM-Agent工程实践]]（追加"PM的多线程存在"章节，video_count 21→22）
- **更新**: index.md（视频总数 36→37）

### [ingest] BV1irBgBUEAe Vibe Coding实践：101款你可以Vibe Code的AI应用
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文视频，28分钟）
- **创建页面**: `wiki/videos/BV1irBgBUEAe-VibeCoding实践101款AI应用.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，27→28视频，更新风格描述）
- **更新概念**: [[Vibe Coding]]（追加七类101应用和五步框架来源）、[[Vibe Building]]（追加应用全景印证来源）
- **更新**: index.md（视频总数 35→36）

### [ingest] BV1pwS1BpEDU OpenAI研究员：AI评估，从前沿研究到生产应用
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（OpenAI Dev Day 演讲，Tail + Henry，21分钟）
- **创建页面**: `wiki/videos/BV1pwS1BpEDU-OpenAI研究员AI评估从前沿研究到生产应用.md`
- **更新概念**: [[AI评估体系]]（追加第三来源视频）
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，27→28视频）
- **备注**: GDPVal 前沿评估 + 产品化评估工具链。与 BV1gXqLBXE87 互补——本视频是 OpenAI 前沿研究视角，后者是 PM 实操视角

### [ingest] BV1ZvSqBoEoa 6个创建Agent平台测评，哪个最好用？
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文视频，30分钟，实际内容为Andrew Ng Agent AI课程精要）
- **创建页面**: `wiki/videos/BV1ZvSqBoEoa-Andrew-Ng-Agent-AI课程精要.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，26→27视频）
- **备注**: 视频标题与内容不符——标题暗示6个平台测评，实际内容是Andrew Ng 8小时Agent AI课程的浓缩笔记。核心贡献：Agent自主性谱系框架、Evals四象限分类、四种设计模式（Reflection/Tool Use/Planning/Multi-Agent）

### [ingest] BV14HndzMEZ1 Claude Code + Figma：Claude的设计主管这么用的
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，39分钟）
- **创建页面**: `wiki/videos/BV14HndzMEZ1-Claude-Code-plus-Figma-Claude的设计主管这么用的.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，25→26视频，更新风格描述和概念链接）
- **创建概念**: [[代码即最高保真]]（代码是设计交付的最高保真形式，Draft PR替代Figma mock）、[[设计-开发桥梁]]（设计师与工程师从"交接"转向"融合"）
- **更新**: index.md（视频总数 32→33，概念数 46→48）

### [ingest] BV1HwdjBHENb Claude Code实战：鲜为人知的 Claude Code 工作流
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，35分钟）
- **创建页面**: `wiki/videos/BV1HwdjBHENb-Claude Code实战工作流.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，25→26视频，更新风格描述）
- **更新主题**: [[LLM-Agent工程实践]]（追加"AI驱动增长闭环"章节，video_count 20→21）
- **更新**: index.md（视频总数 31→32）

### [ingest] BV1jFAHzCEMw GPT 5.4测评：OpenAI 王者归来
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文直播，78分钟）
- **创建页面**: `wiki/videos/BV1jFAHzCEMw-GPT5.4测评OpenAI王者归来.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，22→25视频，更新风格描述）
- **创建概念**: [[模型驾驶风格]]（不同LLM的系统性行为倾向）、[[代码组织与可维护性]]（模块化程度直接影响后续Agent审查能力）、[[AI设计美学]]（不同LLM生成UI设计的系统性审美倾向）
- **更新主题**: [[LLM-Agent工程实践]]（追加"GPT 5.4：OpenAI 追平的实证"视角，video_count 19→20）
- **更新**: index.md（视频总数 30→31，概念数 43→46）

### [ingest] BV1D1w3zMEur Intuition CEO：AI革命不是软件 是农场、矿山和卡车
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，84分钟）
- **创建页面**: `wiki/videos/BV1D1w3zMEur-Intuition CEO：AI革命不是软件 是农场、矿山和卡车.md`
- **创建实体**: [[Qasar Younis]]（新建，Applied Intuition CEO）、[[Applied Intuition]]（新建，物理AI公司）
- **创建概念**: [[物理AI]]（给已有机器注入智能而非造人形机器人）、[[激进实用主义]]（去情绪化决策+安静做事+最佳想法胜出）
- **更新主题**: [[技术人创业与产品思维]]（追加"激进实用主义"章节，video_count 6→7）
- **更新**: index.md（视频总数 29→30，概念数 41→43）

### [ingest] BV1VFczzSEsn OpenClaw实战：21个绝佳使用案例
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文视频，33分钟）
- **创建页面**: `wiki/videos/BV1VFczzSEsn-OpenClaw实战21个绝佳使用案例.md`
- **更新概念**: [[复利工程]]（追加用例间复利效应来源）、[[个人操作系统]]（追加21用例全景图来源）、[[主动式Agent]]（追加量产化与安全张力来源）、[[提示注入]]（追加混合防御策略来源）
- **更新**: index.md（视频总数 28→29）

### [ingest] BV1mncRznEd6 Ghostty创始人：我现在如何用AI写代码？
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，118分钟）
- **创建页面**: `wiki/videos/BV1mncRznEd6-Ghostty创始人如何用AI写代码.md`
- **创建实体**: [[Mitchell Hashimoto]]（新建，HashiCorp联合创始人、Ghostty创建者）
- **创建概念**: [[开源信任系统]]（AI击溃开源"默认允许"模型，担保系统+连带封禁）
- **更新概念**: [[AI Agent自验证循环]]（追加harness工程视角来源）、[[驾驭工程]]（追加维护者视角实践来源）
- **更新主题**: [[LLM-Agent工程实践]]（追加"Harness工程维护者视角与开源信任重建"章节，video_count 18→19）
- **更新**: index.md（视频总数 27→28，概念数 40→41）

### [ingest] BV1NscRzUEia OpenClaw实战：养虾指南！打造你的数字员工
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文视频，40分钟）
- **创建页面**: `wiki/videos/BV1NscRzUEia-OpenClaw实战养虾指南.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，21→22视频，更新风格描述）
- **更新概念**: [[个人操作系统]]（追加"全职员工"跃迁来源）、[[主动式Agent]]（追加低置信度升级和自愈循环来源）、[[提示注入]]（追加三层防御工程化实现来源）、[[上下文工程]]（追加分话题频道隔离和双提示词栈来源）、[[驾驭工程]]（追加生产级实例来源）
- **更新**: index.md（视频总数 26→27）

### [ingest] BV1Sef8BmEU3 Vibe Code实战：8小时马拉松！顶级AI开发者现场演示
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文直播，464分钟）
- **创建页面**: `wiki/videos/BV1Sef8BmEU3-VibeCode实战8小时马拉松.md`
- **创建概念**: [[Vibe Coding]]、[[自主循环开发]]
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，20→21视频，更新风格描述）
- **更新概念**: [[复利工程]]（追加多位实践者验证）、[[Agent原生架构]]（追加 Proof/Notion 集成实证）
- **更新主题**: [[LLM-Agent工程实践]]（追加"Vibe Coding 从原型到生产"视角，video_count 17→18）
- **更新**: index.md（视频总数 25→26，概念数 38→40）

### [ingest] BV1QeZ2BZEFZ Claude Code实战：复合工程，让AI越用越懂你
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文直播，53分钟）
- **创建页面**: `wiki/videos/BV1QeZ2BZEFZ-Claude Code实战复合工程让AI越用越懂你.md`
- **创建实体**: [[Karel]]（新建，Cora CTO，Compound Engineering 哲学提出者）
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，19→20视频，更新风格描述）
- **更新概念**: [[复利工程]]（追加完整实操演示来源）、[[Claude Skill]]（追加"即时上下文注入"定位和脚本扩展能力）、[[Agent原生架构]]（追加Karel的Cora实践和审查视角）、[[上下文工程]]（追加子Agent独立上下文和Skills即时加载的工程化实现）
- **更新主题**: [[LLM-Agent工程实践]]（追加"复合工程闭环"小节，video_count 16→17）
- **更新**: index.md（视频总数 24→25）

### [ingest] BV1hkFkz9E6N Claude：如何让AI 直接做待办事项
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文直播，45分钟）
- **创建页面**: `wiki/videos/BV1hkFkz9E6N-Claude如何让AI直接做待办事项.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，18→19视频，更新风格描述和概念链接）
- **创建概念**: [[上下文智能]]、[[复利规划]]、[[任务即子Agent]]
- **更新概念**: [[上下文工程]]（追加上下文智能vs上下文工程区分）、[[主动式Agent]]（追加任务即子Agent关联）
- **更新主题**: [[LLM-Agent工程实践]]（追加"任务系统与上下文智能"小节，video_count 15→16）
- **更新**: index.md（视频总数 23→24，概念数 35→38）

### [ingest] BV1xEzqBVEeb Claude Cowork : Claude Cowork 是我们所有人的 Claude Code
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文直播，92分钟）
- **创建页面**: `wiki/videos/BV1xEzqBVEeb-ClaudeCowork是我们所有人的ClaudeCode.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，17→18视频，更新风格描述）、[[Every]]（追加视频）
- **创建概念**: [[异步Agent范式]]、[[Agent原生架构]]
- **更新概念**: [[Claude Skill]]（追加 Felix 确认 Skills 为最核心可定制面、Opus 4.5 遵循能力、Deep Research→Skill 创建工作流）、[[驾驭工程]]（追加 Cowork 验证"同一 Harness 不同 UI"策略和 Agent 原生架构四原则）
- **更新主题**: [[LLM-Agent工程实践]]（追加"异步 Agent 范式"小节，video_count 14→15）
- **更新**: index.md（视频总数 22→23，概念数 33→35）

### [re-ingest] BV1UZqLBJEH1 Cursor主管演示：50分钟从新手到精通Cursor
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，50分钟）
- **变更**: 用户重新提供转录稿要求生成页面，发现知识库已有此视频。清理重复页面（删除2个重复文件），更新原页面的概念链接（移除不存在的 [[Cursor Rules]] 和 [[Vibe Coding与工程实践的边界]]，替换为已有概念），更新 registry.json 中的 wiki_page 路径
- **删除文件**: `wiki/videos/BV1UZqLBJEH1-Curosr主管演示：50分钟从新手到精通Cursor.md`、`wiki/videos/BV1UZqLBJEH1-Cursor从新手到精通.md`
- **更新**: registry.json（wiki_page 路径修正）

### [ingest] BV1Ru4QzHEZR Chat PRD: 产品经理是这么用AI的
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，66分钟）
- **创建页面**: `wiki/videos/BV1Ru4QzHEZR-ChatPRD产品经理与AI.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，15→16视频，更新风格描述）
- **创建概念**: [[AI驱动的产品工作流]]、[[AI原生商业模式]]
- **更新概念**: [[原型优先开发]]（追加"原型经理"概念和独立开发者质量论来源）
- **更新**: index.md（视频总数 20→21，概念数 31→33）

### [ingest] BV1paf9BTEBk OpenClaw：现场演示如何使用
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，35分钟）
- **创建页面**: `wiki/videos/BV1paf9BTEBk-OpenClaw现场演示如何使用.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，14→15视频，更新风格描述）
- **创建概念**: [[主动式Agent]]、[[提示注入]]
- **更新概念**: [[上下文工程]]（追加"入职培训"作为上下文工程极致应用来源）、[[AI Agent自验证循环]]（追加主动式Agent的自验证实践来源）、[[智能体分工]]（追加模型层分工实证来源）
- **更新主题**: [[LLM-Agent工程实践]]（追加"主动式Agent：从工具到员工的思维跃迁"小节，video_count 13→14）
- **更新**: index.md（视频总数 19→20，概念数 29→31）

### [ingest] BV1G3zXBPEUk ClawdBot：席卷硅谷! 最新AI工具
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，27分钟）
- **创建页面**: `wiki/videos/BV1G3zXBPEUk-ClawdBot席卷硅谷最新AI工具.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，13→14视频，更新风格描述）
- **创建概念**: [[AI驱动的产品设计工作流]]、[[内部dogfooding]]
- **更新概念**: [[原型优先开发]]（追加 Claude Co 线框图实践来源）、[[Claude Skill]]（追加内部 Skill 用法和个人笔记文件夹替代 Skills 观点）、[[智能体分工]]（追加 Claude Co vs Claude Code 分工实证）
- **更新主题**: [[LLM-Agent工程实践]]（追加"AI 产品设计中的引导 vs 自由张力"小节，video_count 12→13）
- **更新**: index.md（视频总数 18→19，概念数 27→29）

### [ingest] BV1GAzqBWEWx AI产品经理：如何用AI做原型设计、战略和个人OS
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，51分钟）
- **创建页面**: `wiki/videos/BV1GAzqBWEWx-AI产品经理如何用AI做原型设计战略和个人OS.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，12→13视频，更新风格描述）
- **创建概念**: [[原型优先开发]]、[[个人操作系统]]
- **更新概念**: [[上下文工程]]（追加三位PM的上下文管理系统来源）、[[第二大脑]]（追加个人操作系统关联）、[[源码锚定]]（追加三位PM的markdown锚点实践来源）
- **更新主题**: [[LLM-Agent工程实践]]（追加"原型优先与个人OS"小节，video_count 11→12）
- **更新**: index.md（视频总数 17→18，概念数 25→27）

### [ingest] BV1VczqBREQ8 亚马逊Kiro团队：规范驱动开发
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文演讲，63分钟）
- **创建页面**: `wiki/videos/BV1VczqBREQ8-亚马逊Kiro团队规范驱动开发.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，11→12视频，更新风格描述）
- **创建概念**: [[规范驱动开发]]、[[基于属性的测试]]
- **更新概念**: [[AI Agent自验证循环]]（追加 EARS→属性测试贯穿线来源）、[[确定性输出]]（追加规范驱动开发和属性测试关联）、[[驾驭工程]]（追加规范驱动开发作为工作流层实现）
- **更新主题**: [[LLM-Agent工程实践]]（追加"规范驱动开发"小节，video_count 10→11）
- **更新**: index.md（视频总数 16→17，概念数 23→25）

### [ingest] BV1xHrMBvEYT Claude Code 实战：如何成为一名10倍效率的vibe coder？
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，33分钟）
- **创建页面**: `wiki/videos/BV1xHrMBvEYT-Claude Code实战vibe coder效率指南.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，10→11视频，更新风格描述）
- **更新概念**: [[智能体分工]]（追加双工具并行实证来源）、[[微交互设计]]（追加 AI 迭代构建动画的实证）、[[驾驭工程]]（追加 Plan Mode 和 ultrathink 作为约束实例）、[[思考模式]]（追加 Plan Mode 作为工具化实现来源）
- **更新主题**: [[LLM-Agent工程实践]]（追加"工具配置与微操技巧"论据，video_count 9→10）
- **更新**: index.md（视频总数 15→16）

### [ingest] BV1ptrMBhE2X 从零开始构建一个百万美元SaaS的蓝图
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，61分钟）
- **创建页面**: `wiki/videos/BV1ptrMBhE2X-百万美元SaaS蓝图.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，9→10视频，更新风格描述）
- **创建概念**: [[乘风策略]]、[[AI搜索优化]]
- **更新主题**: [[技术人创业与产品思维]]（追加"获客能力"论据，video_count 4→5）
- **更新**: index.md（视频总数 14→15，概念数 21→23）

### [ingest] BV1AwveBXEBE Claude 4.5 vs Gemini 3 Pro：测评
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，59分钟）
- **创建页面**: `wiki/videos/BV1AwveBXEBE-Claude 4.5 vs Gemini 3 Pro测评.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，8→9视频，更新风格描述）
- **创建概念**: [[Vibe Building]]
- **更新概念**: [[Claude Skill]]（追加 frontend design skill 来源和 Vibe Building 联系）
- **更新主题**: [[LLM-Agent工程实践]]（追加"多模型协作与 Vibe Building"小节，video_count 8→9）
- **更新**: index.md（视频总数 13→14，概念数 20→21）

### [ingest] BV1f3veB1EE5 我如何将应用程序设计得好10倍（免费课程）
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，47分钟）
- **创建页面**: `wiki/videos/BV1f3veB1EE5-应用程序设计十倍提升.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，7→8视频，更新风格描述）
- **创建概念**: [[微交互设计]]、[[设计曝光]]
- **更新主题**: [[技术人创业与产品思维]]（追加"设计即营销"论据，video_count 3→4）、[[AI与生产力]]（追加AI平民化设计视角，video_count 2→3）
- **更新**: index.md（视频总数 12→13，概念数 18→20）

### [ingest] BV1FgveB7Ebx Claude Code实战：如何将个人产出提高15倍
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，53分钟）
- **创建页面**: `wiki/videos/BV1FgveB7Ebx-Claude Code实战如何将个人产出提高15倍.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频，6→7视频，更新风格描述）
- **创建概念**: [[复利工程]]、[[智能体分工]]
- **更新概念**: [[驾驭工程]]（追加复利工程关联）、[[上下文工程]]（追加自定义命令的上下文自动化实现）
- **更新**: index.md（视频总数 11→12，概念数 16→18）

### [ingest] BV1zvBgBXE5E AI评估实战：50分钟，AI评估大师课
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，52分钟）
- **创建页面**: `wiki/videos/BV1zvBgBXE5E-AI评估实战50分钟AI评估大师课.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频、更新风格描述，5→6视频）
- **更新概念**: [[AI评估体系]]（追加Nurture Boss来源和一致率陷阱）、[[LLM-as-Judge]]（追加一致率陷阱、二元评分、混淆矩阵等贡献）
- **更新**: index.md（视频总数 10→11）

### [ingest] BV1gXqLBXE87 AI评估实战：50分钟，AI评估完整入门课程
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，51分钟）
- **创建页面**: `wiki/videos/BV1gXqLBXE87-AI评估实战50分钟完整入门课程.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频、更新风格描述，4→5视频）
- **创建概念**: [[AI评估体系]]、[[LLM-as-Judge]]
- **更新概念**: [[确定性输出]]（追加LLM数学能力差案例）、[[AI Agent自验证循环]]（追加与AI评估体系的互补关系）
- **更新主题**: [[LLM-Agent工程实践]]（填补"评估体系"空白，video_count 6→7）
- **更新**: index.md（视频总数 9→10，概念数 14→16）

### [ingest] BV1VUqLBxEWg NotebookLM：30分钟实战，AI时代的知识管理利器
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文视频，30分钟）
- **创建页面**: `wiki/videos/BV1VUqLBxEWg-NotebookLM实战AI时代知识管理利器.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频、更新风格描述，3→4视频）
- **创建概念**: [[源码锚定]]
- **更新概念**: [[第二大脑]]（追加NotebookLM来源）、[[MVP思维]]（追加NotebookLM实践案例）
- **更新主题**: [[AI与生产力]]（追加"向外蒸馏"小节，video_count 1→2）、[[技术人创业与产品思维]]（追加来源视频，video_count 2→3）
- **更新**: index.md（视频总数 8→9，概念数 13→14）

### [ingest] BV1UZqLBJEH1 Cursor主管演示：50分钟从新手到精通Cursor
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，50分钟）
- **创建页面**: `wiki/videos/BV1UZqLBJEH1-Cursor主管演示从新手到精通.md`
- **创建实体**: [[Lee Robinson]]（新建）
- **更新实体**: [[Easonlee的AI笔记]]（追加视频、更新风格描述，2→3视频）
- **创建概念**: [[AI Agent自验证循环]]
- **更新主题**: [[LLM-Agent工程实践]]（追加"Cursor Rules 与自验证"小节，video_count 5→6）
- **更新**: index.md（视频总数 7→8，概念数 12→13）

### [ingest] BV19tqjBZEWD Vibe Coding实战：40 分钟从原型到真正的 SaaS 应用
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，39分钟）
- **创建页面**: `wiki/videos/BV19tqjBZEWD-Vibe Coding实战从原型到SaaS应用.md`
- **更新实体**: [[Easonlee的AI笔记]]（追加视频、更新风格描述）
- **更新概念**: [[上下文工程]]（追加SaaS模板上下文场景）、[[确定性输出]]（追加模板约束场景）
- **更新主题**: [[LLM-Agent工程实践]]（追加"Vibe Coding 的安全陷阱"小节，video_count 4→5）
- **更新**: index.md（视频总数 6→7）

### [ingest] BV1LfmHBuEzt Claude Skill实战：创建一个AI团队
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，33分钟）
- **创建页面**: `wiki/videos/BV1LfmHBuEzt-Claude Skill实战创建AI团队.md`
- **创建实体**: [[Easonlee的AI笔记]]（新建）
- **创建概念**: [[上下文工程]]、[[确定性输出]]、[[Claude Skill]]
- **更新主题**: [[LLM-Agent工程实践]]（追加"Skill：从提示约束到工作流约束"小节，video_count 3→4）
- **更新**: index.md（视频总数 5→6，概念数 9→12）

## 2026-04-30

### [ingest] BV15UndzSE6x Claude Code + Obsidian：打造第二大脑
- **时间**: 2026-04-30
- **来源**: 用户提供转录稿（英文播客，71分钟）
- **创建页面**: `wiki/videos/BV15UndzSE6x-Claude Code与Obsidian打造第二大脑.md`
- **创建实体**: [[Noah Brier]]（新建）、[[Every]]（新建）
- **创建概念**: [[第二大脑]]、[[思考模式]]、[[非确定性直觉]]
- **创建主题**: [[AI与生产力]]
- **更新主题**: [[LLM-Agent工程实践]]（追加"实践中的驾驭工程"小节，video_count 2→3）
- **更新**: index.md（视频总数 4→5，概念数 6→9，主题数 2→3）

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
