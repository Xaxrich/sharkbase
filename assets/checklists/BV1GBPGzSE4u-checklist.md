---
type: asset_checklist
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

## Stitch 设计质量检查清单

- [ ] 设计稿包含 prompt 中描述的所有关键 UI 元素
- [ ] 每屏布局在移动端预览中无溢出、遮挡或截断
- [ ] 配色方案与参考网站风格一致（色差在可接受范围）
- [ ] 字体层级清晰（标题/正文/辅助文字有明确区分）
- [ ] 可滚动区域滚动流畅，无卡顿
- [ ] 品牌元素（logo、品牌色）正确出现
- [ ] 导航逻辑合理，屏幕间有清晰的返回/切换路径
- [ ] 单屏 annotation 修改不超过 3 处（超过则重新生成整页）

## MCP 配置验证清单

- [ ] Stitch API Key 已获取且未过期
- [ ] IDX 中 Stitch MCP 面板显示"Connected"或"Running"
- [ ] IDX 中"List my Stitch projects"返回正确项目列表
- [ ] Flutter SDK 已安装，`flutter --version` 可执行
- [ ] Flutter MCP 面板显示"Connected"或"Running"
- [ ] IDX 能识别 Flutter 项目结构（pubspec.yaml 存在，依赖可安装）
- [ ] MCP 配置后已重启 IDX
- [ ] 两个 MCP Server 同时在线且无报错

## 代码生成质量检查清单

- [ ] 生成的项目结构符合 Flutter 标准（lib/、assets/、pubspec.yaml）
- [ ] 浏览器预览中布局与 Stitch 设计稿基本一致
- [ ] 无编译错误，所有依赖正确安装
- [ ] 导航/路由可用，屏幕间可切换
- [ ] 占位内容已识别并标记（假图片、占位文字、硬编码数据）
- [ ] 代码中无明显的安全硬伤（明文密钥、无验证的用户输入）
- [ ] 可滚动列表滚动流畅，无渲染异常

## App 上线前检查清单

- [ ] 所有占位内容已替换为真实素材
- [ ] 真机上启动无崩溃
- [ ] 关键页面布局在主流 Android 尺寸下正确（小屏/大屏）
- [ ] 图片加载正常，无防盗链失败
- [ ] 基本交互（滚动、点击、导航）响应正常
- [ ] APK 包大小合理（展示型 App 不超过 30MB）
- [ ] 无调试模式残留（debug banner 已移除）
- [ ] 已评估是否需要进一步代码审查后再上生产（AI 生成代码 ≠ 生产代码）
