---
title: "Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments"
id: "qwen-vla"
slug: "qwen-vla"
type: source
material_type: paper
source_type: paper
source_kind: "arxiv_abs_url"
source_input: "https://arxiv.org/abs/2605.30280"
source_url: "https://arxiv.org/abs/2605.30280"
html_url: "https://arxiv.org/html/2605.30280v1"
pdf_url: "https://arxiv.org/pdf/2605.30280v1"
code_url: "https://github.com/QwenLM/Qwen-VLA"
translation_url: "https://hjfy.top/arxiv/2605.30280"
publish_date: "2026-05-28"
date: "2026-05-28"
created: "2026-08-10"
updated: "2026-08-10"
domain: "physical-embodied-intelligence"
primary_domain_slug: "physical-embodied-intelligence"
domains:
  - Physical/Embodied Intelligence
domain_slugs:
  - physical-embodied-intelligence
authors:
  - Qwen Team
affiliation: "Qwen Team"
related_organizations:
  - Qwen Team
related_companies:
  - Alibaba
links:
  original: "https://arxiv.org/abs/2605.30280"
  arxiv: "https://arxiv.org/abs/2605.30280"
  pdf: "https://arxiv.org/pdf/2605.30280v1"
  github: "https://github.com/QwenLM/Qwen-VLA"
  hjfy: "https://hjfy.top/arxiv/2605.30280"
raw_refs:
  - "raw/pdfs/2605.30280.pdf"
source_path: "raw/pdfs/2605.30280.pdf"
tags:
  - vision-language-action
keywords:
  - vision-language-action
images:
  - https://followhub.tenstep.top/papers/2605.30280-qwen-vla-unifying-vision-language-action-modeling-across-tasks-environments-and-robot-embodiment/color-conditioned-grasping-of-green-blue-red-and-yellow-balls-upper-two-panels-show-grasping-of.jpg
related_topics:
  - vision-language-action
related_syntheses:
  - current-vla-landscape-foundation-control-memory-and-transfer
status: analyzed
---

# Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments

## 太长不看

Qwen-VLA 将操作、连续导航、轨迹预测和人类第一视角运动统一为同一 action-and-trajectory prediction 问题；它不是为每个机器人另训策略，而是用 Qwen3.5-4B 与 1.15B 参数 DiT 动作专家共享建模。其关键价值是以 embodiment-aware prompt 保留各平台原生控制语义，并用四阶段训练把语言—动作先验、视觉 grounding、任务对齐和成功率优化串起来。跨操作、导航、真实 OOD 与动态零样本基准的结果表明，这个统一接口并未以明显的 specialist 性能为代价。

## 直观理解

把 Qwen-VLA 看作“同一位驾驶员配不同控制说明书”：图像和指令交给 Qwen 的视觉语言骨干理解，机器人型号、手臂与控制频率写在 prompt 里；DiT 动作专家再把这些高层条件逐步去噪成该平台可执行的一段连续动作或导航轨迹。

## 核心信息

- **作者**：Qwen Team
- **作者单位**：pages
- **来源类型**：arxiv_abs_url
- **输入来源**：https://arxiv.org/abs/2605.30280
- **原文链接**：https://arxiv.org/abs/2605.30280
- **HTML 正文**：https://arxiv.org/html/2605.30280v1
- **PDF 地址**：https://arxiv.org/pdf/2605.30280v1
- **代码地址**：https://github.com/QwenLM/Qwen-VLA
- **中英翻译地址**：https://hjfy.top/arxiv/2605.30280
- **发布日期**：2026-05-28
- **主题域**：physical-embodied-intelligence

## 背景与问题

**动机：** VLM 已能做开放世界感知和语言 grounding，扩散/flow policy 也能生成连续控制；但操作、导航、双臂、灵巧手与人类示范通常各有模型、动作空间和数据配方，阻碍能力与数据跨平台累积。

**问题缺口：** 不同任务在动作维度、频率、预测长度和评测上不同，却都要在视觉观察、语言指令和具体 embodiment 约束下预测物理且语义一致的未来序列。核心问题是如何既不强行抹平原生控制约定，又让一个模型从这些异构监督中迁移视觉 grounding、空间推理与连续控制。

