---
id: "force-touch-robot-policy-review"
slug: "force-touch-robot-policy-review"
title: "机器人策略中的力觉与触觉：从信号语义到闭环控制"
type: synthesis
created: "2026-09-02"
updated: "2026-09-10"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "tactile-representation"
  - "contact-rich-manipulation"
summary: "综合十四篇材料，按力/触觉信号的角色和时间尺度重整机器人策略路线：传感与采集、表示与适配、执行期反馈、事件记忆与后果预测，以及由低层控制器落实的力位与柔顺接口。"
judgment: "力觉与触觉不是可以统一拼接的一个额外模态，而是四类不可互换的策略变量：实测观测、蒸馏先验、预测后果和控制目标。当前最可信的系统原则是先明确力信号的语义与有效时域，再让学习策略负责任务条件化和慢时标决策、让高频反馈或经典控制器负责动作块内的接触稳定；现有证据尚未证明单一端到端模型能同时替代跨硬件表示、持续适配、实时安全闭环和力控制器。"
source_slugs:
  - "tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks"
  - "2606.29948-heterogeneous-tactile-transformer"
  - "2410.07554-forcemimic-force-centric-imitation-learning-with-force-motion-capture-system-for-contact-rich-manipulation"
  - "2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force"
  - "fd-vla-force-distilled-vision-language-action-model-for-contact-rich-manipulation"
  - "2503.02881-reactive-diffusion-policy-slow-fast-visual-tactile-policy-learning-for-contact-rich-manipulation"
  - "t-rex-tactile-reactive-dexterous-manipulation"
  - "2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback"
  - "foar-force-aware-reactive-policy-for-contact-rich-robotic-manipulation"
  - "2605.11048-forceflow-learning-to-feel-and-act-via-contact-driven-flow-matching"
  - "fm-vla-force-based-memory-for-vision-language-action-models-in-contact-rich-manipulation"
  - "facet-0"
  - "adaptive-compliance-policy-learning-approximate-compliance-for-diffusion-guided-control"
  - "2609.05832-cr-vla-force"
topic_slugs:
  - "tactile-representation"
  - "contact-rich-manipulation"
  - "vision-language-action"
  - "long-horizon-memory-for-robot-policies"
claims:
  - "实测力、预测力、期望力和蒸馏力 token 的含义不同，不能用“是否用了 force”作为统一分类或比较依据。"
  - "力觉收益首先取决于时间接口：反馈必须在动作仍可修改时进入策略，长期接触历史则应被编码为事件记忆而非无限扩张的短窗。"
  - "对持续接触和安全敏感任务，慢策略给任务与物理目标、高频控制器落实柔顺和力跟踪，是当前证据最完整的工程分工。"
  - "传感器部署成本可以通过训练期蒸馏降低，但由视觉与状态预测的力先验不能替代对突发碰撞、隐藏卡滞和摩擦突变的真实测量。"
  - "数据采集分布、坐标校准和控制接口的一致性，可能比融合网络本身更早决定力信号是否有用。"
  - "现有论文的成功率、力误差和任务得分不能直接横向排名；平台、传感器、动作频率、任务难度和控制栈均不一致。"
open_questions:
  - "能否在训练时未见的机器人与触觉硬件上，贯通共享表示、旧数据 replay、在线反馈和高频柔顺控制？"
  - "实测历史、预测后果、期望力与蒸馏先验应如何联合建模，同时避免语义混淆和视觉模态压制？"
  - "在等算力、等采样率和等动作时域下，快速解码器、快慢专家、流式单专家和经典高频控制器谁更稳？"
  - "如何建立同时报告任务成功、峰值力、力跟踪误差、接触稳定、扰动恢复、延迟和硬件成本的统一基准？"
  - "学习策略输出错误期望力或错误接触后果时，低层安全约束如何检测、拒绝并恢复？"
confidence: INFERRED
---

# 机器人策略中的力觉与触觉：从信号语义到闭环控制

> 综合 14 篇材料 | 更新日期：2026-09-10

## 当前判断

这批工作共同推翻了一个过于简单的叙事：给视觉策略多加一条 force/tactile 输入，并不会自然得到可靠的接触能力。接触信号是否有价值，取决于三个问题是否被同时回答：它代表什么物理语义、覆盖哪个时间尺度、最终由哪个执行接口把它变成动作。

