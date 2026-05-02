---
type: practice_output
source_task: "用 EARS 格式重写现有需求"
source_bv: BV1VczqBREQ8
capability: 产品定义与规格设计
created: 2026-05-02
---

# EARS 需求：Registry 状态对账

## 原始需求

为 Sharkbase 增加 registry 与文件系统状态对账能力。

## EARS 需求

### R1 文件完整性判断

当系统发现某个 BV 的 5 个 operationalize 输出文件全部存在时，系统应当将该 BV 的 operationalize_status 标记为 done。

### R2 状态不一致识别

当 registry 中某个 BV 的 operationalize_status 为 done，但系统发现任一 operationalize 输出文件缺失时，系统应当将该 BV 标记为 inconsistent，并记录缺失文件列表。

### R3 部分文件存在判断

当系统发现某个 BV 的 operationalize 输出文件部分存在（1-4个）时，系统应当将该 BV 的 operationalize_status 标记为 partial，并列出缺失的输出类型。

### R4 dry-run 安全模式

当用户使用 --dry-run 参数运行 reconcile_registry.py 时，系统应当只输出将要修改的条目，不应写入 registry.json。

### R5 apply 写入模式

当用户使用 --apply 参数运行 reconcile_registry.py 时，系统应当将推断状态写回 registry.json，并记录 reconciled_at 时间戳。

### R6 指定 BV 对账

当用户在命令行指定一个 BV 号时，系统应当只对该 BV 执行对账，不扫描其他视频。

### R7 优先检测不一致

当 registry 中记录 operationalize_status 为 done 但文件系统检测到文件缺失时，系统应当优先判定为 inconsistent，而非 partial。

## 歧义消除对比表

| 原始描述 | 歧义点 | EARS 如何消除 |
|---|---|---|
| "状态对账" | 对什么状态？对什么做对账？ | 明确为 operationalize_status 与文件系统事实的对账 |
| "文件完整" | 哪些文件？什么叫完整？ | 明确为 5 个 operationalize 输出文件全部存在 |
| "修复 registry" | 修复什么字段？修复规则是什么？ | 明确为 operationalize_status + operationalize_outputs + missing_outputs |
| "检测不一致" | 不一致的优先级？和 partial 怎么区分？ | inconsistent 优先于 partial 判断（registry done 但文件缺失） |
| "安全模式" | dry-run 和 apply 的行为边界？ | dry-run 只读不写，apply 写入并记录时间戳 |

## 验收标准

- [ ] 每条需求都符合 EARS 句式（"当……时，系统应当……"）
- [ ] 需求中不含任何实现选型（技术栈、具体工具名）
- [ ] 一个没参与讨论的人阅读后能无歧义理解系统行为
- [ ] 至少识别出 5 个原始描述中的歧义点
