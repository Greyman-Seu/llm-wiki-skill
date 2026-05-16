# Wiki Schema（知识库配置规范）

> 这个文件告诉 AI 如何维护你的知识库。它是 llm-wiki 的规则层，不是普通说明文档。

## 知识库信息

- 主题：{{TOPIC}}
- 创建日期：{{DATE}}
- 语言：{{LANGUAGE}}
- 版本：2.0
- 方法论：Karpathy llm-wiki pattern

## Karpathy 三层结构

| 层 | 本知识库对应 | 规则 |
| --- | --- | --- |
| Raw sources | `raw/` 下的 PDF、网页、公众号、笔记、项目页等 | 原始事实来源，不可变；AI 只读不改。 |
| Wiki | `wiki/sources/`、`wiki/topics/`、`wiki/synthesis/`、`index.md`、`log.md` | AI 生成和维护的知识层。 |
| Schema | `.wiki-schema.md`、templates、校验脚本 | 约束 AI 如何维护 wiki。 |

核心原则：

1. 新材料进入后要整合进已有 wiki，而不是只生成孤立摘要。
2. 不要每次查询都重新从 raw source 推导；重要知识要沉淀进 wiki。
3. `index.md` 是人和 AI 的内容导航。
4. `log.md` 是知识库演化时间线。
5. `graph` 是 wiki 的视图，不是第二套知识模型。

## 目录结构

```
{{WIKI_ROOT}}/
├── raw/                    # 原始素材（AI 只读，不修改）
│   ├── articles/           # 网页文章、博客、项目页
│   ├── tweets/             # X/Twitter 内容
│   ├── wechat/             # 微信公众号文章
│   ├── xiaohongshu/        # 小红书内容
│   ├── zhihu/              # 知乎内容
│   ├── pdfs/               # PDF 文件
│   ├── notes/              # 手写笔记、本地 Markdown/文本
│   └── assets/             # 图片等附件
├── wiki/                   # AI 维护的知识层
│   ├── sources/            # 材料页 / source summary
│   ├── topics/             # 主题路线
│   ├── synthesis/          # 综述判断
│   ├── entities/           # 可选内部概念页，不作为前台主入口
│   ├── comparisons/        # 可选内部对比页
│   └── queries/            # 可选 query 沉淀页
├── index.md                # 内容索引
├── log.md                  # 操作日志
└── .wiki-schema.md         # 本文件
```

## 前台主概念

前台读者只需要理解三层：

```text
材料 -> 主题路线 -> 综述判断
```

| 前台概念 | 内部名称 | 含义 |
| --- | --- | --- |
| 材料 | `source` / source summary | AI 读完原始来源后生成的阅读入口。 |
| 主题路线 | `topic` | 把多篇材料组织到同一条问题线。 |
| 综述判断 | `synthesis` | 跨材料、跨主题形成阶段性判断。 |

必须区分：

```text
raw source != 材料页
```

`raw source` 是不可变原始输入。`材料页` 是 AI 生成的 source summary。

不应成为前台主概念的内容：

- `domain`
- `source_type`
- `tag`
- `entity`
- `query`
- `comparison`
- `community`
- `recommended start`
- `roadmap`

这些可以作为 metadata 或内部辅助结构使用。

## 来源边界

这套边界和安装输出、状态说明、回归测试保持一致。来源进入 raw sources 层后，再由 ingest 决策是否创建或更新材料页。

| 分类 | 当前来源 | 处理原则 |
| --- | --- | --- |
| 核心主线 | `PDF / 本地 PDF`、`Markdown/文本/HTML`、`纯文本粘贴` | 不依赖外挂，直接进入主线。 |
| 可选外挂 | `网页文章`、`X/Twitter`、`微信公众号`、`YouTube`、`知乎` | 先自动提取；失败时退回手动入口。 |
| 手动入口 | `小红书` | 只接受用户手动粘贴。 |

### 素材类型路由

