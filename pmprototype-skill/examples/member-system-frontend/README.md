# Member System Frontend Example

会员系统前台页面原型案例，用来展示本 Skill 从 brief 到结构化原型规格的完整产出。

![Member System Frontend prototype](preview.png)

> 注意：这是产品原型图，不是最终 UI 稿。正式展示或交付前，建议再使用 gptimage2 或 Stitch 做视觉精修。

## Files

- `ia-draft.md`：从 brief 推导核心实体、角色、任务链与页面映射。
- `design-plan.md`：C 端视觉轨、token、页面布局和 Anti-Slop Review。
- `member-home.page.ui.yaml`：会员首页。
- `plan-select.page.ui.yaml`：套餐选择页。
- `benefit-detail.page.ui.yaml`：权益详情页。
- `checkout.page.ui.yaml`：开通确认页。
- `my-membership.page.ui.yaml`：我的会员页。

## Notes

- 这是公开示例规格，不绑定任何私有 Figma 文件。
- YAML 中的 `figma.file_key` 与 `figma.frame_node_id` 保持为空，实际生成 Figma 后再回填。
- 示例按 `surface: c_end`、`390x844` 移动端画布组织。