## 论文摘要（英文原文）

Embodied intelligence is often studied through specialized models for individual tasks such as manipulation or navigation, resulting in fragmented capabilities and limited generalization across tasks, environments, and robot embodiments. In this work, we study whether heterogeneous embodied decision-making problems can be unified within a single vision-language-action model. We present Qwen-VLA, a unified embodied foundation model that extends Qwen’s vision-language modeling stack from perception, understanding, and reasoning to continuous action and trajectory generation through a DiT-based action decoder. Qwen-VLA is trained with a large-scale joint pretraining recipe over diverse data sources, including robotics manipulation trajectories, human egocentric demonstrations, synthetic simulation data, vision-and-language navigation data, trajectory-centric supervision, and auxiliary vision-language data. To support multiple robot platforms, we introduce embodiment-aware prompt conditioning, where robot-specific textual descriptions specify the current embodiment and control convention. We further cast manipulation, navigation, and trajectory prediction into a unified action-and-trajectory prediction framework, enabling transferable visual grounding, spatial reasoning, and continuous action generation across robot morphologies, task families, and environments. Experiments on manipulation, navigation, and trajectory-centric benchmarks show consistent multi-task performance and out-of-distribution generalization under variations in scene layout, background, lighting, object configuration, and robot embodiment. Qwen-VLA-Instruct achieves 97.9% on LIBERO, 73.7% on Simpler-WidowX, 86.1%/87.2% on RoboTwin-Easy/Hard, 69.0% OSR on R2R, 59.6% SR on RxR, 76.9% average OOD success in real-world ALOHA experiments, and 26.6% zero-shot success on DOMINO dynamic manipulation.

## 论文摘要（中文翻译）

具身智能常被拆成操作或导航等单一任务的专用模型，因而在任务、环境和机器人形态之间能力割裂、泛化有限。本文考察能否用单一视觉—语言—动作模型统一异构具身决策。Qwen-VLA 在 Qwen 视觉语言栈上加入基于 DiT 的动作解码器，把感知、理解和推理延伸到连续动作与轨迹生成；它以机器人操作轨迹、人类第一视角示范、合成仿真、视觉语言导航、轨迹监督和辅助视觉语言数据进行大规模联合预训练。为支持多种平台，作者把机器人形态和控制约定写入文本 prompt，并把操作、导航和轨迹预测化为统一的动作—轨迹预测。实验显示其在场景布局、背景、光照、物体配置和机器人形态变化下保持多任务与 OOD 泛化：Qwen-VLA-Instruct 在 LIBERO、Simpler-WidowX、RoboTwin Easy/Hard、R2R、RxR、真实 ALOHA OOD 与 DOMINO 零样本上分别达到 97.9%、73.7%、86.1%/87.2%、69.0% OSR、59.6% SR、76.9% 和 26.6%。

## 方法

**方法概述：** Qwen-VLA 用同一条件预测接口处理机器人动作、导航 waypoint、轨迹与人类姿态序列：强 Qwen3.5-4B 视觉语言骨干负责把视觉、语言和 embodiment 约束联系起来，单一 DiT flow-matching 动作专家负责把它们展开为连续控制。它不要求所有机器人共享同一种 action 定义，而是在条件与损失层面显式处理差异。

**核心机制：** 模型以原生多模态 Qwen3.5-4B 为骨干，将视觉 token 与文本 token 早期融合；单流 DiT flow-matching 动作专家把 VLM hidden states 和 noisy action chunk 拼接，经联合 self-attention、AdaLN timestep conditioning 与 multi-section RoPE 预测速度场，并以少量 Euler 步生成连续序列。动作专家约 1.15B 参数、16 个 DiT blocks；不同任务由有效位 mask 和按数据集 1%/99% 分位数归一化处理。

