---
id: "foar-force-aware-reactive-policy-for-contact-rich-robotic-manipulation"
slug: "foar-force-aware-reactive-policy-for-contact-rich-robotic-manipulation"
title: "FoAR: Force-Aware Reactive Policy for Contact-Rich Robotic Manipulation"
type: source
material_type: "paper"
source_type: paper
source_kind: "online_pdf_url"
source_input: "https://arxiv.org/pdf/2411.15753"
created: "2026-09-06"
updated: "2026-09-06"
date: "2025-05-02"
publish_date: "2025-05-02"
source_url: "https://arxiv.org/abs/2411.15753"
html_url: "https://arxiv.org/html/2411.15753v2"
pdf_url: "https://arxiv.org/pdf/2411.15753"
code_url: "https://tonyfang.net/FoAR/"
translation_url: "https://hjfy.top/arxiv/2411.15753"
arxiv_id: "2411.15753"
authors:
  - "Zihao He"
  - "Hongjie Fang"
  - "Jingjing Chen"
  - "Hao-Shu Fang"
  - "Cewu Lu"
affiliation: "Shanghai Jiao Tong University"
related_organizations:
  - "Shanghai Jiao Tong University"
related_companies: []
domains:
  - "physical-embodied-intelligence"
domain: "physical-embodied-intelligence"
primary_domain_slug: "physical-embodied-intelligence"
domain_slugs:
  - "physical-embodied-intelligence"
tags:
  - "力觉控制"
summary: "FoAR 将高频六维力/扭矩历史、RGB-D 点云和扩散动作头组合成一个阶段感知策略：独立预测未来接触概率 phi，用 phi 对力觉特征做软门控；部署时以 phi、8N 力阈值和 5N·m 扭矩阈值触发 0.006m 反应式位置修正。该设计在小样本真实机器人设置中同时改善接触精度与非接触动作可靠性。"
keywords:
  - "contact-rich manipulation"
  - "force/torque sensing"
  - "reactive control"
links:
  original: "https://arxiv.org/abs/2411.15753"
  arxiv: "https://arxiv.org/abs/2411.15753"
  html: "https://arxiv.org/html/2411.15753v2"
  pdf: "https://arxiv.org/pdf/2411.15753"
  project: ""
  github: ""
  code: "https://tonyfang.net/FoAR/"
  hjfy: "https://hjfy.top/arxiv/2411.15753"
  doi: "https://doi.org/10.48550/arXiv.2411.15753"
raw_refs:
  - "https://arxiv.org/html/2411.15753v2"
  - "https://arxiv.org/pdf/2411.15753"
  - "https://tonyfang.net/FoAR/"
  - "https://arxiv.org/abs/2411.15753"
related_topics:
  - "contact-rich-manipulation"
related_syntheses:
  - "force-touch-robot-policy-review"
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2411.15753v2/teaser.png"
images:
  - "https://arxiv.org/html/2411.15753v2/teaser.png"
  - "https://arxiv.org/html/2411.15753v2/model.png"
  - "https://arxiv.org/html/2411.15753v2/task.png"
  - "https://arxiv.org/html/2411.15753v2/peel.png"
  - "https://arxiv.org/html/2411.15753v2/chop-metric.png"
image_paths: []
status: analyzed
---

# FoAR: Force-Aware Reactive Policy for Contact-Rich Robotic Manipulation

## 太长不看

FoAR 的关键不是把力/扭矩简单拼到视觉策略上，而是先预测未来是否会接触，再用这个概率门控力觉特征，并在部署时用力觉触发小步反应式修正。仅用 50 条示范，它在擦除、削皮和切菜等接触丰富任务上显著超过 RISE 与多种融合基线，并在白板被移动或重写后保持 100% 基本动作成功率。

## 直观理解

把机器人想成同时拥有“远视”和“触觉”：点云负责看清场景与目标，100Hz 力/扭矩历史负责判断是否真正压到物体。FoAR 先问“未来几步会不会接触”，只有答案接近会接触时才放大力觉信息；一旦预测要接触但当前力不足，就沿动作块的前进方向补一个很小的位置步长。这样既避免了非接触阶段的传感器噪声，又不需要完整的阻抗控制器。

