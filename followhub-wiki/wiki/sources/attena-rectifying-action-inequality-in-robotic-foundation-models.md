---
id: "attena-rectifying-action-inequality-in-robotic-foundation-models"
slug: "attena-rectifying-action-inequality-in-robotic-foundation-models"
title: "AttenA+: Rectifying Action Inequality in Robotic Foundation Models"
type: source
material_type: "paper"
source_type: "paper"
created: "2026-06-30"
updated: "2026-06-30"
date: "2026-05-13"
publish_date: "2026-05-13"
authors:
  - "Daojie Peng"
  - "Fulong Ma"
  - "Jiahang Cao"
  - "Qiang Zhang"
  - "Xupeng Xie"
  - "Jian Guo"
  - "Ping Luo"
  - "Andrew F. Luo"
  - "Boyu Zhou"
  - "Jun Ma"
affiliation: "HKUST(GZ); HKU; USTC; IDEA Research; SUSTech; X-Humaniod"
related_organizations:
  - "HKUST(GZ)"
  - "HKU"
  - "USTC"
  - "IDEA Research"
  - "SUSTech"
  - "X-Humaniod"
related_companies:
domains:
  - "Physical/Embodied Intelligence"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "physical-embodied-intelligence"
domain_slugs:
  - "physical-embodied-intelligence"
tags:
  - "vision-language-action"
  - "action-weighting"
summary: "AttenA+ 把机器人轨迹里的低速、精细、接触关键动作视为更高价值的训练信号，用速度场重加权 VLA/WAM 的动作损失，在不改结构和不增参数的情况下提升操作成功率。"
links:
  original: "https://arxiv.org/abs/2605.13548"
  arxiv: "https://arxiv.org/abs/2605.13548"
  html: "https://arxiv.org/html/2605.13548v3"
  pdf: "https://arxiv.org/pdf/2605.13548.pdf"
  github: "https://github.com/DaojiePENG/AttenA-Plus"
  hjfy: "https://hjfy.top/arxiv/2605.13548"
raw_refs:
  - "https://arxiv.org/abs/2605.13548v1"
  - "https://arxiv.org/html/2605.13548v3"
related_topics:
  - "vision-language-action"
related_syntheses:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2605.13548v3/x1.png"
images:
  - "https://arxiv.org/html/2605.13548v3/x1.png"
  - "https://arxiv.org/html/2605.13548v3/x3.png"
  - "https://arxiv.org/html/2605.13548v3/x5.png"
source_url: "https://arxiv.org/abs/2605.13548"
html_url: "https://arxiv.org/html/2605.13548v3"
pdf_url: "https://arxiv.org/pdf/2605.13548.pdf"
code_url: "https://github.com/DaojiePENG/AttenA-Plus"
translation_url: "https://hjfy.top/arxiv/2605.13548"
status: analyzed
---
# AttenA+: Rectifying Action Inequality in Robotic Foundation Models

## 太长不看

AttenA+ 的核心价值是指出 VLA/WAM 训练里一个很朴素但长期被忽略的问题：机器人动作时间步并不等价，慢速精细动作往往比快速过渡动作更决定任务成败。它用速度场给低速关键动作更高 loss 权重，不改模型结构、不加参数，却能在 Libero、RoboTwin 2.0 和真实 Franka 任务上稳定抬高强基线的上限。值得记住的不是某个复杂网络，而是“动作序列的物理结构可以直接进入训练目标”。

## 直观理解

可以把 AttenA+ 理解成给机器人示范轨迹加一个“动作显微镜”：移动到目标附近的高速段通常只是过渡，错一点也能补；靠近物体、对齐、夹取、释放这些低速段才是最怕误差的地方。传统 VLA 把每个动作 token 一视同仁，AttenA+ 则根据专家动作的速度自动调权，让模型把学习容量更多花在这些慢而关键的瞬间。

