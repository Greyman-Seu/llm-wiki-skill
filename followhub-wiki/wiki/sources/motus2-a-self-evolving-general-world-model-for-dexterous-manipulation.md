---
id: "motus2-a-self-evolving-general-world-model-for-dexterous-manipulation"
slug: "motus2-a-self-evolving-general-world-model-for-dexterous-manipulation"
title: "Motus2: A Self-Evolving General World Model for Dexterous Manipulation"
type: source
material_type: "paper"
source_type: "paper"
created: "2026-09-02"
updated: "2026-09-04"
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
summary: "Motus2 用一套共享参数同时实现动作策略、动作条件世界模拟器和进度价值评估器，并通过规划与模型式强化学习形成灵巧操作的闭环策略改进。"
links:
  original: "https://arxiv.org/abs/2608.30237"
  arxiv: "https://arxiv.org/abs/2608.30237"
  pdf: "https://arxiv.org/pdf/2608.30237"
  project: "https://motus-robotics.github.io/motus2"
  github: ""
  hjfy: "https://hjfy.top/arxiv/2608.30237"
  doi: "https://doi.org/10.48550/arXiv.2608.30237"
raw_refs:
  - "https://arxiv.org/html/2608.30237v1"
related_topics:
  - "vision-language-action"
  - "Long-Horizon Memory for Robot Policies"
related_syntheses:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2608.30237v1/motus2_overview.png"
images:
  - "https://arxiv.org/html/2608.30237v1/motus2_overview.png"
  - "https://arxiv.org/html/2608.30237v1/motus2_action_first_mask.png"
  - "https://arxiv.org/html/2608.30237v1/motus2_mbrl.png"
  - "https://arxiv.org/html/2608.30237v1/motus2_scaling_law.png"
  - "https://arxiv.org/html/2608.30237v1/value_traj_multitask_b.png"
image_paths: []
source_url: "https://arxiv.org/abs/2608.30237"
html_url: "https://arxiv.org/html/2608.30237v1"
pdf_url: "https://arxiv.org/pdf/2608.30237"
translation_url: "https://hjfy.top/arxiv/2608.30237"
status: analyzed
---
# Motus2: A Self-Evolving General World Model for Dexterous Manipulation

## 太长不看

Motus2 值得记住的不是“又一个更大的 VLA”，而是它用同一套共享参数实现 policy、simulator 和 evaluator，再把三者闭合成可规划、可更新策略的控制回路。受控实验中，第一视角预训练把五项真机任务平均成功率从 0% 提到 51%，机器人域 mid-training 进一步提到 84%；MBRL、长时记忆和触觉反馈也分别给出可量化增益。但这里的“自进化”仍是受控的模型式后训练，而不是机器人在开放环境中无限自主成长。

## 直观理解

它像一个会做“短推演”的机器人：先根据语言、视觉历史和本体状态一次提出多个动作块；再把每个动作送回同一个模型，想象执行后的视觉结果；最后由价值查询判断哪个分支更接近任务完成。普通控制只跑第一步，Best-of-N 规划会选最高价值动作，MBRL 则把高低价值候选反过来用于移动策略分布。这样，失败轨迹可以教模型“这样做会发生什么、结果有多差”，却不会被直接当成应模仿的动作。

## 核心信息

- **作者**：Hongzhe Bi、Zihao Zhou、Yihang Tang、Jingrui Pang、Shuhe Huang、Haitian Liu、Runqing Wang、Shuai Huang、Yichen Wang、Yiming Cheng、Ruowen Zhao、Zhenghua Li、Hengkai Tan、Xiaolong Liu、Jinhui Wan、Jiabao Liu、Min Zhao、Fan Bao、Jun Zhu
- **作者单位**：GensPI；Tsinghua University；BUAA；BIT
- **来源类型**：arxiv_html_url
- **输入来源**：https://arxiv.org/abs/2608.30237
- **原文链接**：https://arxiv.org/abs/2608.30237
- **HTML 正文**：https://arxiv.org/html/2608.30237v1
- **PDF 地址**：https://arxiv.org/pdf/2608.30237
- **项目页**：https://motus-robotics.github.io/motus2
- **中英翻译地址**：https://hjfy.top/arxiv/2608.30237
- **发布日期**：2026-08-31
- **主题域**：physical-embodied-intelligence
- **数据规模**：约 13 万小时第一视角语料；机器人域 mid-training 超过 100 小时
- **基础模型**：Wan 2.2-TI2V-5B 视频生成骨干
- **评测范围**：5 个主真机任务，另含 2 个 MBRL、2 个长时记忆、2 个触觉任务

