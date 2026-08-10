---
id: "dm05-open-world-embodied-foundation-model"
slug: "dm05-open-world-embodied-foundation-model"
title: "DM0.5: 面向开放世界的通用具身智能基础模型"
type: source
material_type: blog
source_type: blog
source_kind: "blog"
source_input: "https://www.dexmal.com/blog/dm0.5"
source_url: "https://www.dexmal.com/blog/dm0.5"
html_url: "https://www.dexmal.com/blog/dm0.5"
code_url: "https://github.com/dexmal/opendm"
hf_url: "https://huggingface.co/collections/Dexmal/dm05"
publish_date: "2026-08-10"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - Physical/Embodied Intelligence
domains:
  - Physical/Embodied Intelligence
authors:
  - Dexmal 原力灵机
affiliation: "Dexmal 原力灵机（北京/重庆）"
related_organizations:
  - Dexmal
related_companies:
  - Dexmal
tags:
  - robot-foundation-model
keywords:
  - vision-language-action
  - robot-foundation-model
  - long-horizon-memory
  - embodied-reasoning
  - trajectory-alignment
  - open-world-generalization
raw_refs:
  - https://www.dexmal.com/blog/dm0.5
  - https://github.com/dexmal/opendm
  - https://huggingface.co/collections/Dexmal/dm05
  - https://www.modelscope.cn/collections/Dexmal/DM05
related_topics:
  - Vision-Language-Action
related_syntheses:
  - current-vla-landscape-foundation-control-memory-and-transfer
status: analyzed
maturity: release-blog
links:
  original: https://www.dexmal.com/blog/dm0.5
  project: https://www.dexmal.com/blog/dm0.5
  github: https://github.com/dexmal/opendm
  hf: https://huggingface.co/collections/Dexmal/dm05
  modelscope: https://www.modelscope.cn/collections/Dexmal/DM05
confidence: SOURCE
---

# DM0.5: 面向开放世界的通用具身智能基础模型

> 原力灵机（Dexmal）具身基础模型第二代，接棒 26 年 2 月的 DM0，主打走出实验室、走向开放世界。

## 太长不看

DM0.5 延续 VLA 架构（4B VLM 多模态主干 + 680M Action Expert），核心不是堆规模，而是四项系统增强：长历史上下文、具身推理（CoT）、动态动作对齐监督、数据质量清洗。换来的是开放环境 Zero-Shot 泛化、更长记忆、更鲁棒动作和多机型迁移，在 RoboChallenge Table30 v2 真机评测拿下 SOTA，并在 LIBERO / RoboTwin2.0 / R2R+RxR 导航基准上多项领先。

## 直观理解

可以把它看成"给 VLA 模型装了记忆 + 教会它边看边想下一步"：不再只是盯着当前画面输出动作，而是把过去 60 秒的关键视觉信息一起建模，训练时额外学 11 种自回归推理任务（任务规划、事件预测、动作生成），再通过动态路径匹配把"预测动作"和"真实轨迹进展"对齐，从而把采集节奏噪声滤掉、学到任务真正的动作规律。

## 核心信息

- **发布方**：Dexmal 原力灵机
- **来源类型**：blog（官方技术博客）
- **原文链接**：https://www.dexmal.com/blog/dm0.5
- **代码/权重**：GitHub(devmal/opendm)、HuggingFace、ModelScope
- **发布时间**：2026-08（访问）；DM0 于 2026-02 发布
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** VLA 过去两年让机器人走向视觉、语言、动作统一建模，但真实世界远高于一个 Demo。通用机器人基础模型不能只在固定场景做既定任务，必须理解指令、理解"接下来为什么这样做"，在不同相机视角、物体状态、环境、机器人本体和外部干扰下稳定执行，并在少量数据微调后快速适应新任务。

**问题缺口：** DM0 第一代能在可控环境学复杂操作，却还没有真正跨出实验室。要落地开放世界，需要解决长程依赖（很多任务不是单帧马尔可夫能搞定的）、语义理解、数据噪声（遥操作节奏差异）和动作连续性四个问题。

## 方法（基于博客描述）

**架构：** VLA 架构；4B VLM 作为多模态主干 + 680M Action Expert 生成连续动作。相比 DM0，DM0.5 在历史上下文、具身推理、动作监督、数据质量四个层面系统增强。

**三个关键设计：**

1. **Context Abstraction Layer（历史信息融合）**：放弃"每步只喂当前帧"的近似 Markov 策略，把过去若干关键帧与当前帧共同建模，提供最长 1 分钟的任务进程记忆（物体从哪拿起、工具是否用过、区域是否清理、是否经过地标）。训练时从当前时刻向前采样多个历史 slot，每个 slot 经时间/空间抽样合并为固定数量视觉 token，采用随机历史长度与历史增强，让模型同时适应长/短/无有效历史，历史上不可用时可退化回当前观测策略。

