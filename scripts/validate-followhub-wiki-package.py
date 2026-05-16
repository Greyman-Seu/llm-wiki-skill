#!/usr/bin/env python3
"""Validate a built FollowHub Wiki R2 package."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = [
    "manifest.json",
    "sources.json",
    "topics.json",
    "synthesis.json",
    "graph-data.json",
    "search-index.json",
]


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate-followhub-wiki-package.py <package_dir>", file=sys.stderr)
        return 1

    root = Path(sys.argv[1])
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        print(f"ERROR: package dir not found: {root}", file=sys.stderr)
        return 1

    for filename in REQUIRED_TOP_LEVEL:
        if not (root / filename).is_file():
            errors.append(f"missing {filename}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    try:
        manifest = load_json(root / "manifest.json")
        sources = load_json(root / "sources.json")
        topics = load_json(root / "topics.json")
        syntheses = load_json(root / "synthesis.json")
        graph = load_json(root / "graph-data.json")
        search_index = load_json(root / "search-index.json")
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 1

    if manifest.get("data_version") != "followhub-wiki-r2/v1":
        errors.append("manifest data_version must be followhub-wiki-r2/v1")

    counts = manifest.get("counts") if isinstance(manifest.get("counts"), dict) else {}
    expected_counts = {
        "sources": len(as_list(sources)),
        "topics": len(as_list(topics)),
        "synthesis": len(as_list(syntheses)),
    }
    for key, expected in expected_counts.items():
        if counts.get(key) != expected:
            errors.append(f"manifest counts.{key}={counts.get(key)} does not match {expected}")

    source_slugs = validate_collection(root, "source", sources, errors)
    topic_slugs = validate_collection(root, "topic", topics, errors)
    synthesis_slugs = validate_collection(root, "synthesis", syntheses, errors)

    for source in as_list(sources):
        slug = source.get("slug")
        if not source.get("domainSlugs"):
            errors.append(f"source/{slug} missing domainSlugs")
        tags = as_list(source.get("tags")) or as_list(source.get("keywords"))
        if not tags:
            errors.append(f"source/{slug} missing tags")
        if len(tags) > 2:
            warnings.append(f"source/{slug} has more than 2 tags")
        for topic_slug in as_list(source.get("relatedTopicSlugs")):
            if topic_slug not in topic_slugs:
                warnings.append(f"source/{slug} references missing topic: {topic_slug}")
        for synthesis_slug in as_list(source.get("relatedSynthesisSlugs")):
            if synthesis_slug not in synthesis_slugs:
                warnings.append(f"source/{slug} references missing synthesis: {synthesis_slug}")

    for topic in as_list(topics):
        slug = topic.get("slug")
        for source_slug in as_list(topic.get("sourceSlugs")):
            if source_slug not in source_slugs:
                errors.append(f"topic/{slug} references missing source: {source_slug}")
        for synthesis_slug in as_list(topic.get("synthesisSlugs")):
            if synthesis_slug not in synthesis_slugs:
                warnings.append(f"topic/{slug} references missing synthesis: {synthesis_slug}")

    for synthesis in as_list(syntheses):
        slug = synthesis.get("slug")
        for source_slug in as_list(synthesis.get("sourceSlugs")):
            if source_slug not in source_slugs:
                errors.append(f"synthesis/{slug} references missing source: {source_slug}")
        for topic_slug in as_list(synthesis.get("topicSlugs")):
            if topic_slug not in topic_slugs:
                errors.append(f"synthesis/{slug} references missing topic: {topic_slug}")

    node_ids = {node.get("id") for node in as_list(graph.get("nodes")) if isinstance(node, dict)}
    for edge in as_list(graph.get("edges")):
        if not isinstance(edge, dict):
            continue
        source = edge.get("source") or edge.get("from")
        target = edge.get("target") or edge.get("to")
        if source and source not in node_ids:
            warnings.append(f"graph edge references missing source node: {source}")
        if target and target not in node_ids:
            warnings.append(f"graph edge references missing target node: {target}")

    if not isinstance(search_index, list):
        errors.append("search-index.json must be an array")

    for asset in ["graph/knowledge-graph.html", "graph/graph-wash.js", "graph/graph-wash-helpers.js"]:
        if not (root / asset).is_file():
            warnings.append(f"missing optional graph asset: {asset}")

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"FollowHub wiki package validation completed: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


def validate_collection(root: Path, kind: str, rows: Any, errors: list[str]) -> set[str]:
    if not isinstance(rows, list):
        errors.append(f"{kind}s.json must be an array")
        return set()
    seen: set[str] = set()
    for row in rows:
        if not isinstance(row, dict):
            errors.append(f"{kind} row must be object")
            continue
        slug = str(row.get("slug") or "")
        title = str(row.get("title") or "")
        if not slug:
            errors.append(f"{kind} missing slug")
        if not title:
            errors.append(f"{kind}/{slug} missing title")
        if slug in seen:
            errors.append(f"{kind} duplicate slug: {slug}")
        seen.add(slug)
        if not (root / kind / f"{slug}.json").is_file():
            errors.append(f"missing {kind}/{slug}.json")
    return seen


if __name__ == "__main__":
    raise SystemExit(main())
