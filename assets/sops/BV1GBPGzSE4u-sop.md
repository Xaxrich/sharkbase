---
type: asset_sop
bv: BV1GBPGzSE4u
title: "Antigravity+Flutter+Stitch打造惊艳移动应用"
source_type: tutorial
source_tutorial: "wiki/tutorials/BV1GBPGzSE4u-Antigravity+Flutter+Stitch打造惊艳移动应用.md"
capability: []
secondary_capability: []
status: draft
generated_at: 2026-05-01T14:00:10
model: moonshot-v1-auto
---

## SOP 1：Stitch + IDX + Flutter 全链路 App 构建

```
目标：从自然语言需求到手机上运行 App 的完整流程
前置条件：Google 账号、Stitch 访问权限、IDX 访问权限、Android 手机（或 iOS + Mac + Apple Developer 账号）

步骤：
1. 需求结构化
   - 确定App类型（展示型/轻交互型/重业务型）
   - 列出屏幕数量和每屏内容清单
   - 确定风格要求（明暗模式、设计密度、品牌色）
   - 找一个视觉风格参考网站URL

2. Stitch 设计生成
   - 按 prompt 模板撰写描述，提交生成
   - 预览移动端效果，检查关键元素完整性
   - 用 annotation 做局部修改（单次不超过3处，超过则重新生成整页）
   - 迭代至设计可用

3. MCP 配置
   - 获取 Stitch API Key → 在 IDX 中配置 Stitch MCP → 重启确认
   - 配置 Flutter MCP → 验证 Flutter SDK → 重启确认
   - 用"List my Stitch projects"验证连通性

4. IDX 代码生成
   - 按代码生成 prompt 模板向 IDX 下达指令
   - 等待 IDX 读取设计、生成代码、安装依赖
   - 启动浏览器预览，对照设计稿检查一致性

5. 内容替换
   - 扫描占位内容（假图片/假文字/假数据）
   - 获取真实素材，放入 assets 目录
   - 逐项替换，重新预览验证

6. 构建安装
   - 请求 IDX 执行 flutter build apk
   - 下载 APK 到手机安装
   - 真机验证：启动、布局、内容、基本交互

验收：
- App 在真机正常启动，无崩溃
- 关键页面与设计稿视觉一致
- 所有占位内容已替换为真实素材
- 基本交互（滚动、导航）正常
```

## Template：Stitch Prompt 模板

```markdown
Build me a [2/3/4]-screen mobile app for [App名称/活动名/产品名].

Screen 1 (Home): [logo位置], [标题文字], [核心内容区: 如可滚动的列表/卡片/网格], [底部导航栏如有]
Screen 2 (Detail): [标题区], [主图/头像], [描述信息], [操作按钮]
Screen 3 (如有): [内容描述]

Style: [dark/light] mode, [minimal/bold/elegant] design, primary color: [#色值 或 品牌名]
Font: [字体偏好 或 "default"]
Branding: [品牌名, 如 "Google Cloud" / "无特定品牌"]

Reference website: [URL — 此项强烈建议填写，控制输出风格的关键]
```
