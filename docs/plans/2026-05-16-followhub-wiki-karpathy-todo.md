# FollowHub Wiki：Karpathy llm-wiki 对齐 TODO

日期：2026-05-16

参考：<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

## 目标

FollowHub Wiki 要成为 Karpathy llm-wiki 思路在 FollowHub 里的具体落地，而不是另做一套 CMS。

目标使用方式：

1. 用户持续提供材料：论文、PDF、arXiv、公众号、博客、笔记、项目页、视频、报告等。
2. Agent 调用 `llm-wiki-skill` 读取现有 wiki 状态。
3. Skill 判断这次应该新增/更新材料，挂到已有主题还是创建新主题，是否需要更新综述判断。
4. Wiki 作为持续积累的知识工件存在，而不是每次 query 时重新 RAG 一遍。
5. 前台页面从 R2 读取生成后的 wiki 数据，展示成清晰的知识产品。

## Karpathy 原则

### 三层结构

Karpathy 的 llm-wiki 核心是三层：

| Karpathy 层 | FollowHub 对应 | 规则 |
| --- | --- | --- |
| Raw sources | PDF、arXiv、公众号原文、博客、笔记、项目页、视频、报告 | 原始事实来源，不可变；LLM 只读不改。 |
| Wiki | 材料页、主题页、综述页、index、log、graph | LLM 生成和维护；人主要阅读和校正方向。 |
| Schema | `SKILL.md`、`.wiki-schema.md`、templates、校验脚本 | 约束 Agent 如何维护 wiki 的规则层。 |

### 必须保留的原则

1. 不要在每次查询时重新从原始材料推导；知识要被编译进 wiki 并持续维护。
2. 新材料进入后，应该合并进已有知识结构，不是只新增一篇孤立摘要。
3. LLM 负责维护 wiki：摘要、交叉链接、主题更新、矛盾标注、综述修订、index、log。
4. 用户负责选择材料、决定研究方向、判断哪些结论重要。
5. `index.md` 是内容导航，给人和 LLM 都用。
6. `log.md` 是时间线，记录 ingest、query、lint、publish 等操作。
7. `lint` 是核心流程，不是附属功能；要检查断链、过期判断、矛盾、孤立页、缺失主题和数据空洞。
8. 有价值的 query 输出可以沉淀回 wiki。
9. Graph 是 wiki 的视图，不是第二套知识模型。
10. R2 只是发布和运行时读取层，不改变 llm-wiki 的源头模型。

## FollowHub 概念模型

前台读者只需要理解三层：

```text
材料 -> 主题路线 -> 综述判断
```

| 前台概念 | 内部名称 | 含义 |
| --- | --- | --- |
| 材料 | `source` / source summary | LLM 读完一个原始来源后生成的阅读入口。 |
| 主题路线 | `topic` | 把多篇材料收束到同一条问题线。 |
| 综述判断 | `synthesis` | 跨材料、跨主题形成阶段性判断。 |

必须明确：

```text
raw source != 材料页
```

`raw source` 是不可变的原始输入。`材料页` 是 LLM 生成的 source summary，是给人阅读的入口。

### 不应成为前台主概念的内容

下面这些可以作为 metadata 或内部辅助结构，但不应该成为读者必须理解的主入口：

- `domain`
- `source_type`
- `tag`
- `entity`
- `query`
- `comparison`
- `community`
- `recommended start`
- `roadmap`

## 目标使用流程

```text
用户提供论文 / 公众号 / 笔记 / 链接
  -> Agent 调用 llm-wiki-skill
  -> Skill 读取当前 wiki 状态
  -> Skill 提取并分类新材料
  -> Skill 判断：
       是否创建/更新材料？
       是否挂到已有主题？
       是否需要新建主题？
       是否需要修订综述判断？
  -> 生成变更预览
  -> 运行校验
  -> 发布数据包到 R2
  -> 前台从云端数据自动更新
```

