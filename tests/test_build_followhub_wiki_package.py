import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build-followhub-wiki-package.py"
SPEC = importlib.util.spec_from_file_location("build_followhub_wiki_package", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


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


if __name__ == "__main__":
    unittest.main()
