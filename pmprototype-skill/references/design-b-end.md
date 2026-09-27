# B 端视觉 Token（utilitarian-enterprise）

`surface: b_end` 时 `design-plan.md` 从此复制默认值。

## 画布

- width: 1440  
- height: 900  
- content_max: ~1168（24 栏思维，不强制栅格插件）  

## 结构尺寸

- sidebar_width: 200–208  
- topbar_height: 48–56  
- table_row_height: 48–52  
- filter_bar_height: 48–56  

## Color

```yaml
sidebar_bg: "#001529"
page_bg: "#F0F2F5"
surface: "#FFFFFF"
border: "#E8E8E8"
text_primary: "#141414"
text_secondary: "#595959"
text_tertiary: "#8C8C8C"
primary: "#1677FF"
primary_hover: "#4096FF"
success: "#52C41A"
warning: "#FAAD14"
danger: "#FF4D4F"
table_header_bg: "#FAFAFA"
```

## Typography

```yaml
family_body: "PingFang SC"
family_data: "SF Mono"
page_title: { size: 20, weight: 600, lineHeight: 28 }
section_title: { size: 16, weight: 600, lineHeight: 24 }
body: { size: 14, weight: 400, lineHeight: 22 }
caption: { size: 12, weight: 400, lineHeight: 20 }
kpi_value: { size: 24, weight: 600, lineHeight: 32 }
```

禁止 kpi_value 使用 28px+ 夸张数字墙。

## Radius & Shadow

```yaml
button: 6
card: 8
tag: 4
max: 8
shadow_default: none
```

分区用 `1px solid #E8E8E8`，不用卡片阴影墙。

## 组件倾向

| 场景 | 用法 |
|------|------|
| 列表 | flat table + 顶栏筛选条 |
| 详情 | 摘要条 + Tabs + 面板 |
| 工作台 | KPI ≤ 3 + 主表格/列表 + 待办 |
| 表单设置 | 分组表单，label 左对齐 |

## 每屏

- primary 按钮 ≤ 1  
- 导出/新建同时出现时：仅一个 primary  
