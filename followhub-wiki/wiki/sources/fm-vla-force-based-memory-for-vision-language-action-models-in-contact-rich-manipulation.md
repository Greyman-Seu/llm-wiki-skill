---
id: "fm-vla-force-based-memory-for-vision-language-action-models-in-contact-rich-manipulation"
slug: "fm-vla-force-based-memory-for-vision-language-action-models-in-contact-rich-manipulation"
title: "FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation"
type: source
material_type: "paper"
source_type: paper
source_kind: "arxiv_abs_url"
source_input: "https://arxiv.org/abs/2607.18231"
created: "2026-09-01"
updated: "2026-09-01"
date: "2026-07-20"
publish_date: "2026-07-20"
source_url: "https://arxiv.org/abs/2607.18231"
html_url: "https://arxiv.org/html/2607.18231v1"
pdf_url: "https://arxiv.org/pdf/2607.18231"
code_url: "https://qft-333.github.io/FM-VLA-Page/"
translation_url: "https://hjfy.top/arxiv/2607.18231"
arxiv_id: "2607.18231"
authors:
  - "Ruicheng Li"
  - "Qixiu Li"
  - "Ruichun Ma"
  - "Yu Deng"
  - "Lin Luo"
  - "Zhiying Du"
  - "Jianfeng Xiang"
  - "Huizhi Liang"
  - "Ruicheng Wang"
  - "Jiaolong Yang"
  - "Baining Guo"
affiliation: "Tsinghua University; Microsoft Research; Fudan University; USTC"
related_organizations:
  - "Tsinghua University"
  - "Microsoft Research"
  - "Fudan University"
  - "University of Science and Technology of China"
related_companies:
  - "Microsoft Research"
domains:
  - "Physical/Embodied Intelligence"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - "Physical/Embodied Intelligence"
tags:
  - "long-horizon-memory"
  - "contact-rich-manipulation"
summary: "FM-VLA 基于 π0.5 的 PaliGemma/SigLIP 视觉语言骨干与 flow-matching 动作专家，在 noisy-action token 之后追加两类低维历史条件：一类是从 episode 开始累计的右腕六轴 wrench 历史，经 EMA、分位数归一化和预训练 Perceiver-IO Force-VAE 压缩为 8 个长期记忆 token；另一类是最近约 0.9 秒、10 个采样点的双臂关节与夹爪状态，经零初始化线性层投影为 1 个短时状态 token。训练分为无任务标签的 Force-VAE 重建预训练与冻结编码器后的 VLA flow-matching 微调两阶段。"
keywords:
  - "vision-language-action"
  - "force memory"
  - "wrench sensing"
links:
  original: "https://arxiv.org/abs/2607.18231"
  arxiv: "https://arxiv.org/abs/2607.18231"
  html: "https://arxiv.org/html/2607.18231v1"
  pdf: "https://arxiv.org/pdf/2607.18231"
  project: "https://qft-333.github.io/FM-VLA-Page/"
  github: ""
  code: "https://qft-333.github.io/FM-VLA-Page/"
  hjfy: "https://hjfy.top/arxiv/2607.18231"
  doi: "https://doi.org/10.48550/arXiv.2607.18231"
raw_refs:
  - "https://arxiv.org/html/2607.18231v1"
  - "https://arxiv.org/pdf/2607.18231"
  - "https://qft-333.github.io/FM-VLA-Page/"
  - "https://arxiv.org/abs/2607.18231"
related_topics:
  - "long-horizon-memory-for-robot-policies"
  - "contact-rich-manipulation"
related_syntheses:
  - "force-touch-robot-policy-review"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2607.18231v1/overview1.png"
images:
  - "https://arxiv.org/html/2607.18231v1/overview1.png"
  - "https://arxiv.org/html/2607.18231v1/teaser_v1.png"
  - "https://arxiv.org/html/2607.18231v1/token_ablation.svg"
  - "https://arxiv.org/html/2607.18231v1/tasks.png"
image_paths: []
status: analyzed
---

# FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation

## 太长不看

