# C 端视觉 Token（refined-consumer）

`surface: c_end` 时 `design-plan.md` 从此复制默认值。主色可按品牌改，须过 Anti-Slop。

## 画布

```yaml
mobile:
  width: 390
  height: 844
mini_program:
  width: 375
  height: 812
```

禁止默认用 1440 宽画手机页。

## 结构尺寸

- topbar_height: 44–48  
- bottom_tab_height: 50（含 safe area 标注）  
- list_card_gap: 12  
- section_padding_horizontal: 16  

## Color（默认，可品牌替换）

```yaml
page_bg: "#F7F8FA"
surface: "#FFFFFF"
border: "#EBEDF0"
text_primary: "#1A1A1A"
text_secondary: "#666666"
text_tertiary: "#999999"
primary: "#FF6B35"       # brief 可改；禁紫渐变
accent_positive: "#00B578"
warning: "#FF8F1F"
danger: "#FA5151"
```

## Typography

```yaml
family_body: "PingFang SC"
hero: { size: 24, weight: 600, lineHeight: 32 }    # 仅首页/关键页
title: { size: 18, weight: 600, lineHeight: 26 }
body: { size: 15, weight: 400, lineHeight: 24 }
caption: { size: 12, weight: 400, lineHeight: 18 }
```

单屏主标题层级 ≤ 2。

## Radius & Shadow

```yaml
card: 12
image: 8
button_capsule: 22
shadow_card: "0 2px 12px rgba(0,0,0,0.06)"
```

C 端允许轻阴影；仍禁止 glassmorphism 装饰。

## 组件倾向

| 场景 | 用法 |
|------|------|
| 首页 | 可选轻 hero + 宫格入口 + 列表 |
| 列表 | 卡片列表，非 B 端 table |
| 详情 | 头图/摘要 + 信息组 + 底栏 CTA |
| 表单 | 分组 + 底部固定主按钮 |

## 每屏

- 主 CTA ≤ 1（底栏大按钮算 1 个）  
- 禁止 B 端侧栏导航  