2. **Embodiment CoT Tasks（广泛具身推理）**：在机器人数据中引入 11 种自回归任务，除连续动作监督外强化指令遵循、动作预测和时序环境感知。分三类：
   - **任务规划**：当前任务阶段、前后步骤关系、任务进度（做到哪一步、下一步做什么）
   - **事件与环境预测**：任务边界、状态变化、未来关键事件
   - **动作生成**：未来动作或动作语义摘要，形成清晰的动作意图表征
   
   作用：把机器人数据从单一动作监督扩展成"指令理解 + 时序推理 + 动作生成"联合监督，模型不只学"当前画面→动作"，还学"在当前指令和任务进程下为什么这么动"。

3. **Trajectory Alignment Layer（动态动作匹配）**：同一任务多次采集常有不同执行节奏。若把预测动作与原始轨迹的固定时间点强绑定，模型会学到采集节奏而非任务规律。改为"轨迹进展对齐"：模型输出固定长度未来动作片段，数据侧保留细粒度真实轨迹，每个预测动作在真实轨迹中匹配一个严格单调递增的动作锚点（避免时间反转），用动态规划最小化所有匹配的总损失，并额外考虑相邻锚点的轨迹连续性。这降低遥操作时序相位噪声，让模型关注抓取、对准、接触、释放等任务关键动作。

**训练策略：** 多源数据对齐混合训练——机器人操作数据为主体，VLM 数据维持开放词表理解与空间推理，导航数据提供长指令理解与路径决策监督，视频理解数据增强时序建模。分组学习率：视觉语言主干用小 lr 降低灾难性遗忘，动作专家用大 lr 充分学动作分布；混合精度 + 分布式训练。

**推理：** Action Chunk 为单位，默认 10 个 diffusion/Flow Matching steps 生成 50 步 chunk。优化后 4090 单卡 10Hz、H100 单卡 20Hz。

## 数据

**数据构成（多源异构预训练）：**
- **机器人操作数据**：松灵 ALOHA、Galaxea R1 Lite、AgiBot G1、Franka Panda、UR5、ARX5，以及 Dexmal 自研双臂移动操作机器人
- **具身导航数据**：开源 VLM 导航 / 开放词汇导航数据集 + 自采 3D 重建场景导航
- **第一人称人类操作数据**：日常生产环境第一视角操作（手部交互、工具使用、细粒度原子动作）
- **通用多模态视觉语言数据**：图像/视频/视觉指令，自动生成管线增强空间定位、未来状态预测、动作后果分析、反事实推理

**数据清洗策略（五招）：**
1. 异常值去除：过滤明显超出物理范围或不满足运动连续性的样本，校验视觉/状态/动作一致性
2. 静止帧去除：移除长时间无状态或动作变化的静止片段，提高有效动作密度
3. 无价值动作去除：去掉执行不到位/意图不明确/与任务无关的片段，减少噪声监督
4. 动作模式去重：对 ALOHA 等平台等价关节组合去重，保持关节表示一致
5. 错误标注重标：自动化管线跨模态一致性校验，修正子任务标签，不丢数据

## 实验

**Zero-Shot 能力：** 从动作类型（8 类：pick/put/move/pull/cover/wipe/stack/press）与条件约束（7 类：color/shape/size/status/sequence/relative/absolute position）两个维度评测。在 Franka 平台对比 Pi0.5-Droid 与 DM0.5-Droid；在 Dexmal-Mirror 平台对比 DM0 与 DM0.5。DM0.5 在绝大多数维度显著优于 Pi0.5-Droid 与 DM0，动作覆盖面更广、基础操作更稳、指令遵循更强。

**真机测试（RoboChallenge Table30 v2）：** Generalist Setting（每机型一个统一模型）。DM0.5 取得 SOTA：整体 Success Rate 43%，综合 Score 54.42。盖章定位、按按钮等记忆型任务提升显著；双手托盘等双臂协同和插花等精细操作为较强视觉 Grounding 与末端控制能力。

**仿真测试：**
- **LIBERO**：Spatial 99.0 / Object 99.8 / Goal 99.6 / Long 97.4 / Average **99.0**（对比 π0 94.2、π0.5 96.9、OpenVLA-OFT 97.1、GR00T N1.7 97.0、StarVLA 97.9、ABot-M0 98.6、Being-H0.5 98.9、Cosmos Policy 98.5）
- **RoboTwin2.0**：Clean 93.6 / Randomized 93.3 / Average **93.5**（对比 π0 62.2、π0.5 79.8、Motus 87.9、ABot-M0 85.6、StarVLA 88.3、Being-H0.7 89.9、Qwen-VLA 86.7、LingBot-VA 92.2）

**导航测试：** R2R Val-Unseen NE 4.8（最低）、SR 59.7（最高）；RxR Val-Unseen 四项指标（NE / SR / SPL / nDTW）均第一。

