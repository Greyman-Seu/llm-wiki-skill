---
title: "TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM"
source_type: paper
source_kind: "local_pdf"
source_input: "/tmp/turbovla-2607.27205.pdf"
source_url: "https://arxiv.org/abs/2607.27205"
html_url: "https://arxiv.org/html/2607.27205"
pdf_url: "https://arxiv.org/pdf/2607.27205"
code_url: "https://github.com/H-EmbodVis/TurboVLA"
translation_url: "https://hjfy.top/arxiv/2607.27205"
publish_date: "2026-07-29"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - Physical/Embodied Intelligence
domains:
  - Physical/Embodied Intelligence
authors:
  - Hengyi Xie
  - Chenfei Yao
  - Xianjin Wu
  - Xuanyang Xi
  - Yiping Tang
  - Di Xu
  - Yingying Zhu
  - Dingkang Liang
  - Xiang Bai
  - Han Ding
affiliation: ""
related_organizations:
  - Huazhong University of Science and Technology
  - Huawei Technologies
related_companies:
  - Huawei Technologies
tags:
  - vision-language-action
keywords:
  - vision-language-action
raw_refs:
  - https://arxiv.org/abs/2607.27205
  - https://arxiv.org/html/2607.27205v1
images:
  - https://arxiv.org/html/2607.27205v1/x2.png
related_topics:
  - vision-language-action
status: analyzed
---

# TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM

## 太长不看

TurboVLA 将高频控制从 LLM 居中的 V→L→A 改为轻量的直接 V+L→A，在 LIBERO 达到 97.7% 且只需 0.2B、31.2ms、0.9GB。

## 直观理解

它将慢速规划与快速执行分离：执行器只负责把当前画面与指令对齐，并行输出连续动作。

![主要图](https://arxiv.org/html/2607.27205v1/x2.png)

*主要图*

## 核心信息

- **作者**：Hengyi Xie、Chenfei Yao、Xianjin Wu、Xuanyang Xi、Yiping Tang、Di Xu、Yingying Zhu、Dingkang Liang、Xiang Bai、Han Ding
- **作者单位**：暂无
- **来源类型**：local_pdf
- **输入来源**：/tmp/turbovla-2607.27205.pdf
- **原文链接**：https://arxiv.org/abs/2607.27205
- **HTML 正文**：https://arxiv.org/html/2607.27205
- **PDF 地址**：https://arxiv.org/pdf/2607.27205
- **代码地址**：https://github.com/H-EmbodVis/TurboVLA
- **中英翻译地址**：https://hjfy.top/arxiv/2607.27205
- **发布日期**：2026-07-29
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** 现有 VLA 往往把视觉投影到大语言模型空间，再由该空间生成机器人动作。即使使用并行 action expert，LLM 仍处在每个控制周期的关键路径，因此带来显存、延迟和本地部署成本。

**问题缺口：** 论文要验证的是：在任务指令主要描述对象、属性和空间关系的执行级操作中，是否能保留必要的语言 grounding，却不再让大语言模型充当视觉到动作的中心接口，从而提高控制频率。

## 论文摘要（英文原文）

TurboVLA replaces the LLM-centric V→L→A pathway with lightweight bidirectional vision-language interaction and a compact continuous action decoder.

## 论文摘要（中文翻译）

TurboVLA 以轻量双向视觉—语言交互和紧凑连续动作解码器取代 LLM 居中的高频执行路径。

## 方法

**方法概述：** 面向执行级操作的高效率 VLA。

**核心机制：** DINOv3 和 BERT 分别编码视觉与指令，六层双向 cross-attention 交换信息；ACT 风格动作块 decoder 结合机器人状态并行预测动作。

**方法拆解：** - 保留 token 级文本表示以对齐对象、属性和空间关系.
- 双向 cross-attention 同时更新视觉与指令流.
- 一次输出连续动作块，避免自回归动作 token.

在 LIBERO 中，模型用 DINOv3 ViT-B、12 步 7-DoF 动作块和混合四套件训练；在 RoboTwin 2.0 中改用 ViT-L、50 步 14 维双臂动作块。论文的比较单位是“从多模态输入到一个动作块”，因此其延迟优势同时来自更轻的语义路径和非自回归输出，而不只是参数少。

**关键要点：** - 执行级控制不必让大语言模型处于每个控制步的关键路径.

![方法图](https://arxiv.org/html/2607.27205v1/x2.png)

*方法图*

## 结果

**核心结果：** - LIBERO 97.7%，0.2B、31.2ms、0.9GB.
- RoboTwin 2.0 为 60.2%，43.4ms.

在 50 个双臂 RoboTwin 任务上，TurboVLA 的 60.2% 高于 π0.5 的 57.0%，且后者报告 95.6ms；真机 AgileX Piper 的四项任务为 92.5%、80%、90%、87.5%。真机方案以 LIBERO 预训练权重为起点，每任务用 65 条示范微调 12.5k steps，因此它验证的是快速执行的可部署性，而不是零样本开放世界泛化。

消融表明语言没有被“简化掉”：去掉语言时平均成功率从 97.7% 降为 70.8%，Goal 套件从 97.4% 降为 11.6%。无交互、单向交互和双向交互分别为 95.2%、96.1/96.5% 和 97.7%；交互层数 2/4/6/8 的结果为 93.5/95.7/97.7/96.6%，动作 horizon 8/10/12/15 为 96.4/96.9/97.7/95.6%。

**结果表：** | 指标 | TurboVLA |\n| --- | --- |\n| LIBERO 平均成功率 | 97.7% |\n| 参数/延迟/显存 | 0.2B / 31.2ms / 0.9GB |

## 洞察

**核心 insight：** - 适合与慢速规划器组成分层系统.
- 移除的是高频 LLM 中枢而不是语言条件.

**和已有方法的关系：** - 直接对视觉与语言做双向交互.

**可借鉴点：** - 让 LLM 留在任务规划而非高频控制路径.

## 风险与判断

**局限：** - 不证明长程规划或开放式语义推理能力.

**适用场景：** - 消费级 GPU 本地语言条件操作.

**最终判断：** - 跨模型延迟仍受动作块长度和实现细节影响.

更完整的判断是：这不是“VLA 不需要 LLM”，而是将 LLM 放到任务分解、异常恢复或人机交互等低频层，把视觉—语言 grounding 与连续控制交给轻量执行器。对已经具备上层规划器的机器人系统，这是可信且具工程价值的模块化路线。

## 结果速览表

| 指标 | TurboVLA |\n| --- | --- |\n| LIBERO 平均成功率 | 97.7% |\n| 参数/延迟/显存 | 0.2B / 31.2ms / 0.9GB |

## 相关主题

- vision-language-action.