**方法拆解：** - 统一条件分布为 pθ(y_t:t+H-1 | o_t, x, e, z)：o 为图像/视频历史，x 为指令，e 为文字化的机器人平台、手臂配置、控制约定、频率和 horizon，z 为可选任务标识；目标可以是 EEF/关节动作、waypoint、驾驶轨迹或 MANO/骨骼运动。
- 不把各平台动作强转成一种控制格式。对不足最大维度的动作做 zero padding，并以 validity mask 只在有效维度计算 loss；同一个 DiT 参数因此能覆盖 WidowX、Franka、Mobile ALOHA、AgiBot、人类等形态。
- 四阶段配方先冻结 VLM、做无视觉 text-to-action (T2A) DiT 预训练，令语言与 embodiment prompt 成为动作“解压”条件；再做多模态 CPT、下游 SFT，最后只在 SimplerEnv 稀疏成功奖励上 RL，分别解决动作先验、视觉 grounding、任务精度与闭环优化。
- 预训练混合以机器人操作轨迹为主（74.2%），另含人类第一视角轨迹 6.0%、导航 7.5%、作者合成轨迹 3.7%、通用 VL 3.4%、2D 空间 grounding 2.5%、自动驾驶 VQA 2.4% 和细粒度动作 caption 0.2%；公开真实数据超过 10,000 小时，另有超过 1,000 小时内部真实轨迹和 800 万合成轨迹。

**关键要点：** - 将 embodiment 放在 prompt 而不是 per-robot head 中，是该文对“统一”的实质承诺：模型保留原数据集的控制语义，而共享潜在动作建模与视觉语言能力。
- T2A 不是普通 data warm-up；它明确先训练随机 DiT 从压缩的语言意图还原整条动作，再引入视觉，避免随机 decoder 早期用视觉 shortcut 干扰已预训练 VLM。

## 结果

**核心结果：** - 单个 Qwen-VLA-Instruct 在未按 benchmark 单独适配的条件下：LIBERO 97.9%、RoboCasa-GR1 56.7%、Simpler-WidowX 73.7%、RoboTwin Easy/Hard 86.1%/87.2%；在 RoboTwin 两档均高于表中最佳 specialist ABot-M0 的 86.0%/85.0%。
- 真实双臂 ALOHA 上，Base 微调的平均 in-domain 成功率 83.6%，对照的从头训练同构模型为 48.5%；OOD 平均为 76.9%，比 π0.5 高 35.4 个百分点，并在未见背景与指令上为 80.8% 与 84.6%。
- 连续导航 Val-Unseen：R2R 的 OSR/SR 为 69.0/57.5（StreamVLN 为 64.2/56.9），RxR 的 SR/SPL 为 59.6/47.8（StreamVLN 为 52.9/46.0）。DOMINO 35 个动态操作套件上零样本 SR 26.6、MS 39.5；该阶段没有动态操作训练数据。
- 消融直接支持训练配方：T2A 中约 20% 合成+80%真实、全轨迹预测达 71.09%，纯真实为 51.04%；T2A 用 Sigmoid-Normal、SFT 用 Beta 的组合也为 71.09%，两阶段都 Beta 仅 59.38%。保留 VL 共训使 RoboCasa 从 51.1 到 56.0、RoboTwin 从 81.8 到 86.4。

**结果表：** | 评测切面 | Qwen-VLA-Instruct | 可比较证据 |
| --- | ---: | --- |
| 四个操作基准 | LIBERO 97.9；Simpler 73.7；RoboTwin E/H 86.1/87.2 | RoboTwin 超 ABot-M0 86.0/85.0；同时是一个 generalist |
| 真实 ALOHA | in-domain 83.6；OOD 76.9 | 同构从头训练 48.5；OOD 比 π0.5 高 35.4 pp |
| 连续导航 | R2R OSR 69.0 / SR 57.5；RxR SR 59.6 | R2R OSR 比 StreamVLN 高 4.8 pp；RxR SR 高 6.7 pp |
| 动态操作零样本 | DOMINO SR 26.6；MS 39.5 | RL 阶段未使用动态操作数据 |