## 背景与问题

**动机：** 通用灵巧操作不是“看一帧、出一个动作”就能解决的问题。双手会遮住物体，抓取、滑移、拧紧等接触状态仅靠视觉往往不可辨，决定成败的证据还可能出现在很早以前。更重要的是，模仿学习只告诉模型专家做了什么，不告诉它候选动作会导致什么后果、哪个后果更好，也无法有效利用昂贵采集过程中自然产生的失败和次优轨迹。Motus2 因此试图把感知、动作生成、后果预测、结果评估与策略更新统一起来。

**问题缺口：** 现有机器人 world model 常见两种断裂：一类只在视频生成器旁边增加动作头，虽然能预测和行动，却没有判断“任务是否推进”的评价接口；另一类把策略、动力学模型和价值模型拆成不同系统，表示与训练数据无法充分共享。若直接联合训练，还会出现动作 token 偷看未来画面的因果泄漏，以及把失败动作错误地当作模仿目标的问题。论文要解决的是：如何在一套参数中实现 action-first 的三个条件接口，并把不同质量轨迹路由给正确的监督目标。

## 论文摘要（英文原文）

General embodied agents should perceive, predict, act, evaluate, and improve within a unified system. World models have shown great promise in building such agents, yet existing models typically append an action output head to a world simulator, without coupling them into a closed decision-and-learning loop for policy improvement. We present Motus2, a self-evolving general world model for dexterous manipulation. Motus2 advances world modeling through model scaling and data scaling. For model scaling, a single model with shared weights exposes three control interfaces: a policy (world-action model), a simulator (action-conditioned world model), and an evaluator (value model). The policy proposes candidate action chunks, the simulator predicts their visual consequences, and the evaluator assesses the predicted outcomes. Their coupling forms a closed decision-and-learning loop for policy improvement. This formulation uses curated expert demonstrations for action learning, while failed and suboptimal interactions provide valuable evidence for dynamics modeling and value learning. For data scaling, Motus2 progresses from large-scale monocular egocentric data to synchronized stereo egocentric data, followed by robot-domain adaptation with robot trajectories and supplementary human-robot alignment data. Motus2 further studies global-autoregressive and hybrid-memory extensions of its sliding-window context, adds tactile feedback for contact-aware control, and is instantiated on a fully biomimetic platform with stereo vision, dual arms, dual dexterous hands, and tactile sensing. Together, egocentric data scaling and closed-loop general world model scaling provide a general path toward self-evolving dexterous manipulation.

## 论文摘要（中文翻译）

通用具身智能体应该在统一系统中同时完成感知、预测、行动、评估与持续改进。世界模型在构建这类智能体方面很有潜力，但现有模型通常只是给 world simulator 额外接一个动作输出头，并没有把它们耦合成一个用于策略提升的闭环决策与学习系统。Motus2 提出一种面向灵巧操作的自进化通用世界模型。Motus2 通过模型扩展和数据扩展推进 world modeling：在模型侧，同一共享参数同时暴露三种控制接口——policy（world-action model）、simulator（action-conditioned world model）和 evaluator（value model）；policy 提议候选动作块，simulator 预测其视觉后果，evaluator 评估预测结果，这三者耦合成一个闭环，用于策略改进。该框架用高质量专家示范学习动作，而失败和次优交互则为动力学建模与价值学习提供有效证据。在数据侧，Motus2 从大规模单目第一视角数据出发，进一步扩展到同步双目第一视角数据，再迁移到机器人域轨迹和补充的人机对齐数据；同时还研究了滑窗上下文的 global-autoregressive 与 hybrid-memory 扩展，引入触觉反馈用于接触感知控制，并在具备双目、双臂、双灵巧手和触觉传感的仿生平台上实现。