![AttenA+ 总览](https://arxiv.org/html/2605.13548v3/x1.png)

*AttenA+ 作为无结构改动的训练目标增强，可接入 OpenVLA-OFT、π0/π0.5、Diffusion Policy 和 WAM 等不同动作模型。*

## 核心信息

- **作者**：Daojie Peng、Fulong Ma、Jiahang Cao、Qiang Zhang、Xupeng Xie、Jian Guo、Ping Luo、Andrew F. Luo、Boyu Zhou、Jun Ma
- **作者单位**：HKUST(GZ); HKU; USTC; IDEA Research; SUSTech; X-Humaniod
- **来源类型**：arxiv_html_url
- **用户输入版本**：https://arxiv.org/abs/2605.13548v1
- **分析使用版本**：https://arxiv.org/html/2605.13548v3
- **原文链接**：https://arxiv.org/abs/2605.13548
- **PDF 地址**：https://arxiv.org/pdf/2605.13548.pdf
- **代码地址**：https://github.com/DaojiePENG/AttenA-Plus
- **中英翻译地址**：https://hjfy.top/arxiv/2605.13548
- **发布日期**：2026-05-13
- **主题域**：physical-embodied-intelligence

## 背景与问题

**动机：** VLA 和 WAM 正在成为端到端机器人控制的主流路线，但它们大多继承了语言模型式的“平坦训练”假设：序列中每个 token、每个时间步都以相同权重参与优化。对语言 token 来说这也许合理，但机器人操作轨迹天然带有物理层级：快速伸手、移动、绕行通常是过渡段；慢速对齐、接触、抓取、插入、释放才是高精度、高失败风险的关键段。

**问题缺口：** 现有 VLA/WAM 的统一 loss 会把表示能力浪费在大量容错的高速动作上，同时低估“最后几厘米”的精细动作。论文把这种错配称为 action inequality：动作序列的信息密度和物理关键性并不均匀。它要解决的问题不是重新设计一个新骨干，而是怎样把这种轨迹内部的物理先验注入现有基础模型训练，让模型更关注真正决定成败的动作片段。

## 论文摘要（英文原文）

Existing robotic foundation models, while powerful, are predicated on an implicit assumption of temporal homogeneity: treating all actions as equally informative during optimization. This "flat" training paradigm, inherited from language modeling, remains indifferent to the underlying physical hierarchy of manipulation. In reality, robot trajectories are fundamentally heterogeneous, where low-velocity segments often dictate task success through precision-demanding interactions, while high-velocity motions serve as error-tolerant transitions. Such a misalignment between uniform loss weighting and physical criticality fundamentally limits the performance of current Vision-Language-Action (VLA) models and World-Action Models (WAM) in complex, long-horizon tasks. To rectify this, we introduce AttenA+, an architecture-agnostic framework that prioritizes kinematically critical segments via velocity-driven action attention. By reweighting the training objective based on the inverse velocity field, AttenA+ naturally aligns the model's learning capacity with the physical demands of manipulation. As a plug-and-play enhancement, AttenA+ can be integrated into existing backbones without structural modifications or additional parameters. Extensive experiments demonstrate that AttenA+ significantly elevates the ceilings of current state-of-the-art models. Specifically, it improves OpenVLA-OFT to 98.6% (+1.5%) on the Libero benchmark and pushes FastWAM to 92.4% (+0.6%) on RoboTwin 2.0. Real-world validation on a Franka manipulator further showcases its robustness and cross-task generalization. Our work suggests that mining the intrinsic structural priors of action sequences offers a highly efficient, physics-aware complement to standard scaling laws, paving a new path for general-purpose robotic control.

## 论文摘要（中文翻译）

现有机器人基础模型虽然强大，但隐含地假设时间上是同质的：在优化时把所有动作都视为同等有信息量。这种继承自语言建模的“平坦”训练范式，对操作任务底层的物理层级并不敏感。现实中，机器人轨迹本质上是异质的：低速片段往往通过高精度交互决定任务成功，而高速运动通常只是容错性较强的过渡。统一 loss 权重与物理关键性之间的错配，从根本上限制了当前 Vision-Language-Action（VLA）模型和 World-Action Model（WAM）在复杂长程任务中的表现。为纠正这一问题，作者提出 AttenA+，一个架构无关的框架，通过速度驱动的 action attention 优先学习运动学上关键的片段。AttenA+ 基于逆速度场重加权训练目标，使模型学习容量自然对齐操作任务的物理需求。作为即插即用增强，它可以无结构修改、无额外参数地集成到现有骨干中。大量实验表明，AttenA+ 显著提升当前 SOTA 模型的上限：在 Libero benchmark 上将 OpenVLA-OFT 提升到 98.6%（+1.5%），在 RoboTwin 2.0 上将 FastWAM 提升到 92.4%（+0.6%）。真实 Franka 机械臂验证进一步展示了其鲁棒性和跨任务泛化能力。该工作说明，挖掘动作序列的内在结构先验，是标准 scaling law 之外一种高效、物理感知的补充路径。

## 方法

**方法概述：** AttenA+ 不是新模型骨干，而是一个训练目标层面的增强框架。它先从专家轨迹中计算每个时间步的动作速度，再把速度映射成 attention/weight：速度越低、越可能处在精细接触或对齐阶段，loss 权重越高；速度越高、越可能是过渡运动，权重越低。

**核心机制：** 论文用 ground-truth action 的瞬时速度幅值作为任务关键性的无监督 proxy。给定动作向量，取连续运动维度计算速度范数；再通过权重函数 `w_t = F_A(v_t)` 把速度映射为训练权重。这个权重直接乘到原本的 per-step loss 或生成式模型的向量场/score matching 目标上，因此无需改变 VLA/WAM 的网络结构。

**方法拆解：**
- **动作不平等建模**：把轨迹划分为高速容错过渡段和低速高精度交互段，认为后者对成功率和错误累积更关键。
- **速度场构造**：在 Libero 等任务中，用专家动作前 6 个连续维度计算速度幅值，忽略二值 gripper 状态，以避免夹爪开合离散信号污染连续运动关键性估计。
- **四类速度到权重映射**：论文测试 inverse、inverse squared、exponential decay、log 四种函数，让低速动作获得不同程度的非线性放大。
- **稳定性正则**：通过 weight clipping 把权重限制在 `[1/clip_max, clip_max]`，并可做 loss normalization，使平均权重约为 1，避免低速噪声点支配梯度。
- **范式无关集成**：对判别式 VLA，把 L1/L2 动作回归 loss 变成加权 loss；对 flow matching、diffusion policy、WAM 等生成式动作模型，则把同样的速度权重加到向量场或噪声预测目标上。

**关键要点：**
- AttenA+ 的重要性在于“物理先验进入 loss”，而不是架构创新。
- 速度是一个便宜、无需标注、容易跨数据集复用的关键性 proxy。
- 这个方法最适合 precision-demanding manipulation：对齐、夹取、插入、释放、长程多阶段操作。

![速度场与关键动作](https://arxiv.org/html/2605.13548v3/x3.png)

*论文通过速度场展示动作序列信息密度并不均匀，低速段通常对应操作成败关键处。*

## 结果

**核心结果：**
- **Libero SOTA 对比**：AttenA+OFT 在 Libero 上达到平均成功率 98.60%，相比 OpenVLA-OFT 的 97.10% 提升 +1.5%，错误率从 2.90% 降到 1.40%。在强基线已经接近饱和的条件下，这个增益有实际含义。
- **RoboTwin 2.0**：基于 Fast-WAM 的 AttenA+WAM 达到 92.46% 平均成功率，相比 Fast-WAM 91.80% 提升 +0.6%，并略高于 LingBot-VA 的 92.2%；同时不需要 embodied pre-training。
- **跨范式验证**：在 Libero 上，π0.5 加 AttenA+ 后平均成功率从 96.85% 提到 97.95%（+1.10%）；OpenVLA-OFT 加 AttenA+ 从 97.1% 到 98.6%（+1.50%）。说明它不只适用于一个判别式骨干。
- **长程任务收益更明显**：OpenVLA-OFT 在 Libero-10 长程任务上从 94.5% 提到 96.6%（+2.1%），π0.5 在同类任务上从 92.4% 到 94.2%（+1.8%），符合“关键低速段影响错误累积”的假设。
- **真实 Franka 实验**：平均成功率从 92.5% 提到 97.0%。四类任务中，简单关抽屉保持 50/50；放方块从 48/50 到 50/50；多物体从 45/50 到 49/50；长程任务从 42/50 到 45/50。
- **消融结论**：没有单一 weighting strategy 在所有任务上占优；`clip_max=2` 或 `3` 常有收益，过大的 `clip_max=5` 会让低速噪声过度放大并伤害训练稳定性。

**结果表：**

| 设置 | 基线 | AttenA+ | 变化 | 关键信号 |
| --- | --- | --- | --- | --- |
| Libero / OpenVLA-OFT | 97.10% SR | 98.60% SR | +1.50% | 强基线高位继续提升，错误率 2.90%→1.40% |
| Libero / π0.5 | 96.85% SR | 97.95% SR | +1.10% | 生成式 VLA 也有效 |
| RoboTwin 2.0 / Fast-WAM | 91.80% SR | 92.46% SR | +0.66% | WAM 路线也有效，无 embodied pre-training |
| Libero-10 / OpenVLA-OFT | 94.5% SR | 96.6% SR | +2.1% | 长程任务收益更明显 |
| Real Franka | 92.5% SR | 97.0% SR | +4.5% | 真实任务验证低速关键动作假设 |

![实验任务与真实机器人验证](https://arxiv.org/html/2605.13548v3/x5.png)

*AttenA+ 在仿真基准和真实 Franka 任务上验证，真实任务包含关抽屉、放方块、多物体和长程序列操作。*

## 洞察

**核心 insight：**
- 机器人基础模型的下一个增益来源不一定总是更大数据/更大模型，也可能来自更正确地利用动作序列内部的物理结构。
- “动作 token”不应该完全类比语言 token：语言 token 的重要性来自语义上下文，机器人动作的关键性还来自速度、接触、力、误差容忍度等物理属性。
- AttenA+ 的简洁性很强：只要数据里有 expert action，就能后处理得到速度权重，因此是一个很容易成为训练 recipe 的技巧。

**和已有方法的关系：**
- 相比 OpenVLA、π0/π0.5、WAM 等模型论文，AttenA+ 更像一个可叠加的训练目标补丁；它不替代这些骨干，而是试图抬高它们的操作精度上限。
- 相比 VLA-ADP 这类通过 pruning/效率优化处理动作冗余的方法，AttenA+ 不直接删掉动作，而是在保留完整轨迹的情况下重新分配学习重点。
- 相比传统 imitation learning 的轨迹级/样本级加权，AttenA+ 更细到 timestep，并且权重来自物理运动学而不是人工质量标签或额外不确定性估计。

**可借鉴点：**
- 对机器人学习来说，loss design 里加入物理先验可能比盲目扩大 backbone 更经济。
- 如果做 VLA 数据清洗或训练调参，可以额外记录速度/加速度/接触状态，把它们作为训练权重、采样权重或 curriculum 的依据。
- 这个思路可扩展到力觉、触觉、接触事件、夹爪状态变化等更丰富信号：低速不是唯一关键性 proxy，但它是一个足够便宜的起点。

## 风险与判断

**局限：**
- 速度低并不总等于关键，高速抓取、打乒乓球、投掷、动态避障等任务中，关键动作可能恰恰是高速且弹道式的。
- 方法依赖手工设计的 velocity heuristic 和 clipping 阈值，不同任务需要选择不同 weighting strategy；消融也显示没有一种函数通吃所有任务。
- 它只利用速度，没有直接使用力、扭矩、接触、滑移、视觉遮挡等更直接的物理关键性信号。
- 在强基线高成功率场景下，仿真提升有时是 0.6%～1.5%，需要结合任务难度和方差判断工程性价比。

**适用场景：**
- VLA/WAM/扩散策略等已有动作模型的后续训练、微调或 ablation recipe。
- 精密操作、长程操作、插入/对齐/放置/多物体序列等低速关键段明显的任务。
- 数据中已有连续动作轨迹、但不想增加额外标注或修改模型结构的机器人学习项目。

**最终判断：**
- 这篇论文值得进知识库，因为它提供了一个很干净的“动作物理结构 → 训练目标”的范式。AttenA+ 不是复杂系统，但它提醒 VLA 训练不能只照搬语言模型的平坦 token 观；未来更强的机器人基础模型，很可能需要系统地把速度、接触、力觉和任务阶段这些物理信号写进优化过程。

## 结果速览表

| 指标 | AttenA+ 结果 | 结论 |
| --- | --- | --- |
| Libero / OpenVLA-OFT | 98.60% vs 97.10% | 强判别式 VLA 上 +1.50% |
| Libero / π0.5 | 97.95% vs 96.85% | 生成式 VLA 上 +1.10% |
| RoboTwin 2.0 / Fast-WAM | 92.46% vs 91.80% | WAM 上 +0.66%，略超 LingBot-VA |
| Real Franka | 97.0% vs 92.5% | 真实任务平均 +4.5% |
| 核心代价 | 无结构改动、无额外参数 | 主要成本是 loss 权重计算与调参 |
| 主要限制 | 速度 heuristic 不总成立 | 动态高速关键任务需谨慎 |

## 相关主题

- vision-language-action

## 相关页面

- [[Vision-Language-Action]]
- [[OpenVLA: An Open-Source Vision-Language-Action Model]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
- [[当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据]]
