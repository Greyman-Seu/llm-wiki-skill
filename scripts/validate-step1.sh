#!/bin/bash
# 验证 ingest Step 1 的 JSON 输出格式
# 用法：bash validate-step1.sh <json_file>
# 返回：0 = 格式正确，1 = 格式有问题（触发回退）

if [ "$#" -ne 1 ]; then
    echo "ERROR: usage: validate-step1.sh <json_file>"
    exit 1
fi

JSON_FILE="$1"

[ -f "$JSON_FILE" ] || { echo "ERROR: file not found: $JSON_FILE"; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 is required for Step 1 validation"; exit 1; }

python3 - "$JSON_FILE" <<'PY'
import json
import sys

path = sys.argv[1]

try:
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
except Exception:
    print("ERROR: invalid JSON format")
    sys.exit(1)


def fail(message):
    print(f"ERROR: {message}")
    sys.exit(1)


def is_nonempty(value):
    return isinstance(value, str) and len(value.strip()) > 0


def require_array(key):
    if not isinstance(data.get(key), list):
        fail(f"'{key}' must be an array")
    return data[key]


def require_object(key):
    if not isinstance(data.get(key), dict):
        fail(f"'{key}' must be an object")
    return data[key]


VALID_CONFIDENCE = {"EXTRACTED", "INFERRED", "AMBIGUOUS", "UNVERIFIED"}
is_followhub = any(
    key in data
    for key in (
        "source_decision",
        "classification",
        "topic_decisions",
        "synthesis_decision",
    )
)

if is_followhub:
    source = require_object("source_decision")
    classification = require_object("classification")
    topic_decisions = require_array("topic_decisions")
    synthesis = require_object("synthesis_decision")
    graph_edges = require_array("graph_edges")

    if source.get("action") not in {"create_source", "update_source", "link_as_related_source"}:
        fail("source_decision.action must be create_source | update_source | link_as_related_source")
    if not is_nonempty(source.get("reason")):
        fail("source_decision.reason is required")

    if not is_nonempty(classification.get("material_type")):
        fail("classification.material_type is required")
    if not is_nonempty(classification.get("source_type")):
        fail("classification.source_type is required")
    domains = classification.get("domains")
    if not isinstance(domains, list) or len(domains) < 1:
        fail("classification.domains must contain at least one domain")
    tags = classification.get("tags")
    if not isinstance(tags, list) or len(tags) < 1 or len(tags) > 2:
        fail("classification.tags must contain 1-2 tags")

    bad_topics = 0
    for item in topic_decisions:
        if not isinstance(item, dict):
            bad_topics += 1
            continue
        if item.get("action") not in {"attach_existing", "create_topic"} or not is_nonempty(item.get("reason")):
            bad_topics += 1
    if bad_topics:
        fail(f"{bad_topics} topic_decision(s) missing valid action/reason")

    if synthesis.get("action") not in {"unchanged", "update", "create"}:
        fail("synthesis_decision.action must be unchanged | update | create")
    if not is_nonempty(synthesis.get("reason")):
        fail("synthesis_decision.reason is required")

    valid_edge_types = {"supports", "evidence_for", "updates", "contrasts", "relates"}
    invalid_confidences = []
    bad_edges = 0
    for edge in graph_edges:
        if not isinstance(edge, dict):
            bad_edges += 1
            continue
        confidence = edge.get("confidence", "MISSING")
        if confidence not in VALID_CONFIDENCE and len(invalid_confidences) < 3:
            invalid_confidences.append(str(confidence))
        if not is_nonempty(edge.get("from")) or not is_nonempty(edge.get("to")) or edge.get("type") not in valid_edge_types:
            bad_edges += 1
    if invalid_confidences:
        print(f"ERROR: invalid graph edge confidence value(s): {' '.join(invalid_confidences)}")
        print("       Valid values: EXTRACTED | INFERRED | AMBIGUOUS | UNVERIFIED")
        sys.exit(1)
    if bad_edges:
        fail(f"{bad_edges} graph_edge(s) missing from/to or valid type")

    print("OK: FollowHub Step 1 decision validation passed")
    sys.exit(0)

entities = require_array("entities")
topics = require_array("topics")
connections = require_array("connections")
require_array("contradictions")
require_object("new_vs_existing")

non_object_entities = sum(1 for item in entities if not isinstance(item, dict))
if non_object_entities:
    fail(f"{non_object_entities} entity/entities must be objects")

bad_entities = [
    item
    for item in entities
    if not is_nonempty(item.get("name"))
    or not is_nonempty(item.get("type"))
    or not is_nonempty(item.get("confidence"))
]
if bad_entities:
    fail(f"{len(bad_entities)} entity/entities missing required fields (name/type/confidence)")

invalid_entity_conf = [
    str(item.get("confidence", "MISSING"))
    for item in entities
    if item.get("confidence", "MISSING") not in VALID_CONFIDENCE
][:3]
if invalid_entity_conf:
    print(f"ERROR: invalid entity confidence value(s): {' '.join(invalid_entity_conf)}")
    print("       Valid values: EXTRACTED | INFERRED | AMBIGUOUS | UNVERIFIED")
    sys.exit(1)

no_entity_evidence = sum(
    1
    for item in entities
    if item.get("confidence") in {"EXTRACTED", "INFERRED"} and not is_nonempty(item.get("evidence"))
)
if no_entity_evidence:
    print(f"WARN: {no_entity_evidence} entity/entities with EXTRACTED/INFERRED confidence missing 'evidence' field")

non_object_topics = sum(1 for item in topics if not isinstance(item, dict))
if non_object_topics:
    fail(f"{non_object_topics} topic(s) must be objects")
bad_topics = [item for item in topics if not is_nonempty(item.get("name"))]
if bad_topics:
    fail(f"{len(bad_topics)} topic(s) missing required 'name' field")

non_object_connections = sum(1 for item in connections if not isinstance(item, dict))
if non_object_connections:
    fail(f"{non_object_connections} connection(s) must be objects")

bad_connections = [
    item
    for item in connections
    if not is_nonempty(item.get("from"))
    or not is_nonempty(item.get("to"))
    or not is_nonempty(item.get("confidence"))
]
if bad_connections:
    fail(f"{len(bad_connections)} connection(s) missing required fields (from/to/confidence)")

invalid_connection_conf = [
    str(item.get("confidence", "MISSING"))
    for item in connections
    if item.get("confidence", "MISSING") not in VALID_CONFIDENCE
][:3]
if invalid_connection_conf:
    print(f"ERROR: invalid connection confidence value(s): {' '.join(invalid_connection_conf)}")
    print("       Valid values: EXTRACTED | INFERRED | AMBIGUOUS | UNVERIFIED")
    sys.exit(1)

no_connection_evidence = sum(
    1
    for item in connections
    if item.get("confidence") in {"EXTRACTED", "INFERRED"} and not is_nonempty(item.get("evidence"))
)
if no_connection_evidence:
    print(f"WARN: {no_connection_evidence} connection(s) with EXTRACTED/INFERRED confidence missing 'evidence' field")

print("OK: Step 1 JSON validation passed")
PY
