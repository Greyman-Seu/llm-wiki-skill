---
id: "fd-vla-force-distilled-vision-language-action-model-for-contact-rich-manipulation"
slug: "fd-vla-force-distilled-vision-language-action-model-for-contact-rich-manipulation"
title: "FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation"
type: source
material_type: "paper"
source_type: paper
source_kind: "arxiv_html_url"
source_input: "https://arxiv.org/html/2602.02142v2"
created: "2026-09-05"
updated: "2026-09-05"
date: "2026-02-02"
publish_date: "2026-02-02"
source_url: "https://arxiv.org/abs/2602.02142"
html_url: "https://arxiv.org/html/2602.02142v2"
pdf_url: "https://arxiv.org/pdf/2602.02142"
code_url: ""
translation_url: "https://hjfy.top/arxiv/2602.02142"
arxiv_id: "2602.02142"
authors:
  - "Ruiteng Zhao"
  - "Wenshuo Wang"
  - "Yicheng Ma"
  - "Xiaocong Li"
  - "Francis E.H. Tay"
  - "Marcelo H. Ang Jr."
  - "Haiyue Zhu"
affiliation: "National University of Singapore; A*STAR Singapore Institute of Manufacturing Technology; Nanyang Technological University; Eastern Institute of Technology, Ningbo; Harvard University"
related_organizations:
  - "National University of Singapore"
  - "A*STAR Singapore Institute of Manufacturing Technology"
  - "Nanyang Technological University"
  - "Eastern Institute of Technology, Ningbo"
  - "Harvard University"
related_companies: []
domains:
  - "Physical/Embodied Intelligence"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - "Physical/Embodied Intelligence"
tags:
  - "vision-language-action"
summary: "FD-VLA 以 SmolVLA/SmolVLM-2 为基础，冻结预训练 VLM，用 Force Distillation Module 从当前视觉 token、机器人状态 token 与一个可学习 query 中生成单个预测力 token；训练期再用单层 MLP 编码真实力信号，以 L2 距离监督两种力表示对齐。预测力 token 与语言、视觉、状态 token 一起进入 VLM，定向注意力只允许控制流读取感知流，避免状态/力 token 反向污染视觉—语言表示；随后条件 flow-matching 动作专家生成一段连续动作。"
keywords:
  - "force distillation"
  - "contact-rich manipulation"
  - "sensor-free inference"
links:
  original: "https://arxiv.org/abs/2602.02142"
  arxiv: "https://arxiv.org/abs/2602.02142"
  html: "https://arxiv.org/html/2602.02142v2"
  pdf: "https://arxiv.org/pdf/2602.02142"
  project: ""
  github: ""
  code: ""
  hjfy: "https://hjfy.top/arxiv/2602.02142"
  doi: "https://doi.org/10.48550/arXiv.2602.02142"
raw_refs:
  - "https://arxiv.org/html/2602.02142v2"
  - "https://arxiv.org/pdf/2602.02142"
  - "https://arxiv.org/abs/2602.02142"
related_topics:
  - "vision-language-action"
  - "contact-rich-manipulation"
related_syntheses:
  - "force-touch-robot-policy-review"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2602.02142v2/overview.png"
images:
  - "https://arxiv.org/html/2602.02142v2/overview.png"
  - "https://arxiv.org/html/2602.02142v2/result.svg"
image_paths: []
status: analyzed
---

# FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation

## 太长不看

FD-VLA 用真实力信号做训练期教师，让一个由视觉与机器人本体状态条件化的可学习 query 预测潜在力 token；部署时不再需要力传感器，却在三项真实接触操作上达到 61.1% 平均成功率。真正值得记住的不是“无传感器也能估力”，而是把含噪物理模态蒸馏为任务相关中间表示，并用定向注意力保护冻结 VLM 的视觉—语言语义。证据仍局限于单台 UR5e、三项任务和 50 条示范/任务，尚不能视为通用触觉替代方案。

## 直观理解

把训练期的力传感器想成老师：机器人插插头、擦白板、按急停按钮时，老师告诉模型“这种视觉变化与关节状态通常对应怎样的接触”。模型不去回归一个必须物理精确的六维力数值，而是学出一个对动作有用的潜在力 token。部署时老师离场，模型只看双相机图像与本体状态生成这个 token，再让动作专家据此输出动作块；因此它更像学习了一个受力语义提示，而不是软件版力传感器。

