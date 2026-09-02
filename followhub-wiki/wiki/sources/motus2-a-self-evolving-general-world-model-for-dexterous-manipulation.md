---
id: "motus2-a-self-evolving-general-world-model-for-dexterous-manipulation"
slug: "motus2-a-self-evolving-general-world-model-for-dexterous-manipulation"
title: "Motus2: A Self-Evolving General World Model for Dexterous Manipulation"
type: source
material_type: "paper"
source_type: "paper"
created: "2026-09-02"
updated: "2026-09-02"
date: "2026-08-31"
authors:
  - "Hongzhe Bi"
  - "Zihao Zhou"
  - "Yihang Tang"
  - "Jingrui Pang"
  - "Shuhe Huang"
  - "Haitian Liu"
  - "Runqing Wang"
  - "Shuai Huang"
  - "Yichen Wang"
  - "Yiming Cheng"
  - "Ruowen Zhao"
  - "Zhenghua Li"
  - "Hengkai Tan"
  - "Xiaolong Liu"
  - "Jinhui Wan"
  - "Jiabao Liu"
  - "Min Zhao"
  - "Fan Bao"
  - "Jun Zhu"
affiliation: "GensPI; Tsinghua University; BUAA; BIT"
related_organizations:
  - "GensPI"
  - "Tsinghua University"
  - "BUAA"
  - "BIT"
related_companies: []
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "robot-foundation-model"
summary: ""
links:
  original: "https://arxiv.org/abs/2608.30237"
  arxiv: "https://arxiv.org/abs/2608.30237"
  pdf: "https://arxiv.org/pdf/2608.30237"
  project: "https://motus-robotics.github.io/motus2"
  github: ""
  hjfy: "https://translate.google.com/?sl=en&tl=zh&text=Motus2%3A%20A%20Self-Evolving%20General%20World%20Model%20for%20Dexterous%20Manipulation&op=translate"
  doi: "https://doi.org/10.48550/arXiv.2608.30237"
raw_refs:
  - "https://arxiv.org/html/2608.30237v1"
related_topics:
  - "vision-language-action"
  - "Long-Horizon Memory for Robot Policies"
  - "Human-to-Robot Transfer"
related_syntheses:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2608.30237v1/motus2_overview.png"
images: 1
image_paths:
source_url: "https://arxiv.org/abs/2608.30237"
html_url: "https://arxiv.org/abs/2608.30237"
pdf_url: "https://arxiv.org/pdf/2608.30237"
translation_url: "https://translate.google.com/?sl=en&tl=zh&text=Motus2%3A%20A%20Self-Evolving%20General%20World%20Model%20for%20Dexterous%20Manipulation&op=translate"
status: analyzed
---
# Motus2: A Self-Evolving General World Model for Dexterous Manipulation

## 太长不看

Motus2 的重点不是再做一个更强的动作策略，而是把动作、未来预测和价值评估合进同一个共享模型里，让机器人能靠闭环自我改进。

## 直观理解

它像给灵巧操作装了一个“先出手、再想象后果、再判断好坏”的一体化大脑：先提议动作块，再预测这步会发生什么，最后用价值头决定哪条分支更值得走。

## 核心信息

- **作者**：Hongzhe Bi、Zihao Zhou、Yihang Tang、Jingrui Pang、Shuhe Huang、Haitian Liu、Runqing Wang、Shuai Huang、Yichen Wang、Yiming Cheng、Ruowen Zhao、Zhenghua Li、Hengkai Tan、Xiaolong Liu、Jinhui Wan、Jiabao Liu、Min Zhao、Fan Bao、Jun Zhu
- **作者单位**：GensPI；Tsinghua University；BUAA；BIT
- **来源类型**：arxiv_html_url
- **输入来源**：https://arxiv.org/abs/2608.30237
- **原文链接**：https://arxiv.org/abs/2608.30237
- **HTML 正文**：https://arxiv.org/abs/2608.30237
- **PDF 地址**：https://arxiv.org/pdf/2608.30237
- **项目页**：https://motus-robotics.github.io/motus2
- **中英翻译地址**：https://translate.google.com/?sl=en&tl=zh&text=Motus2%3A%20A%20Self-Evolving%20General%20World%20Model%20for%20Dexterous%20Manipulation&op=translate
- **发布日期**：2026-08-31
- **主题域**：physical-embodied-intelligence

## 背景与问题

**动机：** 灵巧操作要求模型在自遮挡、接触突变和长时序反馈里持续判断动作后果，仅靠模仿示范很难知道“什么动作更好”，而单纯预测未来又不知道“哪种未来值得追求”。这篇工作想把感知、预测、行动、评估和改进放进一个统一系统里，让机器人不只会执行，还能从结果里继续变强。

**问题缺口：** 现有 world model 往往只是给模拟器外挂一个动作头，policy、simulator 和 evaluator 彼此分离，无法形成真正的闭环改进。Motus2 要解决的是：如何在共享参数里同时实现动作生成、动作后果预测和价值评估，并把失败与次优交互也变成可学习信号。

## 论文摘要（英文原文）

