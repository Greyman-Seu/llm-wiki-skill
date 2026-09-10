---
id: "long-horizon-memory-for-robot-policies"
slug: "long-horizon-memory-for-robot-policies"
title: "Long-Horizon Memory for Robot Policies"
type: topic
created: "2026-05-11"
updated: "2026-09-10"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "long-horizon-memory"
summary: ""
source_slugs:
  - "mem-multi-scale-embodied-memory-for-vision-language-action-models"
  - "pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities"
  - "fm-vla-force-based-memory-for-vision-language-action-models-in-contact-rich-manipulation"
synthesis_slugs:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
  - "force-touch-robot-policy-review"
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

- [来源: FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation](../sources/fm-vla-force-based-memory-for-vision-language-action-models-in-contact-rich-manipulation.md)
  把整个 episode 的腕部 wrench 历史压缩成 8 个事件记忆 token，并用短时关节状态稳定接触前运动，证明视觉或语言之外的物理信号也可以成为低成本长时记忆。

## 当前判断

- `MEM` 是显式 memory 架构路线
- `π0.7` 更偏通过 richer prompt 和 context 让模型具备更强的阶段性控制
- `FM-VLA` 补出第三类路线：按事件可观测性选择记忆模态，用 wrench 记录视觉上含混的接触进度
- 后续更可能出现多模态、分时间尺度的记忆：视觉/语言保存场景与计划，force/state 保存接触事件与近期运动

## 值得后续关注的问题

- 语言长期记忆如何更新、压缩和纠错
- 视频短期记忆如何在保证实时性的同时保留关键信息
- 如何在视觉、语言、force/tactile 与 proprioception 之间动态选择记忆内容和时间尺度
- high-level memory 与 low-level control 的接口应如何设计

## 相关页面

- [[MEM: Multi-Scale Embodied Memory for Vision Language Action Models]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
- [[FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation]]
- [[force-touch-robot-policy-review|机器人策略中的力觉与触觉：从信号语义到闭环控制]]
- [[Vision-Language-Action]]
