---
id: "emergence-of-human-to-robot-transfer-in-vision-language-action-models"
slug: "emergence-of-human-to-robot-transfer-in-vision-language-action-models"
title: "Emergence of Human to Robot Transfer in Vision-Language-Action Models"
type: source
material_type: "paper"
source_type: "paper"
created: "2026-05-11"
updated: "2026-05-16"
date: "2025-12-27"
authors:
  - "Simar Kareer"
  - "Karl Pertsch"
  - "James Darpinian"
  - "Judy Hoffman"
  - "Danfei Xu"
  - "Sergey Levine"
  - "Chelsea Finn"
  - "Suraj Nair"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "human-to-robot-transfer"
summary: ""
links:
  original: "https://arxiv.org/abs/2512.22414"
  arxiv: "https://arxiv.org/abs/2512.22414"
  pdf: "https://arxiv.org/pdf/2512.22414"
  project: ""
  github: ""
  hjfy: "https://hjfy.top/arxiv/2512.22414"
  doi: ""
raw_refs:
  - "https://arxiv.org/pdf/2512.22414"
related_topics:
  - "vision-language-action"
  - "human-to-robot-transfer"
related_syntheses:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2512.22414/figures/scalingAllV2.jpg"
images: 3
image_paths:
source_url: "https://arxiv.org/abs/2512.22414"
html_url: "https://arxiv.org/html/2512.22414"
pdf_url: "https://arxiv.org/pdf/2512.22414.pdf"
translation_url: "https://hjfy.top/arxiv/2512.22414"
status: analyzed
---
# Emergence of Human to Robot Transfer in Vision-Language-Action Models

## 太长不看

这篇论文的关键判断是：`human-to-robot transfer` 不是简单靠对齐技巧手工做出来的，而是会随着 VLA 预训练规模和多样性增长而“涌现”。也就是说，当机器人预训练覆盖足够多任务、场景和 embodiment 后，模型开始能够真正从 human video 中学到对机器人有用的东西。

## 直观理解

可以把这篇工作看成在问一个很实际的问题：如果我们不能直接拿大量 human video 监督机器人动作，那么能不能先把 human data 当成“另一种 embodiment”，再依赖大规模 VLA 的表示能力自己学出共享结构？作者的答案是：可以，而且这种能力和预训练多样性强相关。

