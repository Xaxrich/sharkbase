---
type: video
bv: BV1HwdjBHENb
title: "Claude Code实战：鲜为人知的 Claude Code 工作流"
uploader: Easonlee的AI笔记
url: https://www.bilibili.com/video/BV1HwdjBHENb
date: 2026-04-30
duration: 35:00
tags: [Claude Code, 落地页设计, AI工作流, A/B测试, MCP]
concepts: [Vibe Coding, 上下文工程, 主动式Agent]
entities: [Easonlee的AI笔记]
topics: [LLM-Agent工程实践]
---

# Claude Code实战：鲜为人知的 Claude Code 工作流

## 一句话摘要

演示了一条从创意验证到落地页设计、上线、A/B测试的完整AI工作流，核心思路是用Claude Code作为中枢，串联Idea Browser、Paper、Tailar、分析工具，形成"创意→设计→代码→数据→优化"的闭环。

## 核心观点

- **Agent即CMS**：未来网站应该是自定义代码构建，Agent直接管理内容更新，而非依赖Webflow/Framer等封闭平台
- **约束比自由更重要**：给Claude的指令要用"subtle""refine"等具体约束词，而非泛泛的"improve the design"，这样产出质量高得多
- **设计系统先行**：先给Claude参考截图，让它提取关键设计元素生成设计系统，后续所有组件基于同一系统构建，避免vibe code的杂乱感
- **工具链闭环**：Idea Browser管创意→Paper管设计迭代→Claude Code管代码→分析工具管数据→Idea Browser管增长记录，数据回流驱动下一轮优化
- **时间不可省略**：即使有最好的工具链，一个精致的落地页仍需数小时迭代，一键出图不存在

## 详细笔记

### 从创意到落地页

1. **Idea Browser + MCP**：Idea Browser作为MCP接入Claude Code，直接拉取项目上下文（目标客户、价值主张、话术等），无需手动复制粘贴
2. **Lead Magnet技能**：基于项目上下文，使用"Lead Magnet Legend"技能自动生成铅磁内容（如"5个毁掉SaaS订单的异议"PDF指南）
3. **活动 streak 机制**：Idea Browser用streak机制推动持续构建，解决"有想法但不知道下一步做什么"的问题

### 设计迭代：Paper的角色

- **Paper是什么**：连接Claude Code的设计迭代工具，填补了"Figma出图→工程实现"之间的空白
- **工作方式**：Claude Code生成设计→Paper中创建多版本迭代→选择方向→回写到代码
- **对比Figma**：Figma刚推出双向API/MCP，但Paper的工具体验更好、更成熟
- **核心价值**：避免直接在代码里反复试错，先在设计层面低成本探索方向

### 设计质量：如何避免Vibe Code感

1. **参考截图驱动设计系统**：截取喜欢的网站截图丢给Claude，让它提取关键元素→生成设计风格指南→后续组件基于该指南构建
2. **Tailar组件库**：Tailar Pro提供大量现成block/插画/组件，截图导入Claude Code后可直接安装使用
3. **约束词策略**：
   - 用"subtle animation"而非"add animation"
   - 用"refine the design, consistent layouts, cohesive"而非"improve the design"
   - Claude对具体约束的响应远优于宽泛指令
4. **迭代流程**：找参考组件→截图→导入Paper→Claude Code安装组件→在Paper中调整→回写代码

### 上线与A/B测试

- **推送即上线**：Claude Code push后直接更新网站，无需部署流程
- **分析工具接入**：通过MCP/Skills连接分析平台，获取流量、滚动深度、点击热力图、漏斗数据
- **A/B实验**：
  - Claude Code直接调用API创建实验
  - 动态更新页面内容，无需开发者介入
  - 可实时查看控制组vs变体组的转化数据
- **自动化CRON**：Claude Code支持定时任务，每周自动拉取Google Ads/Meta数据→运行A/B测试→生成漏斗报告→给出优化建议
- **数据回流Idea Browser**：增长数据作为文件写回Idea Browser，形成跨时间的复合增长视图

### 关于未来的判断

- **Agent将比人类更多访问网站**：Gartner预测2030年20%的电商将由Agent完成
- **Agent税**：政府可能对Agent征收类似薪资税的税收，因为Agent本质是劳动力替代
- **网站应Agent友好**：Cloudflare已推出Agent爬取端点，网站需要考虑Agent可访问性
- **自定义代码网站是方向**：Humblely从Webflow→Framer→自定义代码的迁移路径，核心驱动力是让Agent成为CMS

## 我的评注

- **赞同**：约束词策略非常实用，"subtle""refine"这类具体指令确实是提升Claude设计输出的关键杠杆，这个洞察比具体的工具链更重要
- **赞同**：设计系统先行的思路正确——先建立约束再生成，比事后修补效率高得多
- **质疑**：视频标题"鲜为人知的工作流"有些夸大，本质是MCP串联+参考驱动设计，并非颠覆性方法论；真正的know-how在审美判断和迭代耐心上，工具本身并不稀缺
- **质疑**：Agent即CMS的论断在营销网站成立，但复杂内容工作流（权限、审批、版本回滚）仍需传统CMS，视频忽略了这些约束
- **关联**：与[[Vibe Coding]]概念直接相关——视频本质上在回答"如何让vibe coding产出不像vibe code"，答案是约束系统+参考驱动+迭代打磨

## 与其他知识的关联

- 相关概念：[[Vibe Coding]]、[[上下文工程]]、[[主动式Agent]]
- 相关主题：[[LLM-Agent工程实践]]

## 待深入问题

- 约束词策略是否有系统化的最佳实践？哪些词对Claude的设计输出影响最大？
- A/B测试自动化在实际业务中的置信度问题：Claude给出的"变体建议"质量如何保障？
- Agent友好网站的架构模式是什么？与传统的SEO/可访问性设计有何异同？
- 自定义代码+Agent CMS的模式在团队协作场景下如何处理权限和冲突？