| 来源 | raw 目录 | 提取方式 |
| --- | --- | --- |
| PDF / 本地 PDF | `raw/pdfs/` | 直接读取。 |
| Markdown/文本/HTML | `raw/notes/` | 直接读取。 |
| 纯文本粘贴 | `raw/notes/` | 直接使用。 |
| 网页文章 | `raw/articles/` | `baoyu-url-to-markdown`。 |
| X/Twitter | `raw/tweets/` | `baoyu-url-to-markdown`，可能需要 Chrome 登录态。 |
| 微信公众号 | `raw/wechat/` | `wechat-article-to-markdown`。 |
| YouTube | `raw/articles/` | `youtube-transcript`。 |
| 知乎 | `raw/zhihu/` | `baoyu-url-to-markdown` 或手动粘贴。 |
| 小红书 | `raw/xiaohongshu/` | 用户手动粘贴。 |

## 页面命名规范

- 材料页：`wiki/sources/{slug}.md`
  - slug 优先来自 arXiv ID、DOI、稳定标题；同一材料多次 ingest 必须生成同一 slug。
- 主题页：`wiki/topics/{topic-slug}.md`
  - topic 是问题路线，不是 tag。
- 综述页：`wiki/synthesis/{synthesis-slug}.md`
  - synthesis 是阶段性判断，不是材料摘要合集。
- 实体页：`wiki/entities/{名称}.md`
  - 可选内部页，只在确实能减少重复时创建。

## 受控领域和标签

### Domain

每个材料必须至少有一个主 domain。初始 domain：

- `LLM/VLM`
- `Physical/Embodied Intelligence`
- `AIGC`
- `Agent`

新增 domain 前必须满足：

1. 现有 domain 无法覆盖。
2. 预计后续会有多篇材料归入。
3. 在 `index.md` 或 `.wiki-schema.md` 记录新增原因。

### Tag

每个材料给 1-2 个 tag，最好 1 个。

规则：

- tag 用于检索和聚合，不是每篇材料独有的关键词。
- 不要把标题里的每个术语都变成 tag。
- 如果 tag 已经接近 topic，应优先挂 topic，而不是继续堆 tag。

## Source Schema（材料页）

材料页 frontmatter 必须包含：

```yaml
id:
slug:
title:
type: source
material_type:
source_type:
created:
updated:
date:
authors: []
domains: []
tags: []
summary:
links:
  original:
  arxiv:
  pdf:
  project:
  github:
  hjfy:
  doi:
raw_refs: []
related_topics: []
related_syntheses: []
confidence:
hero_image:
images:
image_paths: []
```

`material_type` 推荐值：

- `paper`
- `wechat`
- `blog`
- `note`
- `project`
- `video`
- `report`
- `dataset`
- `code`

## Topic Schema（主题路线）

主题页 frontmatter 必须包含：

```yaml
id:
slug:
title:
type: topic
created:
updated:
domains: []
tags: []
summary:
source_slugs: []
synthesis_slugs: []
status:
open_questions: []
```

Topic 规则：

1. topic 代表一条问题线，不是普通 tag。
2. 新材料默认优先挂到已有 topic。
3. 只有形成新的持续问题线时才新建 topic。
4. topic 应说明每份材料对该路线的贡献。

## Synthesis Schema（综述判断）

综述页 frontmatter 必须包含：

```yaml
id:
slug:
title:
type: synthesis
created:
updated:
domains: []
tags: []
summary:
judgment:
source_slugs: []
topic_slugs: []
claims: []
open_questions: []
confidence:
```

Synthesis 规则：

1. synthesis 是判断层，不是摘要合集。
2. 不要每次 ingest 都更新 synthesis。
3. 只有新材料改变阶段性判断、反驳已有 claim、显著补强证据、连接多个 topic，或回答 open question 时，才更新 synthesis。
4. 更新 synthesis 时必须说明影响了哪些 claim，以及证据来自哪些 source/topic。

## Ingest 决策流程

每次 ingest 必须按顺序判断：

1. **提取 raw source**：保存原始内容到 `raw/`，AI 不改 raw。
2. **材料去重**：用 URL、arXiv ID、DOI、标题、PDF、项目页、GitHub、hjfy、作者日期判断是否已有材料。
3. **材料动作**：输出 `create_source`、`update_source` 或 `link_as_related_source`。
4. **分类**：为材料分配 domain 和 1-2 个 tag。
5. **主题归并**：优先挂到已有 topic；只有形成新问题线才创建 topic。
6. **综述门槛**：判断 synthesis 是 `unchanged`、`update` 还是 `create`。
7. **变更预览**：写入/发布前展示新增、更新、关联和判断变化。
8. **更新 index/log**：记录本次变更。

