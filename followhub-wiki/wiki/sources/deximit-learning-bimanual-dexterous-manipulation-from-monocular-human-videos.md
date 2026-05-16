---
id: "deximit-learning-bimanual-dexterous-manipulation-from-monocular-human-videos"
slug: "deximit-learning-bimanual-dexterous-manipulation-from-monocular-human-videos"
title: "DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos"
type: source
material_type: "paper"
source_type: "paper"
source_kind: "arxiv_abs_url"
source_input: "https://arxiv.org/abs/2602.10105"
created: "2026-05-16"
updated: "2026-05-16"
date: "2026-02-10"
publish_date: "2026-02-10"
authors:
  - "Juncheng Mu"
  - "Sizhe Yang"
  - "Yiming Bao"
  - "Hojin Bae"
  - "Tianming Wei"
  - "Linning Xu"
  - "Boyi Li"
  - "Huazhe Xu"
  - "Jiangmiao Pang"
affiliation: "Shanghai AI Laboratory; Tsinghua University; The Chinese University of Hong Kong; NVIDIA"
domains:
  - "Physical/Embodied Intelligence"
domain: "physical-embodied-intelligence"
primary_domain_slug: "physical-embodied-intelligence"
domain_slugs:
  - "physical-embodied-intelligence"
tags:
  - "human-video-data-generation"
keywords:
  - "human video"
  - "bimanual dexterous manipulation"
  - "robot data generation"
summary: "DexImit 把单目人类操作视频转换成物理可行的双手灵巧机器人训练数据，补齐 human video 从表示迁移到数据生成的路线。"
links:
  original: "https://arxiv.org/abs/2602.10105"
  arxiv: "https://arxiv.org/abs/2602.10105"
  pdf: "https://arxiv.org/pdf/2602.10105.pdf"
  project: "https://mujc2021.github.io/deximit/"
  github: ""
  hjfy: "https://hjfy.top/arxiv/2602.10105"
  doi: "https://doi.org/10.48550/arXiv.2602.10105"
source_url: "https://arxiv.org/abs/2602.10105"
html_url: "https://arxiv.org/html/2602.10105"
pdf_url: "https://arxiv.org/pdf/2602.10105.pdf"
code_url: "https://mujc2021.github.io/deximit/"
translation_url: "https://hjfy.top/arxiv/2602.10105"
raw_refs:
  - "https://arxiv.org/html/2602.10105"
related_topics:
  - "human-video-robot-data-generation"
  - "human-to-robot-transfer"
related_syntheses:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2602.10105/src/pipeline_new.png"
images: 2
image_paths:
  - "https://arxiv.org/html/2602.10105/src/pipeline_new.png"
  - "https://arxiv.org/html/2602.10105/src/sim_compress.png"
status: analyzed
---

# DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos

## 太长不看

DexImit 的价值在于把大量单目人类操作视频转成可训练的双手灵巧机器人数据，而不是直接把 human embodiment 当成 policy 输入。它通过重建、调度、动作生成和增强四阶段，把 Internet 或生成模型产生的人类视频变成物理可行的机器人轨迹，并在零真实机器人数据下支持 sim-to-real 部署。

## 直观理解

可以把 DexImit 理解成一个 human-video-to-robot-data compiler：先从单目视频里恢复手-物体交互和世界坐标，再把长时程双手动作拆成可调度子任务，最后用力闭合抓取、关键帧运动规划和数据增强生成机器人训练集。

