# 操作日志

> 记录知识库的所有变更历史

---

## 2026-05-10 — 初始化

- **操作**：创建知识库
- **主题**：具身智能研究 Wiki
- **状态**：完成

## 2026-05-11 — 新增素材

- **操作**：消化论文并写入 source note
- **标题**：π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities
- **状态**：完成

## 2026-05-11 — 批量新增素材

- **操作**：使用 arxiv-to-wiki 流程批量写入 source note
- **去重说明**：`rlt.pdf` 与 `arXiv:2604.23073` 为同一篇论文，只保留一份 source note
- **标题**：RL Token: Bootstrapping Online RL with Vision-Language-Action Models
- **标题**：MEM: Multi-Scale Embodied Memory for Vision Language Action Models
- **标题**：Emergence of Human to Robot Transfer in Vision-Language-Action Models
- **状态**：完成

## 2026-05-11 — 首轮主题整理

- **操作**：根据已有 source notes 提炼 topic pages
- **标题**：Vision-Language-Action
- **标题**：Online RL for VLA
- **标题**：Long-Horizon Memory for Robot Policies
- **标题**：Human-to-Robot Transfer
- **状态**：完成

## 2026-05-11 — 新增综合页

- **操作**：基于 5 篇 source notes 生成首篇跨论文 synthesis
- **标题**：当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据
- **状态**：完成

## 2026-05-16 — 新增 arXiv 论文并更新主题

- **操作**：使用 arxiv-to-wiki 流程分析论文并写入 source note
- **标题**：DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos
- **新增主题**：Human Video Robot Data Generation
- **更新主题**：Human-to-Robot Transfer
- **更新综述**：当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据
- **状态**：完成

## 2026-08-10 — 新增 arXiv 论文

- **操作**：使用 arxiv-to-wiki 全流程分析论文并写入 source note（HTML 优先，arxiv-fig 抽取架构图）
- **标题**：Heterogeneous Tactile Transformer
- **arXiv ID**：2606.29948
- **slug**：2606.29948-heterogeneous-tactile-transformer
- **新增主题**：Tactile Representation
- **新 tag**：tactile-representation（已追加到 .wiki-vocabulary.md New Tag Proposal Log）
- **更新索引**：index.md 新增素材条目与主题条目
- **状态**：完成

## 2026-08-10 — 新增 arXiv 论文（Qwen-VLA）

- **操作**：使用 arxiv-to-wiki direct 流程写入并登记 source note；HTML `2605.30280v1` 返回 404，按约定回退到 abs 与 PDF。
- **标题**：Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments
- **arXiv ID**：2605.30280
- **slug**：qwen-vla
- **新增页面**：wiki/sources/qwen-vla.md
- **关联主题**：Vision-Language-Action（仅建立 source 关联，未运行 update-wiki）
- **状态**：完成

## 2026-08-10 — 新增 arXiv 论文（Qwen-RobotManip）

- **操作**：使用 arxiv-to-wiki 流程写入并登记 source note
- **标题**：Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models
- **arXiv ID**：2606.17846
- **slug**：2606.17846-qwen-robotmanip-alignment-unlocks-scale-for-robotic-manipulation-foundation-models
- **核心主张**：对齐 → 规模化 → 泛化；统一状态-动作表示（80维 canonical vector）+ 相机帧 delta 位姿 + in-context policy adaptation
- **关联主题**：Vision-Language-Action（更新调研条目），Human-to-Robot Transfer，Cross-Embodiment
- **综合页**：当前 VLA 路线图（更新，新增"跨具身对齐"子路线）
- **状态**：完成

## 2026-08-10 — 新增企业博客（DM0.5）

- **操作**：处理 feishu 群聊 arxiv2wiki 请求，按 FollowHub wiki 流程将企业技术博客写入 source note（material_type: blog）
- **标题**：DM0.5: 面向开放世界的通用具身智能基础模型（Dexmal 原力灵机）
- **slug**：dm05-open-world-embodied-foundation-model
- **原文链接**：https://www.dexmal.com/blog/dm0.5
- **新增页面**：wiki/sources/dm05-open-world-embodied-foundation-model.md
- **关联主题**：Vision-Language-Action（已加入 source_slugs）
- **tag**：robot-foundation-model（seed tag，无需新增）
- **状态**：完成

## 2026-08-27 ingest | TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback

- **操作**：使用 arxiv-to-wiki direct 流程深度解读论文、写入材料页并更新已有主题路线
- **arXiv ID**：2608.25798v1
- **slug**：2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback
- **核心主张**：把 action chunk 拆成顺序完成与执行的块，保留远期动作的 flow 中间态；执行后刷新触觉，EATA 只让最新触觉影响下一待执行块
- **关键证据**：UniVTAC 六任务平均 65%，真机三任务平均 69%；Fixed Tactile 在消融中无稳定收益，流式更新与 EATA 分别带来独立提升
- **新增页面**：wiki/sources/2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback.md
- **更新主题**：Vision-Language-Action、Tactile Representation
- **综述动作**：unchanged；该论文补强触觉 VLA 的控制接口证据，但尚不足以改变现有总路线图的阶段性判断
- **状态**：完成
