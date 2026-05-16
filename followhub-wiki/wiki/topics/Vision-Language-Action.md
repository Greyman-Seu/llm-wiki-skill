---
id: "vision-language-action"
slug: "vision-language-action"
title: "Vision-Language-Action"
type: topic
created: "2026-05-11"
updated: "2026-05-11"
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

## 当前判断

这几篇放在一起看，VLA 主线已经很清楚：

- `OpenVLA` 解决“基座是否开放、可训、可部署”
- `π0.7` 解决“多源数据如何通过 prompt 变成可控能力”
- `RLT` 解决“如何把通才策略继续打磨到高精度”
- `MEM` 解决“如何把策略延长到 long-horizon”
- `Human-to-Robot Transfer` 解决“如何把人类数据真正吸纳进来”

也就是说，VLA 不再只是一个单点模型设计问题，而已经分化成一套系统问题族。

## 相关页面

- [[OpenVLA: An Open-Source Vision-Language-Action Model]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
- [[RL Token: Bootstrapping Online RL with Vision-Language-Action Models]]
- [[MEM: Multi-Scale Embodied Memory for Vision Language Action Models]]
- [[Emergence of Human to Robot Transfer in Vision-Language-Action Models]]
- [[Online RL for VLA]]
- [[Long-Horizon Memory for Robot Policies]]
- [[Human-to-Robot Transfer]]
