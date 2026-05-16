#!/bin/bash
# build-graph-data.sh — 扫描 wiki/ 生成交互式图谱所需的 graph-data.json
#
# 用法：bash scripts/build-graph-data.sh <wiki_root> [output_path]
#   wiki_root     包含 wiki/ 子目录的知识库根路径
#   output_path   可选，默认 <wiki_root>/wiki/graph-data.json
#
# 环境变量：
#   LLM_WIKI_TEST_MODE=1   启用稳定输出（nodes/edges 按 id 字典序 + 时间戳固定）
#
# 退出码：0 成功；1 路径/依赖错误；2 wiki 结构不完整

set -eu
shopt -s nullglob

SCRIPT_DIR="${BASH_SOURCE[0]%/*}"
[ "$SCRIPT_DIR" = "${BASH_SOURCE[0]}" ] && SCRIPT_DIR="."
SCRIPT_DIR="$(cd "$SCRIPT_DIR" && pwd)"
# shellcheck disable=SC1091
source "$SCRIPT_DIR/shared-config.sh"

WIKI_ROOT="${1:-.}"
DEFAULT_OUTPUT="$WIKI_ROOT/wiki/graph-data.json"
OUTPUT="${2:-$DEFAULT_OUTPUT}"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
HELPER="$SKILL_DIR/scripts/graph-analysis.js"
MAX_CONTENT_BYTES=$((2 * 1024 * 1024))
MAX_CONTENT_LINES=500
MAX_INSIGHT_NODES=250
MAX_INSIGHT_EDGES=1000

command -v python3 >/dev/null 2>&1 || {
  echo "ERROR: python3 is not installed. Install it via:" >&2
  print_install_hint python3
  exit 1
}

NODE_BIN="$(command -v node 2>/dev/null || true)"
if [ -z "$NODE_BIN" ] && command -v zsh >/dev/null 2>&1; then
  NODE_BIN="$(zsh -ic 'command -v node' 2>/dev/null | tail -1 || true)"
fi

[ -n "$NODE_BIN" ] || {
  echo "ERROR: node is not installed. Install it via:" >&2
  print_install_hint node
  exit 1
}

[ -f "$HELPER" ] || {
  echo "ERROR: 找不到图谱分析 helper：$HELPER" >&2
  echo "       重装 skill 可修复（bash install.sh --platform claude）" >&2
  exit 1
}

WIKI_DIR="$WIKI_ROOT/wiki"
[ -d "$WIKI_DIR" ] || {
  echo "ERROR: wiki 目录不存在：$WIKI_DIR" >&2
  echo "       请先运行 init-wiki.sh 初始化知识库。" >&2
  exit 2
}

TMPDIR=$(mktemp -d -t llm-wiki-graph.XXXXXX)
trap 'rm -rf "$TMPDIR"' EXIT

if [ "${LLM_WIKI_TEST_MODE:-0}" = "1" ]; then
  BUILD_DATE="2026-01-01T00:00:00Z"
else
  BUILD_DATE="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
fi

WIKI_TITLE=""
if [ -f "$WIKI_ROOT/purpose.md" ]; then
  WIKI_TITLE=$(awk '/^# / { sub(/^# +/, ""); print; exit }' "$WIKI_ROOT/purpose.md")
fi
[ -n "$WIKI_TITLE" ] || WIKI_TITLE=$(basename "$(cd "$WIKI_ROOT" && pwd)")

NODES_TSV="$TMPDIR/nodes.tsv"
: > "$NODES_TSV"

scan_kind() {
  local subdir="$1" type="$2"
  local dir="$WIKI_DIR/$subdir"
  [ -d "$dir" ] || return 0
  local f id label
  while IFS= read -r f; do
    [ -f "$f" ] || continue
    id=$(basename "$f" .md)
    case "$id" in
      index|log|purpose|.wiki-schema|README) continue ;;
    esac
    label=$(awk '/^# / { sub(/^# +/, ""); gsub(/[[:space:]]+$/, ""); print; exit }' "$f")
    [ -n "$label" ] || label="$id"
    printf '%s\t%s\t%s\t%s\n' "$id" "$label" "$type" "$f" >> "$NODES_TSV"
  done < <(find "$dir" -type f -name '*.md' | LC_ALL=C sort)
}