更准确的系统图景是：力/触觉先解决“感什么、怎样采集和跨硬件表示”，再解决“怎样接入已有策略且不遗忘”；进入执行阶段后，又分成动作块内即时反馈、跨 episode 的事件记忆、候选动作的接触后果预测，以及由策略直接输出期望力或柔顺参数。它们使用相近的传感器，却不是同一个学习问题。

现阶段最稳健的工程路线不是让一个低频大模型包办所有闭环，而是分层：学习策略负责语义理解、任务阶段、动作与物理目标；高频触觉模块、反应式规则或导纳/阻抗控制器负责接触瞬态。FD-VLA 证明真实力可以在训练期充当教师，但它也划清了边界：预测出的力先验不是安全传感器，无法可靠观测视觉与本体状态中不存在的突发接触。

## 先区分四种“力”

| 信号角色 | 它回答什么 | 代表材料 | 能做什么 | 不能据此声称什么 |
| --- | --- | --- | --- | --- |
| 实测观测 | 机器人现在接触了什么、接触历史怎样变化？ | [[2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force|MuSe]]、[[2503.02881-reactive-diffusion-policy-slow-fast-visual-tactile-policy-learning-for-contact-rich-manipulation|RDP]]、[[foar-force-aware-reactive-policy-for-contact-rich-robotic-manipulation|FoAR]]、[[2605.11048-forceflow-learning-to-feel-and-act-via-contact-driven-flow-matching|ForceFlow]]、[[fm-vla-force-based-memory-for-vision-language-action-models-in-contact-rich-manipulation|FM-VLA]] | 发现视觉不可辨的接触、滑移、卡滞与事件进度 | 原始读数越多越好，或静态拼接就足够 |
| 蒸馏先验 | 仅凭视觉与状态，当前大概处于何种受力语境？ | [[fd-vla-force-distilled-vision-language-action-model-for-contact-rich-manipulation|FD-VLA]] | 降低部署传感器成本，为动作模型提供任务相关接触提示 | 替代突发碰撞检测或得到可校准的六维力估计 |
| 预测后果 | 候选动作将引发什么接触结果？ | [[2605.11048-forceflow-learning-to-feel-and-act-via-contact-driven-flow-matching|ForceFlow]]、[[facet-0|Facet-0]] | 用辅助预测塑造动作表示，或让 critic 按接触质量选择动作 | 预测 wrench 已被控制器直接执行，或预测一定物理准确 |
| 控制目标 | 机器人希望施加多大力、在哪个方向让步？ | [[adaptive-compliance-policy-learning-approximate-compliance-for-diffusion-guided-control|ACP]]、[[2410.07554-forcemimic-force-centric-imitation-learning-with-force-motion-capture-system-for-contact-rich-manipulation|ForceMimic]]、[[2609.05832-cr-vla-force|CR-VLA-Force]] | 把期望力、虚拟目标或刚度交给成熟低层控制器 | 学习策略自身已经具备高频稳定性或形式化安全保证 |

这四类变量可以同时出现在一个系统中，但训练目标、误差含义与安全责任不同。综述和基准若只按“用了力/没用力”分组，会把真正决定效果的接口差异抹掉。

## 从传感到执行的六层路线