一次理想 ingest 结束后应该能输出类似：

```text
新增材料：3
更新材料：1
更新主题：4
新增主题：0
更新综述：1
新增图谱关系：7
发布目标：R2 wiki manifest
```

## 当前落地状态（2026-05-16）

已完成：

- Skill 概念收敛到 `source/topic/synthesis`，前台语义对应“材料 / 主题路线 / 综述判断”。
- `domain`、`source_type`、`tag` 改为 metadata 和筛选字段；图谱不再维护第二套知识模型。
- 新增 `.wiki-vocabulary.md` 和模板，约束初始 domain 与 1-2 个 tag 的材料标注规则。
- 新增 `validate-followhub-wiki.sh`，用于发布前校验材料、主题、综述、关联 slug、domain/tag 和图谱边。
- 新增 `build-followhub-wiki-package.py`、`validate-followhub-wiki-package.py`、`publish-followhub-wiki-r2.sh`，可以生成、校验、发布 R2 wiki 数据包。
- 新增 `search-index.json` 生成逻辑，覆盖 title、summary、authors、domains、tags、material/source type 与关联页面。
- `page_github` 新增 `scripts/sync-wiki-data.mjs`，支持从本地 package 或 R2 base URL 同步 wiki 数据。
- `page_github` 构建前会执行 `sync:wiki:optional`，R2 可用时优先更新，R2 暂不可用时使用已有 generated fallback。
- regression 已覆盖 package build、package validate 和 local publish。

仍需真实环境验收：

- 使用实际 R2/rclone target 做一次端到端上传。
- 用用户提供的新测试材料跑 ingest，确认 source 去重、topic 归并、synthesis 更新门槛符合预期。
- 当真实材料达到几十到几百条后，再根据使用体验调分页大小、搜索权重和局部图谱默认视图。

## P0 - 概念与 Schema 对齐

### P0.1 重写 skill 的核心概念契约

**任务**

更新 `SKILL.md` 和 `.wiki-schema.md`，让主要维护对象收敛为：

- `source`：材料页 / source summary
- `topic`：主题路线
- `synthesis`：综述判断

同时明确 raw sources 是不可变事实来源。

**原因**

当前 skill 还是通用 `source/entity/topic/synthesis/query/comparison` 模型。FollowHub 需要更贴近 Karpathy，同时前台概念更收敛。

**验收**

- 文档清楚定义 `raw source`、`材料页/source page`、`topic`、`synthesis`。
- `entity`、`query`、`comparison` 被标注为可选/内部能力，不作为前台主导航。
- ingest 优先更新 source/topic/synthesis，再考虑其他页面。

### P0.2 定义标准数据 Schema

**任务**

定义稳定 schema：

- `source`
- `topic`
- `synthesis`
- `manifest`
- `graph-data`

`source` 最少字段：

```yaml
id:
slug:
title:
material_type:
source_type:
date:
updated:
authors:
summary:
domains:
tags:
links:
  original:
  arxiv:
  pdf:
  project:
  github:
  hjfy:
  doi:
hero_image:
raw_refs:
related_topics:
related_syntheses:
confidence:
```

`topic` 最少字段：

```yaml
id:
slug:
title:
summary:
domains:
tags:
source_slugs:
synthesis_slugs:
status:
open_questions:
updated:
```

`synthesis` 最少字段：

```yaml
id:
slug:
title:
summary:
judgment:
evidence:
source_slugs:
topic_slugs:
claims:
open_questions:
updated:
```

**原因**

前台、图谱、搜索、R2 发布都必须读取同一份契约。

**验收**

- schema 写入文档。
- 模板和 schema 对齐。
- 校验脚本能在缺少必填字段时失败。

### P0.3 增加 domain/tag 受控词表

**任务**

增加领域和标签词表。

初始 domain：

- `LLM/VLM`
- `Physical/Embodied Intelligence`
- `AIGC`
- `Agent`

