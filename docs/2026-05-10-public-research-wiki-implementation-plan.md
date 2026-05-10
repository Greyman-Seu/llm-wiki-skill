# 公开研究 Wiki 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 基于本地 `llm-wiki` 知识库，搭建一个公开可浏览的研究 wiki 站点，同时保留本地 agent 对知识库的持续整理、检索和查询能力。

**Architecture:** 采用“本地知识生产层 + 静态发布层 + 本地 agent 查询层”的分层架构。`llm-wiki` 继续负责知识生产与结构化整理，公开站负责把经过筛选的内容渲染成稳定的静态网页并发布到用户域名。

**Tech Stack:** `llm-wiki`, Markdown, static hosting, optional static site generator, local shell scripts, domain + CDN hosting

---

## 1. 计划范围

本计划覆盖以下实施目标：

- 初始化并稳定使用本地 `llm-wiki`
- 建立公开内容发布规则
- 设计并实现公开站基础页面
- 将图谱页与结构化内容上线到域名
- 保持本地 agent 检索和整理工作流可持续运行

本计划不覆盖：

- 在线编辑后台
- 公开站实时问答
- 数据库存储迁移
- 用户系统
- 评论系统

---

## 2. 交付物

交付完成后，应至少拥有以下结果：

- 一个可用的本地论文研究知识库
- 一批结构化主题页与来源页
- 一个可公开访问的站点首页
- 一个公开可访问的知识图谱页
- 一条可重复执行的静态发布流程
- 一套 wiki 与 blog 的链接规范

---

## 3. 文件与系统边界

### 本地知识库边界

- `raw/`: 原始资料，只增不改
- `wiki/`: agent 整理后的结构化内容
- `wiki/knowledge-graph.html`: 图谱 HTML 产物
- `wiki/graph-data.json`: 图谱数据产物

### 公开站边界

公开站建议单独维护一个站点目录或独立仓库，职责包括：

- 首页与导航
- wiki 内容渲染后的公开页面
- 图谱页静态托管
- blog 外链聚合

### 发布边界

- 本地知识库是事实源
- 公开站只消费经过筛选的公开内容
- agent 查询直接读取本地知识库，不依赖公开站

---

## 4. 阶段拆分

### Phase 1: 本地知识库建立

目标：

- 把 `llm-wiki` 真正跑起来
- 形成第一批可检索内容
- 确认论文 ingest 和 query 工作流稳定

### Phase 2: 公开站骨架建立

目标：

- 建立公开域名上的静态站骨架
- 接入图谱页
- 接入主题页和来源页

### Phase 3: 发布流程稳定化

目标：

- 让“本地整理 -> 生成公开页 -> 部署”成为可重复流程
- 明确哪些内容公开、哪些内容不公开

### Phase 4: 体验增强

目标：

- 加入更新页、聚合页、静态搜索等增强能力

---

## 5. 执行任务

### Task 1: 初始化本地研究知识库

**Files:**
- Create: `<your-wiki-root>/raw/`
- Create: `<your-wiki-root>/wiki/`
- Create: `<your-wiki-root>/purpose.md`
- Create: `<your-wiki-root>/index.md`
- Create: `<your-wiki-root>/log.md`
- Create: `<your-wiki-root>/.wiki-schema.md`

- [ ] **Step 1: 选定知识库根目录**

建议目录：

```text
~/Documents/research-wiki/
```

要求：

- 该目录长期保留
- 不与公开站目录混用
- 作为 agent 的主工作目录

- [ ] **Step 2: 初始化知识库**

Run:

```bash
bash ~/.codex/skills/llm-wiki/scripts/init-wiki.sh "$HOME/Documents/research-wiki" "公开研究 Wiki"
```

Expected:

- 生成 `raw/`
- 生成 `wiki/`
- 生成 `purpose.md`
- 生成 `index.md`
- 生成 `log.md`
- 生成 `.wiki-schema.md`

- [ ] **Step 3: 补充 `purpose.md`**

填写内容至少包含：

- 研究主题范围
- 当前重点问题
- 公开内容策略
- blog 与 wiki 的分工

建议最小字段：

```md
# 研究目标

- 聚焦 AI 论文、agent、推理模型、工具使用与知识工作流

# 关键问题

- 哪些论文值得长期跟踪
- 不同技术路线之间的核心差异是什么
- 哪些观察适合沉淀为 blog 长文

# 公开策略

- wiki 放结构化公开知识
- blog 放高密度分析长文
```

- [ ] **Step 4: 用一份真实素材验证 ingest**

Run:

```bash
# 例：把本地 markdown 或论文文本交给 agent 走 ingest
```

Expected:

- `wiki/sources/` 出现新条目
- `wiki/topics/` 或 `wiki/entities/` 出现关联条目

- [ ] **Step 5: 验证 query 工作流**

验证问题示例：

- “总结我关于 RAG 的已有研究”
- “我记录过哪些和 tool use 有关的论文”
- “对比我知识库里两种 agent 路线的差异”

Expected:

