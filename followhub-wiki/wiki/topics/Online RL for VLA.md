---
id: "online-rl-for-vla"
slug: "online-rl-for-vla"
title: "Online RL for VLA"
type: topic
created: "2026-05-11"
updated: "2026-07-06"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "online-rl"
summary: ""
source_slugs:
  - "rl-token-bootstrapping-online-rl-with-vision-language-action-models"
  - "steam-self-supervised-temporal-ensemble-advantage-modeling-for-real-world-robot-learning"
  - "pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities"
synthesis_slugs:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
status: active
open_questions:
---
# Online RL for VLA

> 通才策略已经有了，接下来的问题是怎样把它快速打磨到高精度 specialist 表现。

## 主题概述

这条主题关注 VLA 预训练之后的在线适配。核心问题不是“VLA 能不能泛化”，而是“当真实机器人需要更高精度、更高速度时，怎么以较低样本成本继续优化它”。

## 当前知识库里的代表工作

- [来源: RL Token: Bootstrapping Online RL with Vision-Language-Action Models](../sources/rl-token-bootstrapping-online-rl-with-vision-language-action-models.md)
  代表作。通过 `RL token` 把预训练 VLA 与轻量 actor-critic 接起来，让 online RL 重点修正 critical phase。

- [来源: STEAM: Self-Supervised Temporal Ensemble Advantage Modeling for Real-World Robot Learning](../sources/steam-self-supervised-temporal-ensemble-advantage-modeling-for-real-world-robot-learning.md)
  从另一个侧面补齐 online/refinement 闭环：它不设计新 VLA 接口，而是用专家轨迹的时间结构学习 frame-level advantage，从人工纠正、失败 rollout 和专家示范中筛出真正推进任务的局部片段，再接入 CFGRL。

- [来源: π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](../sources/pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities.md)
  虽然主体不是 RL 论文，但它明确展示了 generalist policy 可以蒸馏和吸收 specialist 经验，也说明 online optimization 与 foundation policy 不是对立关系。

## 当前判断

- `RLT` 给出的是一条很现实的 engineering 路线：不要重训整个 VLA，只给它暴露一个适合 RL 的接口
- `STEAM` 补的是数据质量与 credit assignment：真实机器人数据不是整条好/坏，而是需要逐帧识别哪些片段真正推进任务
- `π0.7` 则从另一个角度说明，generalist policy 最终仍然需要 specialist-style refinement，只是 refinement 的位置和形式不同

## 值得后续关注的问题

- online RL 的接口应该放在 VLA 哪一层最合适
- 是 refinement head 更重要，还是 reward / advantage / data-quality signal 更重要
- frame-level advantage 这类数据筛选信号，能否和 RL token 这样的轻量接口稳定结合
- 对不同 embodiment，这类轻量接口是否还能保持稳定性

## 相关页面

- [[RL Token: Bootstrapping Online RL with Vision-Language-Action Models]]
- [[STEAM: Self-Supervised Temporal Ensemble Advantage Modeling for Real-World Robot Learning]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
- [[Vision-Language-Action]]
