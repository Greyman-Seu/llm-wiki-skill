---
id: "current-vla-landscape-foundation-control-memory-and-transfer"
slug: "current-vla-landscape-foundation-control-memory-and-transfer"
title: "当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据"
type: synthesis
created: "2026-05-11"
updated: "2026-05-16"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "vision-language-action"
summary: ""
judgment: "当前 VLA 研究已经从单点模型设计演化为基座、可控性、在线精修、记忆和人类数据共同组成的系统问题。"
source_slugs:
  - "openvla-an-open-source-vision-language-action-model"
  - "pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities"
  - "rl-token-bootstrapping-online-rl-with-vision-language-action-models"
  - "mem-multi-scale-embodied-memory-for-vision-language-action-models"
  - "emergence-of-human-to-robot-transfer-in-vision-language-action-models"
  - "deximit-learning-bimanual-dexterous-manipulation-from-monocular-human-videos"
topic_slugs:
  - "human-to-robot-transfer"
  - "human-video-robot-data-generation"
  - "long-horizon-memory-for-robot-policies"
  - "online-rl-for-vla"
  - "vision-language-action"
claims:
open_questions:
confidence: INFERRED
---
# 当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据

> 这 6 篇论文放在一起看，已经足够勾勒出当前具身智能 VLA 与 human data 主线的几条关键分叉。

## 综述结论

如果只看单篇论文，很容易觉得大家都在“继续做更强的 VLA”。但把 `OpenVLA`、`π0.7`、`RLT`、`MEM`、`Human-to-Robot Transfer`、`DexImit` 放在一起，会看到这条路线其实已经分化成六个相互关联的问题：

1. `VLA 基座如何开放、可训、可部署`
2. `heterogeneous data 如何变成可控能力`
3. `通才策略如何继续被打磨到 specialist 级精度`
4. `分钟级任务如何通过 memory 真正支撑起来`
5. `人类数据何时开始能真正被机器人利用`
6. `人类视频如何被显式编译成机器人可训练数据`

这说明当前 VLA 研究已经不再只是单点模型设计，而是在演化成一套完整系统栈。

## 路线 1：基座化

代表工作：
[来源: OpenVLA: An Open-Source Vision-Language-Action Model](../sources/openvla-an-open-source-vision-language-action-model.md)

OpenVLA 回答的是最底层的问题：如果机器人领域要像语言模型一样进入 foundation model 时代，是否有一个真正公开、可训练、可微调、可部署的基座。它的意义不只是性能，而是把训练、适配、部署连成一条开源链路，使后续路线有了可复用底座。

## 路线 2：可控性与多源数据吸纳

代表工作：
[来源: π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](../sources/pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities.md)

π0.7 强调的是：当机器人基础模型开始吃 demonstration、autonomous data、human video、web data 时，真正的难点不是“数据够不够多”，而是“模型能不能分辨这些数据应该怎么用”。它通过子任务语言、subgoal image、episode metadata 把“怎么做”也写进 prompt，本质上是在解决 heterogeneous data 的 disambiguation 问题。

## 路线 3：在线精修

代表工作：
[来源: RL Token: Bootstrapping Online RL with Vision-Language-Action Models](../sources/rl-token-bootstrapping-online-rl-with-vision-language-action-models.md)

RLT 则往下游走一步，解决 foundation policy 落地时的高精度问题。它并不否定 VLA 的 generalist 路线，而是承认现实：很多真实机器人任务最终卡在最后几毫米。它给出的答案是用 `RL token` 之类的轻量接口，在不重训整套大模型的前提下，把关键阶段继续打磨成 specialist 级表现。

## 路线 4：长时程记忆

代表工作：
[来源: MEM: Multi-Scale Embodied Memory for Vision Language Action Models](../sources/mem-multi-scale-embodied-memory-for-vision-language-action-models.md)

MEM 进一步把问题拉长到分钟级任务。它说明单纯增加历史长度不能解决 long-horizon control，memory 必须是分层的：短期视觉记忆负责局部细节和遮挡补偿，长期语义记忆负责任务进度与阶段管理。这意味着 VLA 的未来很可能越来越像“带显式 memory module 的 embodied agent”。