![主要图](https://arxiv.org/html/2512.22414/figures/scalingAllV2.jpg)

*主要图*

## 核心信息

- **作者**：Simar Kareer 等
- **原文链接**：https://arxiv.org/abs/2512.22414
- **PDF 地址**：https://arxiv.org/pdf/2512.22414
- **发布日期**：2025-12-27
- **主题域**：physical-embodied-intelligence

## 背景与问题

**动机：** Human video 覆盖范围大、便宜、自然，但直接拿来训练机器人策略一直很难，因为 humans 和 robots 在外观、动力学和动作空间上差异太大。

**问题缺口：** 以往方法往往要显式设计 human-robot 映射。作者则想验证一种更像 LLM scaling law 的观点：当 VLA 预训练足够大、足够多样时，human-to-robot transfer 会不会自然出现。

## 论文摘要（英文原文）

Vision-language-action (VLA) models can enable broad open world generalization, but require large and diverse datasets. It is appealing to consider whether some of this data can come from human videos, which cover diverse real-world situations and are easy to obtain. However, it is difficult to train VLAs with human videos alone, and establishing a mapping between humans and robots requires manual engineering and presents a major research challenge. Drawing inspiration from advances in large language models, where the ability to learn from diverse supervision emerges with scale, we ask whether a similar phenomenon holds for VLAs that incorporate human video data. We introduce a simple co-training recipe, and find that human-to-robot transfer emerges once the VLA is pre-trained on sufficient scenes, tasks, and embodiments. Our analysis suggests that this emergent capability arises because diverse pretraining produces embodiment-agnostic representations for human and robot data. We validate these findings through a series of experiments probing human to robot skill transfer and find that with sufficiently diverse robot pre-training our method can nearly double the performance on generalization settings seen only in human data.

## 论文摘要（中文翻译）

VLA 能支持广泛的开放世界泛化，但需要大规模多样化数据。一个自然问题是：这些数据能否部分来自 human video？然而仅用 human video 训练 VLA 很困难，而且建立 human 与 robot 之间的映射通常需要大量手工工程。作者借鉴大语言模型中的“能力随规模涌现”现象，提出一个问题：对包含 human video 的 VLA，这种现象是否也成立？他们提出一种简单的 co-training recipe，并发现当 VLA 在足够多样的场景、任务和 embodiment 上预训练后，human-to-robot transfer 能力会涌现出来。分析表明，这种能力来自于多样预训练所形成的 embodiment-agnostic 表示。实验进一步显示，在只出现在 human data 中的泛化设置上，加入 human data 几乎可以把性能翻倍。

## 方法

**方法概述：** 这篇工作不是靠显式人机对齐工程去解决 transfer，而是提出一个更简单的 co-training recipe：把 human video 视作额外 embodiment，并在与机器人数据相近的训练目标下联合微调，再观察能力是否会随着预训练多样性而涌现。

**核心机制：**

- 把 human video 当作额外 embodiment 参与 co-training
- 同时使用高层 sub-task prediction 和低层 action prediction
- 用只存在于 human data 的 generalization benchmark 验证 transfer 是否真的发生
- 分析 latent representation 是否随着 pretraining diversity 增长而对齐

**方法拆解：**

- 对 human data，作者使用 3D hand tracks 和 dense language annotations 构造与机器人数据近似的监督目标
- co-finetuning 时混合 human data 与相关 robot data
- 预训练多样性被系统控制：从较弱 pretraining 到覆盖 scenes/tasks/embodiments 的更强预训练
- 然后比较 human+robot finetuning 与 robot-only finetuning 在 unseen scene/object/task 设置下的差异

![方法图](https://arxiv.org/html/2512.22414/figures/arch.jpg)

*方法图*

**关键要点：**

- 这篇工作关心的不是“人类视频有没有用”，而是“在什么条件下开始有用”
- 预训练多样性被当成 transfer emergence 的主要解释变量
- representation alignment 被拿来解释能力涌现，而不是只看终端任务分数

## 结果

**核心结果：**

- human-to-robot transfer 随着 robot pretraining diversity 增长而显著增强
- 在 scene、object、task 三类 generalization benchmark 上，co-training 带来明显提升
- 论文给出的典型数字包括：Spice `32% -> 71%`，dresser `25% -> 50%`，bussing `53 -> 63`
- 在 egg sorting 任务上，robot-only policy 只有 `57%` sorting accuracy，而 co-trained 后提升到 `78%`
- 作者认为这说明 transfer 不是手工对齐的偶然产物，而是随规模与多样性增长而涌现出的能力

![结果图](https://arxiv.org/html/2512.22414/figures/taskPerf.jpg)

*结果图*

**结果表：**

| 维度 | 结论 |
| --- | --- |
| transfer 触发条件 | 足够多样的 robot pretraining |
| 验证维度 | scene / object / task generalization |
| 代表收益 | 多项任务显著提升，部分接近翻倍 |
| 表示解释 | 更强的 embodiment-agnostic representation |

## 洞察

**核心 insight：**

- 这篇论文真正重要的地方，在于它把 “scaling brings emergence” 从 LLM 语境移到了 embodied learning。它不是简单证明 human video useful，而是证明“随着预训练足够多样，模型开始自己学会利用 human data”。

**和已有方法的关系：**

- 相对显式 human-robot alignment 路线，它更依赖 representation 自然形成
- 相对只看 robot teleoperation 的路线，它尝试把更廉价、更广覆盖的人类数据吸纳进来
- 相对单纯追求更大数据量，它更强调 diversity of scenes, tasks, embodiments

**可借鉴点：**

- 对具身智能来说，多样性可能比单一目标域精调更关键
- 人类视频不一定要先被完全“翻译成机器人动作”才有价值
- 这条路线很适合和 `cross-embodiment transfer`、`world-model / VLA pretraining scale` 一起看

## 风险与判断

**局限：**

- 结论依赖非常强的预训练多样性，普通团队复制门槛高
- 所谓“涌现”也可能部分来自大规模 remix，而不一定完全意味着更深层抽象理解
- human data 与 robot data 的融合仍然需要 carefully designed training recipe，不是零成本接入

**适用场景：**

- 关注 human video 利用、cross-embodiment transfer、数据扩展性的研究
- 想研究具身智能中 scaling law 类现象的场景
- 想把 “human data as another embodiment” 作为系统设计前提的方向

**最终判断：** 这篇是 `human-to-robot transfer` 方向里很值得保留的强论文，也很适合作为你后续 topic 页的种子。

## 结果速览表

| 维度 | 结论 |
| --- | --- |
| 研究问题 | human-to-robot transfer 是否随规模涌现 |
| 核心机制 | co-training + diverse robot pretraining |
| 关键发现 | 足够多样预训练后 transfer 才明显出现 |
| 解释变量 | embodiment-agnostic representation |

## 相关主题

- vision-language-action
- human-to-robot-transfer

## 相关页面

- [[Vision-Language-Action]]
- [[Human-to-Robot Transfer]]
- [[当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
