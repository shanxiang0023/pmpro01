# AI Price Comparison Frontend

AI 比价前台页面原型案例，面向普通消费者的移动端 C 端场景。

## Brief

生成一个符合淘宝消费端视觉习惯的 AI 比价前台原型，功能覆盖搜索、同款聚合、平台报价对比、AI 购买建议、价格趋势、降价订阅和我的清单。

## Pages

| Page | File | Purpose |
|---|---|---|
| 首页 | `home.page.ui.yaml` | 搜索入口、AI省钱播报、快捷入口、商品推荐流 |
| 搜索结果 | `search.page.ui.yaml` | 同款报价聚合、平台筛选、AI低价结论 |
| 商品详情 | `detail.page.ui.yaml` | 商品信息、平台报价、价格趋势、购买 CTA |
| AI比价报告 | `ai-report.page.ui.yaml` | 价格拆解、平台雷达、风险提示、目标价订阅 |
| 我的清单 | `watchlist.page.ui.yaml` | 降价提醒、关注商品、已领优惠 |

## Included Files

- `ia-draft.md`
- `design-plan.md`
- `*.page.ui.yaml`
- `index.html`

## Preview

`index.html` 是本案例的本地高保真 HTML 预览文件，可直接用浏览器打开。  
在 Codex 任务中，Figma MCP 握手失败，因此本案例保留 HTML 作为可视化交付，同时保留 `page.ui.yaml` 供后续重新写入 Figma。

## Design Notes

- surface: `c_end`
- tone: `refined-consumer`
- 主色：淘宝式橙色 `#FF5000`
- Signature：AI省钱指纹，用一句话解释每个商品的最低价、券后价、服务风险和购买时机
- Anti-Slop：PASS