| 层 | 核心问题 | 代表材料 | 已有证据 | 主要缺口 |
| --- | --- | --- | --- | --- |
| 传感设计 | 感知位置、覆盖、分辨率和物理量怎样选择？ | [[tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks|Tactile Genesis]] | 受控仿真表明覆盖面积常比局部高分辨率更重要，per-taxel 力/力矩是有竞争力的默认项 | 大规模真机、耐久、漂移与成本数据 |
| 数据与表示 | 怎样自然采集力位示范，并跨异构硬件复用表示？ | [[2410.07554-forcemimic-force-centric-imitation-learning-with-force-motion-capture-system-for-contact-rich-manipulation|ForceMimic]]、[[2606.29948-heterogeneous-tactile-transformer|HTT]] | 手持 ForceCapture 降低采集门槛；HTT 用 1.6M 同步帧对齐四类传感器，并测试未见触觉指尖 | 采集到部署的动力学偏移；表示迁移尚未贯通控制层 |
| 策略适配 | 旧数据没有力标签时怎样吸收新模态且保留旧能力？ | [[2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force|MuSe]]、[[fd-vla-force-distilled-vision-language-action-model-for-contact-rich-manipulation|FD-VLA]] | replay、缺失模态 mask 和未来预测能缓解遗忘；训练期真实力可监督部署期潜在力先验 | 多模态连续到来时的成本；无传感器方案的不可观测接触 |
| 执行期反馈 | 最新接触怎样在动作执行前改写仍可修订的动作？ | [[2503.02881-reactive-diffusion-policy-slow-fast-visual-tactile-policy-learning-for-contact-rich-manipulation|RDP]]、[[t-rex-tactile-reactive-dexterous-manipulation|T-Rex]]、[[2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback|TacForcing]]、[[foar-force-aware-reactive-policy-for-contact-rich-robotic-manipulation|FoAR]] | 快速解码、快慢专家、流式动作块和阶段门控均优于若干静态融合基线 | 缺等算力延迟比较、跨传感器复现和统一安全指标 |
| 记忆与后果 | 接触历史怎样表示任务进度，未来接触怎样约束动作选择？ | [[fm-vla-force-based-memory-for-vision-language-action-models-in-contact-rich-manipulation|FM-VLA]]、[[facet-0|Facet-0]]、[[2605.11048-forceflow-learning-to-feel-and-act-via-contact-driven-flow-matching|ForceFlow]] | force memory 可记录视觉难辨的事件；未来 wrench 可作为辅助目标或 critic 的评价对象 | 长 episode 的容量、预测校准和 critic 的跨任务泛化 |
| 力位与柔顺执行 | 学习策略怎样把物理目标交给稳定控制回路？ | [[adaptive-compliance-policy-learning-approximate-compliance-for-diffusion-guided-control|ACP]]、[[2410.07554-forcemimic-force-centric-imitation-learning-with-force-motion-capture-system-for-contact-rich-manipulation|ForceMimic]]、[[2609.05832-cr-vla-force|CR-VLA-Force]] | 虚拟目标/刚度、预测 wrench、期望力动作块均可由高频控制器落实 | 控制接口跨机器人迁移、错误目标检测与安全边界 |

## 五条策略路线怎样取舍

### 1. 用最新接触直接修订动作

RDP 把慢速动作生成和快速触觉条件解码分开；T-Rex 让约 5 Hz 的视觉语言专家与约 20 Hz 的触觉专家沿同一 flow 轨迹协作；TacForcing 在单一专家内部保留远期动作中间态，每执行一块就用新触觉修订下一块；FoAR 则先预测接触阶段，再用 100 Hz wrench 门控特征和触发固定小步修正。

共同结论是：反馈必须在动作仍可更改时进入。差异在于修改发生在 decoder、另一个专家、同一生成轨迹还是外部反应式规则中。现有实验协议不同，尚不能判定哪一种结构普遍更优。

### 2. 让力主导局部动作生成

ForceFlow 让短窗 wrench 与本体状态通过 AdaLN 调制每个 flow-matching block，视觉只通过 cross-attention 提供空间锚点，并联合预测动作与下一步力。它强调低维物理信号不能被高维视觉淹没，但约 1.15 秒的重规划周期意味着它仍需要执行器侧安全回路处理更快的碰撞。

### 3. 由策略给物理目标、控制器负责稳定

ACP 输出参考位姿、虚拟目标与刚度幅值，ForceMimic 输出位姿—wrench 后由正交混合力位控制器执行，CR-VLA-Force 则让约 1 Hz 的 VLA 输出位姿与前馈力、由 500 Hz 自适应柔顺控制器持续跟踪。这条路线把任务条件化交给学习，把稳定性与带宽交给控制器，是目前对持续接触最清晰的责任划分。

### 4. 把真实力降为训练期教师

FD-VLA 用真实力潜变量监督视觉—状态条件化的单个预测 token，推理时移除传感器。它适合成本敏感且接触大多可由常见模态推断的任务，但不适合把这个 token 当作过载保护、卡滞检测或可解释力估计。

### 5. 用力记录过去、评价未来

FM-VLA 把完整 episode 的 wrench 历史压成 8 个事件记忆 token，解决按钮计数和重复擦拭等视觉历史含混的问题。Facet-0 则把候选动作与未来 wrench 联合生成，再由 Action-Wrench Critic 评价接触后果。前者回答“已经发生了什么”，后者回答“这样做可能发生什么”，二者都把 force 从即时输入提升为决策状态。

## 关键证据锚点

