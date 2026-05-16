---
id: "mem-multi-scale-embodied-memory-for-vision-language-action-models"
slug: "mem-multi-scale-embodied-memory-for-vision-language-action-models"
title: "MEM: Multi-Scale Embodied Memory for Vision Language Action Models"
type: source
material_type: "paper"
source_type: "paper"
created: "2026-05-11"
updated: "2026-05-16"
date: "2026-03-04"
authors:
  - "Marcel Torne"
  - "Karl Pertsch"
  - "Homer Walke"
  - "Kyle Vedder"
  - "Suraj Nair"
  - "Brian Ichter"
  - "Allen Z. Ren"
  - "Haohuan Wang"
  - "Jiaming Tang"
  - "Kyle Stachowicz"
  - "Karan Dhabalia"
  - "Michael Equi"
  - "Quan Vuong"
  - "Jost Tobias Springenberg"
  - "Sergey Levine"
  - "Chelsea Finn"
  - "Danny Driess"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "long-horizon-memory"
summary: ""
links:
  original: "https://arxiv.org/abs/2603.03596"
  arxiv: "https://arxiv.org/abs/2603.03596"
  pdf: "https://arxiv.org/pdf/2603.03596.pdf"
  project: ""
  github: ""
  hjfy: "https://hjfy.top/arxiv/2603.03596"
  doi: ""
raw_refs:
  - "https://arxiv.org/html/2603.03596v1"
related_topics:
  - "vision-language-action"
  - "long-horizon-memory-for-robot-policies"
related_syntheses:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2603.03596v1/x1.png"
images: 3
image_paths:
source_url: "https://arxiv.org/abs/2603.03596"
html_url: "https://arxiv.org/html/2603.03596"
pdf_url: "https://arxiv.org/pdf/2603.03596.pdf"
translation_url: "https://hjfy.top/arxiv/2603.03596"
status: analyzed
---
# MEM: Multi-Scale Embodied Memory for Vision Language Action Models

## 太长不看

这篇工作的重点，是把机器人策略里的“记忆”从单一历史帧堆叠，升级成多尺度、多模态的长期记忆结构。MEM 用视频短期记忆处理最近视觉细节，用文本长期记忆保留高层语义进度，从而把 VLA 推到更长时间跨度的任务上。

## 直观理解

如果普通 VLA 的记忆更像“最近几秒发生了什么”，那 MEM 想解决的是“机器人十分钟前做过什么、现在做到哪一步、接下来该切到哪个阶段”。它试图让策略同时记住局部感知细节和全局任务进度。

