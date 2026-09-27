# frontend-design 闸门

画原型 Skill 强制检查门。未通过不得进入下一阶段。

| ID | 时机 | 条件 | 不通过则 |
|----|------|------|----------|
| G0 | 任务开始 | 已 Read `SKILL.md` + `前端设计/SKILL.md` + `DESIGN.md` + 本文件 | 停止 |
| G1 | Phase 1 后 | `design-plan.md` 六项齐全（Subject/Tone/Token/Layout/Signature/Differentiation） | 禁止 Phase 3、禁止 Figma |
| G2 | Phase 2 后 | `anti-slop-checklist.md` 全通过，plan 末尾 `结论: PASS` | 只改 plan，禁止 yaml 与 Figma |
| G3 | Phase 3 后 | 每页 `meta.anti_slop: pass` 且 schema 校验通过 | 禁止 Figma |
| G4 | 每屏 Phase 4 后 | `get_screenshot` 与 plan ASCII 基本一致 | patch region，禁止整页重 roll |
| G5 | Phase 5 后 | 每屏已执行「删 1 装饰」 | 继续 patch 至合格 |
| G6 | Phase 7 修改 | 已更新 plan 或 yaml 再 patch Figma | 禁止无文档整页重生成 |

## frontend-design 两阶段（嵌入 G1/G2）

**第一遍（G1）**：brainstorm compact token + layout + signature → `design-plan.md`

**第二遍（G2）**：对照 brief 自检——若 plan 中任一段落换成「任意类似产品」仍成立，视为 AI 模板，必须改写并记录修订。

## AI 默认三套皮（G2 必查）

以下仅当 **brief 明确要求** 才可用；否则命中即 FAIL：

1. 奶油纸 `#F4F1EA` + 高对比衬线 display + 陶土 accent  
2. 近黑底 + 单一酸绿/朱红 accent  
3. 报纸风密排 + 零圆角 + 发丝线装饰  

## 与 DESIGN.md 路由

- `surface: b_end` → 必读 `design-b-end.md`，G2 跑 B 端追加项  
- `surface: c_end` → 必读 `design-c-end.md`，G2 跑 C 端追加项  

## Figma 调用前最后检查

```
[ ] design-plan.md 存在
[ ] Anti-Slop 结论 PASS
[ ] page.ui.yaml meta.anti_slop == pass
[ ] figma-use 已加载
[ ] 脚本内无 Inter、无 #6366F1、无 plan 外 hex
```