| 材料 | 结果锚点 | 应怎样解读 |
| --- | --- | --- |
| MuSe | 去掉 replay 后旧 wiping/peg 任务分别降到 0.5/15、2/15；完整方法为 12.5/15、10/15 | 新模态接入首先是知识连续性问题 |
| RDP | Force 版在 peeling、wiping、bimanual lifting 的任务得分为 0.95、0.87、0.70 | 高频接触条件解码能产生细粒度位姿修正，但指标只适用于其协议 |
| T-Rex | 12 项真机任务平均成功率 65%，同协议最强基线 35% | 异步快慢专家具有实质收益，尚未验证跨手型与跨传感器 |
| TacForcing | 六项 UniVTAC 平均 65%；真机消融中静态触觉 31%，执行期更新加 EATA 为 69% | 触觉采集时刻与动作生效时刻的对齐比静态拼接更关键 |
| ACP | 翻转 96%、花瓶擦拭 93.75%，明显高于固定柔顺基线 | 策略化柔顺有效，但依赖慢速、轻物体和非夹持等假设 |
| FM-VLA | 三任务平均 83.3%，视觉记忆基线 53.7%；延迟仅比无记忆策略增加 3.3 ms | wrench 可成为高效事件记忆，但证据来自单平台三任务 |
| FD-VLA | 三任务平均 61.1%，真实力 token 版本 51.1%，无 FDM 为 38.9% | 任务相关潜在力可优于原始读数，不等于视觉替代真实传感器 |
| Facet-0 | 五项亚毫米装配完整系统平均 82%，最强通用基线 15%；本地适配前为 38% | 接触后果评价有价值，但高结果强依赖受约束任务适配 |
| ForceMimic | 单一削皮任务动作正确 100%、连续削皮超过 10 cm 为 85% | 自然力位示范与控制接口可行，泛化结论仍很窄 |
| FoAR | 三项接触任务得分 0.875/0.850/0.756，扰动下接触 ASR 保持 100% | 阶段门控和简单反应修正有效，阈值与步长需跨任务重标定 |
| ForceFlow | 六任务平均 81.67%、Force Fidelity MAE 8.23 N；ForceVLA 为 45%、23.31 N | 成功与力质量应同时评估，空间 OOD 仍依赖上层定位模块 |
| CR-VLA-Force | 六条件平均成功率 89.2%；40 N 擦板力误差 5.52%（base）/8.78%（OOD） | 慢 VLA 与 500 Hz 柔顺回路互补，但不构成跨平台安全证明 |

这些数字只能作为各自实验内部的证据锚点，不能据此做跨论文排行榜。

## 跨材料结论

1. **先定义语义，再设计融合。** ForceFlow 的历史与未来力、Facet-0 的候选后果、CR-VLA-Force 的期望力和 FD-VLA 的蒸馏 token 名字都含 force，但训练目标和部署责任完全不同。
2. **时间尺度决定结构。** 动作块内修订适合 RDP/T-Rex/TacForcing/FoAR，episode 进度适合 FM-VLA，持续力跟踪则需要 CR-VLA-Force/ACP 一类高频控制接口。
3. **低频学习策略不能自动成为安全回路。** 即使 ForceFlow 或 VLA 能预测接触结果，执行器仍要在模型下一次重规划前处理冲击、饱和和不稳定。
4. **数据—控制一致性是硬门槛。** ForceMimic 中直接加入力的基线因示范约 10 N、部署约 20 N 且局部超过 40 N 的分布失配而退化，说明校准和控制映射不能留给网络自行吸收。
5. **成功率不足以评价力策略。** 至少还要报告峰值力、力跟踪误差、接触保持、损伤、延迟与扰动恢复；ForceFlow 和 CR-VLA-Force 已部分补上这类指标，但尚无统一协议。

## 工程选择指南

| 需求 | 优先参考 | 采用前应确认 |
| --- | --- | --- |
| 已有视觉策略，新加少量带力数据且不能忘旧任务 | MuSe | replay 成本、缺失模态策略、外部控制器能力 |
| 部署平台不装力传感器 | FD-VLA | 接触是否可由视觉/状态推断；另设独立安全保护 |
| action chunk 执行期间接触快速变化 | RDP、T-Rex、TacForcing | 实际采样率、端到端延迟、可修订窗口与算力 |
| 自由空间与接触阶段交替明显 | FoAR | 接触预测可靠性、阈值和固定修正步长的校准 |
| 需要同时优化任务成功与接触质量 | ForceFlow | 重规划周期、力指标定义、空间定位模块 |
| 任务进度由接触次数或覆盖轮次决定 | FM-VLA | 长序列容量、传感器漂移、跨任务记忆迁移 |
| 精密装配需要按接触后果选择候选动作 | Facet-0 | 本地适配数据、动作安全盒和 critic 失效监控 |
| 策略必须显式给出期望力或柔顺 | ACP、ForceMimic、CR-VLA-Force | 机器人控制接口、稳定性约束、错误目标拒绝机制 |
| 先决定触觉硬件和共享表示 | Tactile Genesis、HTT | 仿真到真机差距、异构传感器信息不对称 |

