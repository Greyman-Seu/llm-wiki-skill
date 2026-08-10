---
id: "tactile-representation"
slug: "tactile-representation"
title: "Tactile Representation"
type: topic
created: "2026-08-10"
updated: "2026-08-10"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "tactile-representation"
summary: "触觉传感器表示学习：从单一传感器自监督到跨异构传感器共享 backbone，再到下游感知与操作策略。"
source_slugs:
  - "tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks"
  - "2606.29948-heterogeneous-tactile-transformer"
synthesis_slugs: []
status: "active"
open_questions:
  - "异构触觉 backbone 能否在没有光学传感器的纯阵列平台上保持迁移性？"
  - "跨模态对齐的 imbalance 问题如何缓解？"
  - "触觉 backbone 与 VLA 策略如何最佳拼接？"
---

# Tactile Representation

> 把异构触觉信号（光学式、阵列式、视触融合等）训练成可迁移、可拼接下游策略的共享 backbone。

## 这条主题在讲什么

触觉是接触丰富操作的关键观测，但传感器天然异构：光学式（GelSight 类）给稠密空间信息但帧率受限，阵列式给高频力/压信号但空间分辨率低。直接为每种传感器训练独立 backbone 既浪费同步多模态数据，又难以随硬件迭代。本主题把"如何学习可迁移的触觉表示"作为一条独立问题线。

## 为什么重要

- 触觉是 vision-language-action 模型目前缺的那一路高密度接触信号
- 没有可迁移的触觉 backbone，每次换传感器都要重训策略
- 触觉仿真（Tactile Genesis 类）和真实采集（HTT 类 HPT）正在互相补齐基础设施

## 当前理解

| 子问题 | 代表材料 | 立场 |
| --- | --- | --- |
| 触觉硬件配置（位置/分辨率/类型）如何选？ | [[tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks]] | 覆盖面积优先于分辨率；per-taxel 力/力矩在大多数灵巧任务里最稳健 |
| 异构传感器如何共享 backbone？ | [[2606.29948-heterogeneous-tactile-transformer]] | sensor-specific encoder + shared transformer trunk + 跨模态预测对齐；MAE 重建 + 双向跨模态预测 |
| 触觉 backbone 能否迁移到训练时未见的传感器？ | [[2606.29948-heterogeneous-tactile-transformer]] | 已在未出现的 Sharpa 触觉指尖上验证 toy screw / grasp tofu 上的成功率显著提升 |

## 关键设计要点

- **统一输入规范**：时序窗 τ + 减参考帧，让不同采样率、不同维度的传感器在 backbone 内行为可比。
- **跨模态监督源**：利用"同一次接触被多传感器同步记录"作为天然对齐信号，无需人工标注。
- **解耦结构**：sensor-specific encoder/decoder + shared trunk，让每个传感器保留局部细节、共享语义进入统一潜空间。
- **imbalance 风险**：光学-阵列配对中，光学富信息会主导跨模态预测，阵列侧会出现 −4.3% 这种回退；需要 imbalance-aware 损失。

## 未解决问题

- 异构 backbone 在纯阵列平台（无光学传感器）上是否仍可工作？
- imbalance-aware 跨模态对齐是否能同时拿回阵列侧的损失？
- 触觉 backbone 与 VLA 拼接的最优接口是什么（per-token fusion vs late fusion vs dual-stream）？
- 触觉预训练需要多少跨传感器配对数据才能让 backbone 真正可迁移，而不是只适配原 4 种？

## 相关页面

- [[tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks]]
- [[2606.29948-heterogeneous-tactile-transformer]]
- [[Physical/Embodied Intelligence]]（domain）
