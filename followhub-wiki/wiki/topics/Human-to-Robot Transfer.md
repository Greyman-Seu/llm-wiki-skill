---
id: "human-to-robot-transfer"
slug: "human-to-robot-transfer"
title: "Human-to-Robot Transfer"
type: topic
created: "2026-05-11"
updated: "2026-05-16"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "human-to-robot-transfer"
summary: ""
source_slugs:
  - "emergence-of-human-to-robot-transfer-in-vision-language-action-models"
  - "pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities"
  - "deximit-learning-bimanual-dexterous-manipulation-from-monocular-human-videos"
synthesis_slugs:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
status: active
open_questions:
---
# Human-to-Robot Transfer

> 人类视频什么时候能真正变成机器人能力，不只是数据源问题，也是表示能力和预训练多样性问题。

## 主题概述

这条主题关注 human video、human embodiment data 与 robot policy 之间的迁移。核心问题不是“人类数据多不多”，而是“模型什么时候开始有能力利用这些数据”。

## 当前知识库里的代表工作

- [来源: Emergence of Human to Robot Transfer in Vision-Language-Action Models](../sources/emergence-of-human-to-robot-transfer-in-vision-language-action-models.md)
  这条主题的主工作。它提出：human-to-robot transfer 不是固定技巧，而是会随着 VLA 预训练多样性增长而涌现。

- [来源: π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](../sources/pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities.md)
  虽然不是专门研究 human transfer，但它展示了 non-robot data、egocentric human data 与 robot data 可以被统一吸纳到 foundation model 训练中。

- [来源: DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos](../sources/deximit-learning-bimanual-dexterous-manipulation-from-monocular-human-videos.md)
  这篇补上了另一条路线：不直接让模型从 human video 中学表示，而是把单目人类操作视频重建、调度、规划并增强成双手灵巧机器人训练数据。

## 当前判断

- `Human-to-Robot Transfer` 这篇更强调“能力何时出现”
- `π0.7` 更强调“多源数据如何被统一利用”
- `DexImit` 更强调“人类视频如何被编译成物理可行的机器人数据”
- 放在一起看，可以把问题理解成：
  - 预训练多样性负责让 shared representation 成熟
  - richer context / prompt 负责让这些能力在控制中被真正调用出来
  - 显式数据生成 pipeline 负责把一部分 human video 转成更接近机器人动作空间的 supervision

## 值得后续关注的问题

- human data 在 pretraining 阶段和 finetuning 阶段的作用是否不同
- human-to-robot transfer 与 cross-embodiment transfer 是否本质同源
- 显式 data generation 与 VLA co-training 是替代关系，还是更适合组合使用
- 这种能力的出现，更依赖模型规模还是数据多样性

## 相关页面

- [[Emergence of Human to Robot Transfer in Vision-Language-Action Models]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
- [[DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos]]
- [[Human Video Robot Data Generation]]
- [[Vision-Language-Action]]
