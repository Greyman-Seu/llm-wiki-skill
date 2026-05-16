#!/bin/bash
# Validate FollowHub-style source/topic/synthesis wiki pages.
# Usage: bash validate-followhub-wiki.sh <wiki_root>

set -u

WIKI_ROOT="${1:-}"

if [ -z "$WIKI_ROOT" ] || [ ! -d "$WIKI_ROOT" ]; then
    echo "ERROR: usage: validate-followhub-wiki.sh <wiki_root>"
    exit 1
fi

ERRORS=0
WARNINGS=0

error() {
    ERRORS=$((ERRORS + 1))
    echo "ERROR: $*"
}

warn() {
    WARNINGS=$((WARNINGS + 1))
    echo "WARN: $*"
}

has_field() {
    local file="$1"
    local field="$2"
    grep -Eq "^${field}:" "$file"
}

has_nonempty_scalar() {
    local file="$1"
    local field="$2"
    grep -Eq "^${field}:[[:space:]]*[^[:space:]][^#]*$" "$file"
}

validate_source() {
    local file="$1"
    has_nonempty_scalar "$file" "slug" || error "$file missing non-empty slug"
    grep -Eq "^type:[[:space:]]*source[[:space:]]*$" "$file" || error "$file missing type: source"
    has_nonempty_scalar "$file" "title" || error "$file missing non-empty title"
    has_nonempty_scalar "$file" "material_type" || error "$file missing material_type"
    has_field "$file" "domains" || error "$file missing domains"
    has_field "$file" "tags" || error "$file missing tags"
    has_field "$file" "links" || warn "$file missing links block"
    has_field "$file" "raw_refs" || error "$file missing raw_refs"
    has_field "$file" "related_topics" || warn "$file missing related_topics"
    has_field "$file" "related_syntheses" || warn "$file missing related_syntheses"
}

validate_topic() {
    local file="$1"
    has_nonempty_scalar "$file" "slug" || error "$file missing non-empty slug"
    grep -Eq "^type:[[:space:]]*topic[[:space:]]*$" "$file" || error "$file missing type: topic"
    has_nonempty_scalar "$file" "title" || error "$file missing non-empty title"
    has_field "$file" "source_slugs" || error "$file missing source_slugs"
    has_field "$file" "synthesis_slugs" || warn "$file missing synthesis_slugs"
    has_field "$file" "open_questions" || warn "$file missing open_questions"
}

validate_synthesis() {
    local file="$1"
    has_nonempty_scalar "$file" "slug" || error "$file missing non-empty slug"
    grep -Eq "^type:[[:space:]]*synthesis[[:space:]]*$" "$file" || error "$file missing type: synthesis"
    has_nonempty_scalar "$file" "title" || error "$file missing non-empty title"
    has_field "$file" "judgment" || error "$file missing judgment"
    has_field "$file" "source_slugs" || error "$file missing source_slugs"
    has_field "$file" "topic_slugs" || error "$file missing topic_slugs"
    has_field "$file" "claims" || warn "$file missing claims"
    has_field "$file" "open_questions" || warn "$file missing open_questions"
}

if [ -d "$WIKI_ROOT/wiki/sources" ]; then
    while IFS= read -r file; do
        validate_source "$file"
    done < <(find "$WIKI_ROOT/wiki/sources" -type f -name '*.md' | sort)
else
    warn "$WIKI_ROOT/wiki/sources not found"
fi

if [ -d "$WIKI_ROOT/wiki/topics" ]; then
    while IFS= read -r file; do
        validate_topic "$file"
    done < <(find "$WIKI_ROOT/wiki/topics" -type f -name '*.md' | sort)
else
    warn "$WIKI_ROOT/wiki/topics not found"
fi

if [ -d "$WIKI_ROOT/wiki/synthesis" ]; then
    while IFS= read -r file; do
        validate_synthesis "$file"
    done < <(find "$WIKI_ROOT/wiki/synthesis" -type f -name '*.md' | sort)
else
    warn "$WIKI_ROOT/wiki/synthesis not found"
fi

echo "FollowHub wiki validation completed: $ERRORS error(s), $WARNINGS warning(s)"

if [ "$ERRORS" -gt 0 ]; then
    exit 1
fi

exit 0

