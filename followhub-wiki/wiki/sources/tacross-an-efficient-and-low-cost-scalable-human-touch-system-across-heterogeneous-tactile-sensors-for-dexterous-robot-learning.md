---
id: "tacross-an-efficient-and-low-cost-scalable-human-touch-system-across-heterogeneous-tactile-sensors-for-dexterous-robot-learning"
slug: "tacross-an-efficient-and-low-cost-scalable-human-touch-system-across-heterogeneous-tactile-sensors-for-dexterous-robot-learning"
title: "TACROSS: An Efficient and Low-Cost Scalable Human Touch System Across Heterogeneous Tactile Sensors for Dexterous Robot Learning"
type: source
material_type: "paper"
source_type: paper
source_kind: "arxiv_html_url"
source_input: "https://arxiv.org/html/2610.11945v1"
created: "2026-10-12"
updated: "2026-10-12"
date: "2026-10-08"
publish_date: "2026-10-08"
source_url: "https://arxiv.org/abs/2610.11945"
html_url: "https://arxiv.org/html/2610.11945v1"
pdf_url: "https://arxiv.org/pdf/2610.11945"
code_url: "https://tacross-touch-project.github.io/"
translation_url: "https://hjfy.top/arxiv/2610.11945"
arxiv_id: "2610.11945"
authors:
  - "Bo Chen"
  - "Huanzhang Hu"
  - "Junyang Ma"
  - "Bo Yue"
  - "Fangdi Yu"
  - "Haijier Chen"
  - "Xianxin Lai"
  - "Shuyu Pan"
  - "Zhen Yang"
  - "Xiaoquan Sun"
  - "Wenze Cui"
  - "Zhongliang Jiang"
  - "Shaopeng Liu"
  - "Jiayu Chen"
affiliation: "The University of Hong Kong; The Chinese University of Hong Kong (Shenzhen); Ocean University of China; Wuhan University; Wuhan Textile University; INFIFORCE"
related_organizations:
  - "The University of Hong Kong"
  - "The Chinese University of Hong Kong (Shenzhen)"
  - "Ocean University of China"
  - "Wuhan University"
  - "Wuhan Textile University"
  - "INFIFORCE"
related_companies: []
domains:
  - "physical-embodied-intelligence"
domain: "physical-embodied-intelligence"
primary_domain_slug: "physical-embodied-intelligence"
domain_slugs:
  - "physical-embodied-intelligence"
tags:
  - "tactile-transfer"
  - "human-demonstrations"
  - "dexterous-manipulation"
summary: "TACROSS 将低成本人类触觉采集、跨传感器接触语义对齐和 robot-grounded ACT 策略训练合成一条完整管线，核心贡献是同时处理 Sensing Gap 与 Action Gap：人类触觉帮助学表示，机器人执行动作帮助锚定策略。"
keywords:
  - "tactile representation"
  - "human-to-robot transfer"
  - "contact semantics"
links:
  original: "https://arxiv.org/abs/2610.11945"
  arxiv: "https://arxiv.org/abs/2610.11945"
  html: "https://arxiv.org/html/2610.11945v1"
  pdf: "https://arxiv.org/pdf/2610.11945"
  project: "https://tacross-touch-project.github.io/"
  github: ""
  code: "https://tacross-touch-project.github.io/"
  hjfy: "https://hjfy.top/arxiv/2610.11945"
  doi: "https://doi.org/10.48550/arXiv.2610.11945"
raw_refs:
  - "https://arxiv.org/html/2610.11945v1"
  - "https://arxiv.org/pdf/2610.11945"
  - "https://tacross-touch-project.github.io/"
  - "https://arxiv.org/abs/2610.11945"
related_topics:
  - "tactile-representation"
  - "contact-rich-manipulation"
  - "human-to-robot-transfer"
related_syntheses: []
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2610.11945v1/Fig1_TACROSS_overview_curves.png"
images:
  - "https://arxiv.org/html/2610.11945v1/Fig1_TACROSS_overview_curves.png"
  - "https://arxiv.org/html/2610.11945v1/Fig3_Tactile_Pipeline_20260917.png"
  - "https://arxiv.org/html/2610.11945v1/Fig4_contact_semantics_training_labels.png"
  - "https://arxiv.org/html/2610.11945v1/tacross-four-tasks-horizontal-legend.png"