- agent 能基于本地 wiki 给出结构化回答

---

### Task 2: 建立公开内容筛选规则

**Files:**
- Create: `<your-wiki-root>/PUBLICATION_POLICY.md`
- Modify: `<your-wiki-root>/purpose.md`

- [ ] **Step 1: 新建公开策略文件**

建议文件：

```text
<your-wiki-root>/PUBLICATION_POLICY.md
```

内容至少覆盖：

- 什么内容可以公开
- 什么内容只保留在本地
- 摘要与原文转载边界
- blog 与 wiki 的链接规则

- [ ] **Step 2: 写入公开内容分类**

建议内容：

```md
# 可公开

- 论文摘要
- 概念解释
- 主题概览
- 对比分析

# 谨慎公开

- 大段原文摘录
- 尚未确认的判断
- 半成品草稿

# 不在 wiki 公开

- 高密度完整长文
- 私人工作笔记
```

- [ ] **Step 3: 与知识库工作流对齐**

要求：

- agent 新增公开页面时遵守上述规则
- 后续生成公开站页面时，只消费允许公开的内容

---

### Task 3: 设计公开站目录

**Files:**
- Create: `<public-site-root>/`
- Create: `<public-site-root>/index.html` or static site scaffold
- Create: `<public-site-root>/graph/`
- Create: `<public-site-root>/topics/`
- Create: `<public-site-root>/sources/`
- Create: `<public-site-root>/about/`

- [ ] **Step 1: 选定公开站目录**

建议二选一：

1. 独立仓库
2. 本地独立目录后续推送到静态托管

推荐：

```text
~/Documents/public-research-site/
```

- [ ] **Step 2: 建立最小目录结构**

建议结构：

```text
public-research-site/
├── index.html
├── graph/
├── topics/
├── sources/
├── about/
└── assets/
```

- [ ] **Step 3: 明确页面职责**

要求：

- `index.html` 作为首页
- `graph/` 托管知识图谱
- `topics/` 承载主题页
- `sources/` 承载来源页
- `about/` 说明方法与边界

---

### Task 4: 建立首页与基础导航

**Files:**
- Create: `<public-site-root>/index.html`
- Create: `<public-site-root>/about/index.html`
- Create: `<public-site-root>/assets/`

- [ ] **Step 1: 首页定义最小模块**

首页应包含：

- 站点标题
- 一句话定位
- 图谱入口
- 主题入口
- 最近更新或精选研究入口
- Blog 入口

- [ ] **Step 2: 写首页草稿内容**

建议信息块：

```text
Title: 公开研究 Wiki
Subtitle: 一个由本地 agent 持续维护的结构化研究知识库
Primary CTA: 浏览图谱
Secondary CTA: 查看主题
Tertiary CTA: 阅读 Blog
```

- [ ] **Step 3: 写 About 页面**

About 页应说明：

- 站点来源
- 内容组织方式
- wiki 与 blog 的区别
- 内容公开策略

---

### Task 5: 集成知识图谱页

**Files:**
- Modify: `<your-wiki-root>/wiki/knowledge-graph.html`
- Copy: `<your-wiki-root>/wiki/*graph assets*`
- Create: `<public-site-root>/graph/index.html`

- [ ] **Step 1: 生成图谱产物**

Run:

```bash
bash ~/.codex/skills/llm-wiki/scripts/build-graph-data.sh "$HOME/Documents/research-wiki"
bash ~/.codex/skills/llm-wiki/scripts/build-graph-html.sh "$HOME/Documents/research-wiki"
```

Expected:

- 生成 `wiki/graph-data.json`
- 生成 `wiki/knowledge-graph.html`

- [ ] **Step 2: 复制图谱产物到公开站**

要求：

- 将 `knowledge-graph.html` 放到公开站 `graph/` 目录
- 将依赖资源一并复制

建议目标：

```text
<public-site-root>/graph/index.html
```

- [ ] **Step 3: 验证静态托管兼容性**

检查点：

- 在本地 HTTP 服务下能正常打开
- 页面样式正常
- 节点交互正常
- 图谱搜索正常

Run:

```bash
cd <public-site-root>
python3 -m http.server 8000
```

Expected:

- 访问 `http://localhost:8000/graph/` 能打开图谱页

---

### Task 6: 渲染主题页与来源页

**Files:**
- Read: `<your-wiki-root>/wiki/topics/*.md`
- Read: `<your-wiki-root>/wiki/sources/*.md`
- Create: `<public-site-root>/topics/*.html`
- Create: `<public-site-root>/sources/*.html`

- [ ] **Step 1: 确定一期渲染范围**

一期不要试图公开全部内容。

先挑：

- 3 到 5 个主题页
- 5 到 10 个来源页

- [ ] **Step 2: 确定渲染策略**

推荐二选一：

1. 直接把 Markdown 转静态 HTML
2. 用静态站生成器读取 Markdown 后渲染

推荐：

- 若想尽快上线：直接 Markdown -> HTML
- 若后续要扩展：静态站生成器

