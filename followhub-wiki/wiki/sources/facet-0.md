---
id: "facet-0"
slug: "facet-0"
title: "Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation"
type: source
material_type: "paper"
source_type: paper
source_kind: "web_url"
source_input: "https://pine-lab-ntu.github.io/facet-0/assets/paper/Facet-0.pdf"
created: "2026-09-05"
updated: "2026-09-05"
date: "2026-09-01"
publish_date: "2026-09-01"
source_url: "https://pine-lab-ntu.github.io/facet-0/"
html_url: "https://arxiv.org/html/2609.01596v1"
pdf_url: "https://pine-lab-ntu.github.io/facet-0/assets/paper/Facet-0.pdf"
code_url: "https://github.com/PINE-Lab-NTU/FACET"
translation_url: "https://hjfy.top/arxiv/2609.01596"
arxiv_id: "2609.01596"
authors:
  - "Haoyuan Deng"
  - "Haichao Liu"
  - "Wenkai Guo"
  - "Yuan Ling"
  - "Zaijia Yang"
  - "Yuanjiang Xue"
  - "Haosheng Sun"
  - "Liangzi Wang"
  - "Ziwei Wang"
affiliation: "PINE Lab, Nanyang Technological University, Singapore"
related_organizations:
  - "PINE Lab, Nanyang Technological University"
related_companies: []
domains:
  - "physical-embodied-ai"
domain: "physical-embodied-ai"
primary_domain_slug: "physical-embodied-ai"
domain_slugs:
  - "physical-embodied-ai"
tags:
  - "robot-foundation-model"
summary: "Facet-0 把视觉语言动作模型从“看见目标并移动过去”推进到“预测动作的接触后果并据此选择动作”。系统将三路 RGB、语言、机器人运动学状态与腕部六维力矩历史对齐为共享语义—接触表征，以流匹配联合生成 7 维笛卡尔动作块和未来 6 维力矩轨迹；再通过部署数据训练 Action–Wrench Critic，并以阶段奖励和接触选择性信用进行后训练。最后，轻量 bounded actor 在冻结骨干上适配具体零件动力学。"
keywords:
  - "contact-rich manipulation"
  - "robotic foundation model"
  - "vision-language-action"
  - "force-torque sensing"
  - "reinforcement learning"
  - "precision assembly"
links:
  original: "https://pine-lab-ntu.github.io/facet-0/"
  arxiv: "https://arxiv.org/abs/2609.01596"
  html: "https://arxiv.org/html/2609.01596v1"
  pdf: "https://pine-lab-ntu.github.io/facet-0/assets/paper/Facet-0.pdf"
  project: "https://pine-lab-ntu.github.io/facet-0/"
  github: "https://github.com/PINE-Lab-NTU/FACET"
  code: "https://github.com/PINE-Lab-NTU/FACET"
  model: "https://huggingface.co/Pinelab/Facet-0"
  dataset: "https://huggingface.co/datasets/Pinelab/ManuFacet-1K"
  hjfy: "https://hjfy.top/arxiv/2609.01596"
  doi: "https://doi.org/10.48550/arXiv.2609.01596"
raw_refs:
  - "https://arxiv.org/abs/2609.01596"
  - "https://arxiv.org/html/2609.01596v1"
  - "https://arxiv.org/pdf/2609.01596"
  - "https://pine-lab-ntu.github.io/facet-0/assets/paper/Facet-0.pdf"
  - "https://github.com/PINE-Lab-NTU/FACET"
  - "https://pine-lab-ntu.github.io/facet-0/"
  - "https://huggingface.co/Pinelab/Facet-0"
  - "https://huggingface.co/datasets/Pinelab/ManuFacet-1K"
related_topics:
  - "vision-language-action"
  - "contact-rich-manipulation"
related_syntheses:
  - "force-touch-robot-policy-review"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2609.01596v1/Teaser1.png"
images:
  - "https://arxiv.org/html/2609.01596v1/Teaser1.png"
  - "https://arxiv.org/html/2609.01596v1/Pipeline0828.png"
  - "https://arxiv.org/html/2609.01596v1/fig_posttrain.svg"
image_paths: []
status: analyzed
---

# Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

## 太长不看