## 分歧与限制

- **部署期是否必须有传感器。** FD-VLA 说明部分任务可用蒸馏先验降低成本，其他闭环路线则依赖实时触觉或 wrist wrench。二者面向的风险边界不同，不构成谁替代谁。
- **端到端学习还是显式控制。** RDP、T-Rex、TacForcing 更深入地修改生成过程；ACP、ForceMimic、CR-VLA-Force 把稳定接触交给经典控制器。当前没有统一实验同时比较泛化、延迟与安全。
- **“高频”口径不统一。** 传感采样、策略推理、动作输出和低层控制频率常被混合描述。100 Hz 传感器不等于 100 Hz 模型闭环，1 Hz VLA 也不等于系统只能 1 Hz 反应。
- **证据集中在固定平台。** 多数结果来自单一机械臂或手型、少量任务与 10-30 次级别评测；跨机器人、跨材料、传感器故障和开放环境证据很弱。
- **触觉和腕部力矩不可互换。** 指尖光学/阵列触觉擅长局部滑移与形变，腕部六轴 wrench 擅长整体接触方向和载荷；把二者统一为一个 token 会隐藏可观测性差异。

## 什么会改变这个判断

- 一个统一系统在训练时未见的机器人和传感器上，同时验证 HTT 式表示迁移、MuSe 式无遗忘适配、TacForcing/RDP 式动作块内更新、FM-VLA 式事件记忆与 CR-VLA-Force 式高频柔顺。
- 在相同机器人、数据、算力、传感频率和控制器下，直接比较快速 decoder、快慢专家、单专家流式生成、阶段门控与经典高频力控。
- 建立以任务成功、峰值力、力跟踪、损伤、延迟、恢复、标定漂移和硬件成本为共同维度的公开真机基准，并报告统计置信区间。
- 对错误期望力、传感器饱和/掉线、未知材料、隐藏卡阻和突发碰撞进行系统压力测试，证明学习模型与低层安全约束能协同失效保护。

## 关联主题

- [[tactile-representation|Tactile Representation]]：传感设计、跨硬件表示和触觉策略接口。
- [[contact-rich-manipulation|Contact-Rich Manipulation and Adaptive Compliance]]：运动—力联合学习、柔顺与接触安全。
- [[vision-language-action|Vision-Language-Action]]：新物理模态怎样进入机器人基础策略。
- [[long-horizon-memory-for-robot-policies|Long-Horizon Memory for Robot Policies]]：力历史怎样成为 episode 级事件记忆。

## 关联材料

- [[tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks|Tactile Genesis]]
- [[2606.29948-heterogeneous-tactile-transformer|Heterogeneous Tactile Transformer]]
- [[2410.07554-forcemimic-force-centric-imitation-learning-with-force-motion-capture-system-for-contact-rich-manipulation|ForceMimic]]
- [[2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force|MuSe]]
- [[fd-vla-force-distilled-vision-language-action-model-for-contact-rich-manipulation|FD-VLA]]
- [[2503.02881-reactive-diffusion-policy-slow-fast-visual-tactile-policy-learning-for-contact-rich-manipulation|Reactive Diffusion Policy]]
- [[t-rex-tactile-reactive-dexterous-manipulation|T-Rex]]
- [[2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback|TacForcing]]
- [[foar-force-aware-reactive-policy-for-contact-rich-robotic-manipulation|FoAR]]
- [[2605.11048-forceflow-learning-to-feel-and-act-via-contact-driven-flow-matching|ForceFlow]]
- [[fm-vla-force-based-memory-for-vision-language-action-models-in-contact-rich-manipulation|FM-VLA]]
- [[facet-0|Facet-0]]
- [[adaptive-compliance-policy-learning-approximate-compliance-for-diffusion-guided-control|Adaptive Compliance Policy]]
- [[2609.05832-cr-vla-force|CR-VLA-Force]]