## 方法

**方法概述：** Motus2 从 Wan 2.2-TI2V-5B 视频扩散骨干出发，先学习单目视频，再用同步双目视频与人手动作做联合预训练，随后用机器人轨迹和人机对齐数据进入机器人域。mid-training 时，它把联合可见掩码切换为 action-first 掩码，并加入只读 value query，使同一模型按条件查询分别充当动作策略、动作条件未来模拟器和任务进度评估器。部署时可只生成动作，也可完整执行“候选动作—未来预测—价值排序”；MBRL 再利用排序结果更新动作相关参数。

**核心机制：** 核心不是简单并排三个输出头，而是用信息流约束实现因果分解。动作 token 只能读取语言、当前本体状态和干净的视觉历史，不能读取本 chunk 的未来视频或价值；未来视频 token 可以读取候选动作；只读价值查询又可以读取动作及其后果，但对其他 token 不可见。与此同时，loss gating 按轨迹含义选择监督：精选成功示范同时训练动作和未来预测，失败/次优/任务无关交互只训练模拟或价值，不让策略模仿坏动作。这使同一批异质交互数据能按“行为质量”和“信息价值”解耦使用。

**方法拆解：**

- **三级数据课程**：Stage 1 先用单目第一视角视频训练视觉通路（低分辨率 50 万步、高分辨率 34 万步）；Stage 2 用同步双目视频与 134 维人手动作联合训练 45 万步；随后以超过 100 小时机器人轨迹及人机对齐数据做机器人域 mid-training。
- **共享三接口**：world–action factor 生成可执行动作块，action-conditioned world factor 预测动作后的视觉 latent，value factor 把任务进度离散为 201 个类别；三者共享骨干，而非三个独立网络。
- **轨迹依赖监督路由**：只有精选成功轨迹开启动作监督；失败、次优和任务无关轨迹保留为真实转移证据及负价值样本，分别进入 simulation/evaluation mode。
- **闭环策略改进**：规划每轮产生候选、预测一个 chunk 的未来并按期望价值选优；DiffusionNFT 根据同组候选的标准化价值，把动作分布推向高价值样本、远离低价值样本，同时冻结视频骨干和 evaluator。
- **显式长时记忆**：默认滑窗固定成本但会遗忘；global autoregression 保留所有历史视觉 KV；hybrid memory 则保留首帧锚点、近期高分辨率帧和压缩记忆 token。
- **轻量触觉专家**：复用冻结骨干的中间动作与逐层 KV cache，以 30 Hz 将 48 步动作块分成 8 个子块滚动修正，并额外预测后续力信号来学习接触演化。

**关键要点：**

- “同一模型”靠的是条件因子和读取权限，而不是要求每次控制都生成视频；普通推理可以在动作因子处提前停止。
- 失败数据是否有用取决于监督目标：它不适合行为克隆，却非常适合教动力学和负价值。
- 规划只改善当前候选的选择，MBRL 才改变未来候选来自哪个策略分布；两者在实验中表现为可叠加增益。
- 长时历史与触觉不是装饰模块，而是分别处理视觉部分可观测和接触不可观测这两个灵巧操作的关键缺口。

