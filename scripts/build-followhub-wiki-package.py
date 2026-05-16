#!/usr/bin/env python3
"""Build a FollowHub Wiki R2 package from a llm-wiki directory.

The package is intentionally plain JSON + static assets so page_github can
sync it from R2 before an Astro build, and can still use the same files as a
local development fallback.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DATA_VERSION = "followhub-wiki-r2/v1"
KNOWN_DOMAINS = {
    "LLM/VLM": "llm-vlm",
    "Physical/Embodied Intelligence": "physical-embodied-intelligence",
    "AIGC": "aigc",
    "Agent": "agent",
}
DOMAIN_ALIASES = {
    **{slug: slug for slug in KNOWN_DOMAINS.values()},
    **{name.lower(): slug for name, slug in KNOWN_DOMAINS.items()},
    "physical-embodied-intelligence": "physical-embodied-intelligence",
    "embodied": "physical-embodied-intelligence",
    "llm": "llm-vlm",
    "vlm": "llm-vlm",
}


def eprint(message: str) -> None:
    print(message, file=sys.stderr)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a FollowHub Wiki R2 package.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("wiki_root", help="Wiki root containing wiki/sources, wiki/topics, wiki/synthesis")
    parser.add_argument("output_dir", help="Output package directory")
    parser.add_argument("--page-root", default="", help="Optional page_github root for manifest metadata")
    parser.add_argument("--base-path", default="wiki", help="R2 object prefix")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON files")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings")
    return parser.parse_args()


def slugify(value: Any) -> str:
    text = str(value or "").strip().lower().replace("π", "pi")
    text = re.sub(r"[^a-z0-9\u4e00-\u9fa5]+", "-", text)
    return text.strip("-")


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    if value in {"[]", "{}"}:
        return [] if value == "[]" else {}
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",") if part.strip()]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() in {"null", "none"}:
        return ""
    if re.fullmatch(r"-?\d+", value):
        try:
            return int(value)
        except ValueError:
            pass
    return unquote(value)


def parse_frontmatter(raw: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None
    current_map_key: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        list_match = re.match(r"^\s{2}-\s*(.*)$", line)
        if list_match and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(parse_scalar(list_match.group(1)))
            current_map_key = None
            continue

        map_match = re.match(r"^\s{2}([A-Za-z0-9_-]+):\s*(.*)$", line)
        if map_match and current_key:
            if not isinstance(data.get(current_key), dict):
                data[current_key] = {}
            child_key, child_value = map_match.groups()
            data[current_key][child_key] = parse_scalar(child_value)
            current_map_key = child_key
            continue

        nested_list_match = re.match(r"^\s{4}-\s*(.*)$", line)
        if nested_list_match and current_key and current_map_key and isinstance(data.get(current_key), dict):
            child = data[current_key].setdefault(current_map_key, [])
            if isinstance(child, list):
                child.append(parse_scalar(nested_list_match.group(1)))
            continue

        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            current_key = None
            current_map_key = None
            continue

        key, value = match.groups()
        current_key = key
        current_map_key = None
        value = value.strip()
        if value == "":
            data[key] = []
        else:
            data[key] = parse_scalar(value)
    return data


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    return parse_frontmatter(text[4:end].strip("\n")), text[end + 5 :].lstrip("\n")


def as_list(value: Any) -> list[Any]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [item for item in value if item not in ("", None)]
    return [value]


def as_str_list(value: Any) -> list[str]:
    return [str(item).strip() for item in as_list(value) if str(item).strip()]


def first_heading(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def section_after_heading(body: str, headings: list[str]) -> str:
    lines = body.splitlines()
    heading_set = {heading.strip().lower() for heading in headings}
    capture = False
    collected: list[str] = []
    for line in lines:
        normalized = line.lstrip("#").strip().lower()
        if line.startswith("#") and normalized in heading_set:
            capture = True
            continue
        if capture and line.startswith("## "):
            break
        if capture:
            collected.append(line)
    return "\n".join(collected).strip()


def summary_from_body(body: str, fallback: str) -> str:
    candidates = [
        section_after_heading(body, ["太长不看", "TL;DR", "主题概述", "综述结论", "当前判断"]),
        fallback,
    ]
    for value in candidates:
        text = strip_markdown(value)
        if text:
            return text[:600]
    return ""


def strip_markdown(value: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", str(value or ""))
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[>\-*]\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()


def normalize_domain(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    return DOMAIN_ALIASES.get(raw, DOMAIN_ALIASES.get(raw.lower(), slugify(raw)))


def links_from_frontmatter(data: dict[str, Any]) -> dict[str, str]:
    links = data.get("links")
    if not isinstance(links, dict):
        links = {}
    result = {key: str(links.get(key) or "").strip() for key in ["original", "arxiv", "pdf", "project", "github", "hjfy", "doi"]}
    result["original"] = result["original"] or str(data.get("source_url") or data.get("source_input") or "").strip()
    result["pdf"] = result["pdf"] or str(data.get("pdf_url") or "").strip()
    result["project"] = result["project"] or str(data.get("project_url") or "").strip()
    result["github"] = result["github"] or str(data.get("github_url") or "").strip()
    result["hjfy"] = result["hjfy"] or str(data.get("hjfy_url") or "").strip()
    return result


def read_pages(root: Path, kind: str) -> list[dict[str, Any]]:
    base = root / "wiki" / kind
    if not base.exists():
        return []
    pages: list[dict[str, Any]] = []
    for path in sorted(base.glob("*.md")):
        data, body = split_frontmatter(path.read_text(encoding="utf-8"))
        slug = str(data.get("slug") or slugify(path.stem))
        title = str(data.get("title") or first_heading(body, path.stem))
        pages.append(
            {
                "slug": slug,
                "title": title,
                "frontmatter": data,
                "body": body,
                "path": path,
            }
        )
    return pages


def source_record(page: dict[str, Any]) -> dict[str, Any]:
    data = page["frontmatter"]
    body = page["body"]
    links = links_from_frontmatter(data)
    domains = [normalize_domain(item) for item in as_str_list(data.get("domains"))]
    domains = [item for item in domains if item]
    tags = as_str_list(data.get("tags"))[:2]
    summary = str(data.get("summary") or "").strip() or summary_from_body(body, "")
    source_type = str(data.get("source_type") or data.get("material_type") or "material").strip()
    material_type = str(data.get("material_type") or source_type or "material").strip()
    risk_section = section_after_heading(body, ["风险与判断", "Risks"])
    risk_limitations = split_labeled_items(extract_labeled_block(risk_section, ["局限", "限制", "Limitations"]))
    if not risk_limitations:
        risk_limitations = split_bullets(risk_section)
    risk_scenarios = split_labeled_items(extract_labeled_block(risk_section, ["适用场景", "适用", "Application Scenarios", "Use Cases"]))
    risk_judgment = split_labeled_items(extract_labeled_block(risk_section, ["最终判断", "判断", "Final Judgment", "Verdict"]))
    return {
        "id": str(data.get("id") or page["slug"]),
        "slug": page["slug"],
        "title": page["title"],
        "type": "source",
        "materialType": material_type,
        "sourceType": source_type if source_type in {"paper", "wechat", "web", "note"} else material_type,
        "sourceUrl": links.get("original", ""),
        "htmlUrl": str(data.get("html_url") or links.get("html") or links.get("arxiv") or "").strip(),
        "pdfUrl": links.get("pdf", ""),
        "codeUrl": links.get("github") or links.get("project", ""),
        "translationUrl": links.get("hjfy", ""),
        "links": links,
        "publishDate": str(data.get("date") or data.get("publish_date") or data.get("created") or "").strip(),
        "created": str(data.get("created") or "").strip(),
        "updated": str(data.get("updated") or "").strip(),
        "authors": as_str_list(data.get("authors")),
        "affiliation": str(data.get("affiliation") or "").strip(),
        "keywords": tags,
        "tags": tags,
        "primaryDomainSlug": domains[0] if domains else "",
        "domainSlugs": domains,
        "domains": as_str_list(data.get("domains")),
        "heroImage": str(data.get("hero_image") or data.get("heroImage") or "").strip(),
        "rawRefs": as_str_list(data.get("raw_refs")),
        "relatedTopicSlugs": as_str_list(data.get("related_topics")),
        "relatedSynthesisSlugs": as_str_list(data.get("related_syntheses")),
        "confidence": str(data.get("confidence") or "EXTRACTED").strip(),
        "summary": summary,
        "tldr": section_after_heading(body, ["太长不看", "TL;DR"]) or summary,
        "intuition": section_after_heading(body, ["直观理解"]),
        "abstractEn": section_after_heading(body, ["论文摘要（英文原文）", "Abstract"]),
        "abstractZh": section_after_heading(body, ["论文摘要（中文翻译）", "中文摘要"]),
        "background": section_after_heading(body, ["背景与问题"]),
        "method": section_after_heading(body, ["方法"]),
        "resultHighlights": split_bullets(section_after_heading(body, ["结果"])),
        "insightCore": split_bullets(section_after_heading(body, ["洞察"])),
        "risks": risk_section,
        "riskLimitations": risk_limitations,
        "riskScenarios": risk_scenarios,
        "riskJudgment": risk_judgment,
        "figureGallery": extract_figures(body),
        "body": body,
    }


def normalize_label(value: str) -> str:
    return re.sub(r"[\s:：]+", "", str(value or "").strip().lower())


def extract_labeled_block(section: str, labels: list[str]) -> str:
    wanted = {normalize_label(label) for label in labels}
    capture = False
    collected: list[str] = []
    for line in str(section or "").splitlines():
        label_match = re.match(r"^\s*\*\*([^*]+?)\s*[:：]?\*\*\s*(.*)$", line)
        if label_match:
            label = normalize_label(label_match.group(1))
            tail = label_match.group(2).strip()
            if label in wanted:
                capture = True
                collected = [tail] if tail else []
                continue
            if capture:
                break
        if capture:
            collected.append(line)
    return "\n".join(collected).strip()


def split_labeled_items(value: str) -> list[str]:
    bullets = split_bullets(value)
    if bullets:
        return bullets
    text = strip_markdown(value)
    return [text] if text else []


def split_bullets(value: str) -> list[str]:
    result: list[str] = []
    for line in str(value or "").splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            result.append(strip_markdown(stripped[2:]))
    return result[:12]


def extract_figures(body: str) -> list[dict[str, str]]:
    figures: list[dict[str, str]] = []
    for match in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", body):
        figures.append({"caption": match.group(1).strip() or "图", "src": match.group(2).strip()})
    return figures[:16]


def topic_record(page: dict[str, Any], source_titles: dict[str, str]) -> dict[str, Any]:
    data = page["frontmatter"]
    body = page["body"]
    source_slugs = as_str_list(data.get("source_slugs"))
    synthesis_slugs = as_str_list(data.get("synthesis_slugs"))
    domains = [normalize_domain(item) for item in as_str_list(data.get("domains"))]
    return {
        "id": str(data.get("id") or page["slug"]),
        "slug": page["slug"],
        "title": page["title"],
        "type": "topic",
        "domain": domains[0] if domains else "",
        "domains": as_str_list(data.get("domains")),
        "tags": as_str_list(data.get("tags"))[:2],
        "summary": str(data.get("summary") or "").strip() or summary_from_body(body, ""),
        "status": str(data.get("status") or "active").strip(),
        "created": str(data.get("created") or "").strip(),
        "updated": str(data.get("updated") or "").strip(),
        "sourceSlugs": source_slugs,
        "synthesisSlugs": synthesis_slugs,
        "sourceTitles": [source_titles.get(slug, slug) for slug in source_slugs],
        "relatedPages": extract_wiki_links(body),
        "openQuestions": as_str_list(data.get("open_questions")),
        "body": body,
    }


def synthesis_record(page: dict[str, Any], source_titles: dict[str, str], topic_titles: dict[str, str]) -> dict[str, Any]:
    data = page["frontmatter"]
    body = page["body"]
    source_slugs = as_str_list(data.get("source_slugs"))
    topic_slugs = as_str_list(data.get("topic_slugs"))
    domains = [normalize_domain(item) for item in as_str_list(data.get("domains"))]
    return {
        "id": str(data.get("id") or page["slug"]),
        "slug": page["slug"],
        "title": page["title"],
        "type": "synthesis",
        "kind": str(data.get("kind") or "overview").strip(),
        "domain": domains[0] if domains else "",
        "domains": as_str_list(data.get("domains")),
        "tags": as_str_list(data.get("tags"))[:2],
        "summary": str(data.get("summary") or "").strip() or summary_from_body(body, ""),
        "judgment": str(data.get("judgment") or "").strip(),
        "created": str(data.get("created") or "").strip(),
        "updated": str(data.get("updated") or "").strip(),
        "sourceSlugs": source_slugs,
        "topicSlugs": topic_slugs,
        "sourceTitles": [source_titles.get(slug, slug) for slug in source_slugs],
        "topicTitles": [topic_titles.get(slug, slug) for slug in topic_slugs],
        "relatedPages": extract_wiki_links(body),
        "claims": as_str_list(data.get("claims")),
        "openQuestions": as_str_list(data.get("open_questions")),
        "confidence": str(data.get("confidence") or "").strip(),
        "body": body,
    }


def extract_wiki_links(body: str) -> list[str]:
    values = re.findall(r"\[\[([^\]]+)\]\]", body)
    values.extend(re.findall(r"\[([^\]]+)\]\(\.\./(?:sources|topics|synthesis)/[^)]+\.md(?:#[^)]+)?\)", body))
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        label = str(value).strip()
        if label and label not in seen:
            seen.add(label)
            result.append(label)
    return result


def load_graph_data(wiki_root: Path, source_count: int, topic_count: int, synthesis_count: int) -> dict[str, Any]:
    graph_path = wiki_root / "wiki" / "graph-data.json"
    if graph_path.exists():
        try:
            graph = json.loads(graph_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            graph = {}
    else:
        graph = {}
    graph.setdefault("meta", {})
    graph.setdefault("nodes", [])
    graph.setdefault("edges", [])
    graph["meta"]["source_count"] = source_count
    graph["meta"]["topic_count"] = topic_count
    graph["meta"]["synthesis_count"] = synthesis_count
    return graph


def write_json(path: Path, value: Any, pretty: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2 if pretty else None, separators=None if pretty else (",", ":"))
    path.write_text(text + "\n", encoding="utf-8")


def copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def build_package(args: argparse.Namespace) -> tuple[list[str], list[str]]:
    wiki_root = Path(args.wiki_root).resolve()
    output_dir = Path(args.output_dir).resolve()
    if not wiki_root.exists():
        raise SystemExit(f"wiki root not found: {wiki_root}")

    source_pages = read_pages(wiki_root, "sources")
    topic_pages = read_pages(wiki_root, "topics")
    synthesis_pages = read_pages(wiki_root, "synthesis")

    sources = [source_record(page) for page in source_pages]
    source_titles = {item["slug"]: item["title"] for item in sources}
    topic_titles = {page["slug"]: page["title"] for page in topic_pages}
    topics = [topic_record(page, source_titles) for page in topic_pages]
    syntheses = [synthesis_record(page, source_titles, topic_titles) for page in synthesis_pages]
    graph = load_graph_data(wiki_root, len(sources), len(topics), len(syntheses))

    output_dir.mkdir(parents=True, exist_ok=True)
    for subdir in ["source", "topic", "synthesis", "graph"]:
        (output_dir / subdir).mkdir(parents=True, exist_ok=True)

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    latest_updated = max(
        [str(item.get("updated") or item.get("publishDate") or "") for item in [*sources, *topics, *syntheses]] or [""]
    )
    manifest = {
        "data_version": DATA_VERSION,
        "generated_at": generated_at,
        "wiki_root": str(wiki_root),
        "page_root": str(Path(args.page_root).resolve()) if args.page_root else "",
        "base_path": args.base_path.strip("/"),
        "latest_updated": latest_updated,
        "counts": {
            "sources": len(sources),
            "topics": len(topics),
            "synthesis": len(syntheses),
            "graph_nodes": len(graph.get("nodes", [])),
            "graph_edges": len(graph.get("edges", [])),
        },
        "files": {
            "sources": "sources.json",
            "topics": "topics.json",
            "synthesis": "synthesis.json",
            "graph_data": "graph-data.json",
            "search_index": "search-index.json",
        },
        "collections": {
            "source": [{"slug": item["slug"], "path": f"source/{item['slug']}.json"} for item in sources],
            "topic": [{"slug": item["slug"], "path": f"topic/{item['slug']}.json"} for item in topics],
            "synthesis": [{"slug": item["slug"], "path": f"synthesis/{item['slug']}.json"} for item in syntheses],
        },
        "graph_assets": {
            "html": "graph/knowledge-graph.html",
            "runtime": "graph/graph-wash.js",
            "helpers": "graph/graph-wash-helpers.js",
        },
        "domains": [{"name": name, "slug": slug} for name, slug in KNOWN_DOMAINS.items()],
        "tag_policy": {"min_per_source": 1, "max_per_source": 2, "preferred_per_source": 1},
    }

    search_index = build_search_index(sources, topics, syntheses)
    write_json(output_dir / "manifest.json", manifest, args.pretty)
    write_json(output_dir / "sources.json", sources, args.pretty)
    write_json(output_dir / "topics.json", topics, args.pretty)
    write_json(output_dir / "synthesis.json", syntheses, args.pretty)
    write_json(output_dir / "graph-data.json", graph, args.pretty)
    write_json(output_dir / "search-index.json", search_index, args.pretty)

    for item in sources:
        write_json(output_dir / "source" / f"{item['slug']}.json", item, args.pretty)
    for item in topics:
        write_json(output_dir / "topic" / f"{item['slug']}.json", item, args.pretty)
    for item in syntheses:
        write_json(output_dir / "synthesis" / f"{item['slug']}.json", item, args.pretty)

    for filename in ["knowledge-graph.html", "graph-wash.js", "graph-wash-helpers.js", "d3.min.js", "rough.min.js", "marked.min.js", "purify.min.js"]:
        copy_if_exists(wiki_root / "wiki" / filename, output_dir / "graph" / filename)

    warnings, errors = validate_records(sources, topics, syntheses, graph)
    return warnings, errors


def build_search_index(sources: list[dict[str, Any]], topics: list[dict[str, Any]], syntheses: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for kind, items in [("source", sources), ("topic", topics), ("synthesis", syntheses)]:
        for item in items:
            text = " ".join(
                [
                    str(item.get("title") or ""),
                    str(item.get("summary") or ""),
                    " ".join(as_str_list(item.get("authors"))),
                    " ".join(as_str_list(item.get("tags"))),
                    " ".join(as_str_list(item.get("domains"))),
                ]
            )
            rows.append(
                {
                    "type": kind,
                    "slug": item.get("slug", ""),
                    "title": item.get("title", ""),
                    "summary": item.get("summary", ""),
                    "updated": item.get("updated") or item.get("publishDate") or "",
                    "text": strip_markdown(text).lower(),
                }
            )
    return rows


def validate_records(
    sources: list[dict[str, Any]],
    topics: list[dict[str, Any]],
    syntheses: list[dict[str, Any]],
    graph: dict[str, Any],
) -> tuple[list[str], list[str]]:
    warnings: list[str] = []
    errors: list[str] = []

    def require_slug_unique(kind: str, rows: list[dict[str, Any]]) -> set[str]:
        seen: set[str] = set()
        for row in rows:
            slug = str(row.get("slug") or "")
            if not slug:
                errors.append(f"{kind} missing slug: {row.get('title')}")
            if slug in seen:
                errors.append(f"{kind} duplicate slug: {slug}")
            seen.add(slug)
        return seen

    source_slugs = require_slug_unique("source", sources)
    topic_slugs = require_slug_unique("topic", topics)
    synthesis_slugs = require_slug_unique("synthesis", syntheses)

    for source in sources:
        if not source.get("title"):
            errors.append(f"source/{source.get('slug')} missing title")
        if not source.get("domainSlugs"):
            errors.append(f"source/{source.get('slug')} missing domains")
        if not source.get("tags"):
            errors.append(f"source/{source.get('slug')} missing tags")
        if len(as_str_list(source.get("tags"))) > 2:
            warnings.append(f"source/{source.get('slug')} has more than 2 tags")
        if not source.get("rawRefs"):
            warnings.append(f"source/{source.get('slug')} missing rawRefs")
        for topic_slug in as_str_list(source.get("relatedTopicSlugs")):
            if topic_slug not in topic_slugs:
                warnings.append(f"source/{source.get('slug')} references missing topic: {topic_slug}")
        for synthesis_slug in as_str_list(source.get("relatedSynthesisSlugs")):
            if synthesis_slug not in synthesis_slugs:
                warnings.append(f"source/{source.get('slug')} references missing synthesis: {synthesis_slug}")

    for topic in topics:
        for source_slug in as_str_list(topic.get("sourceSlugs")):
            if source_slug not in source_slugs:
                errors.append(f"topic/{topic.get('slug')} references missing source: {source_slug}")
        for synthesis_slug in as_str_list(topic.get("synthesisSlugs")):
            if synthesis_slug not in synthesis_slugs:
                warnings.append(f"topic/{topic.get('slug')} references missing synthesis: {synthesis_slug}")

    for synthesis in syntheses:
        for source_slug in as_str_list(synthesis.get("sourceSlugs")):
            if source_slug not in source_slugs:
                errors.append(f"synthesis/{synthesis.get('slug')} references missing source: {source_slug}")
        for topic_slug in as_str_list(synthesis.get("topicSlugs")):
            if topic_slug not in topic_slugs:
                errors.append(f"synthesis/{synthesis.get('slug')} references missing topic: {topic_slug}")

    node_ids = {str(node.get("id") or "") for node in graph.get("nodes", []) if isinstance(node, dict)}
    for edge in graph.get("edges", []):
        if not isinstance(edge, dict):
            continue
        source = str(edge.get("source") or edge.get("from") or "")
        target = str(edge.get("target") or edge.get("to") or "")
        if source and source not in node_ids:
            warnings.append(f"graph edge references missing source node: {source}")
        if target and target not in node_ids:
            warnings.append(f"graph edge references missing target node: {target}")
    return warnings, errors


def main() -> int:
    args = parse_args()
    warnings, errors = build_package(args)
    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors or (warnings and args.strict):
        return 1
    print(f"FollowHub wiki package built: {Path(args.output_dir).resolve()}")
    print(f"  warnings: {len(warnings)}")
    print(f"  errors: {len(errors)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
