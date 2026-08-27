---
id: "vision-language-action"
slug: "vision-language-action"
title: "Vision-Language-Action"
type: topic
created: "2026-05-11"
updated: "2026-08-27"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "vision-language-action"
summary: ""
source_slugs:
  - "openvla-an-open-source-vision-language-action-model"
  - "pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities"
  - "rl-token-bootstrapping-online-rl-with-vision-language-action-models"
  - "mem-multi-scale-embodied-memory-for-vision-language-action-models"
  - "emergence-of-human-to-robot-transfer-in-vision-language-action-models"
  - "dexjoco-a-benchmark-and-toolkit-for-task-oriented-dexterous-manipulation-on-mujoco"
  - "attena-rectifying-action-inequality-in-robotic-foundation-models"
  - "qwen-vla"
  - "2606.17846-qwen-robotmanip-alignment-unlocks-scale-for-robotic-manipulation-foundation-models"
  - "dm05-open-world-embodied-foundation-model"
  - "2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback"
synthesis_slugs:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
status: active
open_questions:
---
# Vision-Language-Action

> 把视觉、语言和动作统一进同一策略建模框架，是当前具身智能主线之一。

## 这条主题在讲什么

VLA 的核心不是“把图像和文本都喂给机器人”，而是把机器人控制问题放进 foundation model 语境里，让预训练、多任务泛化、迁移、微调和跨 embodiment 学习都能在一套统一框架里讨论。

## 为什么重要

- VLA 是现在连接大模型能力与机器人执行能力的主干路线
- 它把机器人学习从 task-specific policy 推向 reusable foundation policy
- 很多后续方向，本质上都是在回答“VLA 还缺什么”
  - 更强的可控性
  - 更长的记忆
  - 更高的精度
  - 更好的跨 embodiment 迁移
  - 更低成本地利用人类数据

## 当前知识库里的几条子路线

- **开源基座化**
  来自 [来源: OpenVLA: An Open-Source Vision-Language-Action Model](../sources/openvla-an-open-source-vision-language-action-model.md)
  OpenVLA 强调训练、微调、部署三件事一起开源，代表“VLA 作为公开基础设施”的路线。

- **更强 steerability**
  来自 [来源: π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](../sources/pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities.md)
  π0.7 通过 richer prompt、subgoal image、episode metadata 把“怎么做”也编码进策略上下文。

- **在线 RL 精修**
  来自 [来源: RL Token: Bootstrapping Online RL with Vision-Language-Action Models](../sources/rl-token-bootstrapping-online-rl-with-vision-language-action-models.md)
  RLT 关注如何在保留 VLA 泛化先验的前提下，把精度和速度继续打磨到 specialist 水平。

- **长时程记忆**
  来自 [来源: MEM: Multi-Scale Embodied Memory for Vision Language Action Models](../sources/mem-multi-scale-embodied-memory-for-vision-language-action-models.md)
  MEM 试图解决 VLA 在长达十几分钟任务中的任务进度保持和局部视觉记忆问题。

- **利用 human data**
  来自 [来源: Emergence of Human to Robot Transfer in Vision-Language-Action Models](../sources/emergence-of-human-to-robot-transfer-in-vision-language-action-models.md)
  这条路线关注 VLA 何时开始能真正吃进 human video，并把它转化成机器人能力。

- **灵巧手基准与失败诊断**
  来自 [来源: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo](../sources/dexjoco-a-benchmark-and-toolkit-for-task-oriented-dexterous-manipulation-on-mujoco.md)
  DexJoCo 不提出新 VLA 模型，而是把 VLA/模仿学习策略在灵巧手、双手协作、按钮/插装/铰链交互和视觉随机化下的失败模式系统测出来。

- **训练目标物理化**
  来自 [来源: AttenA+: Rectifying Action Inequality in Robotic Foundation Models](../sources/attena-rectifying-action-inequality-in-robotic-foundation-models.md)
  AttenA+ 不改 VLA/WAM 骨干，而是把动作速度场写进 loss 权重，让模型更重视低速、精细、接触关键的动作片段。

- **chunk 内流式触觉反馈**
  来自 [来源: TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback](../sources/2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback.md)
  TacForcing 不另设快触觉控制器，而是让同一个动作专家按块完成、执行并保留未来块中间态；每次执行后刷新触觉，EATA 只让最新触觉影响下一待执行块，把观测时刻与动作生效时刻显式对齐。

- **历史上下文 + 具身推理 + 动作对齐的系统化**
  来自 [来源: DM0.5: 面向开放世界的通用具身智能基础模型](../sources/dm05-open-world-embodied-foundation-model.md)
  DM0.5 把长历史记忆（最长 60s）、11 种具身推理 CoT 任务、以及轨迹进展对齐三个设计做成一体，换来开放环境 Zero-Shot 泛化和真机 Table30 v2 SOTA。

## 当前判断

这几篇放在一起看，VLA 主线已经很清楚：

- `OpenVLA` 解决“基座是否开放、可训、可部署”
- `π0.7` 解决“多源数据如何通过 prompt 变成可控能力”
- `RLT` 解决“如何把通才策略继续打磨到高精度”
- `MEM` 解决“如何把策略延长到 long-horizon”
- `Human-to-Robot Transfer` 解决“如何把人类数据真正吸纳进来”
- `DexJoCo` 解决“如何用灵巧手任务和失败模式检验这些策略是否真的具备接触密集、双手和长时程能力”
- `AttenA+` 解决“训练目标是否应该反映动作序列内部的物理关键性”
- `TacForcing` 解决“如何在同一个动作生成器内部交错 chunk 生成、执行与触觉更新，并限制反馈的时间作用域”
- `DM0.5` 解决“如何把历史上下文、具身推理、动作监督三件事系统化地收进一个可用的通用 VLA”

也就是说，VLA 不再只是一个单点模型设计问题，而已经分化成一套系统问题族。

## 相关页面

- [[OpenVLA: An Open-Source Vision-Language-Action Model]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
- [[RL Token: Bootstrapping Online RL with Vision-Language-Action Models]]
- [[MEM: Multi-Scale Embodied Memory for Vision Language Action Models]]
- [[Emergence of Human to Robot Transfer in Vision-Language-Action Models]]
- [[DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo]]
- [[AttenA+: Rectifying Action Inequality in Robotic Foundation Models]]
- [[TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback]]
- [[DM0.5: 面向开放世界的通用具身智能基础模型]]
- [[Online RL for VLA]]
- [[Long-Horizon Memory for Robot Policies]]
- [[Human-to-Robot Transfer]]