Facet-0 的关键不是把力觉当作又一个输入通道，而是让策略同时提出动作和该动作将引发的腕部力矩后果，再用接触结果训练分布式价值模型、按接触阶段分配强化学习信用，最后用受安全边界约束的小型 actor 做任务级适配；在五项亚毫米电脑装配任务上达到 82% 平均成功率，而最强基线为 15%。

## 直观理解

可以把 Facet-0 理解成一名装配工：它不仅决定手下一步往哪里动，还会先预测这一步碰到零件后手腕会感受到怎样的力。如果几条轨迹看起来都接近目标，系统会优先选择不会卡住、不会顶歪、接触更干净的那一条；到了新零件上，则只微调一个被动作安全盒限制的小模块，而不重训整套大模型。

![主要图](https://arxiv.org/html/2609.01596v1/Teaser1.png)

*主要图*

## 核心信息

- **作者**：Haoyuan Deng、Haichao Liu、Wenkai Guo、Yuan Ling、Zaijia Yang、Yuanjiang Xue、Haosheng Sun、Liangzi Wang、Ziwei Wang
- **作者单位**：PINE Lab，Nanyang Technological University，Singapore
- **来源类型**：web_url
- **输入来源**：https://pine-lab-ntu.github.io/facet-0/assets/paper/Facet-0.pdf
- **原文链接**：https://pine-lab-ntu.github.io/facet-0/
- **HTML 正文**：https://arxiv.org/html/2609.01596v1
- **PDF 地址**：https://pine-lab-ntu.github.io/facet-0/assets/paper/Facet-0.pdf
- **代码地址**：https://github.com/PINE-Lab-NTU/FACET
- **模型页**：https://huggingface.co/Pinelab/Facet-0
- **数据集**：https://huggingface.co/datasets/Pinelab/ManuFacet-1K
- **中英翻译地址**：https://hjfy.top/arxiv/2609.01596
- **发布日期**：2026-09-01
- **主题域**：physical-embodied-ai

## 背景与问题

**动机：** 亚毫米装配的难点并不只是视觉定位误差，而是接触之后的误差放大：零件边缘轻微错位就会导致卡滞、刮擦或超力。传统 VLA 模型通常由互联网视觉语言知识和示教轨迹驱动，擅长语义与自由空间运动，却缺少对局部接触动力学和失败后果的显式建模。纯视觉轨迹即便几何进度相近，实际接触质量也可能完全不同，因此仅靠行为克隆很难选出既完成任务又不损伤部件的动作。

**问题缺口：** 论文要解决的缺口是：如何在仍以笛卡尔动作作为唯一执行命令的前提下，把腕部力矩的历史与未来后果纳入统一 VLA 表征和生成过程，并让强化学习把有限的更新预算集中在插入、按压、就位等决定成败的接触片段；同时，模型还要能以较低成本适配不同零件的间隙、刚度与摩擦，而不破坏预训练获得的通用视觉语言能力。

## 论文摘要（英文原文）

Real-world robotic assembly at sub-millimeter tolerances demands spatial precision, compliant interaction, and robustness to contact failures. We present Facet-0, a robotic foundation model that predicts and values the contact consequences of its actions. Facet-0 unifies multimodal representation learning and reinforcement learning post-training around a joint action–wrench proposal: a causal wrench history is aligned with vision–language semantics and kinematic state, and flow matching generates each action chunk together with the future wrist-wrench profile it is expected to induce. Deployment rollouts train a distributional Action–Wrench Critic to distinguish motions with similar task progress but different contact outcomes, while phase-aware rewards and contact-selective credit concentrate policy improvement on decisive interactions. To accommodate part-specific dynamics, a lightweight bounded actor reuses the frozen representation for on-robot adaptation; RL remains defined over executable Cartesian actions, while an auxiliary wrench head preserves predictive, non-commanded action–contact coupling. Trained on ManuFacet-1K, a 1,000-hour force-synchronized corpus spanning three embodiments and multiple manufacturing cells, the bounded task-adapted system reaches 82% mean success on five sub-millimeter computer-assembly tasks, compared with 15% for the strongest baseline, with 0.5 mm placement accuracy and 50 ms command latency.

## 论文摘要（中文翻译）

真实世界中的亚毫米级机器人装配同时要求空间精度、柔顺交互以及面对接触失败时的鲁棒性。Facet-0 是一个能够预测并评价动作接触后果的机器人基础模型。它围绕联合动作—腕部力矩提案统一多模态表征学习与强化学习后训练：将因果力矩历史与视觉语言语义、运动学状态对齐，再由流匹配同时生成动作块及其预计引发的未来腕部力矩轨迹。部署轨迹用来训练分布式动作—力矩评论家，以区分任务进度相似但接触结果不同的运动；阶段感知奖励和接触选择性信用把策略改进集中到关键接触时刻。针对不同零件动力学，模型复用冻结表征，通过轻量且受边界约束的 actor 在机器人上适配；强化学习仍然只作用于可执行笛卡尔动作，辅助力矩头仅保持预测性的动作—接触耦合。系统在跨三种机器人、多个制造单元、约 1000 小时的 ManuFacet-1K 上训练，在五项亚毫米电脑装配任务上达到 82% 平均成功率，最强基线为 15%，并报告 0.5 毫米放置精度和 50 毫秒命令延迟。

## 论文定位：它真正补的是哪一块

Facet-0 位于三条路线的交叉点：VLA 基础策略、力觉/接触建模，以及真实机器人 RL 后训练。它和“给 VLA 多接一个六维力传感器”最大的区别，是把未来 wrench 当成候选动作的**预测后果**；它和传统混合力位控制的区别，是不把该预测直接作为力命令；它和普通 VLA 后训练的区别，则是让 critic 同时看到动作与预期接触后果，并把信用重点分给少量决定成败的接触阶段。

因此，这篇论文的中心命题不是“力觉有用”，而是：**一个动作应当连同其物理后果一起被生成和评价。** 这一建模选择把视觉语义、接触动力学与部署期价值学习连接到同一条训练链路中。

## 数据与执行栈

- **ManuFacet-1K**：论文报告约 1,000 小时的力同步精密装配数据，包含示教和闭环部署轨迹，覆盖 UR7e、xArm、Franka 三种具身、两类机箱以及多个制造单元。
- **统一样本结构**：每帧状态包含 6D 末端位姿、夹爪状态和 6D 腕部 wrench，共 13 维；训练统一到 15 Hz，同时保留更高频状态/力信息供 200 Hz 控制器使用。
- **多视角与阶段标签**：模型读取三路 RGB，并将轨迹标注为 approach、align、insert、press、seat、fasten、retreat 等阶段；align、insert、press、seat、fasten 是接触意图最强的片段。
- **多速率闭环**：语义规划和粗粒度动作—力矩提案约 5–10 Hz，细化专家约 20 Hz，底层柔顺控制约 200 Hz。论文摘要中的 50 ms 命令延迟对应 20 Hz 的细化动作更新。
- **规模口径要分清**：论文以约 1,000 小时描述完整语料；项目页还展示持续更新的数据看板，例如当前 trainable hours 与 curated episodes。两者分别是论文总语料口径和在线发布/质检口径，不宜直接等同。

## 方法

**方法概述：** Facet-0 把视觉语言动作模型从“看见目标并移动过去”推进到“预测动作的接触后果并据此选择动作”。系统将三路 RGB、语言、机器人运动学状态与腕部六维力矩历史对齐为共享语义—接触表征，以流匹配联合生成 7 维笛卡尔动作块和未来 6 维力矩轨迹；再通过部署数据训练 Action–Wrench Critic，并以阶段奖励和接触选择性信用进行后训练。最后，轻量 bounded actor 在冻结骨干上适配具体零件动力学。

**核心机制：** Facet-0 以 PaliGemma 视觉语言骨干和流匹配动作专家为核心，将三路 RGB 图像、语言指令、7 维运动学状态以及长度为 10 的因果腕部力矩历史编码成语义—接触表示。每次生成未来 50 步联合提案：7 维笛卡尔动作与 6 维预测腕部力矩成对出现。预测力矩永远不直接下发，只描述动作可能引起的接触后果。部署轨迹进一步训练分布式 Action–Wrench Critic，阶段奖励刻画子目标、速度和超力，接触选择性信用在接触与非接触片段内分别排序。面对具体新零件时，冻结主干，只训练被安全动作盒约束的 TD3+BC actor；其双评论家只评价可执行动作，辅助头继续预测下一时刻力矩。

**方法拆解：**

- 联合动作—力矩流匹配：在 H=50 的时间窗内生成 H×13 的提案，采用一步因果配对，让时刻 t+k 的动作对应 t+k+1 的力矩后果，避免把同时刻相关性误当因果作用。
- 共享但分路的表征训练：动作—力矩生成与因果 VQA 共用视觉语言前缀，但通过结构化注意力分开路径；两类优化器按 4:1 交替，降低不同损失尺度互相干扰。
- 接触选择性强化学习：用部署轨迹训练分布式 Action–Wrench Critic，在接触与自由空间两类片段内分别计算短时程信用，再按接触强度加权流匹配更新。
- 受约束的本地适配：冻结共享表征，仅更新占总参数 6.6% 的 bounded actor；tanh 输出经仿射映射到任务安全动作边界，TD3+BC 同时保持示教锚点。

**关键要点：**

- 未来力矩是动作后果的预测量而不是控制命令，这是论文避免把“力觉建模”误写成“直接力控制”的关键。
- 性能跃迁并非只来自大规模预训练：受控变体从语义—接触对齐的 16%，经价值后训练到 38%，再通过任务级本地适配达到 82%。

![方法图](https://arxiv.org/html/2609.01596v1/Pipeline0828.png)

*方法图*

## 结果

**核心结果：**

- 五项电脑装配任务各测试 20 次且不重跑，Facet-0 Full 在 RAM、CPU、Disk、GPU、Lever 上分别达到 95%、85%、95%、85%、50%，平均 82%。
- 所有通用基线中最高平均成功率为 15%；Facet-0 相当于约 5.5 倍，并在单任务上领先最佳基线 45 到 75 个百分点。
- Disk 的同数据同预算后训练比较中，接触选择性 RL 将成功率从 20% 提至 65%，恢复率从 44% 提至 81%，人工干预率从 47% 降至 24%。

**结果表：**

| 方法 | RAM | CPU | Disk | GPU | Lever | 平均 |
|---|---:|---:|---:|---:|---:|---:|
| π0.5 | 10 | 5 | 25 | 10 | 0 | 10 |
| π0.5 + F | 15 | 5 | 20 | 5 | 0 | 9 |
| π0.5 + RECAP | 35 | 15 | 20 | 5 | 0 | 15 |
| GR00T | 10 | 5 | 5 | 0 | 0 | 4 |
| TA-VLA | 10 | 20 | 30 | 5 | 5 | 14 |
| Facet-0 Align | 15 | 20 | 30 | 10 | 5 | 16 |
| Facet-0 + RL | 45 | 45 | 65 | 35 | 0 | 38 |
| Facet-0 Full | **95** | **85** | **95** | **85** | **50** | **82** |

![结果图](https://arxiv.org/html/2609.01596v1/fig_posttrain.svg)

*结果图*

### 实验细读

五项任务的机械间隙均处于亚毫米级：RAM 0.18 mm、CPU 0.10 mm、Disk 0.30 mm、GPU 0.18 mm、Lever 0.10 mm；对应力限按任务设置，约为 35–70 N，CPU 还区分更严格的阶段力限。每个“方法 × 任务”单元固定执行 20 次且不重跑，因此表中的 5 个百分点就等于一次成功或失败。

完整系统在四项插装任务上达到 85%–95%，但最难的 Lever 只有 50%。这说明方法已明显改善对准、插入与就位，却还没有消除窄间隙、杠杆接触和部件动力学变化造成的长尾失败。论文还报告 13 个接触子目标平均成功率 87%，自由空间 pick 子目标为 100%，进一步说明瓶颈集中在接触而非识别或接近阶段。

### 消融告诉我们什么

以 RAM 为例，完整模型成功率为 95%，峰值力归一化为 0.2×；分别移除 predictive wrench、critic wrench、adaptation wrench 后，成功率为 90%、85%、85%，峰值力为 0.2×、0.5×、0.4×。单独移除一个角色只差 1–2 次成功，证据不足以稳定排序三者的重要性；但全部去掉后成功率降到 45%、峰值力回到 1.0×，说明“力觉贯穿表示—价值—适配”的整体闭环，而非某个孤立模块，才是主要增益来源。

未见过的 memory module 适配只使用 10 条示范、训练 3 小时并更新 6.6% 参数，达到 45% 成功率，而最强基线为 5%。这支持“冻结通用表征 + 小型 bounded actor”的可迁移性，但 45% 仍未达到生产可靠性，也提醒我们不要把 few-shot 适配等同于任务已经解决。

## 洞察

**核心 insight：**

- 这项工作最值得注意的是把世界模型思路缩小到“接触后果模型”：它不试图预测完整未来图像，而只预测与安全和成败高度相关的腕部力矩轨迹，因此更容易被价值模型利用。
- 自由空间与接触阶段的学习信号密度并不相同。分别排序信用、再用接触强度加权，比对整条轨迹做统一优势估计更贴合精密装配的稀疏关键事件结构。

**和已有方法的关系：**

- 相较只把力觉作为输入的 VLA，Facet-0 同时建模过去力觉与未来预测力觉，并将后者交给价值模型区分“几何进度相似、接触结果不同”的轨迹。
- 相较统一处理整条轨迹的离线或在线 RL，它显式分解任务阶段，并把信用集中到 align、insert、press、seat、fasten 等接触片段。

**可借鉴点：**

- 对任何存在关键稀疏交互的策略，可把不可执行的后果变量与动作联合生成，再让评论家评价联合提案；后果头承担预测和表征约束，不必进入控制接口。
- 用冻结大骨干加安全边界内的小 actor 做现场适配：既限制动作探索范围，也把任务特定动力学更新与通用感知表征解耦。

## 风险与判断

**局限：**

- 82% 的完整系统明显依赖任务级本地适配：仅做语义—接触对齐时平均成功率为 16%，价值后训练后为 38%。因此标题中的“基础模型”不应被理解为无需现场数据即可直接泛化；其强项更接近可复用骨干加低成本受约束适配。
- 主实验仍集中在共享机箱夹具、腕部六维力传感器和平行夹爪的电子装配，尚未证明对软体、易碎、多指手、不同末端执行器或更开放工作空间同样有效。
- 每个实验单元仅 20 次试验，移除单个接触角色时常只差 1–2 次成功，作者也承认这些单项贡献的排序尚不确定；更可靠的结论来自全部移除时成功率从 95% 降到 45%。
- 项目仓库目前标注代码即将发布。论文虽给出模型、数据集和训练配方链接，但完整训练和部署链路的可复现成熟度仍需等实际代码开放后验证。

**适用场景：**

- 内存条、CPU、硬盘、GPU 与卡扣等具有 0.10–0.30 毫米间隙、明确力限和可重复工装的精密电子装配。
- 连接器插拔、定位销插入、卡扣压合等能够安装腕部力矩传感器、且动作安全边界可预先定义的工业任务。

**最终判断：** 论文最可信的结论是：显式预测和评价接触后果，再配合受约束的现场适配，可以显著提高亚毫米装配成功率。当前证据还不足以支持它已经成为跨硬件、跨材料、无需任务适配的通用机器人基础模型。

## 结果速览表

| 方法 | RAM | CPU | Disk | GPU | Lever | 平均 |
|---|---:|---:|---:|---:|---:|---:|
| π0.5 | 10 | 5 | 25 | 10 | 0 | 10 |
| π0.5 + F | 15 | 5 | 20 | 5 | 0 | 9 |
| π0.5 + RECAP | 35 | 15 | 20 | 5 | 0 | 15 |
| GR00T | 10 | 5 | 5 | 0 | 0 | 4 |
| TA-VLA | 10 | 20 | 30 | 5 | 5 | 14 |
| Facet-0 Align | 15 | 20 | 30 | 10 | 5 | 16 |
| Facet-0 + RL | 45 | 45 | 65 | 35 | 0 | 38 |
| Facet-0 Full | **95** | **85** | **95** | **85** | **50** | **82** |

## 相关主题

- [[Vision-Language-Action]]
- [[Contact-Rich Manipulation and Adaptive Compliance]]

## 原始链接

- [项目主页](https://pine-lab-ntu.github.io/facet-0/)
- [项目主页提供的 PDF](https://pine-lab-ntu.github.io/facet-0/assets/paper/Facet-0.pdf)
- [arXiv 摘要页](https://arxiv.org/abs/2609.01596)
- [arXiv HTML](https://arxiv.org/html/2609.01596v1)
- [GitHub 仓库](https://github.com/PINE-Lab-NTU/FACET)
- [FACET-0 模型页](https://huggingface.co/Pinelab/Facet-0)
- [ManuFacet-1K 数据集](https://huggingface.co/datasets/Pinelab/ManuFacet-1K)