## 路线 5：人类数据吸纳

代表工作：
[来源: Emergence of Human to Robot Transfer in Vision-Language-Action Models](../sources/emergence-of-human-to-robot-transfer-in-vision-language-action-models.md)

Human-to-Robot Transfer 这篇把视角转向更上游的数据扩展问题。它的关键发现不是“human video useful”，而是“当 robot pretraining 多样性达到某个阈值后，human-to-robot transfer 才开始明显涌现”。这给出一个很重要的判断：具身智能里很多看似需要手工对齐的能力，可能其实是 scale 和 diversity 的副产物。

## 路线 6：人类视频到机器人数据引擎

代表工作：
[来源: DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos](../sources/deximit-learning-bimanual-dexterous-manipulation-from-monocular-human-videos.md)

DexImit 补上了 human data 的另一种用法：不是直接把 human video 作为另一种 embodiment 参与训练，而是把单目人类操作视频经过 4D 重建、双手调度、抓取与运动规划、数据增强，显式转换成双手灵巧机器人训练数据。它说明 human video 的价值不只在 representation transfer，也可能在于成为一个可规模化的数据生成入口。

## 综合判断

把这 5 篇合起来看，目前 VLA 主线至少有三个明显结论：

- **第一，VLA 不是单一路线，而是平台化问题。**
  从 `OpenVLA` 到 `RLT`，可以看到大家已经默认 foundation policy 是起点，不是终点。

- **第二，真正的瓶颈在“如何把广泛数据转成可靠控制”。**
  `π0.7` 关心 prompt 和 steerability，`MEM` 关心 memory abstraction，`Human-to-Robot Transfer` 关心 pretraining diversity，`DexImit` 关心显式 data generation，这些本质都在解决“广覆盖是否真的会变成能力”。

- **第三，后续突破更可能来自系统组合，而不是单点模型变大。**
  基座、可控性、在线精修、长时程记忆、人类数据和数据生成引擎，这些路线更像模块而不是相互替代关系。未来更可能出现的是它们的组合系统。

- **第四，human data 至少有两条不同技术路线。**
  一条是 `Human-to-Robot Transfer` 代表的 co-training / representation transfer，另一条是 `DexImit` 代表的 reconstruction / scheduling / planning data engine。前者更依赖预训练多样性，后者更依赖几何与物理可行性检查。

## 当前知识库的合理结构判断

基于现在只有 6 篇 source 的状态，真正成熟的 topic 其实还不多。

- `Vision-Language-Action` 已经是一个成立的总主题
- `Online RL for VLA`、`Long-Horizon Memory`、`Human-to-Robot Transfer`、`Human Video Robot Data Generation` 目前更像正在形成中的子主题

因此当前更合理的入口，不是强行把每条子方向都做成厚 topic，而是先保留一个总主题页，再用这篇 synthesis 作为跨论文主入口。

## 后续建议

- 再补 2-3 篇 `online RL for VLA / policy refinement` 论文，再厚化 `Online RL for VLA`
- 再补 2-3 篇 `memory / long horizon` 论文，再厚化 `Long-Horizon Memory`
- 再补 `human video / cross-embodiment / multimodal transfer` 论文，再厚化 `Human-to-Robot Transfer`
- 再补 `video-to-robot-data / dexterous data generation / imitation from video` 论文，再判断 `Human Video Robot Data Generation` 是否应升级为更重的综述入口
- 到那时再做更重的 topic，而不是现在就假装它们已经成熟

## 相关页面

- [[Vision-Language-Action]]
- [[OpenVLA: An Open-Source Vision-Language-Action Model]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
- [[RL Token: Bootstrapping Online RL with Vision-Language-Action Models]]
- [[MEM: Multi-Scale Embodied Memory for Vision Language Action Models]]
- [[Emergence of Human to Robot Transfer in Vision-Language-Action Models]]
- [[DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos]]
- [[Human Video Robot Data Generation]]