scan_kind entities entity
scan_kind topics topic
scan_kind sources source
scan_kind comparisons comparison
scan_kind synthesis synthesis
scan_kind queries query

if [ ! -s "$NODES_TSV" ]; then
  mkdir -p "$(dirname "$OUTPUT")"
  OUTPUT_TMP="$TMPDIR/graph-data.empty.json"
  python3 - "$OUTPUT_TMP" "$BUILD_DATE" "$WIKI_TITLE" "$MAX_INSIGHT_NODES" "$MAX_INSIGHT_EDGES" <<'PY'
import json
import sys

output, build_date, wiki_title, max_nodes, max_edges = sys.argv[1:6]
data = {
    "meta": {
        "build_date": build_date,
        "wiki_title": wiki_title,
        "total_nodes": 0,
        "total_edges": 0,
        "initial_view": [],
        "degraded": False,
        "insights_degraded": False,
    },
    "nodes": [],
    "edges": [],
    "insights": {
        "surprising_connections": [],
        "isolated_nodes": [],
        "bridge_nodes": [],
        "sparse_communities": [],
        "meta": {
            "degraded": False,
            "node_count": 0,
            "edge_count": 0,
            "max_insight_nodes": int(max_nodes),
            "max_insight_edges": int(max_edges),
        },
    },
    "learning": {
        "version": 1,
        "entry": {
            "recommended_start_node_id": None,
            "recommended_start_reason": None,
            "default_mode": "global",
        },
        "views": {
            "path": {"enabled": False, "start_node_id": None, "node_ids": [], "degraded": True},
            "community": {
                "enabled": False,
                "community_id": None,
                "label": None,
                "node_ids": [],
                "is_weak": False,
                "degraded": True,
            },
            "global": {"enabled": True, "node_ids": [], "degraded": False},
        },
        "communities": [],
        "degraded": {"path_to_community": True, "community_to_global": True},
    },
}
with open(output, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
PY
  mv "$OUTPUT_TMP" "$OUTPUT"
  echo "空图谱已写入：${OUTPUT}（wiki/ 下无可纳入节点）"
  exit 0
fi

EDGES_RAW="$TMPDIR/edges_raw.tsv"
: > "$EDGES_RAW"

while IFS=$'\t' read -r id label type path; do
  awk -v src="$id" '
    {
      line = $0
      conf = ""
      if (match(line, /<!--[[:space:]]*confidence:[[:space:]]*[A-Z]+[[:space:]]*-->/)) {
        kind_str = substr(line, RSTART, RLENGTH)
        if (match(kind_str, /[A-Z]+/)) {
          conf = substr(kind_str, RSTART, RLENGTH)
        }
      }
      rest = line
      while (match(rest, /\[\[[^]]+\]\]/)) {
        inner = substr(rest, RSTART + 2, RLENGTH - 4)
        rest  = substr(rest, RSTART + RLENGTH)
        n = index(inner, "|")
        if (n > 0) inner = substr(inner, 1, n - 1)
        gsub(/^[[:space:]]+|[[:space:]]+$/, "", inner)
        if (inner == "" || inner == src) continue
        print src "\t" NR "\t" inner "\t" conf
      }
    }
  ' "$path" >> "$EDGES_RAW"
done < "$NODES_TSV"

VALID_IDS="$TMPDIR/valid_ids.txt"
cut -f1 "$NODES_TSV" | sort -u > "$VALID_IDS"

