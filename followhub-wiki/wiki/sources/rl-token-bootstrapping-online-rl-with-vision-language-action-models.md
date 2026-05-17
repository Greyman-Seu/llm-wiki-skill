---
id: "rl-token-bootstrapping-online-rl-with-vision-language-action-models"
slug: "rl-token-bootstrapping-online-rl-with-vision-language-action-models"
title: "RL Token: Bootstrapping Online RL with Vision-Language-Action Models"
type: source
material_type: "paper"
source_type: "paper"
created: "2026-05-11"
updated: "2026-05-17"
date: "2026-04-24"
authors:
  - "Charles Xu"
  - "Jost Tobias Springenberg"
  - "Michael Equi"
  - "Ali Amin"
  - "Adnan Esmail"
  - "Sergey Levine"
  - "Liyiming Ke"
affiliation: "Physical Intelligence"
related_organizations:
  - "Physical Intelligence"
related_companies:
  - "Physical Intelligence"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "online-rl"
summary: ""
links:
  original: "https://arxiv.org/abs/2604.23073"
  arxiv: "https://arxiv.org/abs/2604.23073"
  pdf: "https://www.pi.website/download/rlt.pdf"
  project: ""
  github: ""
  hjfy: "https://hjfy.top/arxiv/2604.23073"
  doi: ""
raw_refs:
  - "https://www.pi.website/download/rlt.pdf"
related_topics:
  - "vision-language-action"
  - "online-rl-for-vla"
related_syntheses:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2604.23073v2/x1.png"
images: 3
image_paths:
source_url: "https://arxiv.org/abs/2604.23073"
html_url: "https://arxiv.org/html/2604.23073"
translation_url: "https://hjfy.top/arxiv/2604.23073"
status: analyzed
---
# RL Token: Bootstrapping Online RL with Vision-Language-Action Models

## 太长不看

这篇工作最重要的点，是给 VLA 和在线 RL 之间找到了一个足够轻量的接口。作者没有直接对整套大模型做昂贵 RL，而是让预训练 VLA 暴露一个紧凑的 `RL token`，再在这个表示上训练小型 actor-critic，从而把 VLA 的泛化能力和 real-world online RL 的样本效率拼接起来。

## 直观理解

可以把 RLT 理解成“让 VLA 给 RL 提供一个好用的中间状态表示”。VLA 继续负责广义感知和先验动作建议，而在线 RL 只负责在关键精细阶段做快速校正，所以它特别适合“最后几毫米”这种高精度操作优化。

