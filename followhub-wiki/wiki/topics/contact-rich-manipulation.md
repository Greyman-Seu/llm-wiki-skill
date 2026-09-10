---
id: "contact-rich-manipulation"
slug: "contact-rich-manipulation"
title: "Contact-Rich Manipulation and Adaptive Compliance"
type: topic
created: "2026-08-28"
updated: "2026-09-10"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "contact-rich-manipulation"
summary: "接触密集操作中的运动—力联合学习路线：如何从示范、实时反馈、训练期力蒸馏或动作后果预测获得任务相关接触表示，并在安全接触、轨迹精度、硬件成本、快速响应与部署价值学习之间动态权衡。"
source_slugs:
  - "adaptive-compliance-policy-learning-approximate-compliance-for-diffusion-guided-control"
  - "2503.02881-reactive-diffusion-policy-slow-fast-visual-tactile-policy-learning-for-contact-rich-manipulation"
  - "fm-vla-force-based-memory-for-vision-language-action-models-in-contact-rich-manipulation"
  - "fd-vla-force-distilled-vision-language-action-model-for-contact-rich-manipulation"
  - "facet-0"
  - "2410.07554-forcemimic-force-centric-imitation-learning-with-force-motion-capture-system-for-contact-rich-manipulation"
  - "foar-force-aware-reactive-policy-for-contact-rich-robotic-manipulation"
  - "2605.11048-forceflow-learning-to-feel-and-act-via-contact-driven-flow-matching"
  - "2609.05832-cr-vla-force"
synthesis_slugs:
  - "force-touch-robot-policy-review"
status: "active"
open_questions:
  - "从单条示范构造的近似柔顺标签能否扩展到六维、夹持、强摩擦与高速接触？"
  - "腕部力矩、指尖触觉和视觉接触估计在柔顺策略中应如何分工与融合？"
  - "学习策略与低层导纳、阻抗或混合力位控制器之间，什么动作接口最能跨机器人迁移？"
  - "不显式输出目标力时，怎样证明策略确实利用高频 wrench 学到了主动压入与卸力，而不是只在复现视觉轨迹？"
  - "如何在不损坏工具或物体的前提下，统一评测接触成功、轨迹误差、峰值力和扰动恢复？"
  - "联合预测动作与未来 wrench 后，critic 的收益有多少来自更好的因果接触表示，又有多少来自任务级本地适配？"
  - "当策略每约 1 秒才刷新一次观测时，十步高频力历史能否应对突发碰撞，还是仍需要独立的高频安全与触觉反应层？"
  - "当学习策略直接预测前馈力时，如何检测错误目标力并在跨机器人控制器迁移时给出可验证的安全边界？"
---

# Contact-Rich Manipulation and Adaptive Compliance

> 这条路线研究机器人在持续接触中如何同时“走对轨迹”和“用对力”，并让柔顺方向与幅值随任务阶段、接触几何和扰动动态变化。

## 这条主题在讲什么

接触密集操作不是纯位置预测问题。刚性控制能压住轨迹误差，却可能把几毫米的视觉或标定偏差放大成巨大内力；各方向统一放软虽然降低碰撞风险，又会因摩擦和外力偏离目标。真正需要的是任务相关、方向相关、时间相关的柔顺性：接触前保证定位，接触后沿约束方向让步，在仍需追踪的方向保持足够刚度，并在几何变化或扰动出现时快速重估。

这个问题会反复出现在擦拭、翻转、插入、沿面跟随、装配、灵巧手和双臂协作中，因此它不是普通 tag，而是一条连接示教学习、力/触觉表示、动作生成和低层控制器接口的持续问题线。

## 为什么重要

- 真实机器人误差不可避免，纯位置策略容易把误差转成危险接触力。
- 固定均匀柔顺不能同时满足精确追踪和安全接触，柔顺性必须随方向与阶段变化。
- 学习策略通常低频运行，稳定接触还需要高频导纳、阻抗或触觉反馈回路兜底。
- 不同机器人开放的控制接口不同，动作表示是否能跨硬件执行会直接决定方法的工程价值。

## 当前理解