EDGES_TSV="$TMPDIR/edges.tsv"
# 合并同一 from+to 的多条 raw edges：
#   - 第一次遇到时记录（有 conf 就用 conf，无 conf 就留空 → 最终默认 EXTRACTED）
#   - 后续遇到带显式 conf 的条目时 **升级**（覆盖之前的空值或 EXTRACTED 默认）
#   - 若后续遇到多条不同的非空 conf，保留首个非空（按首次显式标注优先）
#
# 这解决了"同一对节点被多次 [[]] 引用（正文 + 相关页面列表）时，
#  首次出现的空 conf 会永久锁定 edge type 为 EXTRACTED"的问题。
awk -F'\t' -v valids="$VALID_IDS" '
  BEGIN {
    while ((getline line < valids) > 0) valid[line] = 1
    close(valids)
  }
  {
    from = $1; to = $3; conf = $4
    if (!(to in valid)) next
    if (from == to) next
    key = from "\t" to
    if (!(key in seen)) {
      seen[key] = 1
      saved_conf[key] = conf  # 可能为空，在 END 中兜底为 EXTRACTED
      order[++count] = key
    } else if (conf != "" && saved_conf[key] == "") {
      # 升级：之前未见显式 conf（留空），现在有，采用
      saved_conf[key] = conf
    }
  }
  END {
    for (i = 1; i <= count; i++) {
      split(order[i], parts, "\t")
      t = saved_conf[order[i]]
      if (t != "EXTRACTED" && t != "INFERRED" && t != "AMBIGUOUS") t = "EXTRACTED"
      print parts[1] "\t" parts[2] "\t" t
    }
  }
' "$EDGES_RAW" > "$EDGES_TSV"

TOTAL_SIZE=0
while IFS=$'\t' read -r id label type path; do
  sz=$(wc -c < "$path" 2>/dev/null || echo 0)
  TOTAL_SIZE=$((TOTAL_SIZE + sz))
done < "$NODES_TSV"

DEGRADE=0
if [ "$TOTAL_SIZE" -gt "$MAX_CONTENT_BYTES" ]; then
  DEGRADE=1
fi

NODES_JSONL="$TMPDIR/nodes.jsonl"
: > "$NODES_JSONL"
while IFS=$'\t' read -r id label type path; do
  abs_path=$(cd "$(dirname "$path")" && pwd)/$(basename "$path")
  python3 - "$id" "$label" "$type" "$abs_path" <<'PY' >> "$NODES_JSONL"
import json
import sys

node_id, label, node_type, source_path = sys.argv[1:5]
print(json.dumps({
    "id": node_id,
    "label": label,
    "type": node_type,
    "source_path": source_path,
}, ensure_ascii=False))
PY
done < "$NODES_TSV"

EDGES_JSONL="$TMPDIR/edges.jsonl"
: > "$EDGES_JSONL"
idx=0
while IFS=$'\t' read -r from to etype; do
  idx=$((idx + 1))
  python3 - "e$idx" "$from" "$to" "$etype" <<'PY' >> "$EDGES_JSONL"
import json
import sys

edge_id, from_id, to_id, edge_type = sys.argv[1:5]
print(json.dumps({
    "id": edge_id,
    "from": from_id,
    "to": to_id,
    "type": edge_type,
}, ensure_ascii=False))
PY
done < "$EDGES_TSV"

if [ "${LLM_WIKI_TEST_MODE:-0}" = "1" ]; then
  python3 - "$NODES_JSONL" "$TMPDIR/nodes.raw.json" nodes-test <<'PY'
import json
import sys

src, dst, mode = sys.argv[1:4]
items = [json.loads(line) for line in open(src, encoding="utf-8") if line.strip()]
if mode == "nodes-test":
    items = sorted(items, key=lambda item: item.get("id", ""))
