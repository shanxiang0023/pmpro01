# page.ui.yaml → Figma 映射

## 执行顺序

1. `whoami` → `planKey`  
2. 无 `meta.figma.file_key` → `create_new_file`（先读 figma-create-new-file skill）  
3. 加载 `figma-use`；多 section 页面加载 `figma-generate-design`  
4. 按页循环 → 每页按 `regions[]` 顺序分批 `use_figma`  

## 单批 use_figma 规范

- `description` 写明 region id 与页面 id  
- `skillNames` 含 `figma-use`（及 `figma-generate-design` 若适用）  
- 脚本内颜色 0–1 范围；中文前 `await figma.loadFontAsync`  
- 返回 `createdNodeIds` / `mutatedNodeIds`  
- hex 只来自 design-plan 或 DESIGN 轨，禁止脚本内临时发明  

## Shell 复用

| surface | shell |
|---------|--------|
| b_end | 左栏 200–208 + 顶栏 48–56 + 内容区 |
| c_end | 顶栏（返回+标题）或底 TabBar；无侧栏 |

先实现 shell 函数模式，各页只换 Content regions。

## region 类型 → 节点策略

| type | Figma 实现要点 |
|------|----------------|
| filter_bar | 横向 auto-layout，输入框 + 次要按钮 + 一个 primary |
| data_table | 表头 `#FAFAFA` + 行 48–52px，无外层 card（B端） |
| kpi_row | 最多 3 列，等分或 1+2 |
| summary_strip | 横向：头像/图标 + 标题区 + 次要信息 |
| tabs | 按钮组，仅一个 filled primary |
| card_list | C 端列表卡片，间距 12 |
| bottom_cta | 固定底栏，单 primary 胶囊 |
| form_section | 分组标题 + 字段行 |

## 页型禁止项

生成前对照 `page-templates.yaml` 的 `forbid` 列表。

## 截图验收

每 Frame 完成后 `get_screenshot`，对照 design-plan 该页 ASCII。

## 落盘位置

- Frame 命名：`{page-id}-{页面名}` 或 `P{nn}-{页面名}`  
- 多页横向排列：`x += 1520` 避免重叠  