General embodied agents should perceive, predict, act, evaluate, and improve within a unified system. World models have shown great promise in building such agents, yet existing models typically append an action output head to a world simulator, without coupling them into a closed decision-and-learning loop for policy improvement. We present Motus2, a self-evolving general world model for dexterous manipulation. Motus2 advances world modeling through model scaling and data scaling. For model scaling, a single model with shared weights exposes three control interfaces: a policy (world-action model), a simulator (action-conditioned world model), and an evaluator (value model). The policy proposes candidate action chunks, the simulator predicts their visual consequences, and the evaluator assesses the predicted outcomes. Their coupling forms a closed decision-and-learning loop for policy improvement. This formulation uses curated expert demonstrations for action learning, while failed and suboptimal interactions provide valuable evidence for dynamics modeling and value learning. For data scaling, Motus2 progresses from large-scale monocular egocentric data to synchronized stereo egocentric data, followed by robot-domain adaptation with robot trajectories and supplementary human-robot alignment data. Motus2 further studies global-autoregressive and hybrid-memory extensions of its sliding-window context, adds tactile feedback for contact-aware control, and is instantiated on a fully biomimetic platform with stereo vision, dual arms, dual dexterous hands, and tactile sensing. Together, egocentric data scaling and closed-loop general world model scaling provide a general path toward self-evolving dexterous manipulation.

## 论文摘要（中文翻译）

通用具身智能体应该在统一系统中同时完成感知、预测、行动、评估与持续改进。世界模型在构建这类智能体方面很有潜力，但现有模型通常只是给 world simulator 额外接一个动作输出头，并没有把它们耦合成一个用于策略提升的闭环决策与学习系统。Motus2 提出一种面向灵巧操作的自进化通用世界模型。Motus2 通过模型扩展和数据扩展推进 world modeling：在模型侧，同一共享参数同时暴露三种控制接口——policy（world-action model）、simulator（action-conditioned world model）和 evaluator（value model）；policy 提议候选动作块，simulator 预测其视觉后果，evaluator 评估预测结果，这三者耦合成一个闭环，用于策略改进。该框架用高质量专家示范学习动作，而失败和次优交互则为动力学建模与价值学习提供有效证据。在数据侧，Motus2 从大规模单目第一视角数据出发，进一步扩展到同步双目第一视角数据，再迁移到机器人域轨迹和补充的人机对齐数据；同时还研究了滑窗上下文的 global-autoregressive 与 hybrid-memory 扩展，引入触觉反馈用于接触感知控制，并在具备双目、双臂、双灵巧手和触觉传感的仿生平台上实现。

## 方法

**方法概述：** Motus2 把同一个视频-动作骨干复用成 policy、simulator 和 evaluator 三个接口，再用 action-first 的因果掩码和分层监督把示范、失败、次优轨迹分别路由到能监督的部分，最后通过规划和模型式强化学习把评估分数反向变成策略更新。

**核心机制：** 关键不在于把三个头简单并排，而在于它们共享参数、共享表示、共享历史上下文，但读取权限不同：policy 只能看当前上下文来出动作，simulator 在给定动作后预测未来，evaluator 再看动作和预测结果估值。这样模型既能做 test-time 的 Best-of-N 规划，也能把 outcome value 变成训练信号，形成真正的自我改进回路。

**方法拆解：**

- 先用大规模 egocentric 人类数据预训练共享的视频-动作骨干，再进入机器人域 mid-training。
- 用 action-first 掩码把当前动作、未来视觉和价值查询组织成三种接口，避免动作头偷看未来信息。
- 用 trajectory-dependent loss gating 区分示范、失败和次优轨迹：示范监督动作，其他轨迹主要监督动力学和价值。
- 结合触觉专家、global-autoregressive 和 hybrid-memory 扩展，增强长时序和接触丰富场景下的控制能力。

**关键要点：**

- 失败和次优交互不是噪声，而是学习动力学与价值的有效数据。
- 真正的创新是把 world model 从“预测器”升级成“会自我批改的控制系统”。

![方法图](https://arxiv.org/html/2608.30237v1/motus2_overview.png)

*方法图*

## 结果

**核心结果：**

- 论文展示了 policy / simulator / evaluator 三接口在同一共享模型中的统一实现。
- 数据扩展从单目到双目、再到机器人域适配，强调 egocentric 数据规模和视角质量对灵巧操作的重要性。
- 加入触觉、长时序记忆和仿生平台后，模型更适合接触丰富、部分可观测的操作任务。

**结果表：** | 方向 | 作用 |
| --- | --- |
| Policy | 提议动作块 |
| Simulator | 预测动作后果 |
| Evaluator | 评估任务进展 |

## 洞察

**核心 insight：** Motus2 的意义不只是“世界模型更大”，而是把世界模型变成一个能从结果里反向修正自身策略的闭环控制系统。

**和已有方法的关系：** 相比只做动作模仿的机器人基座，它把失败、次优和预测价值一起纳入训练；相比只做未来预测的 world model，它真正补上了“评估—改进”这一环。

**可借鉴点：** 如果后续要做机器人知识库，这种 policy / simulator / evaluator 的拆法很适合做统一分析模板。

## 风险与判断

**局限：**

- 系统复杂度高，依赖精细的掩码、路由和数据分层；而且论文主要围绕灵巧操作和仿生平台，泛化到更广任务还需要验证。

**适用场景：**

- 接触丰富、部分可观测、需要长时序反馈修正的机器人灵巧操作。

**最终判断：**

- 这是把 world model 推向“可自我改进控制器”的一篇代表性工作。

## 结果速览表

| 方向 | 作用 |
| --- | --- |
| Policy | 提议动作块 |
| Simulator | 预测动作后果 |
| Evaluator | 评估任务进展 |

## 相关主题

- vision-language-action
- Long-Horizon Memory for Robot Policies
- Human-to-Robot Transfer

## 相关页面

- [[Vision-Language-Action]]
- [[Long-Horizon Memory for Robot Policies]]
- [[Human-to-Robot Transfer]]
- [[当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据]]