with open(dst, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
    f.write("\n")
PY
  python3 - "$EDGES_JSONL" "$TMPDIR/edges.raw.json" edges-test <<'PY'
import json
import sys

src, dst, mode = sys.argv[1:4]
items = [json.loads(line) for line in open(src, encoding="utf-8") if line.strip()]
if mode == "edges-test":
    items = sorted(items, key=lambda item: (item.get("from", ""), item.get("to", ""), item.get("type", "")))
    for index, item in enumerate(items, start=1):
        item["id"] = f"e{index}"
with open(dst, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
    f.write("\n")
PY
else
  python3 - "$NODES_JSONL" "$TMPDIR/nodes.raw.json" <<'PY'
import json
import sys

src, dst = sys.argv[1:3]
items = [json.loads(line) for line in open(src, encoding="utf-8") if line.strip()]
with open(dst, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
    f.write("\n")
PY
  python3 - "$EDGES_JSONL" "$TMPDIR/edges.raw.json" <<'PY'
import json
import sys

src, dst = sys.argv[1:3]
items = [json.loads(line) for line in open(src, encoding="utf-8") if line.strip()]
with open(dst, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
    f.write("\n")
PY
fi

ANALYSIS_JSON="$TMPDIR/analysis.json"
if ! "$NODE_BIN" "$HELPER" \
  "$TMPDIR/nodes.raw.json" \
  "$TMPDIR/edges.raw.json" \
  "$ANALYSIS_JSON" \
  "$DEGRADE" \
  "$MAX_CONTENT_LINES" \
  "$MAX_INSIGHT_NODES" \
  "$MAX_INSIGHT_EDGES"; then
  echo "ERROR: 图谱分析 helper 执行失败：$HELPER" >&2
  exit 1
fi

python3 - "$ANALYSIS_JSON" <<'PY' || {
import json
import sys

path = sys.argv[1]
try:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception:
    sys.exit(1)

checks = [
    isinstance(data.get("nodes"), list),
    isinstance(data.get("edges"), list),
    isinstance(data.get("insights"), dict),
    isinstance(data.get("insights", {}).get("surprising_connections"), list),
    isinstance(data.get("insights", {}).get("isolated_nodes"), list),
    isinstance(data.get("insights", {}).get("bridge_nodes"), list),
    isinstance(data.get("insights", {}).get("sparse_communities"), list),
    isinstance(data.get("learning"), dict),
]
sys.exit(0 if all(checks) else 1)
PY
  echo "ERROR: 图谱分析 helper 返回坏 JSON：$ANALYSIS_JSON" >&2
  exit 1
}

if [ "${LLM_WIKI_TEST_MODE:-0}" = "1" ]; then
  python3 - "$ANALYSIS_JSON" "$TMPDIR/nodes.sorted.json" nodes-test <<'PY'
import json
import sys

src, dst, mode = sys.argv[1:4]
with open(src, "r", encoding="utf-8") as f:
    data = json.load(f)
items = data.get("nodes", [])
items = sorted(items, key=lambda item: item.get("id", ""))
with open(dst, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
    f.write("\n")
PY
  python3 - "$ANALYSIS_JSON" "$TMPDIR/edges.sorted.json" edges-test <<'PY'
import json
import sys

src, dst, mode = sys.argv[1:4]
with open(src, "r", encoding="utf-8") as f:
    data = json.load(f)
items = data.get("edges", [])
items = sorted(items, key=lambda item: (item.get("from", ""), item.get("to", ""), item.get("type", "")))
for index, item in enumerate(items, start=1):
    item["id"] = f"e{index}"
with open(dst, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
    f.write("\n")
PY
else
  python3 - "$ANALYSIS_JSON" "$TMPDIR/nodes.sorted.json" nodes <<'PY'
import json
import sys

src, dst, key = sys.argv[1:4]
with open(src, "r", encoding="utf-8") as f:
    data = json.load(f)
with open(dst, "w", encoding="utf-8") as f:
    json.dump(data.get(key, []), f, ensure_ascii=False, indent=2)
    f.write("\n")
PY
  python3 - "$ANALYSIS_JSON" "$TMPDIR/edges.sorted.json" edges <<'PY'
import json
import sys

src, dst, key = sys.argv[1:4]
with open(src, "r", encoding="utf-8") as f:
    data = json.load(f)
with open(dst, "w", encoding="utf-8") as f:
    json.dump(data.get(key, []), f, ensure_ascii=False, indent=2)
    f.write("\n")
PY
fi

python3 - "$TMPDIR/nodes.sorted.json" "$TMPDIR/edges.sorted.json" "$ANALYSIS_JSON" "$TMPDIR/initial-view.json" "$TMPDIR/counts.env" <<'PY'
import json
import sys

nodes_path, edges_path, analysis_path, initial_path, counts_path = sys.argv[1:6]
with open(nodes_path, "r", encoding="utf-8") as f:
    nodes = json.load(f)
with open(edges_path, "r", encoding="utf-8") as f:
    edges = json.load(f)
with open(analysis_path, "r", encoding="utf-8") as f:
    analysis = json.load(f)

degree = {}
for edge in edges:
    degree[edge.get("from")] = degree.get(edge.get("from"), 0) + 1
    degree[edge.get("to")] = degree.get(edge.get("to"), 0) + 1

groups = {}
for node in nodes:
    groups.setdefault(node.get("community", "_"), []).append(node)

reps = []
for group_nodes in groups.values():
    if group_nodes:
        reps.append(max(group_nodes, key=lambda item: degree.get(item.get("id"), 0)).get("id"))

rep_set = set(reps)
rest = [
    node.get("id")
    for node in sorted(nodes, key=lambda item: -degree.get(item.get("id"), 0))
    if node.get("id") not in rep_set
]
initial_view = (reps + rest)[:30]

with open(initial_path, "w", encoding="utf-8") as f:
    json.dump(initial_view, f, ensure_ascii=False, indent=2)
    f.write("\n")

insights_degraded = analysis.get("insights", {}).get("meta", {}).get("degraded") is True
with open(counts_path, "w", encoding="utf-8") as f:
    f.write(f"NODE_COUNT={len(nodes)}\n")
    f.write(f"EDGE_COUNT={len(edges)}\n")
    f.write(f"INITIAL_VIEW_COUNT={len(initial_view)}\n")
    f.write(f"INSIGHTS_DEGRADED={'true' if insights_degraded else 'false'}\n")
PY

# shellcheck disable=SC1090
source "$TMPDIR/counts.env"

mkdir -p "$(dirname "$OUTPUT")"
OUTPUT_TMP="$TMPDIR/graph-data.final.json"

python3 - \
  "$BUILD_DATE" \
  "$WIKI_TITLE" \
  "$NODE_COUNT" \
  "$EDGE_COUNT" \
  "$TMPDIR/initial-view.json" \
  "$TMPDIR/nodes.sorted.json" \
  "$TMPDIR/edges.sorted.json" \
  "$ANALYSIS_JSON" \
  "$DEGRADE" \
  "$INSIGHTS_DEGRADED" \
  "$OUTPUT_TMP" <<'PY'
import json
import sys

(
    build_date,
    wiki_title,
    node_count,
    edge_count,
    initial_path,
    nodes_path,
    edges_path,
    analysis_path,
    degraded,
    insights_degraded,
    output_path,
) = sys.argv[1:12]

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

analysis = read_json(analysis_path)
data = {
    "meta": {
        "build_date": build_date,
        "wiki_title": wiki_title,
        "total_nodes": int(node_count),
        "total_edges": int(edge_count),
        "initial_view": read_json(initial_path),
        "degraded": degraded == "1",
        "insights_degraded": insights_degraded == "true",
    },
    "nodes": read_json(nodes_path),
    "edges": read_json(edges_path),
    "insights": analysis.get("insights", {}),
    "learning": analysis.get("learning", {}),
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
PY

mv "$OUTPUT_TMP" "$OUTPUT"

echo "图谱数据已生成：$OUTPUT"
echo "  节点：$NODE_COUNT"
echo "  关联：$EDGE_COUNT"
echo "  初始视图：$INITIAL_VIEW_COUNT 个节点"
[ "$DEGRADE" = "1" ] && echo "  ⚠ 降级模式：内嵌内容 > 2MB，每节点仅保留前 ${MAX_CONTENT_LINES} 行"
[ "$INSIGHTS_DEGRADED" = "true" ] && echo "  ⚠ 洞察降级：图规模超出预算，仅保留基础权重与社区"
exit 0