![方法图](https://arxiv.org/html/2604.23073v2/x1.png)

*方法图*

## 核心信息

- **作者**：Charles Xu 等
- **机构**：Physical Intelligence
- **原文链接**：https://arxiv.org/abs/2604.23073
- **PDF 地址**：https://www.pi.website/download/rlt.pdf
- **发布日期**：2026-04-24
- **主题域**：physical-embodied-intelligence

## 背景与问题

**动机：** 预训练 VLA 已经能“开箱即用”完成很多 manipulation 任务，但在真实机器人上，最决定成功率的往往是最后的精细接触阶段，比如插接、拧螺丝、卡扣对齐等。

**问题缺口：** 直接用 RL 精调大模型成本太高，传统高样本效率 RL 又往往基于更小模型、会丢掉 VLA 的泛化先验。作者试图解决的就是：能不能在不重训整套 VLA 的前提下，用几小时甚至几分钟真实机器人实践，就把关键精细阶段补强。

## 论文摘要（英文原文）

Vision-language-action (VLA) models can learn to perform diverse manipulation skills "out of the box," but achieving the precision and speed that real-world tasks demand requires further fine-tuning -- for example, via reinforcement learning (RL). We introduce a lightweight method that enables sample-efficient online RL fine-tuning of pretrained VLAs using just a few hours of real-world practice. We (1) adapt the VLA to expose an "RL token," a compact readout representation that preserves task-relevant pretrained knowledge while serving as an efficient interface for online RL, and (2) train a small actor-critic head on this RL token to refine the actions, while anchoring the learned policy to the VLA. Online RL with the RL token (RLT) makes it possible to fine-tune even large VLAs with RL quickly and efficiently. Across four real-robot tasks (screw installation, zip tie fastening, charger insertion, and Ethernet insertion), RLT improves the speed on the hardest part of the task by up to 3x and raises success rates significantly within minutes to a few hours of practice. It can even surpass the speed of human teleoperation on some of the tasks.

## 论文摘要（中文翻译）

VLA 可以开箱执行多样化操作技能，但要达到真实任务要求的精度和速度，通常还需要进一步微调，比如用 RL。作者提出一种轻量方法，可以只用几小时真实机器人实践，就对预训练 VLA 做高样本效率的在线 RL 精调。方法分两步：一是让 VLA 暴露一个 `RL token`，它保留与任务相关的预训练知识，同时作为在线 RL 的高效接口；二是在这个 token 上训练一个小型 actor-critic 头，在保持策略锚定于原始 VLA 的同时对动作进行细化。作者在四个高精度真实机器人任务上表明，RLT 能在几分钟到几小时内显著提升成功率，并把关键阶段速度提升到最高 3 倍，部分任务甚至超过人类遥操作速度。

## 方法

**方法概述：** 这篇论文并不主张把整套大 VLA 直接拿去做重型 online RL，而是主张在预训练 VLA 与轻量 real-world RL 之间插入一个中间接口。作者通过一个 encoder-decoder transformer，从预训练 VLA 的内部特征里提取一个紧凑的 `RL token`，再基于这个 token 训练轻量 actor-critic，从而把 foundation model 的表示能力与在线 RL 的快速适配能力组合起来。

**核心机制：**

- 从 VLA 内部特征中暴露一个 `RL token`
- 用小型 actor-critic 在 `RL token` 上进行样本高效在线 RL
- 用 regularizer 把 actor 锚定在原始 VLA 行为附近，避免从零学起
- 只把 online RL 用在高精度、最难的 critical phase，而不是整段任务

**方法拆解：**

- 先从预训练 VLA 的内部表示中压缩出一个维度更低、任务相关但仍保留预训练知识的 `RL token`
- 在 `RL token` 上训练 actor 和 critic，使 online RL 只优化一个轻量策略层
- actor 输入不仅包含 token，也参考 VLA 的原始动作建议，并通过锚定项限制策略偏移过大
- 训练重点放在真实任务中的关键精细阶段，例如插接、拧入、卡扣等“最后几毫米”问题
- 基础 VLA 继续执行前面较容易的阶段，而 RL 集中提升最容易失败的部分

**关键要点：**

- 让大模型保留先验，小模型承担快速适配
- 强调 real-world online fine-tuning，而不是大规模离线再训练
- 特别适合精细接触和高精度 manipulation 阶段
- 这是把 generalist policy 继续打磨成 specialist-level precision 的务实路线

## 结果

**核心结果：**

- 在 screw installation、zip tie fastening、charger insertion、Ethernet insertion 四个真实机器人任务上，RLT 都能在几分钟到几小时内带来明显收益
- 论文摘要给出的最强结果是：关键阶段速度最高提升 `3x`
- 在困难任务上不仅 throughput 提升，success rate 也明显改善
- 对某些高精度部分，最终策略甚至能超过 expert teleoperation 的速度

![结果图](https://arxiv.org/html/2604.23073v2/x2.png)

*结果图*

**结果表：**

| 维度 | RLT 结论 |
| --- | --- |
| 微调目标 | 关键高精度阶段 |
| 在线学习成本 | 几分钟到几小时 |
| 速度提升 | 最多约 3x |
| 成功率提升 | 困难任务上显著提高 |
| 对比大模型直接 RL | 更轻、更快、更样本高效 |

## 洞察

**核心 insight：**

- 这篇工作最值得记住的不是 `RL token` 这个名词本身，而是它展示了一种 VLA 与 online RL 的分层协作方式：foundation model 提供广义能力，轻量 RL 负责最后的高精度矫正。

**和已有方法的关系：**

- 相对直接对大模型做 RL 的路线，它更强调接口化和参数效率
- 相对完全基于小模型的高样本效率 RL，它尽量不放弃 VLA 的预训练泛化能力
- 相对把 specialist policy 与 generalist policy 割裂开来的做法，它更像在 generalist 上叠一层 task-specific sharpening

**可借鉴点：**

- 对具身智能来说，很多时候不需要重训整套模型，只需要找到一个合适的 adaptation interface
- “critical phase only” 的 online RL 很适合真实机器人环境，因为它把实验预算集中在最值钱的阶段
- 如果后面你关注具身智能系统工程，这篇可以看成是“foundation policy + lightweight adaptation head”范式的代表作

## 风险与判断

**局限：**

- 论文验证任务集中在高精度 manipulation，而不是更复杂的长时程或跨场景连续任务
- 方法高度依赖预训练 VLA 本身已经具备不错的先验；如果底座很弱，`RL token` 未必能救回来
- 这种轻量 RL 接口是否能稳定推广到更多 embodiment、更多奖励形式，还需要更系统的验证

**适用场景：**

- 真实机器人上的高精度技能打磨
- 在 generalist policy 基础上快速追求更高成功率和更高速度
- 实验预算有限、不能承受整套大模型重训的场景

**最终判断：** 这篇是 “VLA 如何接 online RL” 方向里很有代表性的工作，尤其适合放进你后续的 `VLA + RL refinement` 主线。

## 结果速览表

| 维度 | 结论 |
| --- | --- |
| 微调方式 | 轻量在线 RL |
| 核心接口 | RL token |
| 训练对象 | 小型 actor-critic |
| 样本效率 | 几分钟到几小时 |
| 关键收益 | 提升精度、速度和成功率 |

## 相关主题

- vision-language-action
- online-rl-for-vla

## 相关页面

- [[Vision-Language-Action]]
- [[Online RL for VLA]]
- [[当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