![方法图](https://arxiv.org/html/2608.30237v1/motus2_overview.png)

*图 1：同一共享模型暴露 policy、simulator、evaluator 三个接口。*

![Action-first 因果掩码](https://arxiv.org/html/2608.30237v1/motus2_action_first_mask.png)

*图 2：动作不能读取当前 chunk 的未来视频或价值，模拟器和价值查询则按因果顺序逐级开放信息。*

![MBRL 闭环](https://arxiv.org/html/2608.30237v1/motus2_mbrl.png)

*图 3：候选动作经未来预测与价值评分后，进一步转化为 DiffusionNFT 策略更新。*

## 结果

**核心结果：**

- **预训练与机器人域迁移是主要增益来源**：在相同目标任务 SFT 下，WAN-SFT 与 π0.5 在五项真机任务上平均均为 0%；第一视角预训练初始化达到 51%，加入机器人域 mid-training 后达到 84%。Motus2 在 Place Ball、Attach Eraser、Screw Bulb、Multi-Finger、Put Phone 上分别为 100%、100%、90%、70%、60%，每项 20 次 rollout。
- **MBRL 比单纯规划贡献更大，但两者互补**：在 Put Phone 与 Multi-Finger 上，基线平均 65.0%；Best-of-N 规划为 67.5%，仅提高 2.5 个百分点；MBRL 达到 72.5%，提高 7.5 点；二者结合达到 75.0%。
- **完整历史明显优于压缩记忆**：global autoregression 在两个长时任务上，仿真平均 78%、真机平均 57.5%；hybrid memory 仅为 52% 和 25%。这说明早期视觉证据被压缩后，可能丢失决定最终动作的细节。
- **触觉对接触任务有稳定增益**：加入触觉专家后，Pull Out Paper Cup 从 65% 升到 75%，Tear Paper 从 55% 升到 70%，平均由 60.0% 升至 72.5%，同样每项 20 次 rollout。
- **双目第一视角数据呈现规模趋势**：在 2k、4k、10k、20k 小时嵌套子集上，held-out 人手动作预测误差随数据量单调下降，并在测量范围内近似服从对数数据规模关系；但论文没有把这条 proxy scaling law 直接等价为真机成功率 scaling law。

![双目第一视角数据 scaling law](https://arxiv.org/html/2608.30237v1/motus2_scaling_law.png)

*图 4：随着双目第一视角原始数据从 2k 增至 20k 小时，held-out 动作预测误差持续下降。*

## 洞察

**核心 insight：**

- Motus2 最值得保留的设计观念，是把“动作是否值得模仿”和“这段交互是否包含物理信息”分开。失败动作不是好 policy target，却是真实的动力学样本和负价值样本，这让昂贵机器人数据的废品率显著降低。
- 三接口共享参数的真正价值是表示复用和接口一致：policy 产生的动作天然就是 simulator 的条件，simulator 生成的未来又天然进入 evaluator；闭环不需要在三个异构模型之间额外对齐语义空间。
- 实验把“选择”和“学习”清楚地区分开：planning 在现有分布中挑动作，只带来 2.5 点；MBRL 改变动作分布，带来 7.5 点；组合后继续叠加。这比笼统宣称 world model 能提升策略更有解释力。
- 记忆实验给出一个反直觉结果：为效率而压缩历史 token 并不一定优于保留完整视觉 KV。对需要回忆具体位置或指令线索的任务，原始证据的可访问性可能比精巧的记忆压缩结构更重要。

**和已有方法的关系：**

- 相比 Motus 原先统一的 world–action policy 与 simulator，Motus2 新增 value evaluator，并用 Best-of-N 和 DiffusionNFT 把三者闭合；新增点不是更换骨干，而是把已有生成能力改造成决策与学习接口。
- 相比纯 VLA/SFT，Motus2 不要求所有训练数据都是专家动作；但它仍保留成功示范作为 policy anchor，因此不是抛弃模仿学习，而是在模仿之上增加模拟和价值监督。
- 相比把独立 world model 当作外部奖励器的路线，它强调一套参数内的条件查询；优势是共享表示，风险则是 simulator/evaluator 的误差可能高度相关，未必像独立模型那样形成有效制衡。
- 触觉部分更接近 T-Rex 式反应式专家：它不是把高频触觉塞进 5B 主干重算，而是借用中间动作和 detached KV 做局部修正，体现了“低频全局计划 + 高频接触反馈”的分层控制思路。

**可借鉴点：**

- 对任何联合预测—控制模型，都应显式画出 token 可见性并检查因果泄漏；action-first mask 是可直接复用的审计方式。
- 训练数据应按“能监督哪个因子”路由，而不是简单按成功/失败整体丢弃。这个原则也适用于离线 RL、异常轨迹和人类纠错数据。
- world-model planning 应采用短视野滚动重规划，并在每次真实观测后重新锚定；这能减少长 imagined rollout 的误差累积。
- 长时任务优先建立“关键原始证据不能丢”的基线，再考虑压缩记忆；本论文的 global autoregression 结果说明效率优化可能牺牲关键细节。
- 高频模态可作为轻量专家读取主干缓存，而非迫使所有模态统一频率进入大模型；这一结构适合触觉、力矩和声学等局部反馈。

![价值模型轨迹](https://arxiv.org/html/2608.30237v1/value_traj_multitask_b.png)

*图 5：失败轨迹的价值并非始终为低，而是在任务早期推进时上升、关键失败后下降，说明 evaluator 学到的是局部任务进度而非简单成功分类。*

## 风险与判断

**局限：**

- 主结果只有 5 个真机任务，MBRL、记忆和触觉消融又各自只覆盖 2 个任务，每项通常 20 次 rollout；论文报告成功率但没有置信区间，因此 2.5 点 planning 增益尤其需要更大样本验证。
- “自进化”目前指固定 simulator/evaluator 下的候选生成、价值评分和 DiffusionNFT 后训练，且 imagined horizon 只有一个 chunk；它不是开放世界在线终身学习，也没有证明多轮自举不会放大模型偏差。
- 价值读数是离散的相对进度信号，不是校准后的成功概率。policy、simulator、evaluator 又共享主干，模拟偏差和价值偏差可能相关，错误分支存在被共同高估的风险。
- 约 13 万小时是过滤前原始时长，部分双目数据来自采购；数据清洗后有效规模、复现成本和跨机构可获得性并不透明。2k–20k 小时的 scaling law 衡量的是人手动作预测误差，并非直接的机器人任务成功率。
- 论文自己指出触觉跨 embodiment 扩展受手套形变和手型差异限制：人手与机器人手并非几何同构，同一触觉手套模式无法直接迁移，削弱了大规模人类触觉数据的复用价值。

**适用场景：**

- 适合双臂灵巧手、长时部分可观测、接触状态关键且能收集成功/失败混合轨迹的任务；尤其适合把现有视频生成骨干升级为动作提议、短期模拟与价值排序的一体化系统。
- 不适合把它直接视为低成本通用机器人方案：完整系统依赖大规模视频预训练、机器人域数据、模拟与价值查询、多候选推理以及特定触觉硬件，实时成本和工程复杂度都高于普通行为克隆策略。

**最终判断：**

- 这是一篇值得持续跟踪的系统型工作：它把 policy、simulator、evaluator 的因果接口、异质轨迹路由和策略更新闭环讲得较完整，而且主要结论有受控实验支撑。
- 最强证据仍是预训练/mid-training 的 84% 主任务结果和触觉、记忆消融；“通用”“自进化”应保守理解为当前任务族中的工程闭环，而不是已解决开放世界泛化。

## 结果速览表

| 研究问题 | 对照 | 结果 | 读法 |
| --- | --- | --- | --- |
| 人类预训练与机器人域迁移 | WAN-SFT → Pretrain-SFT → Midtrain-SFT | 0% → 51% → 84% | 最大收益来自数据与域适配 |
| 策略自改进 | Motus2 → +Planning → +MBRL → +两者 | 65.0% → 67.5% → 72.5% → 75.0% | MBRL 增益大于只做选优 |
| 长时记忆（真机） | Hybrid → Global AR | 25.0% → 57.5% | 完整历史显著优于压缩记忆 |
| 触觉反馈 | 无触觉 → 有触觉 | 60.0% → 72.5% | 接触任务平均提升 12.5 点 |
| 双目数据扩展 | 2k → 20k 小时 | 验证误差单调下降 | 是动作预测 scaling，不等于真机 SR scaling |

## 相关主题

- vision-language-action
- Long-Horizon Memory for Robot Policies

## 相关页面

- [[Vision-Language-Action]]
- [[Long-Horizon Memory for Robot Policies]]
- [[当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据]]
