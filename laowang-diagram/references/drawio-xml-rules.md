# draw.io XML 生成规则

Mermaid 无法实现真正的泳道容器。当用户要「可拖拽二次修改」「放进 Obsidian 双击打开」「投屏讲解」时，输出 `.drawio` 文件。

## 一、文件骨架

`.drawio` 是 XML，根为 `<mxfile>`，内含 `<diagram>` → `<mxGraphModel>` → `<root>`。

```xml
<mxfile host="app.diagrams.net" agent="laowang-diagram" version="24.0.0" type="device">
  <diagram id="refund-swimlane" name="电商退货退款泳道图">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1600" pageHeight="900"
                  math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- 泳道与节点写在这里 -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**必须保留** `id="0"` 和 `id="1"` 这两个根单元格，缺一个文件打不开。

## 二、泳道（原生 swimlane 容器）

```xml
<mxCell id="lane1" value="买家"
        style="swimlane;horizontal=1;startSize=30;fillColor=#EAF2FF;strokeColor=#3B82F6;fontColor=#1E3A8A;fontStyle=1;"
        vertex="1" parent="1">
  <mxGeometry x="40" y="80" width="1200" height="120" as="geometry" />
</mxCell>
```

| 属性 | 含义 |
|---|---|
| `horizontal=1` | 横向泳道（标题在左，内容右排）。跨职能泳道图用这个 |
| `horizontal=0` | 纵向泳道（标题在上，内容下排） |
| `startSize=30` | 泳道标题栏宽度/高度 |
| `fillColor` | 泳道底色，按角色语义取色 |

### 泳道堆叠坐标

- 横向泳道：`x` 相同，`y` 依次递增，`y(n+1) = y(n) + height(n) + 20`（留 20 间距）。
- 泳道统一宽度（如 1200），只改 `y`。
- 泳道名写角色名，如「买家」「商家」「平台客服」「仓储系统」。

## 三、节点

节点作为泳道的**子元素**，`parent` 指向泳道 ID。

```xml
<mxCell id="n1" value="提交退货申请"
        style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#3B82F6;fontColor=#1E3A8A;"
        vertex="1" parent="lane1">
  <mxGeometry x="140" y="50" width="160" height="40" as="geometry" />
</mxCell>
```

**关键**：子节点坐标相对泳道原点，且 `y` 必须 ≥ `startSize`（30），否则会压住泳道标题栏。横向泳道里通常用 `y=50`。

### 常用节点样式

| 类型 | style 关键片段 |
|---|---|
| 普通步骤 | `rounded=1;whiteSpace=wrap;html=1;` |
| 起止节点 | `rounded=1;arcSize=50;whiteSpace=wrap;html=1;` |
| 判断节点 | `rhombus;whiteSpace=wrap;html=1;` |
| 系统节点 | `rounded=0;whiteSpace=wrap;html=1;fillColor=#F3F4F6;strokeColor=#6B7280;` |
| 异常节点 | `rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF4E5;strokeColor=#F59E0B;dashed=1;` |
| 失败/终止 | `rounded=1;whiteSpace=wrap;html=1;fillColor=#FDECEC;strokeColor=#EF4444;` |

### 节点横向排布

同一泳道内按主干顺序从左往右，`x` 递增 200：

```text
x = 140, 340, 540, 740, 940 ...
```

跨泳道的交接节点要**上下对齐**，让箭头接近垂直，图才不乱。

## 四、连边

连边是根单元格（`parent="1"`）的子元素，不挂在泳道下。

```xml
<mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#1F2937;"
        edge="1" parent="1" source="n1" target="n2">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

### 分支标签

带条件的边，把标签写进 `value`：

```xml
<mxCell id="e2" value="超时未处理"
        style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;dashed=1;strokeColor=#F59E0B;"
        edge="1" parent="1" source="n3" target="n4">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

### 连边规则

- 主干：实线，`strokeColor=#1F2937`
- 异常：虚线，加 `dashed=1;strokeColor=#F59E0B;`
- 失败/终止：虚线，`dashed=1;strokeColor=#EF4444;`
- `source` / `target` 必须指向已存在的节点 ID，**悬空引用会导致文件打开后报错**
- 每条边 ID 唯一（`e1`、`e2`…）

## 五、语义配色（与 Mermaid 版一致）

| 语义 | fillColor | strokeColor | fontColor |
|---|---|---|---|
| 起止 / 成功 | `#E9F9EF` | `#10B981` | `#065F46` |
| 角色动作 | `#FFFFFF` | `#3B82F6` | `#1E3A8A` |
| 系统 / 后台 | `#F3F4F6` | `#6B7280` | `#1F2937` |
| 异常 / 超时 | `#FFF4E5` | `#F59E0B` | `#92400E` |
| 失败 / 终止 | `#FDECEC` | `#EF4444` | `#991B1B` |

泳道底色用对应角色的语义色浅色版，标题文字用深色版。

## 六、校验

生成后必须校验：

```bash
python3 -c "import xml.dom.minidom,sys; xml.dom.minidom.parse(sys.argv[1]); print('XML OK')" path/to/diagram.drawio
```

再人工确认：

- `id="0"` 与 `id="1"` 存在
- 所有 `parent` 指向的 ID 都存在
- 所有 `source` / `target` 指向的 ID 都存在
- 泳道内节点 `y >= startSize`
- 泳道之间无坐标重叠

## 七、打开方式（写进交付说明）

- **draw.io 桌面版**：双击 `.drawio` 直接打开，可拖拽修改
- **Obsidian**：装 Diagram plugin（或 draw.io Integration 插件）后双击预览
- **网页版**：拖进 <https://app.diagrams.net>

交付时把这三种方式告诉用户，并提醒：文件是标准 mxGraph XML，可提交进 Git 做版本管理。