FM-VLA 的关键不是给 VLA 再塞一种当前时刻传感器，而是把整段腕部力/力矩历史压缩成可供动作专家读取的长期事件记忆。它在找隐藏积木、精确计数按钮按压与碗内擦拭三项非马尔可夫任务上达到 83.3% 平均成功率，显著超过视觉记忆 π-MEM 的 53.7%，推理延迟仅比无记忆 π0.5 增加 3.3 ms。最值得记住的是“长时 force + 短时 state”的职责分工，但证据目前仍限于单一双臂平台和小规模任务。

## 直观理解

把机器人想成闭着眼按按钮的人：画面几乎不变，但手腕上每一次清晰的力脉冲都在告诉它“已经按了几次”。FM-VLA 不保存大量旧图像，而是把从任务开始到当前时刻的六轴力/力矩曲线压成 8 个记忆 token，用来记住接触事件；同时再看最近约 0.9 秒的关节状态，知道手臂正在往哪里走，避免尚未接触时因只读 force 而重复或乱动。

![FM-VLA 两阶段架构总览](https://arxiv.org/html/2607.18231v1/overview1.png)

*图 2：第一阶段以 Force-VAE 重建 wrench 历史，第二阶段把冻结编码器输出的 8 个力记忆 token 与 1 个短时状态 token 注入 π0.5 动作专家。*

## 核心信息

- **作者**：Ruicheng Li、Qixiu Li、Ruichun Ma、Yu Deng、Lin Luo、Zhiying Du、Jianfeng Xiang、Huizhi Liang、Ruicheng Wang、Jiaolong Yang、Baining Guo
- **作者单位**：Tsinghua University; Microsoft Research; Fudan University; USTC
- **来源类型**：arxiv_abs_url
- **输入来源**：https://arxiv.org/abs/2607.18231
- **原文链接**：https://arxiv.org/abs/2607.18231
- **HTML 正文**：https://arxiv.org/html/2607.18231v1
- **PDF 地址**：https://arxiv.org/pdf/2607.18231
- **代码地址**：https://qft-333.github.io/FM-VLA-Page/
- **中英翻译地址**：https://hjfy.top/arxiv/2607.18231
- **发布日期**：2026-07-20
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** 现有 VLA 多把当前图像、语言和机器人状态直接映射为下一段动作，这一马尔可夫假设在单步操作中可用，却无法处理“已经检查过哪只杯子”“按钮已按几次”“碗已擦几轮”这类由历史决定正确动作的任务。视觉记忆虽能保存旧帧，但会增加视觉编码与注意力成本；更关键的是，按钮微小位移、遮挡后的场景复原和擦拭进度往往在图像中没有可靠变化，而腕部力/力矩会留下清晰的接触脉冲与持续受力结构。

**问题缺口：** 既有 ForceVLA、TA-VLA 等力增强 VLA 主要利用当前或不到一秒的短窗口 wrench 改善即时动作，能够判断“是否接触、当前用了多大力”，却不能累计整个 episode 的事件计数与任务进度。直接把 100 Hz 的长序列端到端压给动作专家又会遭遇高频噪声、长度泄漏、长依赖学习困难和 token 成本。因此论文要解决的是：如何在不依赖事件标签或文本摘要的情况下，把可变长、含噪的力历史压成固定且有语义的记忆，同时保留足够的短时运动上下文，让 VLA 稳定地产生后续动作。

## 论文摘要（英文原文）

Vision-language-action (VLA) models have achieved impressive generalization in robotic manipulation, and recent memory-augmented VLAs have relaxed the Markovian assumption by conditioning on past images or language summaries. Vision-based memory approaches address this by conditioning on sampled past image frames, but they are computationally expensive and fundamentally limited when temporal events are visually ambiguous, e.g., pushing a button multiple times with small movements. We propose FM-VLA, a VLA model with force-based memory, enabling temporal context reasoning for non-Markovian, contact-rich manipulation. We encode force histories into compact force memory tokens with a variational autoencoder (VAE) pretrained with force time series reconstruction. By projecting force latent representations and short state history as additional conditioning tokens to the action expert module, we enable VLAs to leverage accumulated contact event history to guide manipulation. We evaluate FM-VLA on three memory-dependent tasks, including finding a hidden block, pressing a button, and wiping a dish for a specific number of times. Our lightweight force memory achieves over 80% success rate with minimal inference overhead, significantly outperforming baseline approaches.

## 论文摘要（中文翻译）

视觉—语言—动作（VLA）模型已在机器人操作中展现出出色的泛化能力，近期带记忆的 VLA 通过以历史图像或语言摘要为条件，放宽了马尔可夫假设。视觉记忆方法通常输入抽样的历史图像帧，但计算代价高，并且当时间事件在视觉上含混时存在根本局限，例如按钮位移很小却需要重复按压。本文提出 FM-VLA：一种带力记忆的 VLA，用于非马尔可夫、接触密集操作中的时间上下文推理。作者先以力时间序列重建预训练变分自编码器（VAE），再把力历史编码为紧凑记忆 token；随后将力潜变量与短时状态历史投影成额外条件 token，送入动作专家，使 VLA 能利用累计接触事件指导操作。FM-VLA 在寻找隐藏积木、按指定次数按钮和按指定次数擦拭碗三项记忆依赖任务上进行评测，轻量力记忆以极小推理开销取得超过 80% 的成功率，并显著优于基线。

## 方法

**方法概述：** FM-VLA 基于 π0.5 的 PaliGemma/SigLIP 视觉语言骨干与 flow-matching 动作专家，在 noisy-action token 之后追加两类低维历史条件：一类是从 episode 开始累计的右腕六轴 wrench 历史，经 EMA、分位数归一化和预训练 Perceiver-IO Force-VAE 压缩为 8 个长期记忆 token；另一类是最近约 0.9 秒、10 个采样点的双臂关节与夹爪状态，经零初始化线性层投影为 1 个短时状态 token。训练分为无任务标签的 Force-VAE 重建预训练与冻结编码器后的 VLA flow-matching 微调两阶段。

**核心机制：** 核心机制是先用重建目标迫使 Force-VAE 的潜空间编码力峰值、接触起止、幅值和事件次数等宏观时间结构，再冻结该编码器，只把后验均值投影到动作专家隐藏维度。与从任务损失端到端学习 GRU 或 Q-Former 相比，任务无关的连续信号重建提供更密集的训练约束，使 8 个 token 更容易保留早期接触事件。短时 state token 则回答“手臂在哪里、正往哪里走”，专门补足 force-only 在接触发生前缺少空间与运动线索的问题；两类 token 放在 noisy-action token 之后，也保持了 π0.5 预训练时原有动作 token 的 RoPE 位置。

**方法拆解：**

- 信号预处理：使用右腕 6 轴 wrench，100 Hz 传感器下采样到 30 Hz，以 α=0.3 的因果 EMA 去噪，并按数据集 q01/q99 分位数归一化；训练时随机前置最多约 10 秒、σ=0.05 的低幅高斯噪声，消除序列长度泄露任务进度的捷径。
- Force-VAE 预训练：Perceiver-IO 以 8 个可学习 latent query 通过交叉注意力读取任意长度 wrench 序列，再用 10 层 latent self-attention 压缩；解码器按时间查询重建完整序列，以 masked reconstruction、KL 和 free-bits 联合训练 100k steps，并通过逆频率任务采样平衡三类数据。
- 短时状态支路：取最近 10 个双臂 7-DoF 关节与两个夹爪状态（stride 3，约 0.9 秒），展平后由零初始化线性层映射为单一状态记忆 token，不单独预训练。
- 记忆注入：冻结 Force-VAE 编码器，取 8×96 的后验均值，经零初始化投影升到动作专家宽度；序列按 30 个 noisy-action token、8 个 force-memory token、1 个 state token 排列。
- 两阶段训练：先对所有任务的 wrench 历史做任务无关 VAE 预训练，再在 750 条遥操作示范上联合微调 VLM、flow-matching 动作专家和两个投影器 50k steps；力编码器保持冻结，flow matching 预测 30 步动作 chunk 的直线路径速度。

**关键要点：**

- 长期 wrench 与短期 state 不是冗余模态：前者记接触事件与次数，后者提供接触前的位置和速度趋势；任一支路单独使用都明显退化。
- VAE 的价值不只是压缩，而是用时间序列重建先塑造可读的接触事件潜空间；相同 token 预算下，从任务损失端到端训练的 GRU 和 Q-Former 都明显更差。
- 记忆容量不是越大越好：8 token 最优，16/32 token 反而使成功率下降，作者认为额外 token 超出动作专家预训练时熟悉的长度分布。

![FM-VLA 的 Force-VAE 与记忆 token 注入流程](https://arxiv.org/html/2607.18231v1/overview1.png)

*图 2：Force-VAE 用 Perceiver-IO 把任意长度 wrench 序列压缩为固定 token；VLA 微调时只使用冻结编码器的后验均值。*

## 结果

**核心结果：**

- 主结果：FM-VLA 在 Cups、Buttons、Wipe 三项任务分别达到 100.0%、72.2%、77.8%，平均 83.3%；π0.5、TA-VLA、π-MEM 的平均成功率分别为 27.8%、22.2%、53.7%。
- 最能隔离力记忆价值的是 Buttons：每次按钮按下几乎无视觉位移但产生清晰 wrench 脉冲，FM-VLA 为 72.2%，视觉记忆 π-MEM 仅 33.3%，无记忆 π0.5 与短窗 TA-VLA 都是 11.1%。
- 模态消融表明互补性：force-only 平均 25.9%，因接触前缺少运动上下文而不稳定；state-only 平均 40.7%，虽在 Cups 达到 100%，却无法在 Buttons/Wipe 上可靠计数。
- 架构消融：在 force + short-state 条件相同下，GRU、Q-Former、VAE 的平均成功率分别为 33.3%、57.4%、83.3%；Wipe 上分别为 5.6%、55.6%、77.8%。
- 效率：RTX 4090 上 π0.5 为 60.7±0.3 ms，FM-VLA 为 64.0±0.4 ms，仅增加 3.3 ms；π-MEM 读取 5/16 帧时分别为 99.8±0.4 ms 与 190.0±1.0 ms。

**结果表：**

| 方法 | Cups | Buttons | Wipe | 平均 | 单步延迟 |
| --- | ---: | ---: | ---: | ---: | ---: |
| π0.5（无历史） | 72.2% | 11.1% | 0.0% | 27.8% | 60.7 ms |
| TA-VLA（短窗力） | 50.0% | 11.1% | 5.6% | 22.2% | 未报告 |
| π-MEM（视觉记忆，K=5） | 77.8% | 33.3% | 50.0% | 53.7% | 99.8 ms |
| FM-VLA（VAE，本文） | **100.0%** | **72.2%** | **77.8%** | **83.3%** | **64.0 ms** |

![Force memory token 数量消融](https://arxiv.org/html/2607.18231v1/token_ablation.svg)

*图 3：Wipe 任务上 8 个力记忆 token 最优；4 个形成信息瓶颈，16/32 个则带来动作专家的长度分布偏移。*

![三项任务的轨迹与力信号](https://arxiv.org/html/2607.18231v1/tasks.png)

*图 4：Cups、Buttons、Wipe 的真实机器人轨迹与选定 force channel；接触事件在力曲线上比图像状态更清晰。*

## 洞察

**核心 insight：**

- 记忆模态应按“事件的可观测性”选择，而不是默认历史都用图像表示。接触次数、碰撞和受力阶段天然存在于 wrench 中，用低维物理信号做 memory 既更清楚也更便宜。
- 这篇工作把 force 从即时反馈升级为 episodic state：同一传感流既可服务毫秒级纠偏，也可在更长时间尺度上充当任务进度计数器，关键区别是编码窗口与训练目标。
- 重建式预训练在这里承担“时序语义发现”的角色：没有按钮次数标签，VAE 仍会因为要重建整段曲线而保留峰值、起止和重复结构；这比只靠稀疏任务成功损失学长序列摘要更稳。

**和已有方法的关系：**

- 相对 MemoryVLA、MEM 和本文的 π-MEM，FM-VLA 不保存视觉帧或语言摘要，而是用低维 wrench 记住视觉上含混的接触事件，换来更低的 token/视觉编码成本。
- 相对 ForceVLA、TA-VLA 等 force-aware VLA，FM-VLA 的核心新增不是力模态本身，而是从 episode 开始累计的长期历史与独立的记忆预训练；短窗力基线无法完成事件计数。
- 相对通用 GRU/Q-Former 压缩器，Force-VAE 通过任务无关连续重建先学习历史结构，再冻结给策略使用，减少了长序列表示完全依赖下游操作损失的问题。

**可借鉴点：**

- 对任何可能泄露时间进度的可变长历史输入，都可用随机噪声前缀、随机起点或时间扰动阻止模型只按长度猜阶段。
- 为预训练模型追加新条件 token 时，零初始化投影并保持原 token 的位置编码位置，可降低初始扰动；同时要把新增 token 数量视作重要分布变量。
- 将长期事件记忆与短期运动状态拆成不同编码器和 token，可以把“记住发生过什么”与“知道现在正怎么动”显式解耦。

![视觉记忆与力记忆的对比](https://arxiv.org/html/2607.18231v1/teaser_v1.png)

*图 1：历史图像 token 多且难辨按钮接触事件；wrench 历史低维，并把每次接触保留为明确峰值。*

## 风险与判断

**局限：**

- 评测只在一台 AgiBot G1 双臂机器人和三项人为设计的任务上进行，每方法每任务 18 次试验；尚未验证跨机器人、跨传感器标定、开放场景或自然长任务泛化。
- Force-VAE 只用本论文 750 条示范中的右腕 wrench 预训练，可能把特定机器人、工具、采样频率和任务动力学编码进潜空间；作者也未给出跨任务或跨 embodiment 迁移实验。
- 固定 8-token 瓶颈对数百次接触或更长 episode 可能不足，且 16/32 token 的下降也说明动作专家对新增条件长度存在分布敏感性，未必能靠简单扩容解决。
- 方法依赖腕部六轴力/力矩传感器；对低成本平台、电机电流估计、指尖触觉或多点接触是否仍成立，论文没有验证。

**适用场景：**

- 按钮、开关、装配卡扣、插拔和重复按压等视觉位移极小、但接触峰值清晰且需要精确计数的任务。
- 擦拭、打磨、沿面跟随等需要记住已经覆盖几轮或经过哪些接触阶段，同时保持当前运动稳定的操作。
- 遮挡或场景会恢复原状的搜索与检查任务，前提是接触历史能提供比视觉更可靠的进度标志。

**最终判断：**

- 这是一篇值得持续跟踪的“记忆模态设计”工作：它用清晰的任务构造、消融和延迟数据证明，VLA 的长期记忆不应等同于更多图像帧，物理交互信号可以成为更强、更省的事件日志。
- 但 83.3% 不能直接外推为通用接触操作能力；当前最合理的判断是把 FM-VLA 视为已验证的轻量 episodic force-memory 模块，而不是已经解决跨平台长时机器人记忆。

## 结果速览表

| 方法 | Cups | Buttons | Wipe | 平均 | 单步延迟 |
| --- | ---: | ---: | ---: | ---: | ---: |
| π0.5（无历史） | 72.2% | 11.1% | 0.0% | 27.8% | 60.7 ms |
| TA-VLA（短窗力） | 50.0% | 11.1% | 5.6% | 22.2% | 未报告 |
| π-MEM（视觉记忆，K=5） | 77.8% | 33.3% | 50.0% | 53.7% | 99.8 ms |
| FM-VLA（VAE，本文） | **100.0%** | **72.2%** | **77.8%** | **83.3%** | **64.0 ms** |

## 相关主题

- [[Long-Horizon Memory for Robot Policies]]
- [[Contact-Rich Manipulation and Adaptive Compliance]]
