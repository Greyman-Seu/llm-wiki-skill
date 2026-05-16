#!/bin/bash
# Regression: FollowHub wiki package should build a R2-compatible data bundle.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_ROOT="$REPO_ROOT/followhub-wiki"
TMP_DIR=""

cleanup() {
    [ -n "${TMP_DIR:-}" ] && rm -rf "$TMP_DIR"
}

fail() {
    echo "FAIL: $1" >&2
    exit 1
}

json_value() {
    local file="$1"
    local expr="$2"
    python3 - "$file" "$expr" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    data = json.load(handle)

expr = sys.argv[2]
value = data
for part in expr.split("."):
    if part == "len":
        value = len(value)
    elif isinstance(value, dict):
        value = value.get(part)
    else:
        value = None
print(value)
PY
}

main() {
    command -v python3 >/dev/null 2>&1 || fail "python3 is required"
    [ -d "$WIKI_ROOT" ] || fail "sample followhub-wiki should exist"

    local package_dir publish_dir
    TMP_DIR="$(mktemp -d)"
    package_dir="$TMP_DIR/package"
    publish_dir="$TMP_DIR/published"
    trap cleanup EXIT

    python3 "$REPO_ROOT/scripts/build-followhub-wiki-package.py" "$WIKI_ROOT" "$package_dir" --pretty >/dev/null
    python3 "$REPO_ROOT/scripts/validate-followhub-wiki-package.py" "$package_dir" >/dev/null

    [ -f "$package_dir/manifest.json" ] || fail "manifest.json should be generated"
    [ -f "$package_dir/sources.json" ] || fail "sources.json should be generated"
    [ -f "$package_dir/topics.json" ] || fail "topics.json should be generated"
    [ -f "$package_dir/synthesis.json" ] || fail "synthesis.json should be generated"
    [ -f "$package_dir/graph-data.json" ] || fail "graph-data.json should be generated"
    [ -f "$package_dir/search-index.json" ] || fail "search-index.json should be generated"
    [ -f "$package_dir/source/rl-token-bootstrapping-online-rl-with-vision-language-action-models.json" ] \
        || fail "per-source JSON should be generated"
    [ -f "$package_dir/graph/graph-wash.js" ] || fail "graph runtime asset should be copied"

    local source_json="$package_dir/source/rl-token-bootstrapping-online-rl-with-vision-language-action-models.json"
    [ "$(json_value "$source_json" "riskLimitations.len")" = "3" ] \
        || fail "risk limitations should parse from labeled section"
    [ "$(json_value "$source_json" "riskScenarios.len")" = "3" ] \
        || fail "risk scenarios should parse from labeled section"
    [ "$(json_value "$source_json" "riskJudgment.len")" = "1" ] \
        || fail "risk judgment should parse from labeled section"

    [ "$(json_value "$package_dir/manifest.json" "data_version")" = "followhub-wiki-r2/v1" ] \
        || fail "manifest data_version mismatch"
    [ "$(json_value "$package_dir/manifest.json" "counts.sources")" = "6" ] \
        || fail "manifest source count should match sample"
    [ "$(json_value "$package_dir/sources.json" "len")" = "6" ] \
        || fail "sources array count should match sample"

    bash "$REPO_ROOT/scripts/publish-followhub-wiki-r2.sh" "$package_dir" "local:$publish_dir" >/dev/null
    [ -f "$publish_dir/manifest.json" ] || fail "local publish should copy manifest"
    [ -f "$publish_dir/source/rl-token-bootstrapping-online-rl-with-vision-language-action-models.json" ] \
        || fail "local publish should copy per-source JSON"

    echo "PASS: FollowHub wiki package regression coverage"
}

main "$@"
