# DESIGN.md — 产品原型视觉宪法（B/C 双轨）

> 只管「怎么好看、用什么 token」，**不管 IA、不管有哪些页面**。  
> IA 见 [references/ia-derivation.md](references/ia-derivation.md)；流程闸门见 [references/frontend-design-gates.md](references/frontend-design-gates.md)。

## 路由（brief → 哪套视觉）

```yaml
b_end_signals:
  - 后台 / 管理端 / 运营 / 客服 / 审核 / 配置 / 报表 / 权限
  - 使用者为内部员工
  - 高密度表格、批量操作

c_end_signals:
  - App / 小程序 / H5 / 用户端 / 消费者端
  - 浏览 / 下单 / 个人中心 / 支付 / 转化
  - 单屏主任务、品牌表达

rules:
  - 每份 page.ui.yaml 必填 meta.surface: b_end | c_end
  - 禁止用 B 端 token 画 C 端页，反之亦然
  - 混合产品：同一 Figma 文件可含两轨，但每 Frame 只属一轨
  - brief 模糊：问一次「内部用还是用户用？」；仍模糊则按页面逐屏标 surface

tone_lock:
  b_end: utilitarian-enterprise    # 禁止 frontend-design extreme
  c_end: refined-consumer          # 可品牌表达，禁 landing 炫技
```

## 共用层（摘要）

完整条文：[design-shared.md](references/design-shared.md)

- 间距基数：4px；允许值 `4, 8, 12, 16, 24, 32, 48`
- 字体禁止：Inter、Roboto、Arial、Space Grotesk、system-ui 作中文正文
- 颜色禁止：`#6366F1`、紫蓝渐变、霓虹深色侧栏
- 布局禁止：card-in-card 超过 1 层；非 dashboard 禁止 4 等宽 KPI 横排
- 触控：最小 44px；对比度 WCAG AA

## B 端轨（摘要）

完整 token：[design-b-end.md](references/design-b-end.md)

| 项 | 值 |
|----|-----|
| 画布 | 1440×900 |
| 侧栏 | 200–208px，`#001529` |
| 页背景 | `#F0F2F5` |
| 主色 | `#1677FF` |
| 正文 | PingFang SC 14/22 |
| 数据 | SF Mono 12 |
| 圆角 | button 6 / card 8 / max 8 |
| 阴影 | 默认无；用 `#E8E8E8` 描边分区 |
| 列表页 | flat table，禁止 card 套 table |
| Dashboard | KPI ≤ 3 |

## C 端轨（摘要）

完整 token：[design-c-end.md](references/design-c-end.md)

| 项 | 值 |
|----|-----|
| 画布 | 390×844（mobile 默认） |
| 页背景 | `#F7F8FA` |
| 主色 | brief 定；默认 `#FF6B35`（须过 Anti-Slop，禁紫渐变） |
| 正文 | PingFang SC 15/24 |
| 标题 | 18–24，单屏 1 个主标题层级 |
| 圆角 | card 12 / 胶囊按钮 22 |
| 阴影 | 卡片轻阴影 `0 2px 12px rgba(0,0,0,0.06)` |
| 导航 | TabBar / 顶栏返回；**禁止** B 端侧栏套手机 |
| 主 CTA | 每屏 ≤ 1（底栏主按钮算 1 个） |

## Signature

不在本文件写死。每个项目在 `design-plan.md` 的 Signature 节定义 **1 个**记忆点，须服务 brief，禁止纯装饰渐变。

## 页型

见 [page-templates.yaml](references/page-templates.yaml)：`b_list_page`、`b_detail_page`、`b_dashboard`、`c_home`、`c_list`、`c_detail`、`c_form`、`c_profile`。

## 参考气质

| 允许 | 禁止 |
|------|------|
| B：Ant Design Pro、飞书管理后台 | Vercel landing、Dribbble 炫彩 dashboard |
| C：克制消费 App、微信/支付宝信息架构密度 | SaaS 营销三列 feature、AI 默认三套皮（见 anti-slop） |
