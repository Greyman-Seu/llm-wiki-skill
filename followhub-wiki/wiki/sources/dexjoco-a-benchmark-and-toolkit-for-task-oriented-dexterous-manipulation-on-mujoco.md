---
id: "dexjoco-a-benchmark-and-toolkit-for-task-oriented-dexterous-manipulation-on-mujoco"
slug: "dexjoco-a-benchmark-and-toolkit-for-task-oriented-dexterous-manipulation-on-mujoco"
title: "DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo"
type: source
material_type: "paper"
source_type: "paper"
source_kind: "arxiv_abs_url"
source_input: "https://arxiv.org/abs/2605.16257"
created: "2026-06-26"
updated: "2026-06-26"
date: "2026-05-15"
publish_date: "2026-05-15"
authors:
  - "Hanwen Wang"
  - "Weizhi Zhao"
  - "Xiangyu Wang"
  - "Siyuan Huang"
  - "He Lin"
  - "Boyuan Zheng"
  - "Rongtao Xu"
  - "Gang Wang"
  - "Yao Mu"
  - "He Wang"
  - "Lue Fan"
  - "Hongsheng Li"
  - "Zhaoxiang Zhang"
  - "Tieniu Tan"
affiliation: "NLPR & MAIS, CASIA; SJTU; MBZUAI; Beijing Institute of Basic Medical Sciences; PKU & Galbot; CUHK"
related_organizations:
  - "NLPR & MAIS, CASIA"
  - "Shanghai Jiao Tong University"
  - "MBZUAI"
  - "Beijing Institute of Basic Medical Sciences"
  - "Peking University"
  - "Galbot"
  - "The Chinese University of Hong Kong"
related_companies:
  - "Galbot"
domains:
  - "Physical/Embodied Intelligence"
domain: "physical-embodied-intelligence"
primary_domain_slug: "physical-embodied-intelligence"
domain_slugs:
  - "physical-embodied-intelligence"
tags:
  - "dexterous-manipulation-benchmark"
keywords:
  - "dexterous hand"
  - "benchmark"
  - "MuJoCo"
  - "teleoperation"
  - "VLA evaluation"
summary: "DexJoCo 用 11 个功能型 MuJoCo 灵巧手任务、低成本手套遥操作系统和 1.1K 人类示范，补上了灵巧手任务导向评测与现代策略/VLA 评测工具链的缺口。"
links:
  original: "https://arxiv.org/abs/2605.16257"
  arxiv: "https://arxiv.org/abs/2605.16257"
  pdf: "https://arxiv.org/pdf/2605.16257.pdf"
  project: "https://dexjoco.github.io"
  github: ""
  hjfy: "https://hjfy.top/arxiv/2605.16257"
  doi: "https://doi.org/10.48550/arXiv.2605.16257"
source_url: "https://arxiv.org/abs/2605.16257"
html_url: "https://arxiv.org/html/2605.16257v1"
pdf_url: "https://arxiv.org/pdf/2605.16257.pdf"
code_url: "https://dexjoco.github.io"
translation_url: "https://hjfy.top/arxiv/2605.16257"
raw_refs:
  - "https://arxiv.org/html/2605.16257v1"
  - "https://dexjoco.github.io"
related_topics:
  - "vision-language-action"
  - "human-to-robot-transfer"
related_syntheses:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2605.16257v1/x1.png"
images: 3
image_paths:
  - "https://arxiv.org/html/2605.16257v1/x1.png"
  - "https://arxiv.org/html/2605.16257v1/x2.png"
  - "https://arxiv.org/html/2605.16257v1/x5.png"
status: analyzed
---

# DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo

## 太长不看

