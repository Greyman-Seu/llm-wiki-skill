#!/usr/bin/env python3
"""Migrate bundled FollowHub sample wiki pages to the source/topic/synthesis schema."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DOMAIN_DEFAULT = "Physical/Embodied Intelligence"
SYNTHESIS_SLUG = "current-vla-landscape-foundation-control-memory-and-transfer"


def split_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    raw = text[4:end].strip("\n")
    body = text[end + 5 :]
    return parse_frontmatter(raw), body


def parse_frontmatter(raw: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and current:
            data.setdefault(current, [])
            if isinstance(data[current], list):
                data[current].append(unquote(line[4:].strip()))
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            current = None
            continue
        key, value = match.groups()
        current = key
        value = value.strip()
        if value == "":
            data[key] = []
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [unquote(part.strip()) for part in inner.split(",") if part.strip()]
        else:
            data[key] = unquote(value)
    return data


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def quote(value: object) -> str:
    if value is None:
        return ""
    text = str(value)
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def slugify(text: str) -> str:
    value = text.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def h1_from_body(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def list_block(key: str, values: list[str]) -> list[str]:
    lines = [f"{key}:"]
    if values:
        lines.extend(f"  - {quote(value)}" for value in values)
    return lines


def scalar(key: str, value: object) -> str:
    return f"{key}: {quote(value)}"


def source_tag(slug: str, existing_tags: list[str]) -> str:
    if "rl-token" in slug:
        return "online-rl"
    if slug.startswith("mem-"):
        return "long-horizon-memory"
    if "human-to-robot-transfer" in slug:
        return "human-to-robot-transfer"
    if "openvla" in slug or "pi07" in slug:
        return "robot-foundation-model"
    if any(tag in {"vla", "vision-language-action"} for tag in existing_tags):
        return "vision-language-action"
    return "vision-language-action"


def topic_tag(slug: str) -> str:
    if "human-to-robot-transfer" in slug:
        return "human-to-robot-transfer"
    if "online-rl" in slug:
        return "online-rl"
    if "long-horizon-memory" in slug:
        return "long-horizon-memory"
    return "vision-language-action"


def collect_source_map(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted((root / "wiki" / "sources").glob("*.md")):
        data, body = split_frontmatter(path.read_text(encoding="utf-8"))
        title = str(data.get("title") or h1_from_body(body, path.stem))
        result[title] = path.stem
    return result


def migrate_source(path: Path) -> None:
    data, body = split_frontmatter(path.read_text(encoding="utf-8"))
    title = str(data.get("title") or h1_from_body(body, path.stem))
    slug = path.stem
    existing_tags = [str(x) for x in data.get("tags", [])] if isinstance(data.get("tags"), list) else []
    authors = [str(x) for x in data.get("authors", [])] if isinstance(data.get("authors"), list) else []
    raw_ref = data.get("source_input") or data.get("pdf_url") or data.get("source_url") or ""
    related_topics = [str(x) for x in data.get("related_topics", [])] if isinstance(data.get("related_topics"), list) else []
    images = [str(x) for x in data.get("images", [])] if isinstance(data.get("images"), list) else []
    date = data.get("publish_date") or data.get("created") or ""
    source_type = data.get("source_type") or "material"
    material_type = "paper" if source_type == "paper" else source_type

    lines: list[str] = ["---"]
    lines.extend(
        [
            scalar("id", slug),
            scalar("slug", slug),
            scalar("title", title),
            "type: source",
            scalar("material_type", material_type),
            scalar("source_type", source_type),
            scalar("created", data.get("created") or "2026-05-11"),
            scalar("updated", data.get("updated") or "2026-05-16"),
            scalar("date", date),
        ]
    )
    lines.extend(list_block("authors", authors))
    lines.extend(list_block("domains", [DOMAIN_DEFAULT]))
    lines.extend(list_block("tags", [source_tag(slug, existing_tags)]))
    lines.append(scalar("summary", ""))
    lines.extend(
        [
            "links:",
            f"  original: {quote(data.get('source_url') or data.get('source_input') or '')}",
            f"  arxiv: {quote(data.get('arxiv_url') or '')}",
            f"  pdf: {quote(data.get('pdf_url') or '')}",
            f"  project: {quote(data.get('project_url') or '')}",
            f"  github: {quote(data.get('github_url') or '')}",
            f"  hjfy: {quote(data.get('hjfy_url') or '')}",
            f"  doi: {quote(data.get('doi') or '')}",
        ]
    )
    lines.extend(list_block("raw_refs", [str(raw_ref)] if raw_ref else []))
    lines.extend(list_block("related_topics", related_topics))
    lines.extend(list_block("related_syntheses", [SYNTHESIS_SLUG]))
    lines.append("confidence: EXTRACTED")
    lines.append(scalar("hero_image", images[0] if images else ""))
    lines.append(f"images: {len(images)}")
    lines.extend(list_block("image_paths", []))
    lines.append("---")
    path.write_text("\n".join(lines) + "\n" + body.lstrip("\n"), encoding="utf-8")


def migrate_topic(path: Path, source_map: dict[str, str]) -> None:
    data, body = split_frontmatter(path.read_text(encoding="utf-8"))
    title = h1_from_body(body, path.stem)
    slug = slugify(path.stem)
    source_names = [str(x) for x in data.get("sources", [])] if isinstance(data.get("sources"), list) else []
    source_slugs = [source_map[name] for name in source_names if name in source_map]

    lines = [
        "---",
        scalar("id", slug),
        scalar("slug", slug),
        scalar("title", title),
        "type: topic",
        scalar("created", data.get("created") or "2026-05-11"),
        scalar("updated", data.get("updated") or "2026-05-16"),
    ]
    lines.extend(list_block("domains", [DOMAIN_DEFAULT]))
    lines.extend(list_block("tags", [topic_tag(slug)]))
    lines.append(scalar("summary", ""))
    lines.extend(list_block("source_slugs", source_slugs))
    lines.extend(list_block("synthesis_slugs", [SYNTHESIS_SLUG]))
    lines.append("status: active")
    lines.extend(list_block("open_questions", []))
    lines.append("---")
    path.write_text("\n".join(lines) + "\n" + body.lstrip("\n"), encoding="utf-8")


def migrate_synthesis(path: Path, source_map: dict[str, str], topic_slugs: list[str]) -> None:
    data, body = split_frontmatter(path.read_text(encoding="utf-8"))
    title = h1_from_body(body, path.stem)
    slug = path.stem
    source_names = [str(x) for x in data.get("sources", [])] if isinstance(data.get("sources"), list) else []
    source_slugs = [source_map[name] for name in source_names if name in source_map]

    lines = [
        "---",
        scalar("id", slug),
        scalar("slug", slug),
        scalar("title", title),
        "type: synthesis",
        scalar("created", data.get("created") or "2026-05-11"),
        scalar("updated", data.get("updated") or "2026-05-16"),
    ]
    lines.extend(list_block("domains", [DOMAIN_DEFAULT]))
    lines.extend(list_block("tags", ["vision-language-action"]))
    lines.append(scalar("summary", ""))
    lines.append(scalar("judgment", "当前 VLA 研究已经从单点模型设计演化为基座、可控性、在线精修、记忆和人类数据共同组成的系统问题。"))
    lines.extend(list_block("source_slugs", source_slugs))
    lines.extend(list_block("topic_slugs", topic_slugs))
    lines.extend(list_block("claims", []))
    lines.extend(list_block("open_questions", []))
    lines.append("confidence: INFERRED")
    lines.append("---")
    path.write_text("\n".join(lines) + "\n" + body.lstrip("\n"), encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: migrate-followhub-schema.py <wiki_root>", file=sys.stderr)
        return 1
    root = Path(sys.argv[1])
    if not root.exists():
        print(f"wiki root not found: {root}", file=sys.stderr)
        return 1

    for path in sorted((root / "wiki" / "sources").glob("*.md")):
        migrate_source(path)

    source_map = collect_source_map(root)
    topic_paths = sorted((root / "wiki" / "topics").glob("*.md"))
    for path in topic_paths:
        migrate_topic(path, source_map)

    topic_slugs = [slugify(path.stem) for path in topic_paths]
    for path in sorted((root / "wiki" / "synthesis").glob("*.md")):
        migrate_synthesis(path, source_map, topic_slugs)

    print(f"migrated FollowHub schema under {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