![FD-VLA 训练与无力传感器推理流程](https://arxiv.org/html/2602.02142v2/overview.png)

*图 2：训练期真实力经轻量投影形成监督 token；单 query 从视觉与状态预测潜在力 token。推理期移除真实力支路，预测 token 与视觉、语言、状态一起供 VLM 和动作专家使用。*

## 核心信息

- **作者**：Ruiteng Zhao、Wenshuo Wang、Yicheng Ma、Xiaocong Li、Francis E.H. Tay、Marcelo H. Ang Jr.、Haiyue Zhu
- **作者单位**：National University of Singapore；A*STAR Singapore Institute of Manufacturing Technology；Nanyang Technological University；Eastern Institute of Technology, Ningbo；Harvard University
- **来源类型**：arxiv_html_url
- **输入来源**：https://arxiv.org/html/2602.02142v2
- **原文链接**：https://arxiv.org/abs/2602.02142
- **HTML 正文**：https://arxiv.org/html/2602.02142v2
- **PDF 地址**：https://arxiv.org/pdf/2602.02142
- **代码地址**：论文未提供
- **中英翻译地址**：https://hjfy.top/arxiv/2602.02142
- **发布日期**：2026-02-02
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** VLA 借助预训练视觉—语言模型把语义理解和机器人控制接到一起，但接触密集操作中的插入、持续擦拭和克服按钮弹簧阻力，关键状态往往藏在接触力、滑移与形变中，RGB 图像会受遮挡、光照和深度歧义影响。力/触觉传感器能直接观察这些物理交互，却昂贵、脆弱且并非所有机器人都配备；同时真实 wrench 还混有高频伪影与低频漂移，直接输入策略未必是最容易学习的表示。

**问题缺口：** 已有 Tactile-VLA 倾向把原始触觉较早接入 VLM，可能破坏已经对齐的视觉—语言语义；ForceVLA 把力 token 放在 VLM 之后并用 MoE 晚融合，虽然保护了骨干，却削弱视觉—状态—力的细粒度交互并增加结构复杂度。论文要同时解决三个矛盾：训练期怎样利用真实力监督、部署期怎样摆脱专用传感器、以及怎样让新控制模态进入预训练 VLM 又不造成灾难性干扰。

## 论文摘要（英文原文）

Force sensing is a crucial modality for Vision-Language-Action (VLA) frameworks, as it enables fine-grained perception and dexterous manipulation in contact-rich tasks. We present Force-Distilled VLA (FD-VLA), a novel framework that integrates force awareness into contact-rich manipulation without relying on physical force sensors. The core of our approach is a Force Distillation Module (FDM), which distills force by mapping a learnable query token, conditioned on visual observations and robot states, into a predicted force token aligned with the latent representation of actual force signals. During inference, this distilled force token is injected into the pretrained VLM, enabling force-aware reasoning while preserving the integrity of its vision-language semantics. This design provides two key benefits: first, it allows practical deployment across a wide range of robots that lack expensive or fragile force-torque sensors, thereby reducing hardware cost and complexity; second, the FDM introduces an additional force-vision-state fusion prior to the VLM, which improves cross-modal alignment and enhances perception-action robustness in contact-rich scenarios. Surprisingly, our physical experiments show that the distilled force token outperforms direct sensor force measurements as well as other baselines, which highlights the effectiveness of this force-distilled VLA approach.

## 论文摘要（中文翻译）

力感知是视觉—语言—动作（VLA）框架中的关键模态，因为它能为接触密集任务提供细粒度感知与灵巧操作能力。本文提出 Force-Distilled VLA（FD-VLA），在不依赖部署期物理力传感器的情况下，把力觉意识引入接触密集操作。其核心是 Force Distillation Module（FDM）：一个可学习 query token 在视觉观察和机器人状态条件下被映射为预测力 token，并与真实力信号的潜在表示对齐。推理时，这个蒸馏力 token 被注入预训练 VLM，使模型在保留视觉—语言语义完整性的同时进行力感知推理。该设计既降低了无力/力矩传感器机器人平台的部署成本与复杂性，也在进入 VLM 前增加一次力—视觉—状态融合，从而改善跨模态对齐和接触场景中的感知—动作鲁棒性。真实机器人实验中，蒸馏力 token 甚至优于直接使用传感器力测量的方案。

## 方法

**方法概述：** FD-VLA 以 SmolVLA/SmolVLM-2 为基础，冻结预训练 VLM，用 Force Distillation Module 从当前视觉 token、机器人状态 token 与一个可学习 query 中生成单个预测力 token；训练期再用单层 MLP 编码真实力信号，以 L2 距离监督两种力表示对齐。预测力 token 与语言、视觉、状态 token 一起进入 VLM，定向注意力只允许控制流读取感知流，避免状态/力 token 反向污染视觉—语言表示；随后条件 flow-matching 动作专家生成一段连续动作。

**核心机制：** FDM 把潜在力生成写成单 query 的上下文检索：可学习 token p 作为唯一 query，对由 p、视觉 token 和状态 token 拼成的上下文做多头注意力，再经残差、LayerNorm 与 FFN 得到预测力表示。训练时，真实力经轻量 MLP 投影到同一隐空间，以平方 L2 蒸馏损失约束预测 token；推理时删除真实力支路。预测力与状态属于控制流，只能读取视觉/语言感知流和允许的控制历史，而感知流不能读取控制流，因此冻结 VLM 的原有语义不会被新模态反向改写。最终 transformer 动作专家以条件 flow matching 学习动作块速度场，总损失是策略损失与加权蒸馏损失之和。

**方法拆解：** - 输入编码：主视角与腕部 RGB、语言指令和机器人本体状态分别编码并投影到 SmolVLM-2 的隐藏维度，预训练 VLM 参数保持冻结。
- 力蒸馏：单个 learnable query 对 query+视觉+状态上下文做多头注意力，得到任务相关的预测力 token；真实力只在训练期经 MLP 编码并提供 L2 特征监督。
- 定向融合：视觉/语言构成感知流，状态/预测力构成控制流；控制流可以读取感知流，感知流不能反向读取控制流，以保护预训练语义同时支持动作条件化。
- 动作生成：融合后的多模态表示进入 transformer action expert，以条件 flow-matching 目标预测长度为 H 的连续动作 chunk。
- 训练与部署解耦：每项任务收集 50 条带真实力记录的遥操作示范用于训练，部署阶段只保留相机与机器人状态，不再读取力传感器。

**关键要点：** - 论文预测的是与动作任务对齐的潜在力表示，不保证等价于可标定、可解释的物理六维力估计；它应被理解为 privileged-information distillation。
- 蒸馏 token 优于真实力 token 的结果说明，接触控制需要的是经过视觉—状态条件化和任务损失筛选的表示，而不是原始传感读数越真实越好。
- 定向注意力把“保护大模型语义”和“让控制 token 利用语义”拆成单向信息流，是低成本接入新机器人模态的可复用设计。

![FD-VLA 的 Force Distillation Module 与定向多模态融合](https://arxiv.org/html/2602.02142v2/overview.png)

*图 2：FDM 用一个 learnable query 从视觉与本体状态中检索接触相关特征，并在训练期对齐真实力 token；预测力 token 随后在不反向污染视觉—语言流的约束下参与多模态推理。*

## 结果

**核心结果：** - 真实机器人平台为 UR5e，使用 Azure Kinect 主相机和 RealSense D405 夹爪相机；三项任务分别是插头插座、擦净白板和按下急停按钮，每项 50 条示范、30 次独立评测。
- FD-VLA 三任务平均成功率为 61.1%，高于无力输入 SmolVLA 的 23.3%、DP3 的 11.1% 和无力输入 π0 的 46.7%；π0 参数量约为本文模型十倍。
- 直接加入原始力后，SmolVLA 平均提升 15.6 个百分点但仍比 FD-VLA 低 22.2 个百分点；π0 平均提升 20.0 个百分点但仍低 14.4 个百分点。
- FDM 消融中，无 FDM、使用真实力 token 的 FDM、使用 learnable token 的完整方案平均成功率依次为 38.9%、51.1%、61.1%；完整方案在 Plug/Clean/Press 上分别为 12/30、22/30、21/30。
- Clean Whiteboard 上 FD-VLA 达到 73.3%，至少比所有其他基线高 23.3 个百分点；对新背景与彩色光扰动的泛化仅给出定性结果，没有报告成功率。

**结果表：** | 对比/消融 | Plug | Clean | Press | 平均 |
| --- | ---: | ---: | ---: | ---: |
| SmolVLA（无力） | 未逐项报告 | 未逐项报告 | 未逐项报告 | 23.3% |
| DP3 | 未逐项报告 | 未逐项报告 | 未逐项报告 | 11.1% |
| π0（无力，约 10× 参数） | 未逐项报告 | 未逐项报告 | 未逐项报告 | 46.7% |
| 无 FDM，MLP 编码真实力 | 8/30 | 15/30 | 12/30 | 38.9% |
| FDM + 真实力 token | 12/30 | 17/30 | 17/30 | 51.1% |
| **FDM + learnable 蒸馏 token（FD-VLA）** | **12/30** | **22/30** | **21/30** | **61.1%** |

![FD-VLA 与无力、直接力输入基线在三项真实机器人任务上的成功率](https://arxiv.org/html/2602.02142v2/result.svg)

*图 6：Plug in Socket、Clean Whiteboard、Press Button 三项任务各评测 30 次；FD-VLA 在三项任务及平均成功率上均领先。*

## 洞察

**核心 insight：** - 最反直觉的结果是预测力 token 胜过真实力 token。这并不证明虚拟力比物理传感器准确，而是说明用于控制的充分统计量可以比原始测量更低维、更平滑，并提前融合视觉几何与运动状态。
- FD-VLA 展示了一条适用于稀缺部署模态的路线：训练期用昂贵传感器提供教师特征，推理期由普遍可得模态补全；可类比深度、触觉、事件相机或高精定位的跨模态蒸馏。
- 单向注意力掩码比简单冻结更细：冻结限制参数更新，掩码限制运行时信息流。二者一起把新控制模态的收益隔离在控制侧，降低基础 VLM 表示被扰动的风险。

**和已有方法的关系：** - 相对 Tactile-VLA 的早期直接融合，FD-VLA 不让控制 token 反向改写视觉—语言流；相对 ForceVLA 的 VLM 后 MoE 晚融合，它把预测力提前送进冻结 VLM，以换取更深的跨模态交互。
- 相对 ForceVLA、TA-VLA 或 FM-VLA 这类部署期仍使用 force/wrench 的路线，FD-VLA 把真实力降为训练期监督；代价是失去执行时对突发、不可由视觉与本体状态推断的接触事件的直接测量。
- 从学习范式看，它更接近 privileged-information distillation，而不是完整的无传感器力估计：蒸馏目标位于潜空间，最终评价也是任务成功率而非力预测误差。

**可借鉴点：** - 新模态接入预训练骨干时，可同时使用冻结骨干、零/轻量投影与定向注意力，把“谁能读谁”显式编码，而不是只靠联合训练自行学会隔离。
- 原始物理信号噪声大时，可把监督放在潜在任务表示而非精确数值回归上，再用下游动作损失筛选真正有用的信息。
- 评测跨模态蒸馏时必须同时保留三类对照：无教师模态、直接输入教师模态、蒸馏后的学生表示，否则无法判断收益来自信息本身还是表示与融合方式。

## 风险与判断

**局限：** - 只在单台 UR5e、三项相对短程的实验室任务上验证，每项仅 50 条示范；没有跨机器人、跨相机、跨工具或跨接触材料的迁移证据。
- 部署期没有真实力反馈，因此突发碰撞、隐藏卡阻、摩擦系数突变或纯视觉/本体状态不可辨识的接触无法被可靠观测；论文没有安全上限或异常检测机制。
- 论文没有报告力 token 对真实力的回归误差、校准性、时间响应和故障案例，不能据此把潜在 token 当作可解释的力估计器。
- 主实验只报告任务成功率；峰值接触力、插入力曲线、轨迹误差、物体/设备损伤和统计置信区间均缺失，无法判断更高成功率是否同时更安全。
- 视觉泛化只给定性观察而无数字；基线虽声明统一数据和优化预算，但论文缺少更丰富场景与显著性统计，61.1% 仍意味着约四成失败。

**适用场景：** - 训练设备可安装或临时借用力/力矩传感器，但量产部署平台不希望承担传感器成本与维护负担的插装、按压和表面接触任务。
- 接触状态大多能从相机变化、机器人位姿与关节状态间接推断，且环境分布相对受控的工业操作。
- 需要把新物理模态接入冻结 VLM、同时担心语义灾难性干扰的轻量 VLA 研究原型。

**最终判断：** - FD-VLA 是值得跟踪的模态蒸馏与融合设计：实验明确表明任务相关的预测力表示可以比直接输入原始力更有效，并显著降低部署硬件要求。
- 但它不是“力传感器已可被视觉替代”的证明。对安全关键、遮挡严重、接触突变或材料属性不可见的任务，真实力/触觉反馈仍不可替代；最合理的工程定位是低成本 force-aware prior，而不是闭环安全传感器。
- 后续最值得验证的是跨 embodiment 蒸馏、突发扰动下的失败恢复、预测 token 与真实接触事件的可解释性，以及与部署期低成本力估计混合后的上限。

## 结果速览表

| 对比/消融 | Plug | Clean | Press | 平均 |
| --- | ---: | ---: | ---: | ---: |
| SmolVLA（无力） | 未逐项报告 | 未逐项报告 | 未逐项报告 | 23.3% |
| DP3 | 未逐项报告 | 未逐项报告 | 未逐项报告 | 11.1% |
| π0（无力，约 10× 参数） | 未逐项报告 | 未逐项报告 | 未逐项报告 | 46.7% |
| 无 FDM，MLP 编码真实力 | 8/30 | 15/30 | 12/30 | 38.9% |
| FDM + 真实力 token | 12/30 | 17/30 | 17/30 | 51.1% |
| **FDM + learnable 蒸馏 token（FD-VLA）** | **12/30** | **22/30** | **21/30** | **61.1%** |

## 相关主题

- [[Vision-Language-Action]]
- [[Contact-Rich Manipulation and Adaptive Compliance]]
