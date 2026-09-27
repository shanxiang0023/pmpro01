# Design Plan — 会员系统前台页面原型 v1

## 1. Subject

- 产品：C 端会员开通与会员中心前台页面。
- 受众：准备开通会员的普通用户，以及已开通后需要查看权益状态的会员用户。
- 本文件/首批页面要完成的单一任务：让用户理解会员价值，完成套餐选择与开通确认，并能回到个人会员状态页。
- 假设与待确认：暂按“数字内容 / 工具服务类会员”设计，文案使用可替换的业务占位；真实品牌、价格、权益名称待确认。

## 2. Tone

- surface: c_end
- 气质：refined-consumer
- 参考气质：克制消费 App 的信息密度，接近微信/支付宝里“会员服务”一类的清晰任务流，不做营销落地页式炫技。

## 3. Token

### Color

- primary: `#FF6B35`
- page_bg: `#F7F8FA`
- surface: `#FFFFFF`
- border: `#EBEDF0`
- text_primary: `#1A1A1A`
- text_secondary: `#666666`
- text_tertiary: `#999999`
- accent_positive: `#00B578`
- warning: `#FF8F1F`
- danger: `#FA5151`
- premium_ink: `#2A211B`，用于会员卡头部文字，避免黑金俗套过重。
- premium_soft: `#FFF2E8`，用于权益提示底色，不使用紫蓝渐变。

### Typography

- body: PingFang SC 15/24
- data: SF Mono 12/18，用于价格、小计、到期日等数字。
- scale: 24/32 hero；18/26 title；15/24 body；12/18 caption。

### Spacing / Radius

- spacing_allowed: [4, 8, 12, 16, 24, 32]
- radius: button 22 / card 12 / max 12

## 4. Layout（每页一节）

### member-home — 会员首页

- 页型: c_home
- ASCII:

```text
┌─────────────────────────┐
│ topbar: 会员中心       │
├─────────────────────────┤
│ status card: 当前状态   │
│ 权益温度条 + 到期提示   │
├─────────────────────────┤
│ content_feed: 推荐套餐  │
│ 年卡推荐 / 月卡备选     │
├─────────────────────────┤
│ content_feed: 核心权益  │
│ 4 个权益入口            │
├─────────────────────────┤
│ bottom_tab              │
└─────────────────────────┘
```

- regions 列表: topbar, content_feed, bottom_tab

### plan-select — 套餐选择

- 页型: c_list
- ASCII:

```text
┌─────────────────────────┐
│ topbar: 选择会员套餐   │
├─────────────────────────┤
│ filter_chips: 月/季/年  │
├─────────────────────────┤
│ card_list: 年卡 推荐    │
│ card_list: 季卡         │
│ card_list: 月卡         │
├─────────────────────────┤
│ 底部价格摘要 + 去开通   │
└─────────────────────────┘
```

- regions 列表: topbar, filter_chips, card_list, bottom_cta

### benefit-detail — 权益详情

- 页型: c_detail
- ASCII:

```text
┌─────────────────────────┐
│ topbar: 权益详情       │
├─────────────────────────┤
│ media_header: 权益名称  │
│ 价值说明 / 已省金额     │
├─────────────────────────┤
│ summary_strip: 适用范围 │
├─────────────────────────┤
│ info_sections: 使用方式 │
│ 规则说明 / 常见限制     │
├─────────────────────────┤
│ bottom_cta: 开通会员    │
└─────────────────────────┘
```

- regions 列表: topbar, media_header, summary_strip, info_sections, bottom_cta

### checkout — 开通确认

- 页型: c_form
- ASCII:

```text
┌─────────────────────────┐
│ topbar: 确认开通       │
├─────────────────────────┤
│ form_section: 已选套餐  │
│ 优惠 / 支付方式 / 协议  │
├─────────────────────────┤
│ form_section: 金额明细  │
├─────────────────────────┤
│ bottom_cta: 确认支付    │
└─────────────────────────┘
```

- regions 列表: topbar, form_section, bottom_cta

### my-membership — 我的会员

- 页型: c_profile
- ASCII:

```text
┌─────────────────────────┐
│ profile_header: 头像    │
│ 会员状态 / 到期时间     │
├─────────────────────────┤
│ 权益进度卡              │
├─────────────────────────┤
│ menu_list: 订单/发票    │
│ 兑换码/帮助/协议        │
├─────────────────────────┤
│ bottom_tab              │
└─────────────────────────┘
```

- regions 列表: profile_header, menu_list, bottom_tab

## 5. Signature

- 元素：会员“权益温度条”。
- 落地规则：在首页状态卡和我的会员页出现，用一条克制的横向进度条表示“已解锁权益 / 待体验权益”，辅助用户理解会员价值；不做无意义大渐变，不在每张卡片重复装饰。

## 6. Differentiation

- 相对 AI 默认 dashboard/App，本方案不是 KPI 墙或营销三列 feature，而是围绕“开通会员”这条转化链路组织页面，并用权益温度条承接会员价值感。

---

## Anti-Slop Review

- 日期: 2026-07-09
- surface: c_end
- 命中: 无未修订命中项。
- 修订: 放弃全屏 hero 和三列权益营销结构；保留移动端任务流、底部单 CTA、会员状态卡和权益温度条。
- 结论: PASS
