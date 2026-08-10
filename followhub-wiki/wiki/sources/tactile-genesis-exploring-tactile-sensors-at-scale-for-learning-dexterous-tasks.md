---
title: "Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks"
source_type: paper
source_kind: "local_pdf"
source_input: "/tmp/tactile-genesis-2606.22332.pdf"
source_url: "https://arxiv.org/abs/2606.22332"
html_url: "https://arxiv.org/html/2606.22332"
pdf_url: "https://arxiv.org/pdf/2606.22332"
code_url: "https://neuroagents-lab.github.io/tactile-genesis/"
translation_url: "https://hjfy.top/arxiv/2606.22332"
publish_date: "2026-07-09"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - Physical/Embodied Intelligence
domains:
  - Physical/Embodied Intelligence
authors:
  - Trinity Chung
  - Kashu Yamazaki
  - Dhruv Patel
  - Alexis Duburcq
  - Yiling Qiao
  - Katerina Fragkiadaki
  - Aran Nayebi
affiliation: ""
related_organizations:
  - Carnegie Mellon University
  - Genesis AI
related_companies:
  - Genesis AI
tags:
  - tactile-sensing
keywords:
  - tactile-sensing
raw_refs:
  - https://arxiv.org/abs/2606.22332
  - https://arxiv.org/html/2606.22332
images:
  - https://followhub.tenstep.top/papers/2606.22332-tactile-genesis/figure-1-overview-cropped.png
related_topics:
  - tactile-sensing
status: analyzed
---

# Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks

## 太长不看

Tactile Genesis 用大规模仿真比较触觉设计：先扩覆盖，再选类型，最后加分辨率。

## 直观理解

在同一只虚拟手上替换触觉配置，公平比较硬件观测的价值。

![主要图](https://followhub.tenstep.top/papers/2606.22332-tactile-genesis/figure-1-overview-cropped.png)

*主要图*

## 核心信息

- **作者**：Trinity Chung、Kashu Yamazaki、Dhruv Patel、Alexis Duburcq、Yiling Qiao、Katerina Fragkiadaki、Aran Nayebi
- **作者单位**：暂无
- **来源类型**：local_pdf
- **输入来源**：/tmp/tactile-genesis-2606.22332.pdf
- **原文链接**：https://arxiv.org/abs/2606.22332
- **HTML 正文**：https://arxiv.org/html/2606.22332
- **PDF 地址**：https://arxiv.org/pdf/2606.22332
- **代码地址**：https://neuroagents-lab.github.io/tactile-genesis/
- **中英翻译地址**：https://hjfy.top/arxiv/2606.22332
- **发布日期**：2026-07-09
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** 每一种传感器配置几乎都等于一只新机器人，现实中难以在相同任务和策略下公平比较。视觉与本体感觉无法直接观测滑移、局部接触和力闭合丢失等状态。

**问题缺口：** 在固定灵巧操作流程中，应优先选择何种触觉表示、将其布置在哪里、采用多少分辨率，并且这些结论在带漂移与坏点的噪声下是否保持。

## 论文摘要（英文原文）

Tactile Genesis is a GPU-parallel tactile simulation platform for comparing tactile abstractions in dexterous learning.

## 论文摘要（中文翻译）

Tactile Genesis 是用于比较灵巧操作触觉抽象的 GPU 并行仿真平台。

## 方法

**方法概述：** 面向灵巧手触觉设计的受控学习消融。

**核心机制：** 统一实现接触、深度、力/力矩、弹性体位移、接近、音频和温度；先用 PPO 训练可见特权状态的 teacher，再蒸馏只看本体感觉和一种触觉表示的 student。

**方法拆解：** - 传感器可附着于任意机器人表面并共享位置与分辨率接口.
- 统一建模读延迟、噪声、漂移、坏点、迟滞和串扰.
- 控制变量不变，只替换触觉观测.

为保证比较的是触觉而非策略，teacher 以完整物体状态和本体感觉训练；student 仅以本体感觉加一种触觉表示模仿 teacher，并用预测特权状态的辅助头作训练正则。实现上，接触 kernel 对 probes/environment 向量化，网格和点云查询用 BVH，弹性体 dilation/crosstalk 用 FFT，因此可进入大批量 student 训练的并行规模。

![方法图](https://followhub.tenstep.top/papers/2606.22332-tactile-genesis/figure-1-overview-cropped.png)

*方法图*

## 结果

**核心结果：** - 单 GPU 超过 20,000 并行环境和 1,000+ taxels，相对既有模拟器报告 3–20x 吞吐提升.
- 整手约 200 taxels 已可覆盖实验任务.

三项任务均显示本体感觉 baseline 落后于任意触觉 student。仅指尖明显差于整手；补上手掌和近端指节可填补大部分差距。掌内复位中 per-taxel force/torque 最能反映将发生的滑移；掌内旋转中 proximity 因在接触前感到物体而有优势；螺丝刀的短暂接触任务中各触觉类型都未追上 teacher，缺失的可能是时间整合或视觉而非更复杂接触阵列。

作者还验证了弹性体读数：其 GelSight marker 位移拟合优于 FOTS/HydroShear，但对局部力向量任务不如 force/torque，因为邻近压入与剪切会共同影响一个 marker。真实 XHand1 的指尖聚合力策略得到连续 1–2 次旋转，和仿真中相近观测的趋势吻合，但不构成大规模真机成功率基准。

**结果表：** | 设计选择 | 论文结论 |\n| --- | --- |\n| 覆盖位置 | 整手显著优于仅指尖 |\n| 默认表示 | per-taxel 力/力矩最稳健 |

## 洞察

**核心 insight：** - 覆盖面积通常比指尖高分辨率更值得优先投资.
- 传感器应按滑移、接近和短暂触点等失败机制匹配.

**和已有方法的关系：** - 并列比较多种触觉抽象.

**可借鉴点：** - 使用同一 teacher 和策略隔离观测设计作用.

## 风险与判断

**局限：** - teacher-student 设置限制学生策略上限.

**适用场景：** - 灵巧手传感器布置与策略观测选择.

**最终判断：** - 真机验证是趋势证据而非大规模成功率基准.

硬件决策顺序应是：先覆盖手掌和近端指节，再选择 per-taxel 力/力矩，最后才为具体任务增加 proximity 或更高分辨率。该结论是受控仿真—蒸馏条件下的设计指导，采购真实硬件前仍须针对目标物体、传感器耐久和实际噪声验证。

## 结果速览表

| 设计选择 | 论文结论 |\n| --- | --- |\n| 覆盖位置 | 整手显著优于仅指尖 |\n| 默认表示 | per-taxel 力/力矩最稳健 |

## 相关主题

- tactile-sensing.
