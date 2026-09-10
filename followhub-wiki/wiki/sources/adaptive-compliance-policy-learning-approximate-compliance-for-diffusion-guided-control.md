---
id: "adaptive-compliance-policy-learning-approximate-compliance-for-diffusion-guided-control"
slug: "adaptive-compliance-policy-learning-approximate-compliance-for-diffusion-guided-control"
title: "Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control"
type: source
material_type: paper
source_type: paper
source_kind: "arxiv_abs_url"
source_input: "https://arxiv.org/abs/2410.09309"
source_url: "https://arxiv.org/abs/2410.09309"
html_url: "https://arxiv.org/html/2410.09309v2"
pdf_url: "https://arxiv.org/pdf/2410.09309v2"
code_url: "https://adaptive-compliance.github.io/"
translation_url: "https://hjfy.top/arxiv/2410.09309"
created: "2026-08-28"
updated: "2026-08-28"
date: "2024-10-12"
publish_date: "2024-10-12"
arxiv_id: "2410.09309"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - Physical/Embodied Intelligence
domains:
  - Physical/Embodied Intelligence
authors:
  - Yifan Hou
  - Zeyi Liu
  - Cheng Chi
  - Eric Cousineau
  - Naveen Kuppuswamy
  - Siyuan Feng
  - Benjamin Burchfiel
  - Shuran Song
affiliation: "Stanford University; Toyota Research Institute"
related_organizations:
  - Stanford University
  - Toyota Research Institute
related_companies:
  - Toyota Research Institute
summary: "从单条动觉示范构造近似各向异性柔顺标签，让扩散策略随视觉与力反馈预测参考位姿、虚拟目标和刚度。"
links:
  original: "https://arxiv.org/abs/2410.09309"
  arxiv: "https://arxiv.org/abs/2410.09309"
  html: "https://arxiv.org/html/2410.09309v2"
  pdf: "https://arxiv.org/pdf/2410.09309v2"
  project: "https://adaptive-compliance.github.io/"
  github: ""
  hjfy: "https://hjfy.top/arxiv/2410.09309"
  doi: ""
raw_refs:
  - "https://arxiv.org/abs/2410.09309"
  - "https://arxiv.org/html/2410.09309v2"
  - "https://arxiv.org/pdf/2410.09309v2"
tags:
  - contact-rich-manipulation
keywords:
  - adaptive compliance
  - contact-rich manipulation
  - diffusion policy
  - force feedback
images:
  - https://arxiv.org/html/2410.09309v2/complance-teaser-v5.png
  - https://arxiv.org/html/2410.09309v2/ACP_method_1.svg
  - https://arxiv.org/html/2410.09309v2/ACP_Data_collection_setup.svg
  - https://arxiv.org/html/2410.09309v2/pinching.svg
  - https://arxiv.org/html/2410.09309v2/figures/flipup_settings_v2.jpg
  - https://arxiv.org/html/2410.09309v2/Flipup_curves_v2.png
  - https://arxiv.org/html/2410.09309v2/wiping_curves.png
  - https://arxiv.org/html/2410.09309v2/wiping_motion.png
hero_image: "https://arxiv.org/html/2410.09309v2/complance-teaser-v5.png"
image_paths: []
related_topics:
  - contact-rich-manipulation
related_syntheses:
  - force-touch-robot-policy-review
confidence: EXTRACTED
status: analyzed
---

# Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control

## 太长不看

ACP 把柔顺性从低层控制器里的固定超参数提升为策略需要预测的动作变量：它从单条人体示范近似标注空间与时间变化的刚度方向和幅值，再由扩散策略结合视觉、位姿和力反馈生成。真实机器人翻转与花瓶擦拭分别达到 96% 和 93.75% 总成功率，显著超过固定柔顺和刚性位置策略。最值得记住的是它把接触约束转成可学习标签，但结论依赖慢速、轻物体、非夹持接触等明确假设。

## 直观理解