![主要图](https://arxiv.org/html/2602.10105/src/pipeline_new.png)

*主要图*

## 核心信息

- **作者**：Juncheng Mu、Sizhe Yang、Yiming Bao、Hojin Bae、Tianming Wei、Linning Xu、Boyi Li、Huazhe Xu、Jiangmiao Pang
- **作者单位**：Shanghai AI Laboratory; Tsinghua University; The Chinese University of Hong Kong; NVIDIA
- **来源类型**：arxiv_abs_url
- **输入来源**：https://arxiv.org/abs/2602.10105
- **原文链接**：https://arxiv.org/abs/2602.10105
- **HTML 正文**：https://arxiv.org/html/2602.10105
- **PDF 地址**：https://arxiv.org/pdf/2602.10105.pdf
- **代码地址**：https://mujc2021.github.io/deximit/
- **中英翻译地址**：https://hjfy.top/arxiv/2602.10105
- **发布日期**：2026-02-10
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** 双手灵巧操作需要大量高质量机器人示范，但真实采集成本远高于普通夹爪操作。与此同时，互联网视频和视频生成模型可以提供大量人类操作视频，覆盖工具使用、长时程任务和细粒度手部动作，因此关键问题变成如何把这些视频转成机器人可用的数据。

**问题缺口：** 直接把人手视频当作另一种 embodiment 训练策略会遇到视觉外观、动作空间和动力学差异；而现有从视频重建轨迹再生成机器人数据的方法又依赖深度或高精度重建，面对快速动作、遮挡、复杂交互和长时程双手协作时容易失败。

## 论文摘要（英文原文）

Data scarcity fundamentally limits the generalization of bimanual dexterous manipulation, as real-world data collection for dexterous hands is expensive and labor-intensive. Human manipulation videos, as a direct carrier of manipulation knowledge, offer significant potential for scaling up robot learning. However, the substantial embodiment gap between human hands and robotic dexterous hands makes direct pretraining from human videos extremely challenging. To bridge this gap and unleash the potential of large-scale human manipulation video data, we propose DexImit, an automated framework that converts monocular human manipulation videos into physically plausible robot data, without any additional information. DexImit employs a four-stage generation pipeline: (1) reconstructing hand-object interactions from arbitrary viewpoints with near-metric scale; (2) performing subtask decomposition and bimanual scheduling; (3) synthesizing robot trajectories consistent with the demonstrated interactions; (4) comprehensive data augmentation for zero-shot real-world deployment. Building on these designs, DexImit can generate large-scale robot data based on human videos, either from the Internet or video generation models. DexImit is capable of handling diverse manipulation tasks, including tool use (e.g., cutting an apple), long-horizon tasks (e.g., making a beverage), and fine-grained manipulations (e.g., stacking cups).

## 论文摘要（中文翻译）

双手灵巧操作的数据稀缺严重限制了泛化能力，因为真实机器人数据采集昂贵且依赖人工。人类操作视频天然包含任务概念和底层动作，但人手与机器人灵巧手之间存在很大的 embodiment gap，导致直接从人类视频预训练非常困难。DexImit 提出一个自动框架，在没有额外深度、相机或标注信息的条件下，把单目人类操作视频转换成物理可行的机器人数据。它使用四阶段流程：近似尺度的手-物体交互重建、子任务分解与双手调度、与演示一致的机器人轨迹合成，以及面向零样本真实部署的数据增强。系统能处理工具使用、长时程任务和细粒度操作等多类双手灵巧任务。

## 方法

**方法概述：** DexImit 是一个从单目人类操作视频自动生成双手灵巧机器人训练数据的框架，核心流程是 4D 手-物体重建、action-centric 双手调度、力闭合抓取和运动规划、以及面向 sim-to-real 的数据增强。

**核心机制：** DexImit 用四阶段 pipeline 缩小这个 gap：先用 SpatialTracker v2、Wilor、SAM3D 和 FoundationPose++ 从单目视频中恢复近似尺度的手与物体轨迹，并映射到统一世界坐标；再用 Qwen3-VL 做任务理解和子任务标注，通过 Action-Centric Scheduling 安排多手多阶段动作；随后用基于 force-closure 的抓取合成和关键帧运动规划生成机器人轨迹；最后通过物体位姿、尺度、相机和点云观测增强训练 3D Diffusion Policy。

**方法拆解：**

- 4D 重建：用手部尺寸先验估计单目深度尺度，结合手/物体分割、SAM3D 物体生成、Wilor 手姿态和 FoundationPose++ 6D 跟踪得到连续手-物体轨迹。
- 世界坐标对齐：通过桌面法向、双手初始方向和物体初始包围盒把任意视角视频映射到统一机器人工作空间。
- 双手调度：用 Qwen3-VL 把视频拆成 Task/Subaction，并用 Action-Centric Scheduling 处理单手、协作双手、并发双手和长时程任务。
- 动作生成：用 MANO prompt 和 force-closure 约束生成抓取候选，再按与人手演示的一致性排序，并通过稳定性检查选择最终 grasp；物体运动通过关键帧相对变换转成末端执行器目标。
- 数据增强：随机化物体位姿和尺度、相机位姿以及点云观测缺失/噪声，目标是在没有真实机器人数据的情况下提升零样本部署鲁棒性。

**关键要点：**

- 这篇论文把 human video 的价值从表示迁移推进到可执行数据生成：human video 可以被编译成机器人 demonstrations。
- 最关键的工程选择是不用单一端到端策略硬吃视频，而是把重建、语义调度、物理抓取和增强分层处理。
- DexImit 特别瞄准双手灵巧操作，因为这里真实数据更贵、普通 human-to-robot 路线更容易被 embodiment gap 卡住。

![方法图](https://arxiv.org/html/2602.10105/src/pipeline_new.png)

*方法图*

## 结果

**核心结果：**

- 对象轨迹重建实验中，ST2+FPose 达到 82% 成功率，高于 ST2+PCR 的 76%、DA3+PCR 的 45%、TA+RANSAC 的 38%、VGGT+PCR 的 32% 和 TA+PCR 的 11%。
- 六类仿真任务中，DexImit 在 Put Cup、Grapefruit、Fruits、Pour 上达到 100% 成功率，在 Pot 上达到 78%，在 Stack Cups 上达到 52%；RigVid 和 DexMan 在长时程或复杂双手任务上多项失败。
- 真实零样本部署评估覆盖四个 real-world meta-tasks，并比较三种数据增强 ablation，论文结论是完整增强 pipeline 对 sim-to-real 鲁棒性最关键。
- 运行时间分析显示，5s/10s/20s 输入视频总处理时间约为 173.1s/201.1s/256.6s，单视频约数分钟级，具备批量数据生成潜力。

**结果表：**

| 维度 | DexImit 结果 | 对比/含义 |
| --- | --- | --- |
| 4D 轨迹重建 | ST2+FPose 82% | 高于 ST2+PCR 76%、DA3+PCR 45%、VGGT+PCR 32% |
| 仿真短程任务 | Put Cup/Grapefruit/Fruits/Pour 均 100% | 优于 RigVid/DexMan 的不完整覆盖 |
| 长时程/细粒度任务 | Pot 78%，Stack Cups 52% | baseline 在这些任务上多项失败 |
| 数据生成效率 | 20s 视频约 256.6s | 单视频数分钟，适合规模化但仍非实时 |

![结果图](https://arxiv.org/html/2602.10105/src/sim_compress.png)

*结果图*

## 洞察

**核心 insight：**

- DexImit 提供了 human video 利用的另一条路线：不是等待大模型自然学会跨 embodiment 表示，而是把人类视频显式编译成机器人可训练数据。
- 四阶段 pipeline 的价值在于把难题拆开：几何重建负责把视频落到物理世界，VLM 负责语义分解，抓取/规划负责物理可执行性，增强负责真实部署鲁棒性。
- 这类 data-engine 方法和 VLA co-training 并不冲突：前者可以生产更接近机器人动作空间的 demonstration，后者负责把多源数据吸收到 foundation policy。

**和已有方法的关系：**

- 相对 Human-to-Robot Transfer 的 co-training 路线，DexImit 更偏显式数据生成和物理可行性约束。
- 相对 RigVid/DexMan 等从视频复现轨迹的方法，DexImit 加入近似尺度重建、双手调度和力闭合抓取，降低轨迹噪声与 long-horizon compounding error。

**可借鉴点：**

- 用手部尺寸作为单目视频尺度估计先验，是把 human video 转 robot data 的实用桥接点。
- Action-Centric Scheduling 可以作为长时程双手操作数据生成的中间表示，而不是直接从视频回归连续动作。
- VLM 不只用于理解输入视频，也可以用于自动过滤生成数据是否符合文本描述。

## 风险与判断

**局限：**

- 当前依赖 SAM3D 等刚体几何生成，不能很好处理软体或关节物体。
- 系统针对桌面双手操作，尚不支持移动操作场景。
- 长视频中多模块串联会积累误差，复杂长时程任务有时仍需要人工修正 VLM 子任务分解或重建结果。
- 严重遮挡下的 in-hand manipulation 很难从单目视频可靠恢复，当前不支持专门机制。

**适用场景：**

- 适合需要从互联网视频、人工拍摄视频或视频生成模型中扩展双手灵巧操作数据的场景。
- 适合工具使用、长时程桌面操作、双手协作和细粒度堆叠/倒水/切割等任务。

**最终判断：**

- 这篇论文值得进入 wiki，因为它把 human video 方向从 representation transfer 扩展到 robot data generation，是补齐 human-to-robot 路线的重要材料。
- 它不直接改变 VLA 基座路线的判断，但会改变对 human data 的理解：人类视频既可以作为预训练信号，也可以通过重建与规划被编译成机器人数据。

## 结果速览表

| 维度 | DexImit 结果 | 对比/含义 |
| --- | --- | --- |
| 4D 轨迹重建 | ST2+FPose 82% | 高于 ST2+PCR 76%、DA3+PCR 45%、VGGT+PCR 32% |
| 仿真短程任务 | Put Cup/Grapefruit/Fruits/Pour 均 100% | 优于 RigVid/DexMan 的不完整覆盖 |
| 长时程/细粒度任务 | Pot 78%，Stack Cups 52% | baseline 在这些任务上多项失败 |
| 数据生成效率 | 20s 视频约 256.6s | 单视频数分钟，适合规模化但仍非实时 |

## 相关主题

- human-video-robot-data-generation
- human-to-robot-transfer

## 相关页面

- [[Human Video Robot Data Generation]]
- [[Human-to-Robot Transfer]]
- [[当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据]]