| 子问题 | 代表材料 | 当前证据 |
| --- | --- | --- |
| 单条示范无法辨识完整人体阻抗时，怎样得到可学习标签？ | [[Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control]] | 不恢复真实质量、阻尼和刚度；只构造满足避免巨大内力与鼓励轨迹跟踪两项性质的近似柔顺轮廓。 |
| 柔顺方向怎样表示？ | [[Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control]] | 沿反馈力方向设低刚度、正交方向设高刚度；参考位姿与虚拟目标之差编码低刚度方向。 |
| 学习策略和低层控制器怎样分工？ | [[Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control]] | 扩散策略滚动预测参考位姿、虚拟目标和刚度标量，高频导纳控制器执行重建后的刚度矩阵。 |
| 不显式输出目标力时，怎样学到主动接触修正？ | [[Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation]] | 慢速 latent diffusion 规划 action chunk；快速非对称 tokenizer 用最新力/触觉条件化解码，在位姿动作空间产生亚毫米级闭环修正。 |
| 高频接触反馈还能怎样进入现代生成策略？ | [[Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation]]、[[T-Rex: Tactile-Reactive Dexterous Manipulation]]、[[TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback]] | 三种接口分别是独立快速动作解码器、共享 flow 轨迹上的快慢专家，以及单一流式专家内可修订的未来动作块。 |
| 接触反馈怎样成为长期任务进度，而不只服务即时纠偏？ | [[FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation]] | 用重建预训练的 Force-VAE 把完整 wrench 历史压成 8 个长期事件 token，再由约 0.9 秒的 state token 提供接触前运动上下文。 |
| 部署平台没有力传感器时，训练期真实力还能怎样发挥作用？ | [[FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation]] | 用真实力潜变量监督视觉—状态条件化的 learnable query；推理时只保留预测力 token，但它是任务相关先验而非安全级闭环力反馈。 |
| 怎样让策略在动作执行前就比较接触后果，而不只在碰撞后响应？ | [[Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation]] | 联合生成笛卡尔动作块与未来 wrist-wrench，再由分布式 Action–Wrench Critic 区分几何进度相似但接触结果不同的提案；预测 wrench 不直接执行。 |
| 如何以自然的人手交互采集真实力—位示范，并将其迁移到机器人控制？ | [[ForceMimic: Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation]] | ForceCapture 在无机器人条件下记录六维 wrench、SLAM 位姿和 RGB-D；HybridIL 预测位姿—wrench，并由正交混合力位控制器执行。 |
| 如何在不增加复杂低层力控参数的情况下，把高频力觉用于接触阶段纠偏？ | [[FoAR: Force-Aware Reactive Policy for Contact-Rich Robotic Manipulation]] | 独立未来接触预测器以 phi 门控力觉特征，并在 phi>=0.9 且力/扭矩不足时沿动作方向做 0.006m 位置修正；100Hz 力觉、反应式控制与视觉扩散策略协同工作。 |
| 低维 wrench 怎样避免被高维视觉掩盖，并同时支持物理与空间 OOD？ | [[ForceFlow: Learning to Feel and Act via Contact-Driven Flow Matching]] | 十步 wrench 与本体状态通过 AdaLN 全局调制 flow-matching DiT，视觉只作 cross-attention 空间锚定；V2F 再把 VLM 定位与局部接触执行解耦。 |
| 低频 VLA 怎样把期望力交给高频控制器，并在动作块内部持续柔顺？ | [[2609.05832-cr-vla-force|CR-VLA-Force]] | pi0 每秒预测一次位姿—夹爪—力动作块，历史力 token 与残差 MoE 负责接触感知，VG-ACC 以 500 Hz 根据力误差趋势调刚度；六条件平均成功率 89.2%，擦板 base 力误差 5.52%。 |

<!-- confidence: INFERRED -->

## 关键设计轴

- **柔顺来源**：解析接触模型、重复示范统计、单示范近似标签、强化学习探索，或执行期触觉修正。
- **空间结构**：统一标量刚度、逐轴对角刚度、完整六维刚度矩阵，还是由参考目标与虚拟目标隐式编码方向。
- **时间结构**：接触前预调、接触后响应、动作 chunk 内反馈更新、突发扰动恢复，以及跨整个 episode 的接触事件计数与进度记忆。
- **策略—控制接口**：策略直接输出力、刚度、导纳参数、虚拟目标，或只输出由独立高频控制器修正的位置动作。
- **观测硬件**：腕部六轴力矩适合估计整体接触方向，指尖触觉适合局部滑移与形变；二者的可迁移性、成本和带宽不同。
- **评测目标**：任务成功率之外，还应记录峰值力、工具/物体损坏、接触保持时间、轨迹误差和扰动恢复。

## 当前判断

ACP 给出了一个很有价值的最小接口：策略无需显式知道接触雅可比，只需从示范学习参考位姿、虚拟目标和刚度幅值，就能把方向性柔顺交给成熟低层控制器执行。它证明“柔顺性应该成为策略动作的一部分”，而不是部署时手工固定的控制器超参数。

