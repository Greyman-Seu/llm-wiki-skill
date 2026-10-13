---
id: "spatial-forcing-implicit-spatial-representation-alignment-for-vision-language-action-model"
slug: "spatial-forcing-implicit-spatial-representation-alignment-for-vision-language-action-model"
title: "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model"
type: source
material_type: "paper"
source_type: paper
source_kind: "arxiv_abs_url"
source_input: "https://arxiv.org/abs/2510.12276v2"
created: "2026-10-11"
updated: "2026-10-11"
date: "2025-10-14"
publish_date: "2025-10-14"
source_url: "https://arxiv.org/abs/2510.12276v2"
html_url: "https://arxiv.org/html/2510.12276v2"
pdf_url: "https://arxiv.org/pdf/2510.12276v2"
code_url: "https://spatial-forcing.github.io/"
translation_url: "https://hjfy.top/arxiv/2510.12276"
arxiv_id: "2510.12276"
authors:
  - "Fuhao Li"
  - "Wenxuan Song"
  - "Han Zhao"
  - "Jingbo Wang"
  - "Pengxiang Ding"
  - "Donglin Wang"
  - "Long Zeng"
  - "Haoang Li"
affiliation: "The Hong Kong University of Science and Technology (Guangzhou); Tsinghua University; Westlake University; Zhejiang University; South China University of Technology"
related_organizations:
  - "The Hong Kong University of Science and Technology (Guangzhou)"
  - "Tsinghua University"
  - "Westlake University"
  - "Zhejiang University"
  - "South China University of Technology"
related_companies: []
domains:
  - "Physical/Embodied Intelligence"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - "Physical/Embodied Intelligence"
tags:
  - "vision-language-action"
  - "representation alignment"
summary: "SF 在动作损失旁增加中间层视觉表示对齐损失：VGGT 处理多视角图像得到像素级空间 latent；VLA 视觉 token 经归一化与两层 MLP 后，与带位置嵌入的 VGGT token 做 cosine 对齐。推理时不调用 VGGT、不加模块，保持原 VLA 前向路径。"
keywords:
  - "vision-language-action"
  - "representation alignment"
  - "VGGT"
links:
  original: "https://arxiv.org/abs/2510.12276v2"
  arxiv: "https://arxiv.org/abs/2510.12276v2"
  html: "https://arxiv.org/html/2510.12276v2"
  pdf: "https://arxiv.org/pdf/2510.12276v2"
  project: "https://spatial-forcing.github.io/"
  github: ""
  code: "https://spatial-forcing.github.io/"
  hjfy: "https://hjfy.top/arxiv/2510.12276"
  doi: "https://doi.org/10.48550/arXiv.2510.12276"
raw_refs:
  - "https://arxiv.org/html/2510.12276v2"
  - "https://arxiv.org/pdf/2510.12276v2"
  - "https://spatial-forcing.github.io/"
  - "https://arxiv.org/abs/2510.12276v2"
related_topics:
  - "3d-native-embodied-model"
  - "vision-language-action"
related_syntheses: []
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2510.12276v2/fig_teaser.png"
images:
  - "https://arxiv.org/html/2510.12276v2/fig_teaser.png"
  - "https://arxiv.org/html/2510.12276v2/fig_compare.png"
  - "https://arxiv.org/html/2510.12276v2/fig_probing.png"
  - "https://arxiv.org/html/2510.12276v2/fig_visual.png"
  - "https://arxiv.org/html/2510.12276v2/fig_real.png"
image_paths: []
status: analyzed
---

# Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model

## 太长不看

Spatial Forcing 用 VGGT 的多视角空间 latent 监督 VLA 中间层视觉 token，推理阶段不增结构，在 LIBERO 达到 98.5% 并带来 3.8× 训练效率提升。

## 直观理解

训练时给 VLA 的视觉 token 上一门几何同步课；推理时老师退场，模型仍按原 VLA 路径输出动作。

