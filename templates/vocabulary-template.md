# Wiki Vocabulary（领域与标签词表）

> 这个文件控制 domain 和 tag 的增长，避免每次 ingest 都生成一批新词。

## Domains

每个材料至少选择一个主 domain。新增 domain 前，先确认现有 domain 无法覆盖，并在本文件记录原因。

| Domain | 说明 |
| --- | --- |
| LLM/VLM | 大模型、多模态大模型，包含推理、训练、评测、对齐、视觉语言模型等。 |
| Physical/Embodied Intelligence | 物理智能、具身智能、机器人操作、感知、规划、泛化、跨 embodiment 学习等。 |
| AIGC | 图像、视频、音频、3D 等生成方向。 |
| Agent | 工具调用、规划执行、工作流编排、智能体系统设计。 |

## Tag Rules

1. 每个材料给 1-2 个 tag，最好 1 个。
2. tag 应该能聚合多篇材料，不要为每篇材料创造独有 tag。
3. 如果一个 tag 已经形成持续问题线，应升级为 topic。
4. tag 用英文 kebab-case 或稳定英文术语，除非中文术语更常用。

## Seed Tags

| Tag | 适用范围 |
| --- | --- |
| vision-language-action | VLA、机器人 foundation model、视觉-语言-动作统一建模。 |
| human-to-robot-transfer | 人类数据到机器人策略的迁移。 |
| online-rl | 在线强化学习、真实机器人 fine-tuning。 |
| long-horizon-memory | 长程任务记忆、多尺度记忆、历史上下文。 |
| robot-foundation-model | 机器人通用 foundation model。 |
| multimodal-reasoning | 多模态推理、VLM 能力边界。 |
| tool-use | 工具调用与 agent 执行。 |
| workflow-orchestration | agent workflow、任务编排、系统协作。 |

## New Tag Proposal Log

新增 tag 时，在这里追加：

```text
- YYYY-MM-DD tag-name：为什么现有 tag 不够用；预计能聚合哪些材料。
```