规则：

- 每个材料至少有一个主 domain。
- 每个材料给 1-2 个 tag，最好 1 个。
- tag 要能用于检索和聚合，不能每篇材料都生成完全独立的新 tag。

**原因**

不控制词表，模型会越生成越散，后续筛选和图谱都会变乱。

**验收**

- 新 ingest 必须写入 `domains` 和 `tags`。
- 未知 domain 给 warning。
- tag 太多给 warning。

## P0 - Ingest 决策逻辑

### P0.4 材料去重

**任务**

新增材料前，先和已有材料比较：

- URL
- arXiv ID
- DOI
- 标题相似度
- PDF 文件名
- 项目页
- GitHub
- hjfy 链接
- 作者 + 日期

**原因**

同一工作可能以 arXiv、PDF、项目页、公众号解读、个人笔记等形式进入。多数情况下应合并到同一个材料记录，而不是拆成多个孤立页面。

**验收**

- ingest 输出 `create_source`、`update_source` 或 `link_as_related_source`。
- 已有材料可以补充新链接，不重复建页。
- 变更预览里说明去重判断。

### P0.5 主题归并

**任务**

每个材料进入后，判断它属于已有 topic，还是需要创建新 topic。

规则：

- 优先挂到已有 topic。
- 只有形成新的问题线时才新建 topic。
- topic 不是 tag，必须代表一条可持续积累的问题路线。

**原因**

主题是从材料到综述的中间骨架。

**验收**

- 每个材料至少关联一个 topic，除非明确标记为未归类。
- 新建 topic 必须有理由。
- topic 页列出相关材料，并说明每篇材料的贡献。

### P0.6 综述更新门槛

**任务**

不要每次 ingest 都更新 synthesis。增加判断门槛。

只有新材料满足下面任一条件时，才更新 synthesis：

- 改变阶段性判断。
- 反驳或修正已有 synthesis claim。
- 显著增强或削弱某个判断的证据。
- 连接了多个 topic，形成新判断。
- 回答了 synthesis 里的 open question。

**原因**

synthesis 是判断层，不是材料摘要合集。

**验收**

- ingest 输出 `synthesis_action: unchanged | update | create`。
- 如果 unchanged，说明为什么不更新。
- 如果 update，必须写清影响的 claim 和证据。

### P0.7 发布前变更预览

**任务**

写入或发布前生成变更预览：

```text
新增材料：
- ...

更新材料：
- ...

更新主题：
- ...

更新综述：
- ...

新增图谱关系：
- ...
```

**原因**

Agent 维护 wiki 需要人能快速审查，尤其是 synthesis 变化。

**验收**

- 发布 R2 前必须有 preview。
- preview 区分机械 metadata 更新和判断层更新。

## P1 - 模板与 Markdown Wiki

### P1.1 更新 source 模板

**任务**

修改 `templates/source-template.md`，支持：

- 论文和非论文材料。
- 规范 links。
- domain/tag metadata。
- related topics。
- related syntheses。
- raw refs。
- 阅读摘要。
- 论文类材料的方法、结果、限制。

**验收**

- 论文材料能展示 arXiv/PDF/project/hjfy。
- 非论文材料不展示空的论文专用区块。
- 模板字段能被 sync pipeline 解析。

### P1.2 更新 topic 模板

**任务**

修改 `templates/topic-template.md`，围绕主题路线组织：

- 这个主题在讨论什么。
- 为什么重要。
- 关键材料。
- 当前理解。
- 未解决问题。
- 相关综述。

**验收**

- topic 不是最终判断。
- topic 页能作为从材料走向 synthesis 的中间路线。

### P1.3 更新 synthesis 模板

**任务**

修改 `templates/synthesis-template.md`，围绕综述判断组织：

- 当前判断。
- 材料和主题证据。
- claims。
- 矛盾和限制。
- 什么证据会改变当前判断。
- 相关主题和材料。