![主要图](https://arxiv.org/html/2510.12276v2/fig_teaser.png)

*主要图*

## 核心信息

- **作者**：Fuhao Li、Wenxuan Song、Han Zhao、Jingbo Wang、Pengxiang Ding、Donglin Wang、Long Zeng、Haoang Li
- **作者单位**：The Hong Kong University of Science and Technology (Guangzhou); Tsinghua University; Westlake University; Zhejiang University; South China University of Technology
- **来源类型**：arxiv_abs_url
- **输入来源**：https://arxiv.org/abs/2510.12276v2
- **原文链接**：https://arxiv.org/abs/2510.12276v2
- **HTML 正文**：https://arxiv.org/html/2510.12276v2
- **PDF 地址**：https://arxiv.org/pdf/2510.12276v2
- **项目页面**：https://spatial-forcing.github.io/
- **中英翻译地址**：https://hjfy.top/arxiv/2510.12276
- **发布日期**：2025-10-14
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** 机器人操作要判断夹爪、目标、桌面和相机之间的三维关系，而 VLA 视觉骨干主要来自 2D 图像预训练；深度探测显示其表示难以恢复有意义空间结构。

**问题缺口：** 显式 3D 输入依赖传感器和标定，已有机器人数据也常缺深度；从 2D 图像估深度则把误差转嫁给估计器。论文需要一种复用于 RGB 多视角数据且推理零开销的空间能力注入方法。

![三类 3D VLA 范式](https://arxiv.org/html/2510.12276v2/fig_compare.png)

*三类 3D VLA 范式：显式传感器输入、显式深度估计辅助、隐式表征对齐。*

![深度探测](https://arxiv.org/html/2510.12276v2/fig_probing.png)

*冻结 VLA 表示并训练 DPT 深度头：未对齐表示难以恢复空间结构，SF 对齐后更接近深度图。*

## 论文摘要（英文原文）

Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions. However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in the 3D physical world. Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, hardware heterogeneity, and incomplete depth coverage in existing datasets. Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators. We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit 3D inputs or depth estimators. SF aligns intermediate visual embeddings of VLAs with geometric representations produced by pretrained 3D foundation models. By enforcing alignment at intermediate layers, SF guides VLAs to encode richer spatial representations that enhance action precision. Extensive experiments in simulation and real-world environments demonstrate that SF achieves state-of-the-art results, surpassing both 2D- and 3D-based VLAs. SF further accelerates training by up to 3.8x and improves data efficiency across diverse robotic tasks.

## 论文摘要（中文翻译）

多数 VLA 建立在仅用 2D 数据预训练的 VLM 上，缺乏准确空间感知；显式深度/点云输入受传感器噪声、硬件异构和数据覆盖限制，深度估计又受估计器性能约束。Spatial Forcing 把 VLA 中间视觉嵌入与预训练 3D 基础模型的几何表示对齐，在不依赖显式 3D 输入或深度估计器的情况下隐式强化空间理解。仿真和真机实验显示其超过 2D/3D VLA 基线，最高带来 3.8× 训练加速并改善数据效率。

## 方法

**方法概述：** SF 在动作损失旁增加中间层视觉表示对齐损失：VGGT 处理多视角图像得到像素级空间 latent；VLA 视觉 token 经归一化与两层 MLP 后，与带位置嵌入的 VGGT token 做 cosine 对齐。推理时不调用 VGGT、不加模块，保持原 VLA 前向路径。

**核心机制：** SF 把几何先验作为中间表征正则：VGGT 输出跨视角一致空间 latent，目标 token 加位置嵌入；VLA 第 24 层视觉 token 经 BN 与两层 MLP 后与对应 token 做负 cosine 对齐，并与动作损失联合优化。

**方法拆解：**

- 多视角教师表示：VGGT 同时处理 primary/wrist 图像，输出跨视角一致的像素级空间 latent。
- token 对齐接口：VLA 视觉 token 先归一化、投影，再与带位置嵌入的 VGGT token 做 cosine 对齐。
- 联合目标：动作损失与负 cosine 对齐损失按 α 加权相加，附录显示 α=0.5 优于 0.02、0.1、2.5 和 12.5。
- 部署路径：VGGT 与投影头只用于训练，推理时保持原 VLA 输入、骨干和动作头不变。

**关键要点：**

- SF 把 3D 感知从输入模态问题转换成表征监督问题，普通多视角 RGB 数据即可产生几何教师信号。
- 位置嵌入和监督层位置重要：VGGT+PE 为 96.9%，无 PE 为 94.7%；第 24 层优于第 1、8、16、32 层。

![方法图](https://arxiv.org/html/2510.12276v2/fig_teaser.png)

*方法图*

## 结果

**核心结果：**

- LIBERO 四套件平均 98.5%，高于 OpenVLA-OFT 97.1%、π0 94.2%、SpatialVLA 78.1%；每个任务 500 次评测。
- 单卡消融中 SF 20K 步 93.7%、50K 步 96.5%，基线 150K 步 92.7%；同等成功率训练加速 3.8×。
- 数据效率：5% LIBERO 数据达到 75.8%，1% 数据仅 42.3%；论文报告同等成功率数据效率提升 5.9×。
- RoboTwin 2.0：基于 π0+LoRA，在 easy/hard 双臂任务上报告最高平均成功率；hard 设置包含背景、光照、杂乱和桌高随机化，论文强调改善尤其明显。
- AgileX 真机：单臂 40 条示范、每任务 40 次评测，双臂 20 条示范、20 次评测；堆叠玻璃杯提升 47.5 个百分点，放置绿块达到 85%。

**结果表：**

| 设置 | 指标 | 结果 | 对照 |
| --- | --- | ---: | ---: |
| LIBERO 平均 | 成功率 | SF 98.5% | OpenVLA-OFT 97.1%；GeoVLA 97.7%；3D-CAVLA 98.1% |
| LIBERO-Long | 成功率 | SF 96.0% | OpenVLA-OFT 94.5%；π0 85.2% |
| 同等成功率训练 | 迭代效率 | 3.8× 加速 | OpenVLA-OFT 基线 |
| 5% LIBERO 数据 | 平均成功率 | 75.8% | 1% 数据 42.3%；100% 数据 96.9% |
| 真机堆叠玻璃杯 | 相对提升 | +47.5pp | 对应无 SF 基线 |
| 真机放置绿块 | 成功率 | 85% | 对应无 SF 基线 |

![结果图](https://arxiv.org/html/2510.12276v2/fig_visual.png)

*结果图*

![结果图](https://arxiv.org/html/2510.12276v2/fig_real.png)

*结果图*

## 洞察

**核心 insight：**

- SF 的价值在于把几何先验作为中间表征正则，而不是作为输入特征或显式深度标签，减少传感器依赖并让动作损失继续决定任务相关信息。
- 与 SpatialVLA 等显式 3D 输入相比，SF 不改变部署输入；与 REPA 式表示对齐相比，它把目标换成 VGGT 的多视角几何 latent，并面向 VLA 动作生成。

**和已有方法的关系：** SF 属于训练期教师、推理期移除的表示对齐路线，不同于把深度/点云作为部署输入或先用深度估计器改写观测的路线。

**可借鉴点：** 机器人策略可用训练期教师注入昂贵模态，但需检查教师误差、对齐层、损失权重与 token 位置信息，避免表征坍缩或任务信息被稀释。

## 风险与判断

**局限：**

- 实验集中在 LIBERO、RoboTwin 和少量 AgileX 任务；真机每任务仅 20/40 条示范，任务数量与跨硬件方差不足以证明通用鲁棒性。
- 训练依赖 VGGT 的多视角质量与相机布置，且需额外教师前向、token 对应和显存成本；与 GeoVLA/3D-CAVLA 差距很小。

**适用场景：**

- 适合已有 RGB 多视角数据、难以配置深度/点云传感器、且希望保持原 VLA 推理延迟的空间布局、高度判断和双臂相对位置任务。

**最终判断：**

- 值得作为 VLA 表示对齐基线跟进；核心是 3D 教师监督接入中间视觉 token 并保持推理零开销，但更多机器人、动态场景、接触任务和教师失配条件仍待验证。

## 结果速览表

| 设置 | 指标 | 结果 | 对照 |
| --- | --- | ---: | ---: |
| LIBERO 平均 | 成功率 | SF 98.5% | OpenVLA-OFT 97.1%；GeoVLA 97.7%；3D-CAVLA 98.1% |
| LIBERO-Long | 成功率 | SF 96.0% | OpenVLA-OFT 94.5%；π0 85.2% |
| 同等成功率训练 | 迭代效率 | 3.8× 加速 | OpenVLA-OFT 基线 |
| 5% LIBERO 数据 | 平均成功率 | 75.8% | 1% 数据 42.3%；100% 数据 96.9% |
| 真机堆叠玻璃杯 | 相对提升 | +47.5pp | 对应无 SF 基线 |
| 真机放置绿块 | 成功率 | 85% | 对应无 SF 基线 |

## 相关主题

- [[3d-native-embodied-model|3D-Native Embodied Model]]：本篇提供隐式空间表征对齐路线，说明 3D 先验可以在训练期注入而在推理期零开销保留。
- [[vision-language-action]]
