# AI比价前台原型 Design Plan

## Subject

面向普通消费者的 AI 比价前台移动端原型。单屏核心任务是让用户用淘宝式浏览心智完成「搜商品、看最低券后价、理解AI建议、订阅降价、跳转购买」。

## Tone

- surface: `c_end`
- tone: `refined-consumer`
- 视觉方向：淘宝消费端信息流，橙色转化焦点，高密度商品卡，券/补贴/低价标签清晰可扫。
- 禁止方向：SaaS 营销落地页、紫蓝渐变 AI 感、B端侧栏或大屏报表。

## Token

```yaml
canvas: { width: 390, height: 844 }
font:
  body: "PingFang SC"
  data: "SF Mono"
color:
  page_bg: "#F7F8FA"
  surface: "#FFFFFF"
  text_primary: "#1A1A1A"
  text_secondary: "#666666"
  text_tertiary: "#999999"
  primary: "#FF5000"
  primary_deep: "#E64300"
  orange_soft: "#FFF3EA"
  price_red: "#FF1F1F"
  coupon_yellow: "#FFE7B8"
  border: "#EBEDF0"
  positive: "#00B578"
radius:
  card: 12
  image: 8
  button_capsule: 22
spacing:
  base: 4
  allowed: [4, 8, 12, 16, 24, 32, 48]
shadow:
  card: "0 2px 12px rgba(0,0,0,0.06)"
```

主色采用淘宝高识别橙，页面背景和中性色遵循 C 端轨。公开规范参考了淘宝/阿里开放平台对色彩、功能色、中性色、布局和自适应交付的说明。

## Layout

### P01 首页

```text
┌ 顶部定位 + 搜索框 + 扫码 ┐
├ AI省钱播报横条            ┤
├ 快捷入口：拍照比价/领券/降价/同款 ┤
├ 今日值得买 横向榜单        ┤
├ 双列商品流：图 + 标题 + 券后价 + AI结论 ┤
└ 底部Tab：首页/搜索/订阅/我的 ┘
```

### P02 搜索结果

```text
┌ 返回 + 搜索词 + 筛选 ┐
├ AI低价结论卡：最低价/可省/建议 ┤
├ 平台筛选 + 排序 chips ┤
├ 同款聚合列表：平台报价/券/服务/风险 ┤
└ 固定底部：订阅降价 + 看AI报告 ┘
```

### P03 商品详情

```text
┌ 顶部返回/分享 ┐
├ 商品视觉 + 低价角标 ┤
├ 标题/券后价/AI推荐理由 ┤
├ 平台报价对比卡 ┤
├ 价格趋势 + 保障差异 ┤
└ 固定底部：订阅 + 去淘宝买 ┘
```

### P04 AI比价报告

```text
┌ 报告标题 + 商品摘要 ┐
├ AI结论：现在买/等等看/换平台 ┤
├ 价格拆解：标价/券/补贴/运费 ┤
├ 平台雷达：价格/时效/售后/可信度 ┤
├ 风险提示：非同款/库存/券门槛 ┤
└ 固定底部：按目标价订阅 ┘
```

### P05 我的清单

```text
┌ 我的省钱数据 ┐
├ 降价提醒状态卡 ┤
├ 关注商品列表：目标价/当前价/提醒状态 ┤
├ 浏览历史 + 已领券 ┤
└ 底部Tab：我的 active ┘
```

## Signature

「AI省钱指纹」：每个商品卡都显示一个小型省钱理由条，把最低价、券后价、服务风险和购买时机压缩成一句可扫的 AI 结论。

## Differentiation

不是普通电商首页换皮，也不是 AI 聊天入口；核心差异是把淘宝式商品流和可解释的跨平台价格判断合成一条消费决策链。

## Anti-Slop Review

- 日期: 2026-07-09
- surface: c_end
- 命中: 无
- 修订: 主视觉不使用紫蓝渐变；不做 marketing 三列 feature；每屏只保留一个主 CTA；移动画布固定 390 宽；正文使用 PingFang SC。
- 结论: PASS
