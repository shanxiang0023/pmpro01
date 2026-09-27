# Anti-Slop 自检清单

Phase 2 强制勾选。任一项命中且未在 plan 中修订 → **FAIL**。

## A. frontend-design 通用（B/C 都检）

- [ ] A1 主正文字体不是 Inter / Roboto / Arial / system-ui / Space Grotesk  
- [ ] A2 主色不是 `#6366F1`，无紫蓝渐变主视觉  
- [ ] A3 未命中 AI 三套默认皮（见 frontend-design-gates.md）  
- [ ] A4 plan 的 Layout/Signature 非「换 brief 仍一样」的模板描述  
- [ ] A5 Signature 不是纯装饰（全屏渐变、无意义 hero）  
- [ ] A6 Differentiation 能一句话说清与 AI 默认的差异  

## B. B 端追加（surface: b_end）

- [ ] B1 列表页为 flat table，非 card 外包 table  
- [ ] B2 Dashboard KPI ≤ 3（非 4 等宽横排）  
- [ ] B3 默认无卡片阴影墙（描边分区）  
- [ ] B4 侧栏 200–208px，非随意宽度  
- [ ] B5 信息密度偏运营工具，非 SaaS landing 大留白  
- [ ] B6 每屏 primary 按钮 ≤ 1  

## C. C 端追加（surface: c_end）

- [ ] C1 非 B 端侧栏+顶栏套移动端  
- [ ] C2 单屏主任务清晰，非 dashboard KPI 墙  
- [ ] C3 主 CTA ≤ 1（底栏主按钮算 1）  
- [ ] C4 无 marketing 三列 feature + 全屏 hero（brief 非落地页时）  
- [ ] C5 画布宽度符合 mobile（约 390），非 1440 拉满  

## 修订记录模板

```markdown
## Anti-Slop Review
- 日期: YYYY-MM-DD
- surface: b_end | c_end
- 命中: A2, B2, ...
- 修订: （改了 plan 哪节、为何）
- 结论: PASS | FAIL
```