DexJoCo 的价值不在于提出一个新策略模型，而在于把“灵巧手到底比夹爪强在哪里、现有 VLA/模仿学习策略在哪些灵巧交互上失败”变成了可系统测量的问题。它提供 11 个功能型 MuJoCo 任务、1.1K 条人类示范、低成本手套遥操作采集系统，以及面向视觉随机化、动力学随机化、多任务训练和 action-head 适配的评测工具链。对后续灵巧手机器人学习来说，这篇更像基础设施论文：它给出了一个比 pick-and-place 更接近真实灵巧操作的压力测试场。

## 直观理解

可以把 DexJoCo 理解成一个“灵巧手版 LIBERO / CALVIN”，但任务设计刻意避开简单抓取搬运，转向浇花、敲钉子、折眼镜、开微波炉、解锁 iPad、汉诺塔、装配、拍照等需要手指协调、接触反馈、顺序约束和双手分工的场景。作者不仅搭了仿真环境，还配了一套用 Rokoko 手套和 Vive Tracker 采集人类示范的低成本系统，再把这些数据转成 LeRobot / Diffusion Policy 等现代策略可以消费的格式。它真正想回答的是：当任务从“把东西拿起来”变成“用手完成一个有功能语义的动作”时，当前策略到底卡在哪里。

