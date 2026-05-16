---
id: "long-horizon-memory-for-robot-policies"
slug: "long-horizon-memory-for-robot-policies"
title: "Long-Horizon Memory for Robot Policies"
type: topic
created: "2026-05-11"
updated: "2026-05-11"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "long-horizon-memory"
summary: ""
source_slugs:
  - "mem-multi-scale-embodied-memory-for-vision-language-action-models"
  - "pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities"
synthesis_slugs:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
status: active
open_questions:
---
# Long-Horizon Memory for Robot Policies

> 长时程机器人控制不是只把上下文窗口拉长，而是要决定不同时间尺度的信息如何表示。

## 主题概述

这条主题关注机器人策略如何处理分钟级任务。关键不是更多帧，而是多尺度记忆：哪些信息应该保留为短期视觉痕迹，哪些应该抽象成长期语义状态。

## 当前知识库里的代表工作

- [来源: MEM: Multi-Scale Embodied Memory for Vision Language Action Models](../sources/mem-multi-scale-embodied-memory-for-vision-language-action-models.md)
  明确把 memory 分解成视频短期记忆和语言长期记忆，是这条主题的主工作。

- [来源: π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](../sources/pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities.md)
  通过 subgoal image、subtask instruction、episode metadata 给策略提供 richer context，本质上也是在补 memory 和 progress control。

## 当前判断

- `MEM` 是显式 memory 架构路线
- `π0.7` 更偏通过 richer prompt 和 context 让模型具备更强的阶段性控制
- 这两条路线未来很可能会合流：显式 memory + 可控 prompt 共同支撑 long-horizon embodied policy

## 值得后续关注的问题

- 语言长期记忆如何更新、压缩和纠错
- 视频短期记忆如何在保证实时性的同时保留关键信息
- high-level memory 与 low-level control 的接口应如何设计

## 相关页面

- [[MEM: Multi-Scale Embodied Memory for Vision Language Action Models]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
- [[Vision-Language-Action]]