## 洞察

**核心 insight：**

- **"加记忆 + 教推理 + 动态对齐动作"是 VLA 从演示走向通用化的系统模板**：长历史上下文解决"多帧状态依赖"、CoT 解决"为什么要这么动"、动态匹配解决"采集噪声"。三者合起来让模型从"当前帧驱动的操作策略"升级为"理解任务进程的通用策略"。
- **历史和推理是低成本高回报的监督来源**：不新增真机采集，而是从已有机器人数据里加自回归推理任务 + 历史 slot 采样，属于"把数据榨干"式的训练侧增益。
- **专注动作点而非时间点**：动态动作对齐把监督从"固定时间对齐"改成"轨迹进展对齐"，这一设计对遥操作数据普遍适用，是工程上很值得借鉴的一手。

**和已有方法的关系：**

- 相对 [[OpenVLA]] / [[π0.7]] 等 VLA 通用框架：DM0.5 同属 VLA，区别在于把"历史上下文 + 具身推理 + 动作对齐"作为显式系统设计整体纳入，而不只是扩大模型和数据。
- 相对 [[MEM]] / [[Long-Horizon Memory]] 方向：DM0.5 的长记忆（最长 60s）是"架构上直接支持历史输入"的实现，印证了长程记忆对 VLA 的价值。
- 相对 [[TurboVLA]]（RTX 4090 实时）：DM0.5 在 4090 单卡也给出了 10Hz 推理，属于能上消费级显卡的实时性水平，但主打的是通用泛化而非极致帧率。

**可借鉴点：**

- Context Abstraction Layer 用随机历史长度训练 + 可退化策略，是让模型同时适应长/短/无历史的安全设计，可迁移到任何序列决策模型。
- 把动作监督从"时间对齐"换成"轨迹进展对齐 + 单调匹配 + 动态规划"，可复用到各类遥操作 / 示教数据的策略学习，降低采集节奏偏差。
- 在机器人数据里注入自回归推理任务做联合监督，是低成本提升指令遵循与时序感知的有效手段。

<!-- confidence: MAPPED -->

## 风险与判断

**局限（基于博客公开信息）：**

- 这是发布博客而非完整论文，缺少消融实验细节、训练数据总量、去中心化评测方法与 error bar；"SOTA" 声明需以完整论文/后续复现为准。
- Zero-Shot 评测任务集（8 动作 × 7 条件）为自建，缺乏与第三方开放 benchmark 的严格横向对齐；与 Pi0.5-Droid 的对比只在 Franka 平台。
- Table30 v2 43% SR 说明真实开放环境仍有大量失败空间，"走向开放世界"是方向性陈述，不代表通用落地。
- 博客强调多机型迁移但未给量化数据；4B 主干相对更大 VLA 在极端复杂长程任务上的上限未知。

**适用场景：**

- 需要"一个模型处理多机器人本体 + 多任务"的通用 VLA 选型。
- 真实场景下对光照、视角、干扰鲁棒、并希望零样本跟自然语言指令操作的研究/产品。
- 长程多步任务（需要跨帧状态记忆）或遥操作数据量大的策略训练。

**最终判断：**

- 是**值得记入知识库**的具身基础模型发布：把历史上下文、具身推理、动作对齐三个设计做成一体，且真机 Table30 v2 拿到 SOTA，方向校验较强。
- 对当前具身智能的实际价值：**高**。它把三个相对分散的方向（long-horizon memory、VLA reasoning、action supervision）收敛到一个可运行的通用模型里，并开源权重，是可复现、可跟踪的路线参照。
- 跟踪价值：① 是否有完整论文/消融放出；② 4B 主干能否向更大规模迁移成功；③ 后续 DM 系列在开放世界评测（如 LIBERO、RoboChallenge）的持续表现；④ 开源后社区 fine-tune 到新机型、新任务的泛化证据。

## 结果速览表

| 维度 | 数值 / 结论 |
| --- | --- |
| 模型架构 | 4B VLM 主干 + 680M Action Expert |
| 长记忆 | 最长 60s 历史，1 分钟任务进程 |
| 具身推理 | 11 种自回归任务 × 3 类（规划/预测/动作） |
| 动作监督 | 动态轨迹进展对齐（单调匹配 + 动态规划） |
| 真机 Table30 v2 | SOTA：SR 43% / Score 54.42 |
| LIBERO | 平均 99.0（对比 π0 94.2） |
| RoboTwin2.0 | 平均 93.5（对比 π0.5 79.8） |
| R2R Val-Unseen | NE 4.8 / SR 59.7（最佳） |
| 推理速度 | 4090 单卡 10Hz / H100 单卡 20Hz |
| 备注 | 发布博客，非完整论文，消融/数据总量待补充 |

## 相关主题

- [[Vision-Language-Action]]
