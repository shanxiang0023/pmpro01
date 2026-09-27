# 共用视觉与流程约束

B 端与 C 端均遵守。

## 间距

- 基数：4px  
- 允许：`4, 8, 12, 16, 24, 32, 48`  
- 禁止：13、18、22 等随意值  

## 字体 Nevers

禁止作为中文界面主正文：

- Inter  
- Roboto  
- Arial  
- Space Grotesk  
- system-ui  

推荐：

- 中文正文：PingFang SC、思源黑体 SC  
- 数据/ID/金额：SF Mono、JetBrains Mono  

## 颜色 Nevers

- `#6366F1` 及靛紫主色  
- purple-to-blue 渐变主视觉  
- 霓虹色 + 深黑侧栏组合（非 brief 要求）  
- 指标数字渐变字  

## 布局 Nevers

- card 套 card 超过 1 层  
- 非 dashboard 页使用 4 等宽 KPI 横排  
- 列表页用 card 外包整张 table（B 端）  
- 无 brief 的灰色大块 chart placeholder  

## 无障碍底线

- 触控目标 ≥ 44px  
- 正文对比度 WCAG AA  
- 状态不只靠颜色（加文案/图标）  

## 流程（与 frontend-design 一致）

1. design-plan 先于 Figma  
2. Anti-Slop PASS 先于 Figma  
3. 按 region 分批生成  
4. 每屏 screenshot 再审  
5. 修改走 incremental-edit，禁止整页重 roll  