- [ ] **Step 3: 为每类页面定义统一模板**

主题页至少包含：

- 标题
- 摘要
- 相关来源
- 相关主题
- Blog 延伸阅读

来源页至少包含：

- 标题
- 原始来源链接
- 核心结论
- 方法概述
- 相关主题
- 相关 Blog

- [ ] **Step 4: 先生成首批页面**

Expected:

- `topics/` 下有可浏览页面
- `sources/` 下有可浏览页面
- 页面之间存在基础链接关系

---

### Task 7: 集成 Blog 外链

**Files:**
- Modify: `<public-site-root>/index.html`
- Modify: `<public-site-root>/topics/*.html`
- Modify: `<public-site-root>/sources/*.html`

- [ ] **Step 1: 定义 Blog 入口位置**

要求：

- 首页有 Blog 区块
- 主题页底部有延伸阅读
- 来源页可选挂载对应长文

- [ ] **Step 2: 建立链接规则**

规则建议：

- wiki 页只链接最相关的 1 到 3 篇 blog
- blog 文中回链对应 wiki 页面

- [ ] **Step 3: 避免信息重复**

要求：

- wiki 不复制 blog 正文
- blog 不承担 wiki 索引职责

---

### Task 8: 选定静态托管与域名接入

**Files:**
- Create: deployment config depending on host
- Create: domain DNS notes

- [ ] **Step 1: 选择托管平台**

可选：

- GitHub Pages
- Netlify
- Vercel
- Cloudflare Pages

推荐判断：

- 极简：GitHub Pages
- 更灵活：Netlify / Vercel / Cloudflare Pages

- [ ] **Step 2: 绑定域名**

要求：

- 设置自定义域名
- 配置 DNS
- 开启 HTTPS

- [ ] **Step 3: 验证发布后路径**

检查点：

- 首页可访问
- `/graph/` 可访问
- `/topics/...` 可访问
- `/sources/...` 可访问

---

### Task 9: 固化发布流程

**Files:**
- Create: `<your-wiki-root>/PUBLISH_CHECKLIST.md`
- Create: local publish script or documented commands

- [ ] **Step 1: 写发布检查清单**

至少包括：

- 是否有不应公开内容
- 图谱是否已更新
- 首页与导航是否同步
- 新增页面链接是否有效

- [ ] **Step 2: 固定发布顺序**

推荐顺序：

```text
整理新素材
-> agent ingest
-> agent query / digest / synthesis
-> build graph
-> 生成公开页
-> 本地预览
-> 部署到域名
```

- [ ] **Step 3: 记录回滚方法**

至少应知道：

- 如何回滚到上一次可用静态版本
- 如何撤回某个误公开页面

---

### Task 10: 验证最终工作流闭环

**Files:**
- No new files required

- [ ] **Step 1: 做一次完整演练**

演练内容：

1. 输入一篇论文笔记
2. 让 agent 整理进 wiki
3. 生成主题 / 来源更新
4. 重新生成图谱
5. 同步到公开站
6. 本地预览
7. 发布上线

- [ ] **Step 2: 验证 agent 查询仍然可用**

验证问题示例：

- “根据我的知识库，总结最近关于推理模型的研究重点”
- “哪些公开页面已经覆盖 agent tool use”
- “把这个新论文和我之前记录的几篇做对比”

- [ ] **Step 3: 验证公开站体验**

检查点：

- 首页是否说明清楚
- 图谱是否可用
- 主题页是否有意义
- 来源页是否不是纯原文堆砌
- Blog 跳转是否自然

---

## 6. 风险与控制

### 风险 1: 内容组织过度复杂

控制方法：

- 一期只做少量主题和来源页
- 不要一开始就公开全部 wiki

### 风险 2: wiki 与 blog 职责混乱

控制方法：

- wiki 只写结构化摘要
- blog 承担高密度完整表达

### 风险 3: 发布内容边界不清

控制方法：

- 先写 `PUBLICATION_POLICY.md`
- 发布前检查一次

### 风险 4: 网站工程过早膨胀

控制方法：

- 先静态托管
- 不做后端
- 不做在线问答

---

## 7. 验收标准

满足以下条件即可认为一期完成：

- 本地知识库已经稳定可用
- 至少有一批真实研究内容进入 wiki
- 公开域名可访问首页和图谱页
- 至少有若干主题页和来源页公开可读
- 本地 agent 仍可直接对知识库检索与整理
- Blog 与 wiki 已形成基础链接关系

---

## 8. 下一步执行建议

优先执行顺序建议如下：

1. 初始化并跑通本地知识库
2. 明确公开策略
3. 建立公开站目录
4. 上线首页与图谱页
5. 补主题页和来源页
6. 接入 blog
7. 固化发布流程

---

## 9. 备注

如果后续要继续深化，下一份文档建议写成更工程化的执行细案，例如：

- 公开站具体技术选型对比
- Markdown 到 HTML 的渲染方案比较
- 自动部署流水线文档
- 搜索功能二期设计