image_paths: []
status: analyzed
---

# TACROSS: An Efficient and Low-Cost Scalable Human Touch System Across Heterogeneous Tactile Sensors for Dexterous Robot Learning

## 太长不看

TACROSS 用 10.86 美元的压阻手套快速采集人类触觉示范，并通过接触事件语义而非原始 taxel 数值对齐到电容式 Revo2 机器人手，再由少量机器人执行示范提供动作真值。

## 直观理解

可以把 TACROSS 理解成一个“触觉翻译器 + 机器人锚定策略”：人类手套和机器人手指传感器说不同的物理语言，系统先把双方都翻译成“哪里接触、多强、处于抓取/加载/滑移/释放哪个阶段”的公共语义，再让这些语义帮助 ACT 学会机器人的真实动作；人类数据提供触觉知识，机器人数据决定最终动作标签。

![主要图](https://arxiv.org/html/2610.11945v1/Fig1_TACROSS_overview_curves.png)

*主要图*

## 核心信息

- **作者**：Bo Chen、Huanzhang Hu、Junyang Ma、Bo Yue、Fangdi Yu、Haijier Chen、Xianxin Lai、Shuyu Pan、Zhen Yang、Xiaoquan Sun、Wenze Cui、Zhongliang Jiang、Shaopeng Liu、Jiayu Chen
- **作者单位**：The University of Hong Kong; The Chinese University of Hong Kong (Shenzhen); Ocean University of China; Wuhan University; Wuhan Textile University; INFIFORCE
- **来源类型**：arxiv_html_url
- **输入来源**：https://arxiv.org/html/2610.11945v1
- **原文链接**：https://arxiv.org/abs/2610.11945
- **HTML 正文**：https://arxiv.org/html/2610.11945v1
- **PDF 地址**：https://arxiv.org/pdf/2610.11945
- **代码地址**：https://tacross-touch-project.github.io/
- **中英翻译地址**：https://hjfy.top/arxiv/2610.11945
- **发布日期**：2026-10-08
- **主题域**：physical-embodied-intelligence

## 背景与问题

**动机：** 接触密集灵巧操作中的抓取发生、加载、稳定性、滑移和释放常常被 RGB 视觉遮蔽；直接在目标机器人上采触觉又占用机械臂、灵巧手和传感器，带来标定、复位与运营成本。论文把问题放在真实数据工程约束下：机器人遥操作每小时约 40 条 episode、整套采集设备约 12000 美元，而人类手套可把采集从机器人可用性中解耦。

**问题缺口：** 论文要解决两个叠加的错位。第一是 Sensing Gap：人类侧是压阻手套，机器人侧是电容式 Revo2，双方在换能原理、taxel 布局、分辨率、量纲、噪声、漂移、滞回和时间响应上不同，同数值不等于同接触，同接触也会激活不同通道。第二是 Action Gap：人手重定向目标不是 Revo2 真实执行过的动作，形态学和运动学差异使其只能当伪标签；若当作真值监督，会把重定向误差写入策略。

## 论文摘要（英文原文）

Collecting tactile demonstrations on robots is costly and slow, motivating the use of lower-cost human tactile gloves for scalable data collection. However, human capacitive/piezoresistive gloves and robotic tactile sensors differ fundamentally in transduction principle, sensor layout, spatial resolution, and dynamic response, making alignment of raw sensor channels ill-posed. To address this problem, we present TACROSS, a scalable system for learning from human touch and transferring it to robots that bridges this heterogeneity by aligning tactile streams at the level of contact events rather than raw sensor values. The hardware component of TACROSS integrates a piezoresistive glove with five layers and a cost of USD 10.86 with 285 sensing points. To align contact semantics, we design canonicalizers and residual adapters that map heterogeneous signals into a shared tactile latent with 256 dimensions via a temporal Transformer with attention across fingers. We further introduce a robot-grounded policy learning scheme in which robot demonstrations provide the sole source of ground-truth action supervision, while human demonstrations support tactile representation learning and provide confidence-weighted auxiliary supervision through valid retargeted hand targets. We evaluate our system on four contact-rich manipulation tasks. Compared to conventional teleoperation, our proposed system achieves a 3.5-fold efficiency improvement while reducing demonstration acquisition equipment cost by 95.7%. We will open-source the TACROSS hardware and software system and publicly release a tactile dataset comprising over 150 hours of recordings.

## 论文摘要（中文翻译）

机器人触觉示范采集昂贵且缓慢，促使研究者使用更便宜的人类触觉手套。然而人类电容/压阻手套与机器人触觉传感器在换能原理、布局、空间分辨率和动态响应上根本不同，直接对齐原始通道是病态问题。TACROSS 在接触事件层面而非原始数值层面对齐触觉流；硬件端包含五层压阻手套、285 个 sensing points 和 10.86 美元 BOM；学习端用 canonicalizer、残差 adapter 和跨手指时序 Transformer 得到 256 维共享 tactile latent。机器人示范是唯一动作真值，人类示范用于触觉表示学习和置信度加权辅助监督。四项接触密集任务上，系统相对传统遥操作取得 3.5 倍采集效率提升，采集设备成本下降 95.7%。

## 方法

**方法概述：** TACROSS 将低成本人类触觉采集、跨传感器接触语义对齐和 robot-grounded ACT 策略训练合成一条完整管线，核心贡献是同时处理 Sensing Gap 与 Action Gap：人类触觉帮助学表示，机器人执行动作帮助锚定策略。

**核心机制：** TACROSS 用“公共接触语义 + 机器人动作锚定”替代原始通道匹配。每个域先把异构触觉转换成带 mask 的解剖区域 contact field，字段包括接触概率、相对强度及其变化、持续时间、面积、压力中心、不稳定性代理和置信度，并用四级强度与六个因果阶段描述事件。域专属浅层 adapter 再把 masked 语义映射到共同 token；共享的 causal temporal Transformer 和跨手指 Transformer 从 16 帧×5 指的 80 个 token 中建模接触演化与手指协同，输出 256 维 hand latent。训练目标同时包含 multi-positive InfoNCE、接触/强度/阶段预测、时间正则和 domain-adversarial loss。最终 ACT 只把机器人真实动作作为动作真值，人类 HaMeR + 几何重定向结果按置信度和有效性 mask 作为辅助监督。

**方法拆解：**
- 硬件与同步：五层压阻手套包含 12×15 掌区和五个 3×7 指区，宣称 285 个物理 sensing points；矩阵复用、12-bit ADC 和腕部控制器约 150 Hz 输出，系统记录原始/校准触觉、RGB、姿态、时间戳、样本年龄、mask 与伪动作。校准时逐通道扣除基线、乘增益、裁剪并保留 validity mask，缺失通道不与真实零接触混淆；多模态按原生时间戳选取不晚于当前参考时间的最新样本。
- 接触 canonicalizer：按解剖区域而非通道编号聚合双方信号，生成同序字段 [p,F,ΔF,d,A,u,v,ρ,γ]，其中 F 是相对强度而非绝对校准力，ρ 是不稳定性代理而非直接滑移测量；mask 显式标注不支持字段、缺失手指和无效区域，防止把缺失当作零接触。
- 域内 adapter 与共享编码：human/robot 各自 adapter 接收 masked fields、mask、强度/阶段 embedding、区域上下文和 anatomical identity；共享编码器用 temporal attention 建模 16 帧事件演化，用 inter-finger attention 建模五指协同，每支 2 层、4 head、128 维，由 learned hand token 输出 256 维 latent。
- 对齐与监督：正样本不需要人机逐帧同步，而按任务/物体、primitive、活跃手指、强度和阶段选择语义兼容窗口；InfoNCE 拉近兼容 latent、推开 phase/force hard negatives，接触、强度回归/ ordinal、阶段、时间正则和 domain-adversarial 七项 loss 权重依次为 1、1、0.5、0.5、1、0.2、0.1。
- robot-grounded 策略：HaMeR 恢复 21 个人手 3D keypoint，转到以腕为中心、按手掌宽归一的正交 palm frame；非拇指关节按用户 open/fist 标定归一，拇指包含屈曲/外展与拇食指尖相对位置，映射到 Revo2 六个主动通道并经过滤波、变化限幅与关节边界。ACT 使用 3 个 240×320 RGB 视角、本体状态和 256→512 投影后的 tactile latent，在 15 Hz 预测 60 步、8 或 13 维动作 chunk；tactile encoder 前 20000 step 冻结后再低学习率联合训练。

**关键要点：**
- 跨传感器触觉迁移的关键对象是接触事件语义，不是 taxel 数值；mask 与阶段/强度监督让压阻手套和电容 Revo2 能进入同一控制相关表示空间。
- 人类数据不能直接替代机器人动作标签；TACROSS 用人类触觉扩表示、用机器人动作锚定策略，是比“伪动作当真值”更稳妥的混合监督。

![方法图](https://arxiv.org/html/2610.11945v1/Fig4_contact_semantics_training_labels.png)

*方法图*

## 结果

**核心结果：**
- 采集效率：Robot-only、Ego-R、Ego-V 分别约 40、112、140 episodes/h，对应 1.00×、2.80×、3.50×；设备成本分别约 12000、2150、520 美元，Ego-V 相对 Robot-only 低 95.7%。
- 语料规模：三种采集配置总计 183.95 h、24913 条 recorded episodes、22486 条 valid；其中人类 Ego-R+Ego-V 合计 159.09 h、23677 条 recorded、21412 条 valid。
- 固定 30 条机器人示范时，150 条人类示范让四任务平均成功率从 Robot-only 51.3% 提升到 full TACROSS 91.9%（+40.6 pp）；无人类触觉为 73.1%，无 contact-semantic alignment 仅 49.4%。
- 固定 15 条机器人示范并把人类示范从 0 增至 90，四任务平均成功率从 32.5% 提升到 85.6%；105 条 robot-only 为 88.1%，说明人类数据能大幅降低机器人示范需求但并未完全消除。
- 单独 T4 水果序列中，92 条 robot-only 为 38/40（95.0%）；50 robot+50 Ego 为 37/40（92.5%），机器人示范减少 45.7%，估计采集时间从 158.8 降至 110.3 min（-30.6%）。

**结果表：**

| 配置 | 机器人:人类 | 平均成功率 | 关键解释 |
|---|---:|---:|---|
| Robot-only | 30:0 | 51.3% | 只有少量真实机器人动作，触觉/人类经验不足 |
| 去人类触觉 | 30:150 | 73.1% | 人类视觉/动作语料有帮助，但缺触觉增益 |
| 去 contact-semantic alignment | 30:150 | 49.4% | 异构触觉直接混合反而干扰学习 |
| Full TACROSS | 30:150 | 91.9% | 语义对齐 + robot-grounded 监督最有效 |
| Full TACROSS | 16:160 | 88.1% | 机器人示范减少 46.7%，仍保持高性能 |

| 采集方式 | 速度 | 系统成本 | 语料 |
|---|---:|---:|---|
| Robot-only | 40 eps/h；1.00× | $12,000 | 24.86 h，1074 valid |
| Ego-R | 112 eps/h；2.80× | $2,150 | 89.49 h，11669 valid |
| Ego-V | 140 eps/h；3.50× | $520 | 69.60 h，9743 valid |

![结果图](https://arxiv.org/html/2610.11945v1/tacross-four-tasks-horizontal-legend.png)

*结果图*

## 洞察

**核心 insight：**
- TACROSS 的核心启发是把“传感器等价性”降级为“控制事件等价性”：抓取发生、加载、稳定、疑似滑移和释放对策略更关键，也更可能跨压阻/电容硬件稳定存在。
- 触觉数据扩充与动作监督应分层处理。人类示范解决触觉事件覆盖，机器人示范解决可执行动作分布；把两者都塞进同一个 action loss 会混淆“看过什么接触”和“应该怎么动”。
- 有效性 mask 是跨硬件表示的基本组件，因为它区分“没有接触”“传感器不支持”“通道坏了”和“重目标无效”，这些状态对学习的意义完全不同。

**和已有方法的关系：**
- 相对 Heterogeneous Tactile Transformer 等跨触觉传感器表示工作，TACROSS 特别面对压阻与电容两类换能原理和完整人手—机器人手差异，并把表示直接接入真实 ACT 策略。
- 相对 ForceMimic 等 human data 系统，TACROSS 不追求人类动作直接可执行，而是用机器人示范作为唯一 action ground truth，从而明确处理 Action Gap。

**可借鉴点：**
- 为异构机器人传感器设计 canonical semantic field：接触概率、强度变化、持续时间、面积、压力中心、阶段与置信度 mask，比通道级 distillation 更可迁移。
- 用 multi-positive contrastive learning 处理非同步人机示范：不要求同帧配对，而按任务、primitive、活跃手指和接触阶段选择兼容窗口。
- 把人类手部动作显式降级为 confidence-weighted pseudo-label，同时保留少量 robot action anchor，可减少跨本体动作误差。

## 风险与判断

**局限：**
- 系统仍依赖机器人示范和针对 Revo2/人手几何的标定重定向；论文自己承认尚未泛化到其他机械手，不能视为零机器人数据方案。
- 四任务全部集中于桌面小物体、液体和水果操作，任务约束由作者定义；尚缺跨任务泛化、扰动鲁棒性、失败恢复和安全接触力上限报告。
- 论文存在报告不一致：摘要/正文称 150+ 小时人类数据，Table II 可得 159.09 h；正文 1:10 full TACROSS 写 88.3%，但该表四个任务均值为 88.1%；同时宣称 285 sensing points 却说明每帧输出 256 值，需要开源代码澄清物理点、有效通道和 streamed channel 的关系。
- 对齐正样本依赖任务、物体、primitive、活跃手指、强度与阶段元数据，domain-adversarial 也不能保证语义完备；若人类与机器人接触分布差异过大，共享 latent 可能学到伪相关。

**适用场景：**
- 低成本扩充接触丰富灵巧操作数据，尤其液体转移、点胶、移液和易损物体抓放等视觉难以判断接触状态的桌面任务。
- 机器人本体仍有少量可遥操作示范、但大规模采集昂贵的场景，可用人类 Ego 数据提升表示并降低机器人示范量。

**最终判断：**
- 这篇论文的工程路线有价值，但应按 embodiment-specific transfer system 理解，而不是通用跨机器人触觉基础模型。结论支持 contact-semantic alignment 和 robot action anchoring，可借鉴；跨硬件、跨任务和安全性仍待更强验证。

## 结果速览表

| 配置 | 机器人:人类 | 平均成功率 | 关键解释 |
|---|---:|---:|---|
| Robot-only | 30:0 | 51.3% | 只有少量真实机器人动作，触觉/人类经验不足 |
| 去人类触觉 | 30:150 | 73.1% | 人类视觉/动作语料有帮助，但缺触觉增益 |
| 去 contact-semantic alignment | 30:150 | 49.4% | 异构触觉直接混合反而干扰学习 |
| Full TACROSS | 30:150 | 91.9% | 语义对齐 + robot-grounded 监督最有效 |
| Full TACROSS | 16:160 | 88.1% | 机器人示范减少 46.7%，仍保持高性能 |

| 采集方式 | 速度 | 系统成本 | 语料 |
|---|---:|---:|---|
| Robot-only | 40 eps/h；1.00× | $12,000 | 24.86 h，1074 valid |
| Ego-R | 112 eps/h；2.80× | $2,150 | 89.49 h，11669 valid |
| Ego-V | 140 eps/h；3.50× | $520 | 69.60 h，9743 valid |

## 相关主题

- [[Tactile Representation]]
- [[Contact-Rich Manipulation and Adaptive Compliance]]
- [[Human-to-Robot Transfer]]