**验收**

- synthesis 读起来是阶段性判断，不是普通摘要。
- evidence 能回到 source/topic。

### P1.4 保持 index/log 有用

**任务**

每次 ingest 更新：

- `index.md`
- `log.md`

**原因**

这是 Karpathy 模式里让 LLM 和人都能导航、理解历史的核心文件。

**验收**

- `index.md` 清楚分组 source/topic/synthesis。
- `log.md` 使用可解析格式，例如：

```text
## [2026-05-16] ingest | Paper title
## [2026-05-16] publish | wiki manifest
```

## P1 - R2 云端数据

### P1.5 定义 R2 目录结构

**任务**

发布 wiki 数据到 R2：

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
    knowledge-graph.html
    graph-wash.js
    graph-wash-helpers.js
```

**原因**

前台应该像 Follow 一样主要读云端数据。本地 generated JSON 只能作为开发 fallback。

**验收**

- manifest 包含数量、更新时间、数据版本、文件路径。
- 前台可以只依赖 R2 渲染。
- 本地 JSON 不再是线上主数据源。

### P1.6 明确发布链路

**任务**

固定流程：

```text
llm-wiki-skill
  -> wiki-sync-page
  -> publish-wiki
  -> R2
  -> page_github frontend
```

**验收**

- 一个命令能构建数据包。
- 一个命令能发布到 R2。
- 发布前校验 manifest 和必要文件。

## P1 - 前台页面

### P1.7 前台统一从 R2 读取 Wiki 数据

**任务**

在 `page_github` 增加统一 wiki data fetch 层。

规则：

- 优先读 R2。
- 本地 generated data 只作为开发 fallback。
- 不允许每个页面各写一套数据加载逻辑。

**验收**

- 首页、材料库、材料详情、主题列表、主题详情、综述列表、综述详情、图谱都使用同一个数据源。
- 页面数量和图谱数量一致。

### P1.8 前台导航保持三层

**任务**

主入口保持：

- 材料
- 主题路线
- 综述判断
- 图谱

**验收**

- domain、source type、tag 只作为筛选或 metadata。
- 不再出现重复入口卡片。
- 页面不放没有信息增量的说明文字。

### P1.9 材料库分页和检索

**任务**

材料库要能支撑几百条材料。

支持：

- 搜索。
- 分页。
- 类型筛选。
- domain 筛选。
- tag 筛选。
- 上一页/下一页在材料浏览区域跟随。

**验收**

- 页面不会一次堆几百条 list。
- 搜索覆盖 title、summary、authors、tags、domains、source type。

## P1 - 图谱

### P1.10 图谱使用 wiki 同源数据

**任务**

图谱从 source/topic/synthesis 关系生成。

节点跳转：

- source -> `/wiki/source/<slug>`
- topic -> `/wiki/topic/<slug>`
- synthesis -> `/wiki/synthesis/<slug>`

**验收**

- 图谱数量和 wiki 数量一致。
- 节点点击打开或聚焦对应 wiki 页面。
- 不维护第二套 graph-only 页面模型。

### P1.11 支持局部图谱

**任务**

点击 topic 或 synthesis 时，默认展示关联子图，而不是全图。

**验收**

- 点击 topic 展示 topic + 相关材料 + 相关综述。
- 点击 synthesis 展示 synthesis + 相关主题 + 证据材料。
- 全图作为显式入口保留。

## P2 - 校验与 Lint

### P2.1 数据校验脚本

**任务**

增加 wiki 数据校验。

检查：

- slug 唯一。
- 必填字段存在。
- route 目标存在。
- related slug 存在。
- 每个材料都有 domain/tag。
- synthesis 数量正确。
- graph edge 引用的 node 存在。
- links 格式有效。

**验收**

- 发布前自动运行。
- error 阻止发布。
- warning 和 error 分开。

### P2.2 Karpathy Wiki 健康检查

**任务**

扩展 lint：

- 断链。
- 孤立材料/主题/综述。
- 矛盾信息。
- 过期 synthesis claim。
- 缺失 topic 关联。
- index 未收录页面。
- raw source 没有材料页。
- 材料页没有 raw ref。

**验收**

- lint 报告给出修复建议。
- 区分机械问题和判断问题。

## P2 - Skill 运行时增强

### P2.3 升级 ingest JSON

**任务**

把 Step 1 JSON 从通用 `entities/topics/connections` 升级为 FollowHub 决策对象：

```json
{
  "source_decision": {},
  "classification": {},
  "topic_decisions": [],
  "synthesis_decision": {},
  "graph_edges": [],
  "warnings": []
}
```

**验收**

- validator 校验这个决策对象。
- Step 2 页面生成消费这个对象。

### P2.4 稳定 slug 规则

**任务**

定义这些内容的 slug 和 alias 规则：

- materials。
- topics。
- synthesis pages。

**验收**

- 同一 source 多次运行生成同一 slug。
- 重命名时保留 alias 或 redirect。
- Markdown wiki link 和前台 route 指向同一目标。

### P2.5 链接提取与规范化

**任务**

ingest 时规范化这些链接：

- original URL。
- arXiv。
- PDF。
- project。
- GitHub。
- hjfy。
- DOI。
- WeChat original。

**验收**

- 材料详情页能渲染正确 icon 和按钮。
- 缺失链接不会产生空 UI。

## P2 - 迁移

### P2.6 迁移现有 FollowHub Wiki 数据

**任务**

把当前 source/topic/synthesis markdown 和 generated JSON 迁移到新 schema。

**验收**

- 现有 12 个材料、11 个主题、3 个综述都保留。
- 已知 route 返回 200。
- 图谱数量一致。
- 已有论文链接、PDF、项目页、hjfy 尽可能保留。

### P2.7 兼容旧字段

**任务**

临时保留旧 markdown 字段解析。

**验收**

- 旧页面迁移期还能 sync。
- 新页面使用新 schema。
- compatibility 代码有明确移除 TODO。

## P3 - 搜索与规模

### P3.1 Search Index

**任务**

材料变多后生成搜索索引：

```text
wiki/search-index.json
```

索引字段：

- title
- summary
- authors
- domains
- tags
- material type
- source type
- related topic titles
- related synthesis titles

**验收**

- 几百条材料时搜索仍然快。
- 搜索结果链接使用 canonical wiki routes。

### P3.2 大规模 Wiki Routing

**任务**

当 topic/material 数量变大后，增加 routing 文件：

```text
wiki/routing.json
```

**原因**

Wiki 变大后，agent 不应该每次 query/ingest 都扫全库。

**验收**

- query 和 ingest 可以先缩小到相关 domain/topic。
- routing 从 wiki 自动生成，不手写维护。

## 完成定义

这个项目完成时应满足：

1. 用户给一篇论文、公众号、博客、笔记或项目链接后，agent 能进入稳定 ingest 流程。
2. Agent 能判断新增材料还是更新已有材料。
3. Agent 能把材料挂到已有主题，或有理由地创建新主题。
4. Agent 能判断 synthesis 保持不变、更新，还是新建。
5. 发布前有变更预览。
6. 校验通过后才能发布。
7. R2 拿到完整 wiki 数据包。
8. 前台从 R2 渲染。
9. 图谱、数量、搜索、路由全部使用同一份 source/topic/synthesis 数据。
10. `index.md` 和 `log.md` 持续更新，并能服务后续 agent session。

## 不做什么

1. 不把 FollowHub Wiki 做成通用 CMS。
2. 不把 domain/tag/source type 变成前台主概念。
3. 不维护独立于 wiki 的第二套图谱数据。
4. 不在每次新增材料后机械更新 synthesis。
5. 不让 R2 取代 llm-wiki 的源头模型；R2 只是发布后的运行时产物。