![DexJoCo overview](https://arxiv.org/html/2605.16257v1/x1.png)

*DexJoCo 总览：11 个任务、1.1K 人类示范、领域随机化回放与策略评测工具链。*

## 核心信息

- **作者**：Hanwen Wang、Weizhi Zhao、Xiangyu Wang、Siyuan Huang、He Lin、Boyuan Zheng、Rongtao Xu、Gang Wang、Yao Mu、He Wang、Lue Fan、Hongsheng Li、Zhaoxiang Zhang、Tieniu Tan
- **作者单位**：NLPR & MAIS, CASIA; SJTU; MBZUAI; Beijing Institute of Basic Medical Sciences; PKU & Galbot; CUHK
- **来源类型**：arxiv_abs_url
- **输入来源**：https://arxiv.org/abs/2605.16257
- **原文链接**：https://arxiv.org/abs/2605.16257
- **HTML 正文**：https://arxiv.org/html/2605.16257v1
- **PDF 地址**：https://arxiv.org/pdf/2605.16257.pdf
- **项目页**：https://dexjoco.github.io
- **中英翻译地址**：https://hjfy.top/arxiv/2605.16257
- **发布日期**：2026-05-15
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** 机器人操作社区已经有不少成熟的夹爪平台数据集和基准，但人类级操作往往依赖灵巧手：按按钮、挤压夹子、折叠眼镜、双手握持与插装、连续步骤执行等都不是简单开合夹爪能自然完成的。要推动这类能力，研究者需要标准化任务、可复现环境、统一数据格式和能暴露失败模式的评测协议。

**问题缺口：** 现有灵巧手 benchmark 往往有四类不足：一是只考虑 hand-only 设置，脱离真实机械臂-手系统；二是任务集中在 in-hand manipulation 或 pick-and-place，不能凸显灵巧手相对夹爪的功能优势；三是缺少好用的人类示范采集系统，导致数据要么靠 RL 生成、要么行为不自然；四是缺乏统一语言指令与现代 VLA/模仿学习评测格式，难以比较不同策略。

**DexJoCo 的定位：** 这篇论文把问题定位为“task-oriented dexterous manipulation”：不是单纯让手指动起来，而是让灵巧手在有功能语义的场景里完成任务。它更接近一个研究基础设施，目标是让后续模型在相同任务、相同数据和相同随机化设置下暴露真实瓶颈。

## 论文摘要（英文原文）

Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning.

## 论文摘要（中文翻译）

实现接近人类水平的操作能力，需要机器人灵巧手能够处理复杂物体交互；而推进这类能力又需要标准化 benchmark 来进行系统评测。然而，现有灵巧操作基准缺少能够体现灵巧手相对平行夹爪独特能力的任务，也缺乏完整评测流水线。本文提出 DexJoCo，一个面向任务导向灵巧操作的 benchmark 与工具包，包含 11 个有功能语义的任务，用于评估工具使用、双手协调、长时程执行和推理能力。作者开发了一个低成本数据采集系统，并在这些任务上采集 1.1K 条轨迹，同时支持领域随机化来评估鲁棒性。论文在视觉与动力学随机化、多任务训练、action-head 适配等多种设置下评测现代模型，通过系统实验总结出当前灵巧操作策略的重要局限，为未来灵巧手机器人学习指出关键挑战。

## 方法

**方法概述：** DexJoCo 由四层组成：MuJoCo 中的机械臂-灵巧手任务环境、低成本人类示范采集系统、可转换为主流格式的数据管线，以及对 ACT、Diffusion Policy、π0.5、GR00T N1.5 等策略的统一评测协议。

![DexJoCo pipeline](https://arxiv.org/html/2605.16257v1/x2.png)

*DexJoCo pipeline：任务构建、遥操作采集、轨迹增强、格式转换和策略评测。*

**1. 机器人与观测/动作设定。** DexJoCo 基于 MuJoCo，机器人由 Rethink Robotics mount、Franka Panda 机械臂和 Allegro Hand 组成。观测包含第三人称与腕部 RGB/RGB-D、交互物体 pose、机器人运动状态、末端执行器 pose 和手部关节角。动作空间采用目标绝对末端位姿与 Allegro Hand 目标绝对关节角，这使数据既能表达机械臂移动，也能表达高维手指控制。

**2. 低成本遥操作采集系统。** 作者用 Rokoko Smartgloves 捕捉手部运动，用 HTC Vive Tracker 与 Base Station 捕捉腕部/末端位姿，整体成本约 2,300 美元。手部 retargeting 使用 GeoRT 思路，将人类 fingertip keypoints 映射到 Allegro Hand 关节配置，目标包括保持指尖运动方向、扩大工作空间覆盖、保持均匀灵敏度、保留 pinch 行为以及避免自碰撞。这个设计的重点是：不用昂贵动捕房，也尽量避免 RGB 手势估计的遮挡问题。

**3. 任务设计。** 每个任务定义为交互物体集合与目标约束集合，目标约束包括顺序/时序、目标 pose、关节状态和接触条件。任务只有在这些约束同时满足时才算成功。任务设计遵循四个原则：功能性交互、依赖灵巧性、长时程组合性、双手协调。具体任务包括 Hammer Nail、Click Mouse、Pick Bucket、Pinch Tongs、Fold Glasses、Water Plant，以及 Unlock iPad、Hanoi、Assembly、Microwave、Photograph 等双手任务。

![DexJoCo tasks](https://arxiv.org/html/2605.16257v1/x5.png)

*任务设计覆盖工具使用、按钮/铰链交互、双手协作、插装与长时程流程。*

**4. 领域随机化。** DexJoCo 支持对象位置、桌面高度、第三人称相机位姿、光照方向/颜色、桌面纹理等随机化。一个关键设计是通过轨迹 replay 做视觉增强：同一条人类示范可以在不同渲染条件下重放，用于测试视觉鲁棒性，而不是只在固定场景上过拟合。

**5. 策略训练和评测。** 论文评测了 DP-Transformer、DP-CNN、ACT、π0.5 和 GR00T N1.5。数据可以转换到 LeRobot Dataset v3.0 和 Diffusion Policy Zarr 等格式，评测采用 server-client 部署框架。实验设置还包括视觉随机化、动力学随机化、多任务训练，以及对 VLA action head 是否保留预训练权重的比较。

## 结果

**核心结果：** DexJoCo 对当前策略非常难。即便是预训练 VLA 或强模仿学习基线，在双手、插装、按钮点击、铰链挤压和长时程记忆任务上也会系统失败。视觉随机化会显著降低成功率，说明这些策略仍然容易依赖固定外观/视角；而语言泛化实验显示，VLA 在解锁 iPad 任务中没有真正学会语言条件控制，而是倾向固定动作偏置。

**关键实验信号：**

- 在只随机化物体位置和桌面高度的 `rand-obj` 设置下，平均成功率最高的是 π0.5（52.5%），DP-Transformer 也达到 50.4%，DP-CNN 为 47.6%，GR00T N1.5 为 40.2%，ACT 为 35.5%。
- 在额外加入相机、光照、纹理的 `rand-full` 视觉随机化后，所有模型都明显下降：π0.5 从 52.5% 降到 34.1%，DP-Transformer 从 50.4% 降到 20.0%，DP-CNN 从 47.6% 降到 28.4%。
- DP-CNN 在 Unlock iPad 和 Pinch Tongs 上异常强，作者推测这可能来自 FiLM 方式注入观测，比 self/cross attention 更利于精细视觉交互。
- 失败模式集中在按钮、插入、挤压/释放和记忆：模型能拿起设备或移动物体，但经常按不到目标按钮；能抓住夹子但不能连续挤压释放；能把热狗放进微波炉但又随手带出来。
- 多任务训练在相同训练步数下会退化：DP-Transformer 在所有任务下降，说明当前容量/训练设置还不能自然吸收这些异质灵巧任务。
- 动力学随机化下，π0.5 平均比 DP-Transformer 更稳，提示大规模预训练对扰动有帮助，但并不能解决高维灵巧动作空间本身的瓶颈。
- 保留预训练 action head 比完全随机初始化更好，说明 VLA 的动作头权重仍有迁移价值；但由于大多数预训练来自夹爪数据，高维灵巧手动作仍存在 embodiment mismatch。

**结果速览表：**

| 设置 / 模型 | DP-T | DP-C | ACT | π0.5 | GR00T N1.5 | 主要含义 |
|---|---:|---:|---:|---:|---:|---|
| rand-obj 平均成功率 | 50.4 | 47.6 | 35.5 | 52.5 | 40.2 | 任务本身已经有挑战，但强模型可在部分单臂任务上达到较高成功率 |
| rand-full 平均成功率 | 20.0 | 28.4 | 22.7 | 34.1 | 30.5 | 视觉随机化造成普遍退化，外观/视角鲁棒性不足 |
| 困难双手任务 | 多数模型低成功 | 部分精细交互较强 | 偏弱 | 相对较强但仍失败 | 不稳定 | 灵巧手长时程和双手协调不是现有 VLA 的自然强项 |
| 语言泛化 | — | — | — | 失败 | — | 解锁任务中表现更像固定动作偏置，而非真实语言条件控制 |

## 洞察

**1. Benchmark 的任务语义比模型榜单更重要。** DexJoCo 最有价值的部分不是 π0.5 比 DP-T 高多少，而是它把灵巧手的关键能力拆成可以测的失败面：按钮点击、铰链/夹子、插装、双手异步分工、长时程步骤、视觉鲁棒性和语言条件控制。这些正是普通夹爪 benchmark 很难暴露的问题。

**2. 灵巧手 foundation model 不能只继承夹爪 VLA。** 论文讨论指出，当前 VLA 多在夹爪数据上预训练，动作空间与 Allegro Hand 这类高维灵巧手不匹配。即使视觉语言骨干很强，action head 也未必能表达高维手指耦合。后续可能需要 hand-centric pretraining、embodiment-aware action representation 或更明确的手部关节/接触建模。

**3. 视觉-only 对接触密集任务不够。** DexJoCo 的失败案例很清楚：模型常常“看见了物体”，但不知道按钮有没有按下、夹子有没有挤压到位、插装是否真正对齐。仅靠 RGB 和 proprioception 可能不足以覆盖接触力、滑移、局部形变等信息；触觉或接触状态可能是下一阶段精细操作的必要模态。

**4. 对数据生成路线也有启发。** 这篇和 DexImit 互补：DexImit 解决如何从人类视频生成灵巧操作数据，DexJoCo 则提供标准任务和评测压力场。一个自然方向是用 DexImit/人类视频生成方法扩充 DexJoCo 这类功能型任务，再观察模型是否真的解决按钮、插装和双手协作。

**可借鉴点：**

- 做灵巧手 benchmark 时，应优先设计“功能完成条件”，而不是只定义末端位姿误差。
- 数据采集系统可以采用低成本手套 + tracker + retargeting，而不必一开始就依赖昂贵动捕房。
- 评测协议应同时包含视觉随机化、动力学随机化和 action-head adaptation，否则很容易高估模型能力。
- failure taxonomy 应成为 benchmark 的一部分：成功率之外，还要记录精细动作失败、插入失败、记忆失败、交互元素忽略等模式。

## 风险与判断

**局限：**
- DexJoCo 仍是 MuJoCo 仿真 benchmark，真实机器人部署中的接触、摩擦、传感器噪声、材质形变和执行延迟没有被完整覆盖。
- 数据规模为 1.1K 条轨迹，对训练大规模通用灵巧手策略来说仍偏小，更适合评测和方法验证，而不是单独支撑 foundation model 训练。
- 任务虽然比 pick-and-place 更丰富，但仍集中在桌面场景和固定机器人/手配置上，对移动操作、软体物体、复杂工具链和开放世界任务覆盖有限。
- 论文暴露了语言泛化失败，但没有提供解决方法；它更像诊断工具，而不是完整模型方案。

**适用场景：**
- 用作灵巧手模仿学习、VLA action head 适配、视觉鲁棒性、双手协调和接触密集操作的统一评测场。
- 用作新数据生成/遥操作采集方法的下游验证，例如从人类视频生成轨迹后在 DexJoCo 任务上训练策略。
- 用作分析策略失败模式的工具，尤其适合研究按钮、铰链、插装、长时程和双手任务。

**最终判断：**
- 这是一篇值得放进知识库的基础设施论文。它本身不解决灵巧手策略学习，但清楚定义了“哪些能力还没解决”，并给出可复现实验场。对 FollowHub 的 embodied intelligence 线索来说，DexJoCo 可以作为评测基准节点，连接 OpenVLA/π0.5/GR00T 等 VLA 模型、DexImit 这类数据生成工作，以及未来 hand-centric foundation model 方向。

## 结果速览表

| 维度 | DexJoCo 设计 | 为什么重要 |
|---|---|---|
| 任务 | 11 个功能型灵巧操作任务，覆盖工具使用、双手协调、长时程、推理 | 避免 benchmark 退化为简单抓取搬运 |
| 数据 | 1.1K 条人类示范轨迹 | 为模仿学习和 VLA 评测提供统一数据 |
| 采集 | Rokoko 手套 + Vive Tracker，约 2,300 美元 | 降低灵巧手数据采集门槛 |
| 随机化 | 对象、桌高、相机、光照、纹理、动力学 | 测试视觉与动力学鲁棒性 |
| 基线 | DP-T、DP-C、ACT、π0.5、GR00T N1.5 | 覆盖从经典模仿学习到现代 VLA 的策略类型 |
| 主要发现 | 视觉随机化、双手任务、精细交互、语言泛化仍是瓶颈 | 指向后续 hand-centric pretraining、多模态接触感知和更强时序记忆 |

## 相关主题

- [[Vision-Language-Action]]：DexJoCo 是评测 VLA 是否真正适配灵巧手高维动作空间的重要压力测试。
- [[Human-to-Robot Transfer]]：低成本手套遥操作和 retargeting 体现了从人手示范到机器人灵巧手数据的另一条路线。
- [[DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos]]：DexImit 偏数据生成，DexJoCo 偏任务基准和评测，两者共同指向灵巧操作数据与 benchmark 的基础设施化。
