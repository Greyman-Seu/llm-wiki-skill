---
id: "tactile-force-into-pretrained-robot-policies"
slug: "tactile-force-into-pretrained-robot-policies"
title: "触觉与力觉如何进入预训练机器人策略：表示、持续适配与执行闭环"
type: synthesis
created: "2026-08-29"
updated: "2026-08-29"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "tactile-representation"
  - "vision-language-action"
summary: "五篇材料共同勾勒出触觉与力觉进入机器人基础策略的四层栈：传感设计、跨硬件表示、无遗忘持续适配，以及与动作生效时间对齐的执行闭环。"
judgment: "触觉与力觉的收益不来自静态拼接；可扩展路线必须让可迁移表示、旧能力保持、可修订动作状态和低延迟反馈接口同时成立，而当前工作仍只分别验证了这条链上的局部环节。"
source_slugs:
  - "tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks"
  - "2606.29948-heterogeneous-tactile-transformer"
  - "2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force"
  - "t-rex-tactile-reactive-dexterous-manipulation"
  - "2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback"
topic_slugs:
  - "tactile-representation"
  - "vision-language-action"
claims:
  - "传感覆盖、物理量选择、表示迁移、策略适配和执行期反馈是相互依赖但不能互相替代的层。"
  - "MuSe 的离线持续适配与 T-Rex、TacForcing 的执行期闭环解决不同时间尺度的问题，完整系统需要把两者结合。"
  - "双专家快慢回路与单专家流式生成是两条尚未在等算力、等延迟条件下比较的闭环接口路线。"
  - "跨硬件泛化目前主要停留在表示层，尚未贯通到持续适配和真实闭环控制层。"
open_questions:
  - "HTT 式共享触觉 backbone 能否在 MuSe 式持续适配后，继续支撑 T-Rex 或 TacForcing 式执行期闭环？"
  - "当多个新模态依次加入时，replay、missing-modality mask 与参数高效适配如何避免成本线性增长？"
  - "双专家快慢回路和单专家流式生成在相同闭环频率、算力与动作时域下谁更稳定？"
  - "能否建立同时测量旧任务保持、新任务迁移、跨传感器泛化、闭环延迟和接触安全的统一基准？"
confidence: INFERRED
---

# 触觉与力觉如何进入预训练机器人策略：表示、持续适配与执行闭环

> 当前阶段最可靠的判断是：接触感知不是在输入端多拼一个 token，而是一条从传感器到控制时序都必须打通的系统链。

## 当前判断

把这五篇材料放在一起，触觉与力觉进入机器人基础策略至少需要四层接口同时成立：先决定哪些接触量值得感知，再把异构硬件压进可迁移表示；随后让原本只有视觉数据的策略吸收新模态而不遗忘；最后还要保证最新观测能在动作真正执行前进入仍可修订的控制状态。

这四层目前已有分别成立的证据，但尚没有一篇工作把它们端到端贯通。`Tactile Genesis` 与 `HTT` 更接近上游感知基础设施，`MuSe` 补上预训练策略的持续适配，`T-Rex` 与 `TacForcing` 则给出两种执行期闭环。最重要的结论不是哪一篇替代另一篇，而是只解决其中一层不足以得到可扩展的接触控制系统。

## 四层路线

| 层 | 核心问题 | 代表材料 | 当前证据 | 尚缺什么 |
| --- | --- | --- | --- | --- |
| 传感设计 | 应该感知哪里、哪种物理量、多少分辨率？ | [[tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks|Tactile Genesis]] | 受控仿真显示覆盖面积通常比指尖高分辨率更优先，per-taxel 力/力矩是较稳健默认项 | 大规模真机与耐久、漂移、成本验证 |
| 表示迁移 | 光学式、阵列式等异构触觉能否共享 backbone？ | [[2606.29948-heterogeneous-tactile-transformer|Heterogeneous Tactile Transformer]] | 1.6M 同步帧、四种传感器的自监督对齐，并在预训练未见的 Sharpa 指尖上验证策略迁移 | 信息不对称导致阵列侧退化；跨硬件闭环尚未验证 |
| 持续适配 | 旧数据没有新模态标签时，怎样吸收 F/T 且保留旧能力？ | [[2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force|MuSe]] | early + late fusion、未来视频/F/T 预测和旧数据 replay；去掉 replay 后旧任务表现显著塌陷 | 仍是离线适配，且主要覆盖一种 F/T 配置与有限任务 |
| 执行闭环 | 高频接触状态怎样及时改写尚未执行的动作？ | [[t-rex-tactile-reactive-dexterous-manipulation|T-Rex]]、[[2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback|TacForcing]] | T-Rex 用快慢专家共享 flow 轨迹；TacForcing 用单专家分块生成和 EATA 对齐观测—动作时间 | 缺等算力延迟对比、跨传感器泛化与统一安全指标 |

## MuSe 补上的关键缺口

在 MuSe 之前，这组材料已经说明“触觉应该怎样表示”和“执行中为什么要不断刷新”，但中间少了一层：一个已经用海量 vision-action 数据训练好的策略，如何在旧数据根本没有力标注时接入新传感器。

MuSe 把这个问题明确写成 multisensory continual learning。它不把 434 条新多感官 episode 当作重训基础模型的替代品，而是把 1,271 条旧 episode 继续放进 replay；旧样本的 F/T 通道用 learnable mask 占位并屏蔽对应重建损失，动作与视频目标则继续约束原有世界模型。结果上，去掉 replay 后旧 wiping / peg 任务分别只剩 0.5/15 和 2/15，而完整 MuSe 达到 12.5/15 和 10/15。这个差距说明，新模态适配首先是知识连续性问题，其次才是融合结构问题。

