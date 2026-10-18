---
id: "unified-visual-tactile-action-modeling-from-human-demonstrations-for-dexterous-manipulation"
slug: "unified-visual-tactile-action-modeling-from-human-demonstrations-for-dexterous-manipulation"
title: "Unified Visual-Tactile-Action Modeling from Human Demonstrations for Dexterous Manipulation"
type: source
material_type: paper
source_type: paper
source_kind: "arxiv_html_url"
source_input: "https://arxiv.org/html/2609.34182v2"
source_url: "https://arxiv.org/abs/2609.34182"
html_url: "https://arxiv.org/html/2609.34182v2"
pdf_url: "https://arxiv.org/pdf/2609.34182"
code_url: "https://github.com/uni-vta/UVTA"
dataset_url: "https://huggingface.co/datasets/Chopper233/UVTA"
project_url: "https://uni-vta.github.io/"
translation_url: "https://hjfy.top/arxiv/2609.34182"
created: "2026-10-18"
updated: "2026-10-18"
date: "2026-09-29"
publish_date: "2026-09-29"
arxiv_id: "2609.34182"
authors:
  - "Wenqiao Li"
  - "Qianyou Zhao"
  - "Jiawen Hao"
  - "Xuezhou Zhu"
  - "Tengyu Liu"
  - "Kaifeng Zhang"
  - "Chuan Wen"
  - "Siyuan Huang"
affiliation: "Shanghai Jiao Tong University; BIGAI; Sharpa Robotics; Beijing Institute of Technology"
related_organizations:
  - "Shanghai Jiao Tong University"
  - "State Key Laboratory of General Artificial Intelligence, BIGAI"
  - "Sharpa Robotics"
  - "Beijing Institute of Technology"
related_companies:
  - "Sharpa Robotics"
domains:
  - "Physical/Embodied Intelligence"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - "Physical/Embodied Intelligence"
tags:
  - "tactile-representation"
keywords:
  - "visual-tactile-action model"
  - "human demonstrations"
  - "dexterous manipulation"
  - "tactile world model"
summary: "UVTA 用可穿戴触觉动捕采集大规模人类接触经验，把人手与机器人手映射到共享 20 维触觉和 31 维动作空间，并通过未来触觉预测学习跨本体接触表征。"
links:
  original: "https://arxiv.org/abs/2609.34182"
  arxiv: "https://arxiv.org/abs/2609.34182"
  html: "https://arxiv.org/html/2609.34182v2"
  pdf: "https://arxiv.org/pdf/2609.34182"
  project: "https://uni-vta.github.io/"
  github: "https://github.com/uni-vta/UVTA"
  dataset: "https://huggingface.co/datasets/Chopper233/UVTA"
  code: "https://github.com/uni-vta/UVTA"
  hjfy: "https://hjfy.top/arxiv/2609.34182"
  doi: "https://doi.org/10.48550/arXiv.2609.34182"
raw_refs:
  - "https://arxiv.org/html/2609.34182v2"
  - "https://arxiv.org/pdf/2609.34182"
  - "https://github.com/uni-vta/UVTA"
  - "https://arxiv.org/abs/2609.34182"
images:
  - "https://arxiv.org/html/2609.34182v2/figures/teaser_2.jpg"
  - "https://arxiv.org/html/2609.34182v2/figures/human_data_system_1.jpg"
  - "https://arxiv.org/html/2609.34182v2/figures/dataset.jpg"
  - "https://arxiv.org/html/2609.34182v2/UVAT.png"
  - "https://arxiv.org/html/2609.34182v2/human_scaling.svg"
  - "https://arxiv.org/html/2609.34182v2/figures/result_1.jpg"
hero_image: "https://arxiv.org/html/2609.34182v2/figures/teaser_2.jpg"
image_paths: []
related_topics:
  - "tactile-representation"
  - "contact-rich-manipulation"
related_syntheses: []
confidence: EXTRACTED
status: analyzed
---

# Unified Visual-Tactile-Action Modeling from Human Demonstrations for Dexterous Manipulation

## 太长不看

UVTA 的核心贡献是把“人类触觉示范”变成机器人灵巧操作的可扩展监督。它不要求人手动作直接可执行，而是把人类与机器人轨迹统一到 20 维触觉、31 维动作空间，并让共享视觉-触觉表征同时预测未来动作和未来触觉轨迹。真机五任务上，UVTA 的平均阶段化成功率为 70%，高于最强视触基线 T-Rex 的 29%；人类数据从 0 增至 1,000 条时，三任务平均从 0% 升至 84%，且曲线在 1,000 条尚未饱和。它的价值在于提出了比本体形态更稳定的“接触物理后果”作为跨本体迁移接口。