## Step 1 JSON 决策对象

ingest 的结构化分析应优先输出这个对象：

```json
{
  "source_decision": {
    "action": "create_source | update_source | link_as_related_source",
    "target_slug": "",
    "reason": ""
  },
  "classification": {
    "domains": [],
    "tags": [],
    "material_type": "",
    "source_type": ""
  },
  "topic_decisions": [
    {
      "action": "attach_existing | create_topic",
      "target_slug": "",
      "title": "",
      "reason": ""
    }
  ],
  "synthesis_decision": {
    "action": "unchanged | update | create",
    "target_slug": "",
    "reason": "",
    "affected_claims": []
  },
  "graph_edges": [
    {
      "from": "",
      "to": "",
      "type": "supports | relates | contrasts | updates | evidence_for",
      "confidence": "EXTRACTED | INFERRED | AMBIGUOUS | UNVERIFIED",
      "evidence": ""
    }
  ],
  "warnings": []
}
```

兼容旧 skill 时可以保留 `entities/topics/connections`，但 FollowHub 新流程必须优先消费这个决策对象。

## 交叉引用规范

- 页面间使用 `[[页面名]]` 语法，保持 Obsidian 兼容。
- 前台路由使用 slug：
  - source -> `/wiki/source/<slug>`
  - topic -> `/wiki/topic/<slug>`
  - synthesis -> `/wiki/synthesis/<slug>`
- Markdown 链接和前台路由必须能从同一份 slug 映射生成。
- 每个页面底部维护“相关页面”列表。

## Query（查询）规则

1. 先读 `index.md`，定位相关 source/topic/synthesis。
2. 再按需要搜索 `wiki/`。
3. 回答必须标注来源页面。
4. 如果回答产生可复用判断，询问是否沉淀为 synthesis 或 query 页面。
5. query 页面是衍生内容，不能替代 raw source 或 source page。

## Lint（健康检查）规则

检查项：

- 断链。
- 孤立 source/topic/synthesis。
- 缺失 raw ref。
- raw source 没有材料页。
- 材料没有 domain/tag。
- topic 没有关联材料。
- synthesis 没有关联 topic 或 source。
- synthesis claim 无证据。
- index 与实际文件不一致。
- graph edge 指向不存在节点。

输出报告时区分：

- error：阻止发布。
- warning：允许发布但需要后续修。
- judgment issue：需要用户判断。

## R2 发布规则

R2 是发布产物，不是源头模型。

推荐目录：

```text
wiki/
  manifest.json
  sources.json
  topics.json
  synthesis.json
  graph-data.json
  source/<slug>.json
  topic/<slug>.json
  synthesis/<slug>.json
  graph/
```

发布前必须校验：

- manifest 数量和文件一致。
- source/topic/synthesis slug 唯一。
- related slug 都存在。
- graph 节点和边都能解析。

## 别名词表（Alias Table）

用于 query 和 digest 时自动展开搜索。搜索任意一个词，会同时搜索同一行的所有别名。

格式：每行一组同义词，用 `=` 分隔。

```
LLM = 大语言模型 = 大模型 = Large Language Model
VLM = 视觉语言模型 = Vision-Language Model
VLA = 视觉语言动作模型 = Vision-Language-Action
RAG = 检索增强生成 = Retrieval Augmented Generation
fine-tuning = 微调 = 精调
prompt engineering = 提示工程 = 提示词工程
```

维护原则：

- 只收录知识库里实际出现过的同义词。
- 每组控制在 5 个以内。
- ingest 发现新同义词时，先建议添加，不要自动无限扩展。

## 关系类型词汇表

| 类型关键词 | 含义 |
| --- | --- |
| supports | A 支撑 B |
| evidence_for | A 是 B 的证据 |
| updates | A 更新 B |
| contrasts | A 与 B 对比或存在张力 |
| relates | A 与 B 相关但关系较弱 |

不确定的关系保持 `relates`，不要强行细分。