把机器人想成拿着海绵擦花瓶的人：手既不能像铁棍一样硬，否则位置误差会把工具压坏；也不能各方向都软，否则摩擦会把手带偏。ACP 让策略同时给出“想走到哪里”的参考位姿和“弹簧实际拉向哪里”的虚拟目标，两者的方向差告诉控制器哪一维应该软，再用一个标量决定软到什么程度；于是低层控制器可以在接触变化时快速顺着约束让步，同时在其他方向继续精确跟踪。

![主要图](https://arxiv.org/html/2410.09309v2/complance-teaser-v5.png)

*图 1：翻转与花瓶擦拭对柔顺性的空间、时间和任务依赖。*

## 核心信息

- **作者**：Yifan Hou、Zeyi Liu、Cheng Chi、Eric Cousineau、Naveen Kuppuswamy、Siyuan Feng、Benjamin Burchfiel、Shuran Song
- **作者单位**：Stanford University、Toyota Research Institute
- **来源类型**：arxiv_abs_url
- **输入来源**：https://arxiv.org/abs/2410.09309
- **原文链接**：https://arxiv.org/abs/2410.09309
- **HTML 正文**：https://arxiv.org/html/2410.09309v2
- **PDF 地址**：https://arxiv.org/pdf/2410.09309v2
- **代码地址**：https://adaptive-compliance.github.io/
- **中英翻译地址**：https://hjfy.top/arxiv/2410.09309
- **发布日期**：2024-10-12
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** 接触密集操作同时要求位置轨迹与接触力正确。过高刚度可以精确追踪，却会把视觉或标定误差转成巨大内力，造成物体滑动、工具损坏或安全停机；各方向统一降低刚度虽然更安全，却会让摩擦把末端带离目标。更困难的是，所需柔顺性会随接触阶段、受力方向和任务而变化：翻转物体时应沿推力方向软、沿弧线切向保持硬，擦拭花瓶时双臂还要根据三维曲面和接触法向持续调整。

**问题缺口：** 已有柔顺控制往往依赖已知接触几何、摩擦和动力学模型，或要求同一任务的多次重复轨迹来估计刚度；这些条件难以覆盖视觉场景变化和意外扰动。单条人体示范也不足以唯一恢复完整质量、阻尼与刚度，因为人的手改变了系统的有效动力学，某些时段甚至没有足够的力—运动变化。论文因此不追求还原人体真实柔顺性，而是询问：能否在温和物理假设下，从每条不同的示范构造一个足以避免约束冲突、又保留轨迹精度的近似柔顺标签，并让策略根据视觉和力反馈在线泛化？

## 论文摘要（英文原文）

Compliance plays a crucial role in manipulation, as it balances between the concurrent control of position and force under uncertainties. Yet compliance is often overlooked by today’s visuomotor policies that solely focus on position control. This paper introduces Adaptive Compliance Policy (ACP), a novel framework that learns to dynamically adjust system compliance both spatially and temporally for given manipulation tasks from human demonstrations, improving upon previous approaches that rely on pre-selected compliance parameters or assume uniform constant stiffness. However, computing full compliance parameters from human demonstrations is an ill-defined problem. Instead, we estimate an approximate compliance profile with two useful properties: avoiding large contact forces and encouraging accurate tracking. Our approach enables robots to handle complex contact-rich manipulation tasks and achieves over 50% performance improvement compared to state-of-the-art visuomotor policy methods. For result videos, see https://adaptive-compliance.github.io/.

## 论文摘要（中文翻译）

柔顺性在机器人操作中至关重要，因为它需要在不确定条件下同时平衡位置与力控制。然而，当代视觉运动策略通常只关注位置控制，柔顺性往往被忽略。本文提出自适应柔顺策略 ACP：一个从人类示范学习、能够针对操作任务在空间和时间上动态调整系统柔顺性的框架，相比依赖预选柔顺参数或假设各方向恒定均匀刚度的方法更进一步。由于从人类示范完整恢复柔顺参数本身是不适定问题，作者改为估计一种近似柔顺轮廓，使其同时具备避免巨大接触力和鼓励准确轨迹跟踪两项性质。该方法使机器人能够处理复杂的接触密集操作，并相对先进视觉运动策略获得超过 50% 的性能提升。

## 方法

**方法概述：** ACP 的完整流程是“柔顺示教采集—近似刚度标注—多模态扩散策略—高频低层执行”。操作者在低刚度、低阻尼、低虚拟质量的导纳控制下直接牵引 UR5e，系统同步记录 RGB、末端位姿与六轴力矩；离线阶段从力方向构造各向异性刚度矩阵和虚拟目标位姿；训练阶段让扩散策略根据近期视觉、位姿和力历史联合预测参考位姿、虚拟目标与低刚度幅值；推理时再重建完整刚度矩阵交给高频导纳控制器。

**核心机制：** 核心近似是沿反馈力方向使用低刚度、在所有正交方向使用高刚度。反馈力给出接触法向锥内部的一条方向；在“接触力主导、所有接触力非零、接触不形成夹持锥”的假设下，释放该方向的速度约束总能找到满足接触不穿透条件的运动，而其余方向保持高刚度有助于精确追踪。作者用以归一化力方向为第一基向量的正交基旋转对角刚度矩阵，并让低刚度随力幅值从最大值连续降到最小值；参考位姿与虚拟目标的差编码低刚度方向，低刚度标量编码幅值，从而把显式力目标转成跨机器人更容易执行的位置式表示。

**方法拆解：** - 示教采集：UR5e 在低刚度、低阻尼和低虚拟质量的导纳控制下接受动觉示教，GoPro、末端位姿与 ATI mini-45 六轴力矩同步记录，操作者通过直接触觉反馈自然展示不同接触阶段。
- 柔顺方向标注：对每个时刻取滤波后的反馈力方向为低刚度轴，其余正交轴设为经验高刚度；当力很小时所有方向使用高刚度，避免自由空间追踪变软。
- 柔顺幅值标注：低刚度在力幅小于阈值时保持最大值，随后随力幅线性下降，超过上阈值后固定为最小值，以缓和噪声方向估计并在强接触时增加让步。
- 动作表示：每个机械臂每步输出 19 维，包括 9 维参考位姿、9 维虚拟目标位姿和 1 个低刚度标量；两位姿之差决定推理时的柔顺方向。
- 多模态扩散策略：近期两帧 RGB 经 CLIP 预训练 ViT-B/16 编码，末端位姿取三帧历史；力矩历史用五层因果卷积或六通道频谱图加 CoordConv/ResNet-18 编码，再以 Transformer 自注意力融合视觉与力特征并条件化扩散动作头。
- 训练与执行：整段力矩先用一秒移动平均平滑，再计算刚度与虚拟目标，使标签带有即将接触的后见信息；推理时从两目标方向重建刚度矩阵，把参考位姿、虚拟目标和刚度发送给高频导纳控制器。

**关键要点：** - ACP 学习的是“满足任务所需的近似柔顺轮廓”，不是从单次示范恢复人体真实阻抗；这个目标重定义使不适定估计问题变成可规模化监督学习问题。
- 参考位姿与虚拟目标位姿的差把力方向编码进位置动作空间，让没有力矩传感器但支持阻抗控制的机器人也有机会执行同一种策略输出。
- FFT 力编码只在擦拭这种高频接触变化更复杂的任务上显示明显优势；翻转任务中因果卷积版本 95% 与 FFT 版本 96% 基本持平。

![方法图](https://arxiv.org/html/2410.09309v2/ACP_method_1.svg)

*图 2：普通视觉运动策略、固定柔顺策略与 ACP 的输出和控制接口对比。*

![方法图](https://arxiv.org/html/2410.09309v2/ACP_Data_collection_setup.svg)

*图 3：带直接触觉反馈的低刚度动觉示教装置。*

![方法图](https://arxiv.org/html/2410.09309v2/pinching.svg)

*图 4：非夹持与夹持接触示例，对应理论假设 III 的适用边界。*

## 结果

**核心结果：** - 物体翻转共收集 230 条示范、覆盖 15 个物体，每种策略进行 100 次测试；ACP 总成功率 96%，ACP 无 FFT 为 95%，固定均匀柔顺策略为 23%，刚性位置策略为 14%。
- 翻转的五类测试覆盖训练物体、未见物体、先推后翻、不同夹具位姿和不稳定夹具；ACP 分别达到 90%、95%、95%、100% 和 100%，说明视觉与力反馈能够对几何变化和夹具扰动在线调节柔顺方向。
- 花瓶擦拭收集 200 条双臂示范，在 16 次测试中 ACP 总成功率 93.75%，无 FFT 版本 81.25%，固定柔顺策略 43.75%；刚性策略因多次折断擦拭工具而未进入量化表。
- 擦拭任务中 ACP 在小标记、接触前扰动和接触后扰动场景均为 100%，大标记为 80%；固定柔顺策略分别只有 60%、25%、100% 和 20%，主要受摩擦导致的轨迹偏离影响。
- FFT 相比因果卷积主要改善擦拭：总成功率从 81.25% 提高到 93.75%，作者观察到频谱编码与 RGB 交互后更善于选择下一次擦拭位置，但论文没有给出更细的频率消融。

**结果表：** | 任务 / 策略 | ACP | ACP 无 FFT | 固定柔顺策略 | 刚性位置策略 |
| --- | ---: | ---: | ---: | ---: |
| 物体翻转总成功率 | **96%** | 95% | 23% | 14% |
| 花瓶擦拭总成功率 | **93.75%** | 81.25% | 43.75% | 未报告，频繁损坏工具 |
| 翻转：未见物体 | 95% | 100% | 15% | 0% |
| 翻转：不稳定夹具 | 100% | 90% | 0% | 10% |

![结果图](https://arxiv.org/html/2410.09309v2/figures/flipup_settings_v2.jpg)

*图 5：翻转任务覆盖未见物体、配置变化和不稳定夹具等测试场景。*

![结果图](https://arxiv.org/html/2410.09309v2/Flipup_curves_v2.png)

*图 6：翻转过程中 ACP 预测的世界坐标刚度、参考位姿、虚拟目标和柔顺方向。*

![结果图](https://arxiv.org/html/2410.09309v2/wiping_curves.png)

*图 7：擦拭臂的刚度与目标轨迹；低刚度方向大体跟随曲面接触法向。*

![结果图](https://arxiv.org/html/2410.09309v2/wiping_motion.png)

*图 8：ACP、刚性策略和固定柔顺策略的擦拭结果对比。*

## 洞察

**核心 insight：** - 最重要的贡献是把柔顺性纳入策略动作，而不是把固定柔顺留给低层控制器。视觉运动策略过去只学“轨迹在哪里”，ACP 进一步学“轨迹偏差在哪个方向可以被接触力推开”。
- 论文没有求解完整接触几何，而是用力方向作为接触约束锥的可观测代理；这是一个典型的“只恢复决策所需结构、不恢复全部物理参数”的建模选择。
- 一秒移动平均不仅去噪，还把未来接触信息泄露进动作标签，使策略能在真正接触前开始降低刚度。它对平滑接触有利，但也意味着监督标签是离线后见构造，在线突发接触仍只能依赖反馈修正。
- 翻转中 FFT 没有优势、擦拭中明显有优势，说明力信号编码器应匹配任务的接触频谱；不是所有接触密集任务都需要高成本频域表示。

**和已有方法的关系：** - 相对普通 Diffusion Policy，ACP 保留视觉条件的扩散动作生成与滚动时域执行，但把输出从单一位姿扩展为参考位姿、虚拟目标和刚度，使低层控制不再只有固定参数。
- 相对固定均匀柔顺策略，ACP 只沿当前接触力方向让步，在正交方向保持高刚度，因此同时避免过大内力和摩擦导致的轨迹漂移。
- 相对解析柔顺优化与重复示范估计，ACP 不需要测试时显式计算接触雅可比，也不要求每个场景重复同一轨迹；代价是理论保证只在简化接触假设内成立。

**可借鉴点：** - 在学习控制中，可把难以辨识的完整物理参数改写为满足安全与跟踪性质的近似标签，并用已知定理约束标签方向。
- 用“参考目标 + 虚拟目标”编码力或柔顺方向，是一种能复用现有位置接口和低层阻抗控制器的工程抽象。
- 对接触标签使用适度后见平滑可以提前标注接触过渡，但部署前应检查平滑窗口带来的延迟、信息泄露与意外碰撞响应边界。

## 风险与判断

**局限：** - 理论和标签构造依赖三项关键假设：接触力相对惯性、摩擦和重力占主导，所有已建立接触的法向力非零，并且接触法向锥不形成夹持；夹持、快速运动、重物或强摩擦场景可能违反这些条件。
- 实验只在 UR5e 上验证三维平移柔顺，虽然公式可扩展到六维，但转动柔顺、不同机器人控制接口和跨硬件迁移没有实证。
- 策略仍依赖昂贵的 ATI mini-45 力矩传感器和高频信号流；“无力传感器机器人可执行虚拟目标”只说明动作表示兼容，不等于该机器人能够在没有力反馈输入时运行同一策略。
- 比较只包含同数据同训练轮数的 Diffusion Policy 变体，未与基于显式接触模型、混合力位控制或强化学习得到的强柔顺控制器进行统一协议对比。
- 擦拭评测总共只有 16 次且刚性策略因损坏工具被排除出结果表，样本规模与不完整基线使 93.75% 的统计稳定性有限。

**适用场景：** - 适合速度较低、物体较轻、接触法向可由六轴力矩稳定反映的推、擦、沿面跟随、装配预接触和其他非夹持接触操作。
- 适合已有高频导纳或阻抗控制器、能够采集动觉示教与同步视觉—力数据，并希望让策略跨物体几何或夹具扰动调整柔顺性的研究平台。
- 不应直接用于高速冲击、重物搬运、多点夹持、强摩擦主导或缺少力反馈的安全关键部署，除非重新验证假设并加入保护控制。

**最终判断：** - ACP 是接触密集模仿学习中值得保留的一条关键路线：它以很小的动作表示扩展，把固定控制器参数变成随状态预测的策略变量，并在两项真实任务中给出大幅、可解释的增益。
- 其 96% 和 93.75% 结果不能简单外推为通用接触操作已解决，因为任务数、硬件、运动速度与接触类型都受限，擦拭样本尤其小。
- 后续最值得验证的是六维柔顺、跨机器人迁移、夹持与摩擦主导任务、无需高端力传感器的状态估计，以及和现代触觉 VLA 或在线强化学习结合后的恢复能力。

## 结果速览表

| 任务 / 策略 | ACP | ACP 无 FFT | 固定柔顺策略 | 刚性位置策略 |
| --- | ---: | ---: | ---: | ---: |
| 物体翻转总成功率 | **96%** | 95% | 23% | 14% |
| 花瓶擦拭总成功率 | **93.75%** | 81.25% | 43.75% | 未报告，频繁损坏工具 |
| 翻转：未见物体 | 95% | 100% | 15% | 0% |
| 翻转：不稳定夹具 | 100% | 90% | 0% | 10% |

## 相关主题

- [[Contact-Rich Manipulation and Adaptive Compliance]]：ACP 代表“从示范学习任务相关柔顺性，再由策略与低层控制器分工执行”的路线。

## 相关页面

- [[T-Rex: Tactile-Reactive Dexterous Manipulation]]
- [[TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback]]
- [[Tactile Representation]]
<!-- confidence: INFERRED -->
