import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build-followhub-wiki-package.py"
SPEC = importlib.util.spec_from_file_location("build_followhub_wiki_package", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

VALIDATOR_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate-followhub-wiki-package.py"
VALIDATOR_SPEC = importlib.util.spec_from_file_location("validate_followhub_wiki_package", VALIDATOR_PATH)
VALIDATOR = importlib.util.module_from_spec(VALIDATOR_SPEC)
assert VALIDATOR_SPEC and VALIDATOR_SPEC.loader
VALIDATOR_SPEC.loader.exec_module(VALIDATOR)


class SourceRecordSectionTests(unittest.TestCase):
    def test_labeled_background_and_method_fields_survive_packaging(self):
        page = {
            "slug": "example",
            "title": "Example",
            "frontmatter": {
                "id": "example",
                "source_type": "paper",
                "material_type": "paper",
                "domains": ["Physical/Embodied Intelligence"],
                "tags": ["vision-language-action"],
            },
            "body": """# Example

## 背景与问题

**动机：** 视觉无法可靠观察被遮挡的接触变化。

**问题缺口：** 快速触觉与慢速视觉之间存在频率错配。

## 方法

**方法概述：** 先做视觉规划，再用触觉细化动作。

**核心机制：** 两个专家共同完成一条去噪轨迹。

**方法拆解：**

- **慢专家**缓存视觉语言上下文。
- **快专家**根据最新触觉修正动作。

**关键要点：**

- 触觉必须进入闭环，而不是只做静态条件。
""",
        }

        record = MODULE.source_record(page)

        self.assertEqual(record["backgroundMotivation"], "视觉无法可靠观察被遮挡的接触变化。")
        self.assertEqual(record["backgroundGap"], "快速触觉与慢速视觉之间存在频率错配。")
        self.assertEqual(record["methodOverview"], "先做视觉规划，再用触觉细化动作。")
        self.assertEqual(record["methodCore"], "两个专家共同完成一条去噪轨迹。")
        self.assertEqual(
            record["methodBreakdown"],
            ["慢专家缓存视觉语言上下文。", "快专家根据最新触觉修正动作。"],
        )
        self.assertEqual(record["methodTakeaways"], ["触觉必须进入闭环，而不是只做静态条件。"])

        errors = []
        VALIDATOR.validate_structured_source_fields(record, errors)
        self.assertEqual(errors, [])

    def test_heading_background_and_method_fields_survive_packaging(self):
        page = {
            "slug": "heading-example",
            "title": "Heading Example",
            "frontmatter": {
                "id": "heading-example",
                "source_type": "paper",
                "material_type": "paper",
                "domains": ["Physical/Embodied Intelligence"],
                "tags": ["vision-language-action"],
            },
            "body": """# Heading Example

## 背景与问题

### 动机

- 视觉无法可靠观察被遮挡的接触变化。
- 触觉可以提供高频反馈。

### 问题缺口

- 快速触觉与慢速视觉之间存在频率错配。

## 方法

### 方法概述

先做视觉规划，再用触觉细化动作。

### 核心机制

1. 慢专家缓存视觉语言上下文。
2. 快专家根据最新触觉修正动作。

### 方法拆解

1. **慢专家**
   - 缓存视觉语言上下文。
2. **快专家**
   - 根据最新触觉修正动作。

### 关键要点

- 触觉必须进入闭环，而不是只做静态条件。

### 数据扩展与清洗

这段属于后续小节，不应泄漏到关键要点。
""",
        }

        record = MODULE.source_record(page)

        self.assertEqual(
            record["backgroundMotivation"],
            "- 视觉无法可靠观察被遮挡的接触变化。\n- 触觉可以提供高频反馈。",
        )
        self.assertEqual(record["backgroundGap"], "- 快速触觉与慢速视觉之间存在频率错配。")
        self.assertEqual(record["methodOverview"], "先做视觉规划，再用触觉细化动作。")
        self.assertEqual(
            record["methodCore"],
            "1. 慢专家缓存视觉语言上下文。\n2. 快专家根据最新触觉修正动作。",
        )
        self.assertEqual(
            record["methodBreakdown"],
            ["慢专家 缓存视觉语言上下文。", "快专家 根据最新触觉修正动作。"],
        )
        self.assertEqual(record["methodTakeaways"], ["触觉必须进入闭环，而不是只做静态条件。"])

        errors = []
        VALIDATOR.validate_structured_source_fields(record, errors)
        self.assertEqual(errors, [])

    def test_validator_rejects_lost_heading_field(self):
        source = {
            "slug": "broken-heading-example",
            "body": "## 方法\n\n### 方法概述\n\n详细方法。",
            "methodOverview": "",
        }
        errors = []

        VALIDATOR.validate_structured_source_fields(source, errors)

        self.assertEqual(
            errors,
            ["source/broken-heading-example lost structured field methodOverview during packaging"],
        )


if __name__ == "__main__":
    unittest.main()
