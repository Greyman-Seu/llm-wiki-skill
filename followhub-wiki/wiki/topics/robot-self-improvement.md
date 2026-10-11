---
id: "robot-self-improvement"
slug: "robot-self-improvement"
title: "Robot Self-Improvement"
type: topic
created: "2026-10-11"
updated: "2026-10-11"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "robot-foundation-model"
summary: "关注机器人策略如何根据自身 rollout 失败持续生成纠正经验、更新采数分布，并检验这种递归改进能否跨场景、跨轮次稳定延续。"
source_slugs:
  - "2609.38905-embodirsi"
synthesis_slugs: []
status: active
open_questions:
  - "多轮自我改进何时饱和、震荡或产生数据冗余？"
  - "episode 内纠正与跨 episode 定向采数的贡献能否被干净拆分？"
  - "失败归因错误会在多大程度上放大训练偏差？"
  - "Real2Sim 练习场的重建误差和系统成本是否抵消真实数据节省？"
---
# Robot Self-Improvement

> 机器人策略改进的核心问题从“怎样学一个策略”扩展为“当前策略下一步应该生成什么经验”。

## 主题概述

这条主题收集通过策略自身执行反馈驱动后续训练的工作，重点区分三类机制：从失败中间状态生成纠正监督、根据失败分布改变后续采数、以及在真实/仿真练习场中重复评估与更新。它与 online RL 相关，但不要求所有方法都使用 TD 学习或环境 reward。

## 代表工作

- [来源: EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation](../sources/2609.38905-embodirsi.md)
  把目标桌面重建为长期可复用仿真练习场；agent 监控 policy rollout，从 policy-reached state 生成纠正轨迹，并把最终失败归因到空间弱区以定向补采示范。匹配 400 条轨迹预算时比静态采集高 20.6 个百分点，R2+10 实机成功率达 83.1%。

## 当前判断

- 有价值的 self-improvement 不一定是模型改写自身，而是让数据采集策略随执行弱点共同演化。
- 训练时的外部恢复和测试时的 policy-only 自主行为必须分开报告，否则容易夸大系统可用性。
- 该方向仍缺少跨 held-out 场景、长时间多轮更新、组件贡献和总成本的可复现验证。

## 相关页面

- [[2609.38905-embodirsi|EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation]]
- [[Online RL for VLA]]
- [[Vision-Language-Action]]