![结果图](https://followhub.tenstep.top/papers/2605.30280-qwen-vla-unifying-vision-language-action-modeling-across-tasks-environments-and-robot-embodiment/color-conditioned-grasping-of-green-blue-red-and-yellow-balls-upper-two-panels-show-grasping-of.jpg)

*结果图*

## 洞察

**核心 insight：** - 统一的难点不是把 action tensor padding 成一样长，而是明确控制语义。文字 embodiment prompt 让共享模型知道“这些数如何被执行”，而 mask/zero padding 仅解决张量计算层面的异构性。
- 四阶段训练揭示了一个值得复用的分工：高层 VLM 已有语义压缩能力，随机连续动作 decoder 需要先学反向的、语言条件下的轨迹展开；否则视觉 token 容易成为捷径而非 grounding。
- 该文最大的证据不是 LIBERO 97.9%，而是同一预训练能把 ALOHA OOD 从 36.2%（从头训练）推到 76.9%，并保住 VLN；这支持混合数据能形成可迁移空间—运动先验，但不证明所有 morphology 都可仅靠 prompt 接入。

**和已有方法的关系：** - 相对为单一平台或单类任务分别训练 specialist 的路线，Qwen-VLA 使用同一 Qwen backbone、同一 DiT expert 和 prompt/mask 接口；它的比较对象包含 π0、π0.5、GR00T N1.6、StarVLA-OFT 与 ABot-M0。
- 相对 token 自回归动作建模，DiT flow matching 更直接服务连续、多峰、高频 action chunk；相对仅 VLA 共训，保留一部分 VL 数据可提升需细粒度识别与组合解析的 RoboCasa/RoboTwin。

**可借鉴点：** - 面对多 embodiment 数据，先记录每个平台的控制频率、horizon、臂配置和 action convention，再把它作为显式条件；不要在预处理阶段静默把不可交换的控制语义标准化掉。
- 为连续控制接入强 VLM 时，可把 decoder pretraining、视觉联合预训练、任务 SFT 和 success-driven RL 分开做消融，避免把优化不稳定或增益来源混成一个“大训练配方”。

## 风险与判断

**局限：** - 跨 embodiment 的控制语义依赖人工编写的文字描述、数据集级归一化和有效维 mask；论文没有证明只换一段 prompt 就能在从未训练的新机器人上零样本安全运行，实际接入仍需该形态的数据与 SFT。
- 强结果横跨不同 benchmark、指标与训练/适配设定，不能把 97.9% LIBERO、76.9% ALOHA OOD、69.0 R2R OSR 简化成统一的“通用成功率”；论文也未给出跨平台的统一安全、时延或长期故障恢复评测。
- RL 只在 SimplerEnv 的稀疏二值奖励上采样；虽有温和迁移证据，但对真实世界奖励错设、接触动力学、长时程误差和安全约束的影响仍未被系统验证。

**适用场景：** - 适合研究团队已有多种机器人和混合示范数据、希望共享视觉语言 grounding 与动作先验，却允许为新平台收集少量适配数据的研发流程。
- 适合作为同时研究操作与连续导航的基础模型候选，尤其是需要用复杂自然语言、物体关系和背景变化来检验迁移的场景；不应直接当作无额外安全层的生产机器人控制器。

**最终判断：** - 这是值得进入 VLA 主线的系统性论文。其最有价值的贡献是将 heterogeneous embodiment 的条件接口、数据混合与 staged optimization 同时做成可检验的统一方案；性能强但并未消除新形态数据、实时安全验证和真实长时程闭环的工程门槛。

## 结果速览表

| 评测切面 | Qwen-VLA-Instruct | 可比较证据 |
| --- | ---: | --- |
| 四个操作基准 | LIBERO 97.9；Simpler 73.7；RoboTwin E/H 86.1/87.2 | RoboTwin 超 ABot-M0 86.0/85.0；同时是一个 generalist |
| 真实 ALOHA | in-domain 83.6；OOD 76.9 | 同构从头训练 48.5；OOD 比 π0.5 高 35.4 pp |
| 连续导航 | R2R OSR 69.0 / SR 57.5；RxR SR 59.6 | R2R OSR 比 StreamVLN 高 4.8 pp；RxR SR 高 6.7 pp |
| 动态操作零样本 | DOMINO SR 26.6；MS 39.5 | RL 阶段未使用动态操作数据 |

## 相关主题

- vision-language-action.
