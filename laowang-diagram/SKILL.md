---
name: laowang-diagram
description: |
  把多角色业务链路抽象成标准泳道流程图与架构分层说明。输入参与角色、主干步骤与异常分支，
  输出规范 Mermaid flowchart 源码（可直接渲染）与可选 draw.io XML（可二次拖拽修改）。
  用户说画流程图、泳道图、跨角色流程、业务链路图、框架图、状态机、时序图、架构分层图时使用。
  适用于产品经理梳理退货退款、审批、履约、工单、对账等跨角色流程，评审前把几千字文字描述压成一张能讲透全局的图。
  不输出位图渲染结果，不做美化插画；需要 PNG 视觉成品时转 diagram-generator。
version: "1.0"
updated: "2026-09-20"
---

# 老王业务流程与框架图（laowang-diagram）

把「一段说不清的多角色业务」变成「一张评审会上讲得透的图」。

输入是**大白话**：谁参与、主干怎么走、哪里会出岔子。
输出是**规范源码**：Mermaid flowchart（默认）+ draw.io XML（需要二次拖拽时），外加一段架构分层说明。

## 能力边界

| 能力 | 触发场景 | 输入 | 产出 |
|------|----------|------|------|
| **泳道流程图** `swimlane` | 多角色协作 + 有交接与异常分支 | 角色清单、主干步骤、异常情况 | 规范 Mermaid flowchart（`subgraph` 分泳道）+ 分层说明 |
| **主干流程图** `flow` | 单角色或纯系统内部流程 | 步骤序列、判断条件 | Mermaid flowchart |
| **状态机图** `state` | 单据/订单/工单的状态流转 | 状态集合、触发事件、守卫条件 | Mermaid stateDiagram-v2 |
| **时序图** `sequence` | 强调系统间调用先后与返回 | 参与方、消息序列 | Mermaid sequenceDiagram |
| **draw.io 导出** `drawio` | 需要真泳道容器、二次拖拽精修 | 上述任一结构 | `.drawio` XML |
| **分层说明** `layering` | 总是附带 | 已定稿的图 | 角色层 / 流程层 / 系统层 文字说明 |

**不做**：编造业务里不存在的角色与分支；把图渲染成 PNG（那是 `diagram-generator` 的职责）；用装饰性插画替代逻辑结构。

## 启动必读

1. 本文件 `SKILL.md`
2. [references/swimlane-extraction.md](references/swimlane-extraction.md) —— 从大白话抽角色、主干、异常的方法与追问清单
3. [references/mermaid-flowchart-rules.md](references/mermaid-flowchart-rules.md) —— Mermaid 规范语法与禁用写法
4. [references/layering-notes.md](references/layering-notes.md) —— 分层说明的固定结构

按需再读：

- 图型选型拿不准 → [references/diagram-type-selection.md](references/diagram-type-selection.md)
- 要出 draw.io 文件 → [references/drawio-xml-rules.md](references/drawio-xml-rules.md)
- 起手抄模板 → [assets/swimlane-template.mmd](assets/swimlane-template.mmd)、[assets/swimlane-template.drawio](assets/swimlane-template.drawio)
- 看完整实例 → [examples/ecommerce-refund-swimlane.md](examples/ecommerce-refund-swimlane.md)

## 路由规则

1. 用户给了**多个角色**且提到交接、超时、驳回、异常 → 走 `swimlane`。
2. 用户只给一串步骤、没有角色概念 → 走 `flow`，别硬套泳道。
3. 用户描述的是「一个单据从 A 状态到 B 状态」→ 走 `state`。
4. 用户强调「谁先调谁、什么时候返回」→ 走 `sequence`。
5. 用户说「要能拖拽改」「要 draw.io 文件」「要放进 Obsidian」→ 在结构定稿后追加 `drawio`。
6. 用户只说「画个流程图」但没给素材 → 读 swimlane-extraction 的追问清单，一次问 1–3 个高优先级问题，别一次甩 10 个问题。

**顺序固定**：先定结构（角色 → 主干 → 异常），再选图型，最后出源码。结构没定就出图 = 重画。

## 工作流程

### 步骤 1：抽取结构（不写图，先写清单）

按 [references/swimlane-extraction.md](references/swimlane-extraction.md) 产出三份内部清单：

```text
角色清单：买家 / 商家 / 平台客服 / 仓储系统
主干步骤：每条标「谁 → 做什么 → 交给谁」
异常分支：每条标「触发条件 → 谁处理 → 结果」
```