MuSe 也没有完成最后一层闭环。它预测未来 F/T，再把轨迹交给外部 adaptive compliance controller；因此它证明了“接触动力学可被预测并成为控制目标”，却还没有回答执行中观测变化后如何在线修订这条目标。这个缺口正好由 T-Rex 和 TacForcing 的时间接口补充。

## 两条执行期反馈路线

### 路线 A：快慢专家共享一条生成轨迹

[[t-rex-tactile-reactive-dexterous-manipulation|T-Rex]] 用约 5 Hz 的动作专家处理视觉语言规划，再由约 20 Hz 的触觉专家复用缓存、继续细化同一条 flow-matching 去噪轨迹。完整模型在 12 个真机任务上平均 65%，最强基线为 35%；去掉触觉后，代表任务平均降到 42%。它的优势是频率职责清楚，代价是需要额外专家、100 小时触觉中训练数据和较高算力。

### 路线 B：单专家内部交错生成与执行

[[2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback|TacForcing]] 不增加独立快控制器，而是让近期动作块先完成并执行，远期块保持 flow 中间态；执行后的新触觉只通过 EATA 影响下一待执行块。其关键反例是固定触觉在消融中并不优于无触觉，真机平均甚至从 42% 降到 31%；加入执行期刷新后升到 48%，再加 EATA 达到 69%。这说明“有没有触觉”不如“触觉采集时刻、动作生效时刻和可修订窗口是否对齐”重要。

两条路线都反对一次性静态拼接，也都让触觉进入同一动作分布；真正未决的是，在相同闭环频率、算力、传感延迟和动作时域下，多专家分工与单专家流式调度谁更稳、更容易部署。

## Claims

1. **接触感知是一条接口栈，不是单一模态特征。** Tactile Genesis、HTT、MuSe、T-Rex 和 TacForcing 分别覆盖传感、表示、适配与控制时序；任何一层的成功都不能自动推出下一层成立。
2. **离线持续适配与在线执行闭环正交。** MuSe 主要解决跨数据阶段的 forward/backward transfer；T-Rex 和 TacForcing 主要解决单次执行时域内的观测—动作反馈。完整系统需要两种时间尺度同时成立。
3. **静态接入不是可信基线终点。** MuSe 的 no-replay 退化和 TacForcing 的 fixed-tactile 反例都表明，直接融合新模态可能伤害旧能力或当前控制；必须显式设计记忆保持与时间作用域。
4. **跨硬件仍是最薄弱的端到端证据。** HTT 已在表示层展示未见传感器迁移，但 MuSe、T-Rex、TacForcing 的主要控制结果仍绑定特定传感配置和平台。

## 分歧与限制

- 这五篇使用的“触觉/力觉”并非同一种信号：从 per-taxel 力/力矩、光学形变、阵列信号到六轴 F/T 都有覆盖，不能把某一种传感器上的收益直接外推到另一种。
- Tactile Genesis 的主要设计结论来自仿真—蒸馏设置；HTT 的跨硬件优势主要在表示与少量下游任务；后三篇的强结果则集中在固定真机平台，证据链仍不对称。
- MuSe 依赖外部 compliance controller，T-Rex 和 TacForcing 更直接修改动作生成；三者的成功率、任务难度和控制栈不同，现有数字不能横向排名。
- T-Rex 与 TacForcing 都缺少统一的端到端延迟、触觉采样延迟、算力和安全过载指标，因此“无需独立快控制器”或“快专家更及时”都还不是部署级结论。

## 什么会改变这个判断

- 一个统一实验把 HTT 式跨传感器 encoder、MuSe 式 replay/mask 适配和 T-Rex 或 TacForcing 式在线反馈串起来，并在训练时未见硬件上保持旧任务与新任务表现。
- 在等算力、等闭环频率和等动作时域下直接比较双专家与单专家路线，同时报告延迟、抖动、力峰值和失败恢复。
- 多个新模态按时间顺序加入同一 foundation policy 后，仍能以有界 replay 成本保持全部旧能力。
- 从“单个平台多任务”扩展到跨机器人、跨手型、跨触觉传感器的真实接触基准，并给出统计置信区间。

## 关联主题

- [[tactile-representation|Tactile Representation]]：提供传感设计、表示迁移、持续适配与反馈接口这条主问题线。
- [[Vision-Language-Action]]：提供预训练 foundation policy、动作生成与能力保持的系统背景。

## 关联材料

- [[tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks|Tactile Genesis]]：上游传感配置与物理量选择。
- [[2606.29948-heterogeneous-tactile-transformer|Heterogeneous Tactile Transformer]]：异构触觉共享表示与未见传感器迁移。
- [[2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force|MuSe]]：新 F/T 模态的持续适配、未来预测与防遗忘。
- [[t-rex-tactile-reactive-dexterous-manipulation|T-Rex]]：多速率专家的高频触觉动作细化。
- [[2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback|TacForcing]]：单专家流式生成和执行感知触觉注意力。

## 待跟进

- 等待 T-Rex、TacForcing 的代码、统一延迟数据与跨硬件复现。
- 跟踪 MuSe 是否扩展到触觉图像、音频或多种依次加入的新模态。
- 在接触丰富操作主题成熟后，把 compliance / impedance 控制接口纳入同一证据链。