![主要图](https://arxiv.org/html/2603.03596v1/x1.png)

*主要图*

## 核心信息

- **作者**：Marcel Torne 等
- **原文链接**：https://arxiv.org/abs/2603.03596
- **HTML 正文**：https://arxiv.org/html/2603.03596v1
- **PDF 地址**：https://arxiv.org/pdf/2603.03596.pdf
- **发布日期**：2026-03-04
- **主题域**：physical-embodied-intelligence

## 背景与问题

**动机：** 长时程机器人任务不是简单地看当前帧就能决策。比如做饭、整理厨房、做三明治，机器人既要记住最近的遮挡和物体位置，也要记住更长时间的任务阶段进展。

**问题缺口：** 传统 end-to-end policy 的记忆往往只是在输入里堆过去观测，难以同时兼顾短期视觉细节和长期语义状态。作者要解决的是：怎样让 VLA 在长达十几分钟的任务中真正具备“多层次记忆”。

## 论文摘要（英文原文）

Conventionally, memory in end-to-end robotic learning involves inputting a sequence of past observations into the learned policy. However, in complex multi-stage real-world tasks, the robot's memory must represent past events at multiple levels of granularity: from long-term memory that captures abstracted semantic concepts (e.g., a robot cooking dinner should remember which stages of the recipe are already done) to short-term memory that captures recent events and compensates for occlusions (e.g., a robot remembering the object it wants to pick up once its arm occludes it). In this work, our main insight is that an effective memory architecture for long-horizon robotic control should combine multiple modalities to capture these different levels of abstraction. We introduce Multi-Scale Embodied Memory (MEM), an approach for mixed-modal long-horizon memory in robot policies. MEM combines video-based short-horizon memory, compressed via a video encoder, with text-based long-horizon memory. Together, they enable robot policies to perform tasks that span up to fifteen minutes, like cleaning up a kitchen, or preparing a grilled cheese sandwich. Additionally, we find that memory enables MEM policies to intelligently adapt manipulation strategies in-context.

## 论文摘要（中文翻译）

传统端到端机器人学习中的记忆，通常只是把过去一段观测序列输入给策略。然而在复杂的多阶段真实任务中，机器人记忆必须在多个粒度上表示过去事件：既要有记录高层语义进度的长期记忆，也要有补偿遮挡和保留近期细节的短期记忆。作者的核心观点是，长时程机器人控制需要把多种模态结合起来，分别承载这些不同层次的抽象。为此他们提出 MEM，将视频短期记忆和文本长期记忆结合起来，使策略能够完成长达十五分钟的任务，并在上下文中更智能地调整 manipulation 策略。

## 方法

**方法概述：** MEM 试图把机器人策略中的记忆做成分层结构，而不是简单地把更多历史帧堆进上下文窗口。它把 memory 分成两类：短期 dense visual memory 和长期 semantic memory，并分别用视频编码器和语言记忆来承载。

**核心机制：**

- 高层 policy 更新 language memory，用于记录长期语义事件与任务阶段
- 低层 policy 使用短期 observation-based memory，处理遮挡、近时感知和局部调整
- 两类 memory 一起接入 VLA，使策略既能记住高层进度，也能保留近期视觉细节

**方法拆解：**

- 语言长期记忆负责存“已经做过什么、还没做什么、当前任务阶段是什么”
- 视频短期记忆通过高效 video encoder 压缩近期视觉历史，避免直接把长序列原样送进 backbone
- MEM 被集成进 π0.6 这类通用 VLA，使其能在长时程任务上保持 runtime 可接受
- 论文还强调 memory 不只是提升 recall，还能帮助策略在上下文里改变 manipulation strategy

![方法图](https://arxiv.org/html/2603.03596v1/x3.png)

*方法图*

**关键要点：**

- 长期语义记忆和短期视觉记忆必须分开建模
- memory 设计要考虑实时性，否则长历史会让推理延迟不可用
- 这是把 VLA 往 long-horizon agent 化推进的一条关键路线

## 结果

**核心结果：**

- MEM 支持跨度长达 `15 分钟` 的任务
- 代表任务包括 cleanup kitchen、preparing a grilled cheese sandwich 等多阶段真实操作
- 论文强调：没有 memory 的强 generalist policy 如 π0.6，在这些任务上明显不足；而组合短期视频记忆和长期语言记忆后，性能显著提升
- 除了完成长时程任务，MEM 还支持 in-context adaptation，例如根据任务过程动态改变 grasp 高度、开门方向等 manipulation strategy

![结果图](https://arxiv.org/html/2603.03596v1/x5.png)

*结果图*

**结果表：**

| 维度 | MEM 结论 |
| --- | --- |
| 记忆结构 | 视频短期 + 语言长期 |
| 时间跨度 | 最长约 15 分钟 |
| 代表收益 | 长时程任务完成率与策略适应性提升 |
| 相对无记忆基线 | 明显更强 |

## 洞察

**核心 insight：**

- 这篇论文最重要的贡献，是把机器人 memory 从“上下文长度问题”提升成了“表示分层问题”。作者不是简单让模型看更多历史，而是明确区分哪些信息应该以视觉形式保留、哪些信息应该以语义形式长期保存。

**和已有方法的关系：**

- 相对直接堆历史帧的做法，它更关注 memory abstraction
- 相对只做 low-level history encoder 的路线，它把 long-horizon semantic progress 也纳入体系
- 相对 agent 式高层规划，这篇更接近把 memory 直接内嵌进 policy 结构

**可借鉴点：**

- 未来 long-horizon VLA 很可能都需要显式 memory decomposition
- language memory 很适合作为任务阶段与语义进度的载体
- 这篇对“具身智能为什么需要 memory module”给出了很有说服力的结构性答案

## 风险与判断

**局限：**

- 长期语言记忆如何更新、压缩与纠错，本身就是新的复杂系统问题
- 多模态 memory 会显著增加训练和系统设计复杂度
- 这条路线虽然强，但也意味着更高的工程门槛和更重的模型维护成本

**适用场景：**

- 长时程多阶段 manipulation
- 需要显式任务进度管理的具身系统
- 面向 kitchen cleanup、recipe execution 这类真实长流程场景

**最终判断：** 这篇是你这套 wiki 里非常值得保留的 `memory for embodied intelligence` 核心论文，后续很适合做 topic 页的骨架。

## 结果速览表

| 维度 | 结论 |
| --- | --- |
| 记忆类型 | 视频短期 + 文本长期 |
| 目标问题 | 长时程多阶段控制 |
| 实现重点 | 记忆分层与高效编码 |
| 代表能力 | 最长 15 分钟任务 |

## 相关主题

- vision-language-action
- long-horizon-memory-for-robot-policies

## 相关页面

- [[Vision-Language-Action]]
- [[Long-Horizon Memory for Robot Policies]]
- [[当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据]]
- [[π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities]]