关键判断：**异常分支不是补充项，是主干的一部分**。只有正常路径的流程图在评审会上会被研发一句话问穿。

### 步骤 2：选图型

按路由规则选。泳道图只在「角色 ≥ 2 且存在跨角色交接」时才用；单角色硬套泳道只会让图变宽。

### 步骤 3：出 Mermaid 源码

严格按 [references/mermaid-flowchart-rules.md](references/mermaid-flowchart-rules.md) 写。核心约束：

- 每个角色一个 `subgraph`，泳道名用中文角色名。
- 节点 ID 用 ASCII（`A1`、`M2`、`CS1`），显示文字写在 `[]` 里。**ID 和标签分离**，中文只出现在标签中。
- 标签含特殊字符（`()`、`[]`、`{}`、`、`、`:`）时用双引号包起来：`A1["提交退货申请（48h 内）"]`。
- 判断节点用 `{}`，起止节点用 `([])`。
- 异常分支用虚线 `-.->`，正常主干用实线 `-->`。
- 语义配色用 `classDef`，不靠随机颜色。
- 写完跑一遍自检：`python3 scripts/check_mermaid.py <文件.mmd>`

### 步骤 4：补分层说明

按 [references/layering-notes.md](references/layering-notes.md) 输出四段：角色层、流程层、系统层、异常与边界。每段只讲这一层新增了什么信息，不复述图上已经画出来的箭头。

### 步骤 5：需要时导出 draw.io

用户要可拖拽源文件时，按 [references/drawio-xml-rules.md](references/drawio-xml-rules.md) 生成 `.drawio`，每个角色一个原生 swimlane 容器。

### 步骤 6：交付

在回复里给出：

```text
图型：跨角色泳道流程图（Mermaid flowchart TD）
泳道：买家 / 商家 / 平台客服 / 仓储系统
分支：主干 1 条 + 异常 2 条
产物：<路径>.mmd（Mermaid 源码）、<路径>.md（含分层说明）
渲染：Obsidian 装 Diagram plugin 后双击即可预览；draw.io 文件用 draw.io 桌面版打开可拖拽修改
```

## Mermaid 泳道的真实边界（重要，别对用户吹）

Mermaid **没有原生 swimlane 语法**。行业通用做法是用 `subgraph` 模拟泳道，这有两个硬限制：

1. 泳道只能**整块堆叠**，不能实现「同一角色在不同阶段出现两次」的经典泳道排布。
2. 泳道内部无法强制水平流动方向，跨泳道的箭头走向由布局引擎决定。

因此：

- 角色少、交接简单 → Mermaid 足够，**优先用它**，因为纯文本、可 diff、可版本管理。
- 角色多、需要严格泳道对齐、要投屏讲解 → 出 draw.io，它有原生 swimlane 容器。

**不要向用户承诺「Mermaid 能画出标准泳道图」**。要如实说明上述差异，再给建议。

## 硬性规则

- 不在图里写业务里不存在的角色、状态或分支。缺信息就问，不脑补。
- 不输出只有正常路径的流程图交付。
- 节点标签不超过 18 个汉字；超了拆成两个节点或把细节移到分层说明。
- 一张图节点总数控制在 25 个以内；超了就拆图，不硬塞。
- 节点 ID 一律 ASCII，中文只出现在标签和泳道名里。
- 不把语法源码当正文内容写进知识库；产物落在任务归属目录，无归属时进 `99-收件箱/待整理/`。
- 不生成 PNG；用户明确要视觉成品图时，说明并转 `diagram-generator`。

## 质量检查

交付前逐条过：

- 每个角色是否都有独立泳道，泳道内是否只放该角色的动作？
- 主干路径是否从头走到尾、无断链、无孤岛节点？
- 异常分支是否都标了触发条件？「超时」「拒收」「并发冲突」这类是否都有出口？
- 跨泳道交接点是否明确（谁交给谁、交的是什么）？
- 虚线是否只用于异常/可选路径？
- 泳道名、节点标签是否全中文、无错字？
- `subgraph` 与 `end` 是否配平？`check_mermaid.py` 是否通过？
- 分层说明是否只讲图上看不出的信息，没有复述箭头？
- 是否如实说明了 Mermaid 泳道的限制？

## 产出说明模板

```text
已生成 <图型>，放在：<路径>
泳道：<角色列表>；分支：主干 <n> 条 + 异常 <m> 条
重点标注：<最关键的那个异常分支或系统边界>
验证：check_mermaid.py 通过；subgraph/end 配平；无孤岛节点
```
