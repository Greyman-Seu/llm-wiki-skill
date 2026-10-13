---
id: "3d-native-embodied-model"
slug: "3d-native-embodied-model"
title: "3D-Native Embodied Model"
type: topic
created: "2026-10-12"
updated: "2026-10-13"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "3d-representation"
  - "world-action-model"
summary: "收集把具身模型的观测、动作、世界状态和异构数据统一到显式 3D 空间的路线，比较 BEV、点流、体素、SE(3) 动作空间与世界预测接口的取舍。"
source_slugs:
  - "2610.12099-unitas-a-3d-native-world-action-model-for-embodied-manipulation"
  - "2606.02274-dexterity-bev-aligning-3d-world-and-actions-for-generalizable-robot-policies-learning"
  - "spatial-forcing-implicit-spatial-representation-alignment-for-vision-language-action-model"
synthesis_slugs: []
status: active
open_questions:
  - "BEV 投影、点流、体素与隐式 3D latent 在什么任务复杂度和传感器噪声下最合适？"
  - "统一 3D 接口能否在无可靠相机外参、无深度和无精确 URDF 的开放环境中保持收益？"
  - "跨本体共享的是动作轨迹、场景后果、技能语义还是控制接口？哪一层迁移最有效？"
  - "3D-native 世界模型的预测精度怎样转化为规划、安全和在线纠错收益？"
  - "空间/时间对齐管线自身的标注误差和计算成本是否被充分评估？"
---
# 3D-Native Embodied Model

> 目标不是“给 VLA 加深度图”，而是让观测、身体、动作与世界后果共享一个可计算的物理空间。

## 主题概述

3D-native embodied model 关注具身基础模型的物理接口：多视角图像如何被锚定到度量坐标，机器人/人类动作如何摆脱本体与基座约定，环境状态如何被显式预测，不同采样率和遥操作速度如何被归一化。该主题将 BEV 表示、aligned vertex map、point flow、scene flow、统一 TCP/SE(3) 动作、隐式空间 latent 对齐和异构数据处理管线放在同一条研究线上，后续可继续注入 3D-aware VLA、world model、跨本体动作表示和数据对齐工作。

## 代表工作

- [来源: UNITAS: A 3D-Native World Action Model for Embodied Manipulation](../sources/2610.12099-unitas-a-3d-native-world-action-model-for-embodied-manipulation.md)
  把观测、action flow 和 scene flow 放进同一度量 3D 帧。机器人夹爪和人类手都是点轨迹，环境响应是动作条件 scene flow；物理时间 tokenizer 处理异构采样率。1.7B 模型在 LIBERO 达 99.8%，RoboTwin scene prediction 的 Moving ADE 为 0.427 cm。

- [来源: Dexterity-BEV: Aligning 3D World and Actions for Generalizable Robot Policies Learning](../sources/2606.02274-dexterity-bev-aligning-3d-world-and-actions-for-generalizable-robot-policies-learning.md)
  提供坐标与数据基础设施：aligned vertex map/vertex spectrum 接入 2D VLM，合成 BEV 图降低相机位姿差异，统一 TCP/SE(3) 与速度归一化处理跨本体和跨遥操作轨迹。Modified LIBERO 中从 2D 基线的 `<10%` 提升到 89.9%。

- [来源: Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model](../sources/spatial-forcing-implicit-spatial-representation-alignment-for-vision-language-action-model.md)
  提供训练期隐式对齐路线：VGGT 从多视角 RGB 产生空间 latent，监督 VLA 第 24 层视觉 token；推理时不调用 VGGT、不增加模块。LIBERO 平均 98.5%，同等成功率训练加速 3.8×，5% 数据下达 75.8%。

## 路线对比

| 维度 | Dex-BEV | UNITAS | Spatial Forcing |
| --- | --- | --- | --- |
| 核心对象 | 多视角观测、机器人动作、异构数据管线 | 观测、身体动作与环境响应的联合模型 | VLA 中间层视觉表征 |
| 3D 表示 | aligned vertex map、vertex spectrum、BEV 图 | world-aligned PE、action flow、scene flow | VGGT 空间 latent |
| 动作接口 | 统一 TCP 与 canonical BEV 帧中的 SE(3) pose | 末端 action chunk 与身体点轨迹并行输出 | 不改变原动作接口 |
| 时间处理 | 按标准平移/旋转速度重参数化轨迹 | 以物理秒编码并 tokenizer 整条点轨迹 | 不显式重参数化时间 |
| 世界预测 | 不显式预测未来状态 | 输出动作条件 scene flow / 点轨迹 | 不预测世界状态 |
| 推理开销 | 依赖 BEV 构建与几何输入 | policy-only 可跳过流分支 | 零新增结构，VGGT 只在训练期使用 |
| 最强证据 | 强相机与布局扰动下 89.9% | RoboTwin 场景误差 0.427 cm + LIBERO 99.8% | LIBERO 98.5%，训练加速 3.8× |
| 主要依赖 | 精确相机外参与可定义 BEV ROI | 几何 query、对应点监督、有限 3 秒窗口 | VGGT 教师、多视角配对与层选择 |

## 当前判断

- **Dex-BEV 解决“先把数据放进同一个物理坐标系”**：它证明输入输出与时间的系统对齐可以显著提升跨本体和抗视角扰动能力，但本身还不是生成式世界模型。
- **UNITAS 把该接口推进到世界动作层**：身体点与环境点共享 flow 表示，使动作生成和后果预测可以共享监督，而不必通过视频像素作为中间表示。
- **两者互补而非替代**：Dex-BEV 的 BEV/TCP/时间对齐可以作为 UNITAS 类点流模型的预处理和数据组织层；UNITAS 则补上 Dex-BEV 缺少的动作条件未来预测。
- **Spatial Forcing 提供低侵入迁移路径**：它不要求部署期深度、相机标定或新动作空间，适合作为已有 RGB VLA 的空间表征增强；但它也没有解决动作语义、跨本体坐标或世界后果预测。
- **显式几何不是免费午餐**：外参、深度、URDF、TCP、对应点与轨迹标注的误差都会进入学习目标；专题后续必须同时记录性能和标注/校准成本。
- **跨本体迁移的关键是语义层选择**：BEV/SE(3) 让空间一致，point flow 让运动语义一致，但接触力学、技能效果与控制约束仍未被完全表达。

## 后续注入标准

- **纳入**：提出或评估显式 3D 空间接口、BEV/点流/体素/3D latent、统一跨本体动作空间、3D 世界预测、或面向机器人数据的几何-时间对齐管线。
- **优先级高**：有强相机/本体/布局扰动实验、跨数据集预训练、动作条件世界预测、消融拆分空间表示与动作接口，或讨论校准误差与部署成本。
- **避免重复**：仅在输入端拼接深度但没有改变观测-动作关系的工作，放入 Vision-Language-Action 或相关 3D-aware VLA 页面即可，除非它对跨本体/时空对齐有明确贡献。

## 相关页面

- [[2610.12099-unitas-a-3d-native-world-action-model-for-embodied-manipulation|UNITAS]]
- [[2606.02274-dexterity-bev-aligning-3d-world-and-actions-for-generalizable-robot-policies-learning|Dexterity-BEV]]
- [[spatial-forcing-implicit-spatial-representation-alignment-for-vision-language-action-model|Spatial Forcing]]
- [[Vision-Language-Action]]
- [[OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining]]
