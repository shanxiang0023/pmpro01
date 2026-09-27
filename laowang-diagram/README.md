# pm-diagram

产品经理业务流程与框架图 Agent Skill：把**多角色业务链路**抽象成**标准泳道流程图 + 架构分层说明**。兼容 Cursor、Codex、Claude Code 等支持 Agent Skills 的运行时。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 解决什么问题

业务一复杂，文档里写几千字，评审会上还是讲不清「谁在什么时候做什么、超时走哪条分支、退款由哪个系统触发」。

这个 Skill 输入大白话（角色、主干、异常），输出规范源码（Mermaid flowchart / draw.io XML），把文字描述压成一张能讲透全局的图。

## 能力

| 能力 | 输入 | 产出 |
|------|------|------|
| **跨角色泳道流程图** | 角色清单、主干步骤、异常分支 | Mermaid `flowchart` + `subgraph` 泳道 |
| **主干流程图 / 状态机图 / 时序图** | 步骤序列、状态集合、调用序列 | 对应 Mermaid 语法 |
| **draw.io 导出** | 已定稿结构 | `.drawio` XML（原生 swimlane 容器，可拖拽精修） |
| **架构分层说明** | 已定稿的图 | 角色层 / 流程层 / 系统层 / 异常与边界 四段文字 |

**不做**：编造业务里不存在的角色与分支；输出 PNG 位图（需要视觉成品图请用 `diagram-generator`）。

## 安装

**方式一：手动 clone（项目级）**

```bash
git clone https://github.com/pmlaowangba-lab/laowang-diagram.git .agents/skills/laowang-diagram
```

**方式二：手动 clone（用户级）**

```bash
git clone https://github.com/pmlaowangba-lab/laowang-diagram.git ~/.agents/skills/laowang-diagram
```

**方式三：让 WorkBuddy 自己装**

```text
帮我把 GitHub 仓库 pmlaowangba-lab/laowang-diagram 安装到 .agents/skills/
```

## 快速开始

```text
用 $laowang-diagram，绘制一张【电商退货退款】跨角色泳道流程图。涉及角色，买家、商家、平台客服、仓储系统。
必须包含，正常退货验收流程、卖家超时未处理自动退款、商品验收不合格拒收并引发客服介入 3 条分支逻辑。
输出为规范的 Mermaid flowchart 语法，并提供架构分层说明。
```

更多提示词见 [examples/sample-prompts.md](examples/sample-prompts.md)，完整实例见 [examples/ecommerce-refund-swimlane.md](examples/ecommerce-refund-swimlane.md)。

## 目录结构

```text
.
├── SKILL.md                     # Skill 入口
├── README.md
├── LICENSE
├── agents/openai.yaml
├── references/                  # 抽取方法、语法规则、分层写法、图型选型
├── assets/                      # Mermaid / draw.io 模板
├── examples/                    # 提示词与完整实例
└── scripts/check_mermaid.py     # 产物自检
```

## 自检

交付前跑一遍，校验 Mermaid 语法与 draw.io 引用完整性：

```bash
python3 scripts/check_mermaid.py assets/swimlane-template.mmd
python3 scripts/check_mermaid.py examples/ecommerce-refund-swimlane.md
python3 scripts/check_mermaid.py examples/ecommerce-refund-swimlane.drawio
```

检查项：`subgraph`/`end` 配平、节点 ID 合法性、保留字冲突、标签裸括号、孤岛与死节点、节点数超限；draw.io 侧检查根单元格、`parent`/`source`/`target` 引用完整性、泳道内节点坐标。

## 依赖

- **Mermaid 渲染**：Obsidian 装 Diagram plugin；或把代码贴进 <https://mermaid.live>
- **draw.io 文件**：draw.io 桌面版双击打开；或拖进 <https://app.diagrams.net>；Obsidian 可装 draw.io Integration 插件

## 已知边界

Mermaid **没有原生 swimlane 语法**，本 Skill 用 `subgraph` 模拟泳道。硬限制是泳道只能整块堆叠，同一角色无法在不同阶段分两次出现。需要严格泳道对齐或投屏讲解时，请用 draw.io 版本（有原生 swimlane 容器）。这一点在 [SKILL.md](SKILL.md) 中已明确写出，不会向用户含糊带过。

## License

MIT — 见 [LICENSE](LICENSE)。
