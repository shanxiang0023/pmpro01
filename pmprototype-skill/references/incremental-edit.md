# 增量修改协议

用户改需求、改视觉时遵守。目标：**不抽卡**。

## 禁止

- 收到「把按钮改大」「加一列」→ 整文件或整页重新 `use_figma`  
- 不更新 plan/yaml 直接改画布  
- Anti-Slop 曾 FAIL 的项在修改中重新引入（如改回 Inter、#6366F1）  

## 必须

### 结构变更（加列、加模块、改 Tab）

1. Read 对应 `{page-id}.page.ui.yaml`  
2. Read Figma `get_metadata` 定位 region / 表头 / 行容器 nodeId  
3. Edit yaml 对应 `regions` / `components`  
4. 单 region `use_figma` patch  
5. 交付：改了哪些 yaml 字段、哪些 nodeId  

### 视觉变更（颜色、字号、圆角）

1. 改 `design-plan.md` Token 节  
2. 若主色/字体级变更 → 重跑 Anti-Slop（可只检 A 段 + 对应 B/C 段）  
3. patch 受影响节点；全站 token 变更时按页批量 patch，仍按 region  

### 加页 / 删页

1. 更新 `ia-draft.md`  
2. 新页：完整走 Phase 1–5（可复用已有 design-plan 的 Token 节）  
3. 删页：Figma 删 Frame + 删 yaml 文件  

## 用户说「我自己在 Figma 改」

停止 Agent 画布写入；仅在被要求时同步 yaml/plan 文档。

## 用户说「重做一版」

仍须新 `design-plan.md` + Anti-Slop PASS；可新 Figma 文件或新 Page，**不是**无 spec 的口头重 roll。
