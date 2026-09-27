# Design Plan 模板

Phase 1 产出 `design-plan.md`，生成 Figma 前必须存在。

```markdown
# Design Plan — {项目名} v{版本}

## 1. Subject
- 产品：
- 受众：
- 本文件/首批页面要完成的单一任务：
- 假设与待确认：

## 2. Tone
- surface: b_end | c_end
- 气质：（b_end → utilitarian-enterprise / c_end → refined-consumer）
- 参考气质：（从 DESIGN.md 允许列表选，一句）

## 3. Token

### Color（命名 + hex，从 DESIGN 轨复制后微调须说明）
- primary:
- page_bg:
- surface:
- border:
- text_primary / secondary:

### Typography
- body:
- data:（ID、金额；无则写 N/A）
- scale:（列出会用到的字号档位）

### Spacing / Radius
- spacing_allowed: [4, 8, 12, 16, 24, 32]
- radius: button / card / max

## 4. Layout（每页一节）

### {page-id} — {页面名}
- 页型:（见 page-templates.yaml）
- ASCII:
```
（线框）
```
- regions 列表:（与后续 yaml 一致）

## 5. Signature
- 元素：
- 落地规则：（在哪些组件/页面出现，如何克制）

## 6. Differentiation
- 相对 AI 默认 dashboard/App，本方案差在哪：（一句话）

---

## Anti-Slop Review
（Phase 2 填写，见 anti-slop-checklist.md）
```