![主要图](https://arxiv.org/html/2411.15753v2/teaser.png)

*主要图*

## 核心信息

- **作者**：Zihao He、Hongjie Fang、Jingjing Chen、Hao-Shu Fang、Cewu Lu
- **作者单位**：Shanghai Jiao Tong University
- **来源类型**：online_pdf_url
- **输入来源**：https://arxiv.org/pdf/2411.15753
- **原文链接**：https://arxiv.org/abs/2411.15753
- **HTML 正文**：https://arxiv.org/html/2411.15753v2
- **PDF 地址**：https://arxiv.org/pdf/2411.15753
- **代码地址**：https://github.com/arXiv/html_feedback
- **中英翻译地址**：https://hjfy.top/arxiv/2411.15753
- **发布日期**：2025-05-02
- **主题域**：physical-embodied-intelligence

## 背景与问题

**动机：** 擦除、削皮、切菜等任务的难点不是到达某个视觉目标，而是在接触发生后持续保持合适的法向力、方向和时序。接触前后的 RGB 或点云差异很小，视觉策略无法可靠知道工具是否真正压到表面；力/扭矩传感器能直接暴露物理交互，但在抓取、移动等非接触阶段又会产生噪声。此前把力觉特征全程拼接或作为额外 token 的做法没有区分任务阶段，可能反过来伤害抓取和接近动作。

**问题缺口：** 论文要解决的是一个具体的阶段选择问题：如何让策略只在即将接触或已经接触时依赖高频力/扭矩，同时保留视觉策略在非接触阶段的泛化能力；以及如何把这种接触判断转化为无需手工调刚度、接触方向的在线纠偏。FoAR 以未来接触概率作为共享接口，将感知融合和反应式控制统一起来。

## 论文摘要（英文原文）

Contact-rich tasks present significant challenges for robotic manipulation policies due to the complex dynamics of contact and the need for precise control. Vision-based policies often struggle with the skill required for such tasks, as they typically lack critical contact feedback modalities like force/torque information. To address this issue, we propose FoAR, a force-aware reactive policy that combines high-frequency force/torque sensing with visual inputs to enhance the performance in contact-rich manipulation. Built upon the RISE policy, FoAR incorporates a multimodal feature fusion mechanism guided by a future contact predictor, enabling dynamic adjustment of force/torque data usage between non-contact and contact phases. Its reactive control strategy also allows FoAR to accomplish contact-rich tasks accurately through simple position control. Experimental results demonstrate that FoAR significantly outperforms all baselines across various challenging contact-rich tasks while maintaining robust performance under unexpected dynamic disturbances.

## 论文摘要（中文翻译）

接触丰富任务具有复杂的接触动力学，并要求精确控制，因此对机器人操作策略很具挑战。基于视觉的策略通常缺少力/扭矩等关键接触反馈，难以完成这类任务。论文提出 FoAR，一种融合高频力/扭矩感知与视觉输入的力觉感知反应式策略。FoAR 构建在 RISE 之上，引入由未来接触预测器引导的多模态特征融合，在非接触和接触阶段动态调节力/扭矩数据的使用比例。其反应式控制策略还使机器人仅用简单的位置控制就能准确完成接触丰富操作。实验表明，FoAR 在多种具有挑战性的接触丰富任务上显著超过所有基线，并能在意外动态扰动下保持稳健性能。

## 方法

**方法概述：** FoAR 将高频六维力/扭矩历史、RGB-D 点云和扩散动作头组合成一个阶段感知策略：独立预测未来接触概率 phi，用 phi 对力觉特征做软门控；部署时以 phi、8N 力阈值和 5N·m 扭矩阈值触发 0.006m 反应式位置修正。该设计在小样本真实机器人设置中同时改善接触精度与非接触动作可靠性。

**核心机制：** 策略输入当前 RGB-D 点云 p_t、约 2 秒窗口的 100Hz 六维力/扭矩历史 f_(t-To:t) 和 RGB 图像 I_t。稀疏 3D 编码器与 Transformer 产出 512 维场景特征 h_s，三层 MLP 加时间 Transformer 产出 512 维力觉特征 h_f；独立的 ResNet18+MLP 接触预测器输出未来接触概率 phi。融合特征为 [h_s; phi*h_f+(1-phi)*h*]，再条件化扩散去噪动作头生成未来动作块；训练用动作 L2 损失与接触二元交叉熵之和，部署时按 phi 和力/扭矩阈值做反应式位置修正。

**方法拆解：**

- 阶段感知编码：点云经稀疏 3D ResNet 与 Transformer 得到场景 token；100Hz 力/扭矩序列经 MLP、正弦位置编码和时间 Transformer 得到力觉 token。
- 未来接触门控：独立预测器用当前 RGB 与力觉历史预测未来接触概率 phi，并将力觉特征软门控到 phi*h_f+(1-phi)*h*，避免非接触噪声污染策略。
- 扩散动作生成：门控后的多模态特征作为条件，扩散动作头逐步去噪生成长度为 T_a 的末端执行器动作块。
- 部署反应式控制：当 phi>=0.9 且当前力低于 8N 或扭矩低于 5N·m 时，沿预测动作块的平均前进方向补偿 epsilon=0.006m；接触与非接触阶段使用独立时间集成缓冲区。

**关键要点：**

- “是否需要触觉”本身是可学习的时序决策，软门控比全程拼接或 token 注入更能处理接触稀疏性。
- 未来接触预测和反应式控制是协同设计：预测器既控制特征融合，也决定何时启用力觉纠偏，降低了单独设计模块的接口错配。

![方法图](https://arxiv.org/html/2411.15753v2/model.png)

*方法图*

![方法图](https://arxiv.org/html/2411.15753v2/task.png)

*方法图*

## 结果

**核心结果：**

- 真实平台为 Flexiv Rizon + Dahuan AG-95 + OptoForce 六轴力/扭矩传感器 + RealSense D435，工作空间 45cm x 60cm x 40cm；每个擦除/削皮任务 50 条示范，切菜 40 条示范。
- 擦除、一般擦除和削皮得分分别为 0.875、0.850、0.756，三项抓取与接触动作 ASR 均为 100%；对应最佳基线 RISE 得分为 0.500、0.500、0.377。
- 切菜中 FoAR 平均切出 3.9±0.9 段，归一化段长均值/标准差 0.353/0.094；RISE 仅 1.8±0.6 段，0.727/0.411，FoAR 更接近示范 oracle 的 5.0 段和 0.200/0.056。
- 擦除消融显示 100Hz+预测器+反应式控制得分 0.875、擦除 ASR 100%；去掉反应式控制得分降至 0.650，降到 2Hz/10Hz 时分别为 0.625/0.800。
- 一般擦除的 Rewrite、Move、Rewrite+Move 扰动下，FoAR 得分/抓取 ASR/擦除 ASR 始终为 0.800-0.850/100%/100%，而 RISE 与 force-token 版本明显波动。

**结果表：**

| 任务/方法 | 得分 | 关键 ASR |
| --- | ---: | ---: |
| 擦除 FoAR | 0.875 | 抓取 100%，擦除 100% |
| 擦除（一般）FoAR | 0.850 | 抓取 100%，擦除 100% |
| 削皮 FoAR | 0.756 | 抓取 100%，削皮 100% |
| 擦除 RISE | 0.500 | 抓取 100%，擦除 75% |
| 削皮 RISE | 0.377 | 抓取 100%，削皮 50% |
| 切菜 FoAR | 3.9±0.9 段 | Place ASR 70% |
| 切菜 RISE | 1.8±0.6 段 | Place ASR 30% |

![结果图](https://arxiv.org/html/2411.15753v2/peel.png)

*结果图*

![结果图](https://arxiv.org/html/2411.15753v2/chop-metric.png)

*结果图*

## 洞察

**核心 insight：**

- 这项工作的主要贡献更像“控制接口设计”而非新的扩散骨干：把接触状态预测变成融合门控和控制触发器，使一个视觉策略能在不同物理阶段切换信息源。
- FoAR (3D-cls) 共享点云编码器后反而显著变差，说明接触预测关注“是否接触”的粗粒度线索，而动作策略需要物体位置和末端姿态等细粒度线索，两个目标应保持表示隔离。
- 100Hz 力觉并非越高越好，而是与 10Hz 动作输出形成快慢时标互补；2Hz/10Hz/100Hz 的消融直接展示了接触瞬态对采样率的敏感性。

**和已有方法的关系：**

- 相较 RISE、ACT 和 Diffusion Policy 的纯视觉路线，FoAR 增加了高频力觉和阶段门控；相较 force-token/force-concat，它显式建模接触时机而不是全程注入。

**可借鉴点：**

- 对任何稀疏激活的传感模态先学习一个“何时可信”的门控变量，再把门控同时接到特征融合和执行逻辑，可迁移到触觉、音频或事件相机。
- 保留非接触与接触两套时间集成缓冲区，避免接触阶段的动作块污染自由空间轨迹，是实现反应式策略时一个低成本的工程细节。

## 风险与判断

**局限：**

- 静态阈值（8N、5N·m、phi=0.9）依赖传感器、工具和任务，换环境后需要重新标定，尚未证明跨机器人或跨物体的阈值不变性。
- 实验规模较小且为单臂、单相机、三类精心设计任务；切菜仅 FoAR 与 RISE 各 10 次，统计置信区间和失败模式覆盖有限。
- 位置控制下的纠偏只是沿动作方向的固定小步，不能显式控制法向力、顺应性或切向摩擦；论文也承认复杂环境可能需要混合力/位置或阻抗控制。

**适用场景：**

- 适合擦除、削皮、插入、打磨、切割等接触状态难以从视觉区分、且需要持续或瞬时力调整的单臂操作。
- 也适合作为现有视觉扩散策略的增量模块：当已有位置控制接口但缺少力觉闭环时，可先复用门控预测器和小步纠偏。

**最终判断：**

- 证据支持 FoAR 在受控真实机器人场景中显著改善接触成功率和动作质量，但不能据此宣称已解决通用力控；其优势依赖 OptoForce 传感器、示范分布和任务阈值，跨平台部署仍需校准与更强控制器。

## 结果速览表

| 任务/方法 | 得分 | 关键 ASR |
| --- | ---: | ---: |
| 擦除 FoAR | 0.875 | 抓取 100%，擦除 100% |
| 擦除（一般）FoAR | 0.850 | 抓取 100%，擦除 100% |
| 削皮 FoAR | 0.756 | 抓取 100%，削皮 100% |
| 擦除 RISE | 0.500 | 抓取 100%，擦除 75% |
| 削皮 RISE | 0.377 | 抓取 100%，削皮 50% |
| 切菜 FoAR | 3.9±0.9 段 | Place ASR 70% |
| 切菜 RISE | 1.8±0.6 段 | Place ASR 30% |

## 相关主题

- contact-rich-manipulation.