## 直观理解

可以把 UVTA 看成让机器人“看一次、摸一次、想象接下来会摸到什么”：腕部相机给出局部视觉，VTPM 把机器人视觉-触觉形变图折算成与人手指尖 FSR 对齐的 20 维压力 token；二者拼接成共享表征后，一个扩散动作头生成 16 步动作，另一个触觉头预测接下来 16 步触觉。人手和机器人手虽然形态不同，但“按压导致压力增大、滑动导致触觉变化、松开会释放接触”的物理关系是共享的。人类数据主要教会模型理解这些关系，机器人数据则提供可执行的动作分布；部署时只解码机器人归一化动作。

![UVTA teaser](https://arxiv.org/html/2609.34182v2/figures/teaser_2.jpg)

*UVTA teaser：人类手与机器人手共享通用交互表征。*

## 核心信息

- **作者**：Wenqiao Li、Qianyou Zhao、Jiawen Hao、Xuezhou Zhu、Tengyu Liu、Kaifeng Zhang、Chuan Wen、Siyuan Huang
- **作者单位**：Shanghai Jiao Tong University、BIGAI、Sharpa Robotics、Beijing Institute of Technology
- **来源类型**：arxiv_html_url
- **输入来源**：https://arxiv.org/html/2609.34182v2
- **原文链接**：https://arxiv.org/abs/2609.34182
- **HTML 正文**：https://arxiv.org/html/2609.34182v2
- **PDF 地址**：https://arxiv.org/pdf/2609.34182
- **项目主页**：https://uni-vta.github.io/
- **代码地址**：https://github.com/uni-vta/UVTA
- **数据集**：https://huggingface.co/datasets/Chopper233/UVTA
- **中英翻译地址**：https://hjfy.top/arxiv/2609.34182
- **发布日期**：2026-09-29
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** 灵巧操作高度依赖接触时机、压力、形变和滑移，而这些状态在视觉中经常被遮挡或语义含糊。传统机器人触觉示范需要多维灵巧手遥操作，操作者又难以获得足够触觉反馈，因此同步视觉、触觉和动作的数据采集成本高、场景多样性受限。人类示范天然包含丰富的接触经验，但人手与机器人手在运动学、传感布局和动作空间上并不一致，不能简单把人的关节角当成机器人命令。

**问题缺口：** 现有 human-to-robot 方法多依赖可恢复的人体运动或重定向后的动作空间，视频预训练也难以显式捕捉局部接触动力学；触觉学习则主要使用机器人触觉数据，或把人类触觉预训练与机器人策略训练分成多个阶段。缺口在于如何在同一训练目标中吸收大规模人类触觉经验，同时保留目标机器人的可执行动作监督，并避免人类动作被误当作机器人控制命令。

![Tactile motion-capture system](https://arxiv.org/html/2609.34182v2/figures/human_data_system_1.jpg)

*Fig. 2：可穿戴 22-DoF 被动外骨骼、VIVE 腕部位姿、指尖 FSR 阵列与腕部 RGB 相机组成同步采集系统。*

## 论文摘要（英文原文）

Dexterous manipulation requires tactile feedback. However, robot tactile demonstrations are difficult to scale because dexterous-hand teleoperation provides limited tactile feedback to the operator. In contrast, human demonstrations offer a substantially more scalable source of diverse tactile interactions. Motivated by a simple premise—hands can change, but the underlying physics of interaction does not—we leverage human tactile data to improve dexterous manipulation policies. Specifically, we first build a tactile motion-capture system that synchronously records images, tactile signals, and hand motions. Using this system, we construct the UVTA dataset spanning five contact-rich tasks, with 1,000 human demonstrations covering diverse interaction patterns and 150 robot demonstrations per task. To transfer the underlying physics of human interaction to robot control, we propose a Unified Visual-Tactile-Action Model that maps both embodiments into aligned tactile and action representations and jointly predicts future action and tactile trajectories. The joint objective enables human demonstrations to supervise contact-aware representation learning, while only robot actions are executed during deployment. In real-robot evaluations across five tasks, our method achieves an average success rate of 70%, outperforming the strongest visual-tactile baseline, which achieves 29%, and an architecture ablation, which achieves 42%. Performance improves consistently with additional human demonstrations and exhibits no saturation at 1,000 demonstrations per task, validating the effectiveness of scalable human tactile data for dexterous manipulation.

## 论文摘要（中文翻译）

灵巧操作需要触觉反馈，但机器人触觉示范难以扩展，因为灵巧手遥操作本身很难给操作者提供足够触觉反馈。相比之下，人类示范提供了规模更大、更多样的触觉交互来源。作者基于“手可以不同，交互的底层物理不变”这一前提，利用人类触觉数据改进机器人灵巧操作策略。他们先构建一个同步记录图像、触觉信号和手部运动的触觉动捕系统，再用它建立覆盖五个接触密集任务的 UVTA 数据集：每个任务包含 1,000 条多样人类示范和 150 条机器人示范。为了把人类交互的物理规律迁移到机器人控制，论文提出 Unified Visual-Tactile-Action Model，把两种本体映射到对齐的触觉与动作表示，并联合预测未来动作和触觉轨迹。联合目标让人类示范监督接触感知表征学习，而部署时只执行机器人动作。五任务真机评估中，该方法平均成功率为 70%，超过最强视触基线的 29% 和架构消融的 42%；性能随人类示范数量持续提升，到 1,000 条仍未饱和。

## 方法

**方法概述：** UVTA 的工作流由三层组成：先用可穿戴触觉动捕和机器人遥操作分别采集数据；再通过 VTPM、腕部相对运动和 22 维手指关节角把两类数据映射到统一触觉与动作表示；最后用同一视觉-触觉条件训练扩散动作头与未来触觉回归头。人类和机器人数据以相等采样质量共同训练，但部署时使用机器人归一化统计量解码动作。触觉预测不进入控制器，而是通过损失回传塑造共享视觉编码器。

**核心机制：** 人类数据的迁移接口不是逐点模仿运动，而是“动作产生什么接触后果”。动作扩散头让模型学会目标本体的可执行动作分布，触觉世界头强迫共享表征预测接触随运动如何变化；两者共享同一个 404 维视觉-触觉条件。由于未来触觉监督来自人类与机器人两类交互，模型能从人类多样接触中学习压力、滑动和释放的物理结构，同时不被要求直接执行人手轨迹。

**方法拆解：**

- **同步触觉动捕系统**：人手每个指尖安装 4 个 FSR 区域，五指形成 20 维压力信号；两个 VIVE Tracker 估计腕部 6-DoF 位姿，被动 22-DoF 连杆外骨骼通过指尖正运动学和受限逆运动学恢复手部关节；腕部鱼眼 RGB 相机的相机-腕部外参与 Sharpa North 对齐。所有流用共享主机时钟打点并重采样到 30 Hz。
- **UVTA 数据集**：五个任务各包含 1,000 条人类示范和 150 条机器人示范，总计 5,750 条。机器人数据在固定场景、初始位姿和桌面高度下由遥操作采集，提供可执行动作；人类数据不接入机器人，改变物体实例、背景和黑白手套外观，扩展接触与场景多样性。
- **统一触觉空间**：VTPM 把机器人 Wave 视觉-触觉形变图的每个手指有效像素分配到四个 canonical taxel 区域，聚合强度后形成与人手 FSR 对齐的 20 维压力表示；两侧分别做录制基线校正和本体归一化，消除不同传感器的原生噪声和量程差异。
- **统一动作空间**：每步动作 31 维，其中 9 维是当前腕部坐标系下的相对腕部位移加 6D 旋转表示，22 维是绝对手指关节角。相对腕部动作减少对全局工作空间的依赖，绝对手指角保留灵巧手的精确构型。
- **共享表征与双头预测**：ViT-S/8 把 224×224 腕部 RGB 编成 384 维视觉 token，与 20 维触觉 token 直接拼接为 404 维表征。FiLM 条件化 1D U-Net 在 50 个噪声级别训练去噪，输出 16×31 动作 chunk；404→512→320 的 MLP 从无噪表征回归 16×20 未来触觉。
- **训练与 rollout**：加权采样给人类与机器人数据集相等概率质量，动作损失分别平均 9 维腕部和 22 维手指组并等权相加，避免手指维度数量压过腕部；总损失为动作损失加 0.2 倍触觉损失，AdamW 训练 300 epoch。部署时 DDIM 16 步采样 16 步动作，执行前 8 个 waypoint 后重新观测规划。

**关键要点：**

- UVTA 的跨本体假设建立在共享交互物理上：接触形成、形变、滑移、释放和物体响应不因手的具体形态而完全改变。
- 人类动作参与训练监督，但从不直接作为机器人命令；机器人统计量才用于部署解码。
- 未来触觉预测是表征学习目标，不是执行期控制器；这一点避免触觉去噪误差污染扩散动作生成。

![Unified model architecture](https://arxiv.org/html/2609.34182v2/UVAT.png)

*Fig. 4：视觉 token 与触觉 token 拼接后，同时驱动扩散动作头和未来触觉预测头。*

![Dataset overview](https://arxiv.org/html/2609.34182v2/figures/dataset.jpg)

*Fig. 3：每任务 150 条低变化机器人示范与 1,000 条多场景人类示范互补。*

## 结果

**核心结果：**

- **主对比**：在 Flip Page、Screw Light Bulb、Toggle Switch、Ball Classification、Liquid Transfer 五个任务上，UVTA 分别取得 83%、80%、88%、56%、44%，平均 70%；ViTacFormer、RDP、T-Rex 分别平均 1%、14%、29%。
- **消融**：去掉未来触觉预测但保留当前触觉输入后，平均从 70% 降至 42%；同时去掉触觉输入后为 26%。加入本体感知条件反而降至 18%，作者观察到策略更像重放固定轨迹而不是响应视觉-触觉变化。
- **人类数据 scaling**：固定每任务 150 条机器人示范，把人类示范从 0 增至 250、500、750、1,000 条，三任务平均从 0% 提升到 8%、29%、51%、84%；750→1,000 的增益仍有 33 个百分点，曲线没有饱和迹象。
- **数据互补性**：仅人类数据得 0%，因为人类轨迹不可直接执行；仅 150 条机器人数据在该实验设置中也为 0%。这说明收益来自“人类多样接触监督 + 机器人可执行动作监督”的联合训练。
- **评估口径**：每个任务 10 次真机 rollout，阶段化评分给部分完成度。例如 Flip Page 分离页边 0.3、翻多页 0.7、正好翻一页 1.0。因此 70% 是进度型平均成功率，不是完整任务全成功率。

**结果表：**

| 配置 | Flip Page | Light Bulb | Toggle Switch | Ball Classification | Liquid Transfer | 平均 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| ViTacFormer | 0 | 4 | 0 | 0 | 0 | 1 |
| RDP | 10 | 20 | 20 | 18 | 0 | 14 |
| T-Rex | 43 | 26 | 24 | 36 | 15 | 29 |
| 仅人类数据 | 0 | 0 | 0 | 0 | 0 | 0 |
| 去掉未来触觉预测 | 58 | 38 | 50 | 44 | 21 | 42 |
| 仅视觉 | 47 | 23 | 26 | 20 | 14 | 26 |
| 加本体感知 | 22 | 20 | 14 | 20 | 15 | 18 |
| **UVTA** | **83** | **80** | **88** | **56** | **44** | **70** |

![Human-data scaling](https://arxiv.org/html/2609.34182v2/human_scaling.svg)

*Fig. 5：固定 150 条机器人示范时，人类触觉示范从 0 增至 1,000 条，三个任务及其平均性能持续提升。*

![Real-robot rollouts](https://arxiv.org/html/2609.34182v2/figures/result_1.jpg)

*Fig. 6：UVTA 在五个接触密集任务上的代表性真机执行轨迹。*

## 洞察

**核心 insight：**

- UVTA 的关键不是把触觉作为额外输入，而是把“未来触觉轨迹”作为世界模型监督，使视觉表征被迫编码动作与接触后果之间的物理联系。
- 人类数据的价值被限定在表征学习层，执行层仍由机器人数据和机器人归一化动作负责；这比直接动作重定向更符合“共享物理、不同形态”的前提。
- 触觉回归头放在扩散轨迹之外是重要工程设计：触觉预测影响训练梯度，但不让触觉去噪误差参与动作采样，降低执行链路的不确定性。
- 相比只学习当前触觉，未来触觉更关注接触演化，能区分类似视觉状态但物理后果不同的动作。

**和已有方法的关系：** 相对人类视频预训练，UVTA显式采集压力和接触后果，避免只靠视觉推断触觉；相对 T-Rex、RDP 等视触策略，它把人类触觉示范纳入同一动作-触觉联合目标，而不是只用机器人触觉；相对分阶段的触觉预训练或人类触觉中训练，UVTA 采用单阶段人类-机器人共同训练，并用平衡采样处理数据量差异。它与 Tacross/Heterogeneous Tactile Transformer 关注的跨传感器表示相关，但核心问题是跨本体迁移而非仅传感器统一。

**可借鉴点：** 数据系统可以把人类采集装备设计成与目标机器人腕相机、触觉布局和动作维度近似对齐，降低迁移接口成本；训练多本体数据时可用本体分别归一化加部署侧机器人解码，避免人类动作被误执行；对接触密集任务，增加“预测未来触觉/力”这一辅助目标可能是比堆叠更多视觉特征更直接的物理监督。

## 风险与判断

**局限：**

- 现阶段只测量五个指尖，每指四个 FSR 区域，手掌、手背和其他接触面未被记录；VTPM 也会把机器人视觉-触觉形变压缩到 20 维压力 token，可能丢失空间纹理、剪切力和高频力信息。
- 实验覆盖五个实验室任务、一个 Sharpa North/Sharpa Wave 平台、每个任务一个专用策略、至多 1,000 条人类示范和一个模型规模，尚不能证明跨机器人、跨任务、跨多本体或更大规模数据下的行为。
- 每任务 10 次 rollout 的统计量很小；70% 是阶段化部分得分，不等同于完整成功率。主结果和消融都应理解为研究信号而非稳定的工程成功率。
- 人类与机器人动作通过统一 31 维布局和标定转换对齐，论文未证明该接口在其他手型、触觉传感器或不同腕相机几何上可直接迁移。
- 未来触觉预测不用于控制，说明系统尚缺少执行期利用预测触觉进行规划、回退或安全约束的机制；触觉信号质量、时间同步和基线漂移仍可能影响表征。

**适用场景：**

- 适合指尖接触主导、视觉易遮挡、需要根据压力或滑移调整的灵巧任务，例如翻页、旋灯泡、按开关、通过触摸辨识材质和移液。
- 适合已有一定量机器人遥操作示范但难以扩展，同时能搭建可穿戴触觉动捕、能将机器人触觉映射到 20 维 taxel、并把人类/机器人动作转换到统一腕手布局的系统。
- 适合把人类数据用作表征学习增强而非直接动作来源的研究路线，尤其在机器人数据不足以覆盖物体、背景和接触多样性时。

**最终判断：**

- UVTA 是一篇证据清晰的人触数据迁移论文：采集系统、统一表示、联合目标和 scaling 实验共同支持“人类触觉示范能改善机器人灵巧操作”。
- 它最有价值的观点是把跨本体监督放在共享接触物理后果上，而不是放在不可靠的人机动作一一对应上。未来触觉预测从 70% 到 42% 的消融差，是这一设计必要性的强证据。
- 但当前结果仍受限于小评测规模、单平台、任务专用策略和指尖触觉覆盖。应把它视为向 scalable tactile learning 迈出的系统级验证，而不是已解决的通用跨本体触觉策略。

## 结果速览表

| 问题 | UVTA 的回答 |
| --- | --- |
| 人类触觉数据是否有价值？ | 五任务平均 70%，高于最强基线 29%；无人类数据设置为 0%。 |
| 未来触觉预测是否关键？ | 去掉后平均从 70% 降至 42%；再去掉触觉输入为 26%。 |
| 人类数据是否可扩展？ | 0→1,000 条人类示范，三任务平均 0%→84%，750→1,000 仍提升 33 个百分点。 |
| 数据规模 | 每任务 1,000 条人类 + 150 条机器人，总计 5,750 条、30 Hz 同步。 |
| 当前边界 | 五个实验室任务、单平台、任务专用策略、指尖触觉、每任务 10 次评估。 |

## 相关主题

- [[tactile-representation|Tactile Representation]]：UVTA 通过 VTPM 和未来触觉预测，把人类触觉示范纳入机器人接触表征学习。
- [[contact-rich-manipulation|Contact-Rich Manipulation and Adaptive Compliance]]：翻页、旋灯泡、按开关、材质分类和移液都是视觉不可靠、接触反馈关键的灵巧操作场景。