但当前证据仍主要来自慢速、轻物体、非夹持接触和单一 UR5e 平台。后续路线需要把这一接口与高频指尖触觉、六维柔顺、跨硬件动作表示和在线恢复结合起来，才能判断它是否能从两项强演示扩展为通用接触操作方法。

FM-VLA 又补充了另一条轴：force 不仅是高频控制反馈，也可以成为低成本的 episodic memory。它在按钮计数和重复擦拭上显著胜过视觉记忆，说明接触策略需要同时设计快反馈与慢记忆；不过固定 8-token 压缩目前只在单一双臂平台、三项小规模任务上成立。

FD-VLA 则把真实力从“部署期输入”改成“训练期教师”：预测力 token 的三任务平均成功率为 61.1%，高于直接真实力 token 的 51.1%。这说明控制所需的接触表示可以经过视觉—状态条件化与任务损失筛选，但也划出清晰边界——没有实时传感器时，模型无法可靠捕捉视觉和本体状态不可辨识的突发碰撞、隐藏卡阻或摩擦突变。

Facet-0 把这条路线再推进一步：历史 wrench 不只条件化动作生成，未来 wrench 也作为动作后果与动作块联合提出，并由部署期价值模型评价。五项亚毫米电脑装配中，完整系统平均成功率为 82%，而语义—接触对齐和价值后训练两级分别只有 16% 与 38%；这既支持预测接触后果的价值，也说明当前高成功率强依赖任务级 bounded actor，不能直接外推为无需适配的通用接触能力。

ForceMimic 则从数据入口补上另一块：ForceCapture 让人直接操作手持工具，五分钟完成一次削皮示范，避免力反馈遥操作的十三分钟级耗时和三次操作中断。它的 HybridIL 在单一西葫芦削皮任务中达到 100% 动作正确率和 85% 的连续长削皮率，但同时揭示了数据—控制一致性的硬门槛：仅把机器人力传感作为输入的 Force DP 反而只有 60%/10%，因为训练示范约 10N 的力分布与部署约 20N、局部超过 40N 的交互不匹配。

ForceFlow 进一步给出一条“力作为全局调节条件”的融合路线：十步 wrench history 通过 AdaLN 进入每个 DiT block，视觉序列只通过 cross-attention 提供空间锚定，同时把未来 wrench 作为动作生成的辅助目标。它在六项任务中达到 81.67% 平均成功率和 8.23 N 平均 Force Cost，消融又把历史与预测的角色拆开——前者主要决定可行性，后者主要改善力质量。不过 32/64 步执行、约 1.15 秒的重规划周期也说明，这仍是中频滚动策略，不能替代执行器侧的高频安全回路。

CC-VLA 则把这个缺口变成显式系统接口：1 Hz 的 pi0 输出期望位姿和前馈力，500 Hz 的 VG-ACC 根据实时力误差在线调刚度。它在擦板 base/OOD 上把相对力误差压到 5.52%/8.78%，并在六个按钮、插入、开窗条件上达到 89.2% 平均成功率。这个结果支持“慢策略给目标、快控制器保接触”的路线，但其安全性仍只在单台 UR5e 和有限位姿偏移中验证，不能当作端到端形式化保证。

## 未解决问题

- 接触力不再主导、摩擦或惯性显著时，沿合力方向放软是否仍是正确近似？
- 多点夹持会违反非夹持锥假设，如何在不丢失抓持稳定性的情况下选择柔顺子空间？
- 一秒后见平滑能提前标注接触，但突发碰撞没有未来信息；训练和执行之间的差异如何补偿？
- 能否用低成本腕力估计、视觉接触估计或电机电流替代高端六轴力矩传感器？
- 面向安全的评测怎样避免“刚性基线先损坏工具、因而无法完成统计”这种不完整比较？

## 相关页面

- [[Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control]]
- [[Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation]]
- [[FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation]]
- [[FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation]]
- [[Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation]]
- [[ForceMimic: Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation]]
- [[ForceFlow: Learning to Feel and Act via Contact-Driven Flow Matching]]
- [[2609.05832-cr-vla-force|CR-VLA-Force: Learning Control-aware Compliance VLA Model for Robust Contact-rich Robotic Manipulation]]
- [[T-Rex: Tactile-Reactive Dexterous Manipulation]]
- [[TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback]]
- [[Tactile Representation]]
- [[force-touch-robot-policy-review|机器人策略中的力觉与触觉：从信号语义到闭环控制]]
- [[Physical/Embodied Intelligence]]（domain）
