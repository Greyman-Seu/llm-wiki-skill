---
id: "tactile-representation"
slug: "tactile-representation"
title: "Tactile Representation"
type: topic
created: "2026-08-10"
updated: "2026-08-29"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "tactile-representation"
summary: "触觉与力觉如何从传感设计和跨硬件表示，进入预训练策略的持续适配与执行期闭环。"
source_slugs:
  - "tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks"
  - "2606.29948-heterogeneous-tactile-transformer"
  - "2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force"
  - "t-rex-tactile-reactive-dexterous-manipulation"
  - "2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback"
synthesis_slugs:
  - "tactile-force-into-pretrained-robot-policies"
status: "active"
open_questions:
  - "异构触觉 backbone 能否在没有光学传感器的纯阵列平台上保持迁移性？"
  - "跨模态对齐的 imbalance 问题如何缓解？"
  - "触觉 backbone 与 VLA 策略如何最佳拼接？"
  - "HTT 式跨硬件表示能否直接作为 MuSe、T-Rex 或 TacForcing 的触觉编码器？"
  - "离线持续适配与执行期高频反馈能否在同一策略中结合，同时保持旧任务能力？"
  - "TacForcing 的 block size、闭环延迟与反馈响应性在等算力预算下如何权衡？"
---

# Tactile Representation

> 跟踪触觉与力觉从传感器选择、共享表示，到预训练策略适配和执行期反馈的完整接口链。

## 这条主题在讲什么

触觉是接触丰富操作的关键观测，但传感器天然异构：光学式（GelSight 类）给稠密空间信息但帧率受限，阵列式或 F/T 传感器给高频力学信号但空间结构更弱。问题也不止是学一个 backbone：旧的视觉策略通常没有触觉标签，动作生成器又可能在执行前一次性定稿。本主题因此追踪一条连续问题线——如何选传感信号、学习可迁移表示、把新模态接入已有策略并在执行时及时使用它。

## 为什么重要

- 触觉是 vision-language-action 模型目前缺的那一路高密度接触信号
- 没有可迁移的触觉 backbone，每次换传感器都要重训策略
- 触觉仿真（Tactile Genesis 类）和真实采集（HTT 类 HPT）正在互相补齐基础设施
- 即使表示可用，策略仍需同时解决旧数据缺失新模态、灾难性遗忘和反馈时效性

## 当前理解

| 子问题 | 代表材料 | 立场 |
| --- | --- | --- |
| 触觉硬件配置（位置/分辨率/类型）如何选？ | [[tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks]] | 覆盖面积优先于分辨率；per-taxel 力/力矩在大多数灵巧任务里最稳健 |
| 异构传感器如何共享 backbone？ | [[2606.29948-heterogeneous-tactile-transformer]] | sensor-specific encoder + shared transformer trunk + 跨模态预测对齐；MAE 重建 + 双向跨模态预测 |
| 触觉 backbone 能否迁移到训练时未见的传感器？ | [[2606.29948-heterogeneous-tactile-transformer]] | 已在未出现的 Sharpa 触觉指尖上验证 toy screw / grasp tofu 上的成功率显著提升 |
| 旧数据没有 F/T 标注时，预训练策略如何吸收新模态而不遗忘？ | [[2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force|Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force]] | early + late fusion 联合动作、视频、未来 F/T 预测；旧数据 replay 与 missing-modality mask 同时保留视觉动作先验 |
| 高频触觉如何与低频 VLA 协同？ | [[t-rex-tactile-reactive-dexterous-manipulation|T-Rex: Tactile-Reactive Dexterous Manipulation]] | 慢动作专家缓存视觉语言上下文，快触觉专家沿同一 flow 去噪轨迹细化动作，形成约 5 Hz / 20 Hz 的异步闭环 |
| 动作 chunk 执行期间，最新触觉如何继续修改未来动作？ | [[2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback|TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback]] | 未来动作保留 flow 中间态，动作块边生成边执行；EATA 只让当前触觉条件化下一待执行块，避免远期动作接收陈旧信号 |

## 关键设计要点

- **统一输入规范**：时序窗 τ + 减参考帧，让不同采样率、不同维度的传感器在 backbone 内行为可比。
- **跨模态监督源**：利用"同一次接触被多传感器同步记录"作为天然对齐信号，无需人工标注。
- **解耦结构**：sensor-specific encoder/decoder + shared trunk，让每个传感器保留局部细节、共享语义进入统一潜空间。
- **imbalance 风险**：光学-阵列配对中，光学富信息会主导跨模态预测，阵列侧会出现 −4.3% 这种回退；需要 imbalance-aware 损失。
- **持续适配接口**：MuSe 用缺失模态 mask、旧数据 replay 和未来多感官预测，让没有 F/T 标签的预训练数据仍能约束新模态适配，避免只在新任务上微调造成旧能力塌陷。
- **多速率控制接口**：T-Rex 把低频视觉规划和高频触觉细化放在同一 flow 轨迹上，说明表示进入策略后还需要清楚的频率分工。
- **时间作用域接口**：触觉更新不应无条件广播给所有未来动作；TacForcing 用 EATA 让当前触觉只影响下一动作块，并把更远动作保留为待后续触觉修订的中间态。

## 当前判断

这几条路线不是互相替代的模型技巧，而是同一条系统链上的不同层：Tactile Genesis 决定“感什么”，HTT 解决“跨硬件怎样表示”，MuSe 解决“怎样把新模态接进已有策略且不忘旧能力”，T-Rex 与 TacForcing 再回答“执行时怎样及时改动作”。当前证据已经说明静态拼接不足，但还没有一个系统同时证明跨传感器迁移、持续适配、旧任务保持和低延迟闭环。

## 未解决问题

- 异构 backbone 在纯阵列平台（无光学传感器）上是否仍可工作？
- imbalance-aware 跨模态对齐是否能同时拿回阵列侧的损失？
- 触觉 backbone 与 VLA 拼接的最优接口是什么（per-token fusion vs late fusion vs dual-stream）？
- MuSe 的 replay + missing-modality mask 能否扩展到多个依次到来的新传感器，而不让回放成本随模态数量持续增长？
- T-Rex 的双专家异步细化与 TacForcing 的单专家流式生成，在哪种算力、延迟和任务时域下各自更合适？
- 单一流式专家已证明执行期更新与 EATA 有效，但论文尚未报告 block size、推理延迟、触觉采样延迟和等算力对比，不能据此判断真实闭环效率。
- 触觉预训练需要多少跨传感器配对数据才能让 backbone 真正可迁移，而不是只适配原 4 种？

## 相关页面

- [[tactile-genesis-exploring-tactile-sensors-at-scale-for-learning-dexterous-tasks]]
- [[2606.29948-heterogeneous-tactile-transformer]]
- [[2606.30988-multisensory-continual-learning-adapting-pretrained-visuomotor-policies-to-force|Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force]]
- [[t-rex-tactile-reactive-dexterous-manipulation|T-Rex: Tactile-Reactive Dexterous Manipulation]]
- [[2608.25798-tacforcing-streaming-action-generation-with-execution-time-tactile-feedback|TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback]]
- [[tactile-force-into-pretrained-robot-policies|触觉与力觉如何进入预训练机器人策略：表示、持续适配与执行闭环]]
- [[Physical/Embodied Intelligence]]（domain）
