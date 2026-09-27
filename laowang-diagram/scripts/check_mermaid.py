#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""laowang-diagram 产物自检脚本。

支持两类文件：
  - .mmd / .md  -> 校验 Mermaid flowchart 源码（.md 会自动抽取 ```mermaid 代码块）
  - .drawio     -> 校验 draw.io XML（根单元格、引用完整性、泳道内节点坐标）

用法：
    python3 check_mermaid.py path/to/diagram.mmd
    python3 check_mermaid.py path/to/example.md
    python3 check_mermaid.py path/to/diagram.drawio

退出码：0 = 全部通过；1 = 存在错误；2 = 存在警告但无错误。
"""

import os
import re
import sys
import xml.dom.minidom

# Mermaid 保留字，不能直接作为节点 ID
KEYWORDS = {
    "end", "graph", "flowchart", "subgraph", "class", "classdef", "style",
    "linkstyle", "click", "direction", "state", "default", "flowchart-v2",
}

# 形状开括号 -> 闭括号
SHAPE_PAIRS = [
    ("([", "])"),
    ("[[", "]]"),
    ("((", "))"),
    ("[", "]"),
    ("(", ")"),
    ("{", "}"),
]

ARROW_RE = re.compile(r"(-\.-+>|--+>|==+>|--+o|--+x|<-->|---|-\.-|===|\.\.\.)")

# 节点定义：ID 紧跟形状开括号
NODE_OPEN_RE = re.compile(r"([A-Za-z][A-Za-z0-9_]*)\s*(\[\[|\(\[|\(\(|\[|\(|\{)")

# 需要加引号的字符
NEEDS_QUOTE = set("()[]{}、，：；\"'")


class Finding(object):
    def __init__(self, level, line, code, msg):
        self.level = level
        self.line = line
        self.code = code
        self.msg = msg

    def __str__(self):
        loc = "L%d" % self.line if self.line else "-"
        return "[%s] %s %s: %s" % (self.level, loc, self.code, self.msg)


def extract_mermaid(text):
    """从 .md 里抽取所有 ```mermaid 代码块；.mmd 直接返回全文。"""
    blocks = re.findall(r"```mermaid\s*\n(.*?)```", text, re.S)
    if blocks:
        return blocks
    return [text]


def strip_comments(line):
    idx = line.find("%%")
    if idx >= 0:
        return line[:idx]
    return line


def find_label(line, start):
    """从 start 位置（形状开括号处）取出标签文本，返回 (label, end_index)。"""
    for opener, closer in SHAPE_PAIRS:
        if line.startswith(opener, start):
            label_start = start + len(opener)
            end = line.find(closer, label_start)
            if end < 0:
                return None, start + len(opener)
            return line[label_start:end], end + len(closer)
    return None, start


def parse_nodes(line, lineno, findings):
    """抽取本行的节点定义，返回 (清理掉标签的行, [ids], {id: label}, {id: shape})。"""
    ids = []
    labels = {}
    shapes = {}
    spans = []
    pos = 0
    while True:
        m = NODE_OPEN_RE.search(line, pos)
        if not m:
            break
        node_id = m.group(1)
        shape_start = m.start(2)
        shape = m.group(2)
        label, end = find_label(line, shape_start)
        if label is None:
            findings.append(Finding("ERROR", lineno, "UNCLOSED-SHAPE",
                                    "节点 %s 的形状括号未闭合" % node_id))
            pos = m.end()
            continue
        spans.append((m.start(1), end))
        ids.append(node_id)
        labels[node_id] = label.strip()
        shapes[node_id] = shape
        pos = end
    if not spans:
        return line, [], {}, {}
    # 用 ID 替换整段定义，便于后续在同一行上识别连边
    rebuilt = []
    last = 0
    for (s, e), nid in zip(spans, ids):
        rebuilt.append(line[last:s])
        rebuilt.append(nid)
        last = e
    rebuilt.append(line[last:])
    return "".join(rebuilt), ids, labels, shapes


def check_label(node_id, label, lineno, findings):
    if not label:
        findings.append(Finding("ERROR", lineno, "EMPTY-LABEL",
                                "节点 %s 的标签为空" % node_id))
        return
    stripped = label.strip()
    quoted = stripped.startswith('"') and stripped.endswith('"') and len(stripped) > 1
    if quoted:
        return
    bad = sorted(set(ch for ch in stripped if ch in NEEDS_QUOTE))
    if bad:
        findings.append(Finding(
            "ERROR", lineno, "UNQUOTED-LABEL",
            "节点 %s 的标签含特殊字符 %s，需用双引号包裹：%s[\"%s\"]"
            % (node_id, "".join(bad), node_id, stripped)))
    if len(stripped) > 18:
        findings.append(Finding(
            "WARN", lineno, "LONG-LABEL",
            "节点 %s 标签 %d 字，超过 18 字，渲染后易溢出" % (node_id, len(stripped))))


def check_mermaid(source, findings, origin):
    lines = source.splitlines()
    depth = 0
    subgraph_lines = []
    defined = {}
    node_shapes = {}
    incoming = {}
    outgoing = {}
    edges = []
    node_count = 0

    for i, raw in enumerate(lines, 1):
        line = strip_comments(raw).strip()
        if not line:
            continue
        low = line.lower()
        if low.startswith("flowchart") or low.startswith("graph "):
            continue
        if low.startswith("subgraph"):
            depth += 1
            subgraph_lines.append((i, line))
            continue
        if low == "end":
            if depth == 0:
                findings.append(Finding("ERROR", i, "UNBALANCED-END",
                                        "多出一个 end，没有对应的 subgraph"))
            else:
                depth -= 1
            continue
        if low.startswith(("classdef", "class ", "style ", "linkstyle",
                           "click ", "direction")):
            continue

        cleaned, ids, labels, shapes = parse_nodes(line, i, findings)
        for nid in ids:
            node_count += 1
            if nid in KEYWORDS:
                findings.append(Finding(
                    "ERROR", i, "RESERVED-ID",
                    "节点 ID %s 命中 Mermaid 保留字，会导致解析冲突" % nid))
            prev = defined.get(nid)
            if prev is not None and prev != labels[nid]:
                findings.append(Finding(
                    "ERROR", i, "DUPLICATE-ID",
                    "节点 %s 被重复定义为不同标签（%s / %s）"
                    % (nid, prev, labels[nid])))
            defined[nid] = labels[nid]
            node_shapes[nid] = shapes[nid]
            check_label(nid, labels[nid], i, findings)
            incoming.setdefault(nid, 0)
            outgoing.setdefault(nid, 0)

        # 在清理后的行上找连边
        # 单捕获组 split 的结果形如 [左, 箭头, 右, 箭头, 右, ...]
        parts = ARROW_RE.split(cleaned)
        if len(parts) > 2:
            for idx in range(0, len(parts) - 2, 2):
                left_text = re.sub(r"\|[^|]*\|", " ", parts[idx])
                right_text = re.sub(r"\|[^|]*\|", " ", parts[idx + 2])
                left = re.findall(r"[A-Za-z][A-Za-z0-9_]*", left_text)
                right = re.findall(r"[A-Za-z][A-Za-z0-9_]*", right_text)
                if not left or not right:
                    continue
                src, dst = left[-1], right[0]
                edges.append((src, dst, i))
                for n in (src, dst):
                    defined.setdefault(n, None)
                    node_shapes.setdefault(n, None)
                    incoming.setdefault(n, 0)
                    outgoing.setdefault(n, 0)
                outgoing[src] = outgoing.get(src, 0) + 1
                incoming[dst] = incoming.get(dst, 0) + 1

    if depth != 0:
        findings.append(Finding("ERROR", len(lines), "UNBALANCED-SUBGRAPH",
                                "subgraph 与 end 不配平，缺 %d 个 end" % depth))
    if not edges:
        findings.append(Finding("ERROR", 0, "NO-EDGE", "整图没有任何连边"))
    if node_count > 25:
        findings.append(Finding("WARN", 0, "TOO-MANY-NODES",
                                "节点数 %d 超过 25，建议拆图" % node_count))

    for nid in sorted(defined):
        # 体育场形 ([...]) 与圆形 ((...)) 视为起止节点，豁免入边/出边检查
        if node_shapes.get(nid) in ("([", "(("):
            continue
        if defined[nid] is None and incoming.get(nid, 0) == 0 and outgoing.get(nid, 0) == 0:
            findings.append(Finding("ERROR", 0, "DEAD-NODE",
                                    "节点 %s 只被定义、从未参与任何连边" % nid))
        elif incoming.get(nid, 0) == 0 and outgoing.get(nid, 0) > 0:
            findings.append(Finding(
                "WARN", 0, "POSSIBLE-ORPHAN",
                "节点 %s 没有任何入边，若不是起始节点请检查" % nid))
        elif outgoing.get(nid, 0) == 0 and incoming.get(nid, 0) > 0:
            findings.append(Finding(
                "WARN", 0, "POSSIBLE-DEADEND",
                "节点 %s 没有任何出边，若不是终止节点请检查" % nid))

    if not any("subgraph" in l for _, l in subgraph_lines):
        findings.append(Finding("WARN", 0, "NO-SWIMLANE",
                                "没有 subgraph，未形成泳道结构"))
    return edges


def check_drawio(path, findings):
    try:
        dom = xml.dom.minidom.parse(path)
    except Exception as exc:  # noqa: BLE001
        findings.append(Finding("ERROR", 0, "XML-PARSE", "XML 解析失败：%s" % exc))
        return

    cells = dom.getElementsByTagName("mxCell")
    ids = {}
    for cell in cells:
        cid = cell.getAttribute("id")
        if not cid:
            findings.append(Finding("ERROR", 0, "CELL-NO-ID", "存在没有 id 的 mxCell"))
            continue
        if cid in ids:
            findings.append(Finding("ERROR", 0, "CELL-DUP-ID",
                                    "mxCell id 重复：%s" % cid))
        ids[cid] = cell

    for required in ("0", "1"):
        if required not in ids:
            findings.append(Finding("ERROR", 0, "MISSING-ROOT",
                                    "缺少根单元格 id=\"%s\"，draw.io 将无法打开" % required))

    lanes = 0
    for cid, cell in ids.items():
        if cell.getAttribute("vertex") == "1" and "swimlane" in cell.getAttribute("style"):
            lanes += 1
        parent = cell.getAttribute("parent")
        if parent and parent not in ids:
            findings.append(Finding("ERROR", 0, "DANGLING-PARENT",
                                    "mxCell %s 的 parent=%s 不存在" % (cid, parent)))
        for attr in ("source", "target"):
            ref = cell.getAttribute(attr)
            if ref and ref not in ids:
                findings.append(Finding("ERROR", 0, "DANGLING-EDGE",
                                        "连边 %s 的 %s=%s 不存在" % (cid, attr, ref)))
        if cell.getAttribute("edge") == "1":
            if not cell.getAttribute("source") or not cell.getAttribute("target"):
                findings.append(Finding("WARN", 0, "EDGE-NO-ENDPOINT",
                                        "连边 %s 缺少 source 或 target" % cid))

    # 泳道内节点坐标检查
    for cid, cell in ids.items():
        if "swimlane" not in cell.getAttribute("style"):
            continue
        start_size = 30
        m = re.search(r"startSize=(\d+)", cell.getAttribute("style"))
        if m:
            start_size = int(m.group(1))
        for child in cell.getElementsByTagName("mxCell"):
            geo = child.getElementsByTagName("mxGeometry")
            if not geo:
                continue
            y = geo[0].getAttribute("y")
            if y and float(y) < start_size:
                findings.append(Finding(
                    "ERROR", 0, "NODE-OVERLAPS-LANE-TITLE",
                    "节点 %s 的 y=%s 小于泳道 startSize=%d，会压住泳道标题栏"
                    % (child.getAttribute("id"), y, start_size)))

    if lanes == 0:
        findings.append(Finding("WARN", 0, "NO-SWIMLANE",
                                "未发现 swimlane 容器，未形成泳道结构"))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1

    total_errors = 0
    total_warnings = 0

    for path in argv[1:]:
        if not os.path.exists(path):
            print("[ERROR] - FILE-MISSING: 文件不存在：%s" % path)
            total_errors += 1
            continue

        findings = []
        if path.endswith(".drawio"):
            check_drawio(path, findings)
        else:
            with open(path, "r", encoding="utf-8") as fh:
                text = fh.read()
            for idx, block in enumerate(extract_mermaid(text), 1):
                if len(extract_mermaid(text)) > 1:
                    findings.append(Finding("INFO", 0, "BLOCK",
                                            "第 %d 个 mermaid 代码块" % idx))
                check_mermaid(block, findings, path)

        errors = [f for f in findings if f.level == "ERROR"]
        warnings = [f for f in findings if f.level == "WARN"]
        total_errors += len(errors)
        total_warnings += len(warnings)

        status = "PASS" if not errors and not warnings else (
            "FAIL" if errors else "WARN")
        print("=" * 64)
        print("%s  %s" % (status, path))
        print("=" * 64)
        for f in findings:
            print("  " + str(f))
        if not findings:
            print("  无问题。")

    print("")
    print("汇总：%d 个错误，%d 个警告" % (total_errors, total_warnings))
    if total_errors:
        return 1
    if total_warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
