---
id: "phoenix-mwa-scaling-robotic-manipulation"
slug: "phoenix-mwa-scaling-robotic-manipulation"
title: "Phoenix（MWA™-Phoenix）: Scaling Robotic Manipulation through Visual and Interaction Representations"
type: source
material_type: "paper"
source_type: paper
source_kind: "project_page_url"
source_input: "https://openphoenix-team.github.io/Phoenix-pages/"
created: "2026-10-22"
updated: "2026-10-22"
date: "2026-10-21"
publish_date: "2026-10-21"
source_url: "https://openphoenix-team.github.io/Phoenix-pages/"
html_url: "https://openphoenix-team.github.io/Phoenix-pages/"
pdf_url: ""
project_url: "https://openphoenix-team.github.io/Phoenix-pages/"
code_url: "https://github.com/Anyverse-Dynamics/Phoenix-MWA"
translation_url: ""
arxiv_id: ""
authors:
  - "Anyverse Dynamics"
  - "OpenPhoenix Team"
  - "Yupeng Zheng"
  - "Zhongpu Xia"
  - "Chaoyue Li"
  - "Linbo Wang"
  - "Xiang Li"
  - "Zebin Xing"
  - "Qichao Zhang"
  - "Haoran Li"
  - "Dongbin Zhao"
affiliation: "无界动力（Anyverse Dynamics）；中国科学院自动化研究所；中国科学院大学；新加坡国立大学；清华大学"
related_organizations:
  - "Anyverse Dynamics（无界动力）"
  - "中国科学院自动化研究所"
  - "中国科学院大学"
  - "新加坡国立大学"
  - "清华大学"
related_companies:
  - "无界动力"
domains:
  - "Physical/Embodied Intelligence"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - "Physical/Embodied Intelligence"
tags:
  - "world-action-model"
summary: "Phoenix（MWA™-Phoenix）是无界动力开源的端侧 7B 隐空间世界动作模型基座：DINOv3 视觉骨干经 VGGT-Ω 几何与 V-JEPA 时序双教师蒸馏得到 Phoenix Encoder，再由因果语义 VAE（CS-VAE）压成紧凑因果视觉潜空间，与 Wan VAE 外观潜变量拼接后进入 VideoDiT/ActionDiT 的 MoT 联合 flow matching，同步生成未来视觉状态与动作；向上再由 Phoenix-ILA 把运动、触觉形变与力代理联合编码为交互潜变量补齐“最后一厘米”接触操作，由 Phoenix-PhysCanvas 视触觉世界模型仿真器承接 GRPO 强化学习。仅靠 RGB、不用深度真值，在 LIBERO-Plus（94.63%）、LIBERO-Pro（66.48%）、RoboCasa-GR1（82.67%）、RoboTwin 2.0 C2R（72.42%）、Bench2Dex（45.6%）与 RoboDojo 真机榜（26.11%）六项评测取得榜首或最优表现。"
keywords:
  - "world-action-model"
  - "latent-space-world-model"
  - "dual-teacher-distillation"
links:
  original: "https://openphoenix-team.github.io/Phoenix-pages/"
  project: "https://openphoenix-team.github.io/Phoenix-pages/"
  github: "https://github.com/Anyverse-Dynamics/Phoenix-MWA"
  code: "https://github.com/Anyverse-Dynamics/Phoenix-MWA"
  model: "https://huggingface.co/AnyverseDynamics"
raw_refs:
  - "https://openphoenix-team.github.io/Phoenix-pages/"
  - "https://github.com/Anyverse-Dynamics/Phoenix-MWA"
  - "https://huggingface.co/AnyverseDynamics"
related_topics:
  - "vision-language-action"
  - "robot-self-improvement"
related_syntheses: []
confidence: EXTRACTED
hero_image: "https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig1-benchmark-overview.webp"
images:
  - "https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig1-benchmark-overview.webp"
  - "https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig0-mwa-architecture.png"
  - "https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig2-encoder-csvae-mwa.webp"
  - "https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig3-phoenix-ila.webp"
  - "https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig4-physcanvas-rl.webp"
  - "https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig5-pretraining-data-pool.webp"
  - "https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig8-action-space-80d.webp"
  - "https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig9-effective-rank.webp"
image_paths: []
status: analyzed
---

# Phoenix（MWA™-Phoenix）: Scaling Robotic Manipulation through Visual and Interaction Representations

## 太长不看

无界动力开源的 MWA™-Phoenix 是目前综合榜单表现最强的开源机器人世界动作模型（WAM）基座：约 6B 联合视频—动作骨干，仅 RGB 输入、不用深度真值，在 LIBERO-Plus、LIBERO-Pro、RoboCasa-GR1、RoboTwin 2.0 C2R、Bench2Dex、RoboDojo 真机六项各有侧重的评测上同时登顶或最优。真正值得记住的不是单点分数，而是它把“几何+时序双教师蒸馏的视觉表征”“运动与触觉共同编码的交互潜变量（ILA）”“视触觉世界模型里的 GRPO 强化学习（PhysCanvas）”连成了一条从大规模预训练到真机精细操作的完整链路，且预训练数据全部来自开源数据集、代码与权重开放。对关注 WAM 预训练配方、接触操作和“世界模型内 RL”的读者，这是当前最完整的开源参照系。

## 直观理解

把 Phoenix 想成一条三级火箭。第一级 MWA™-Phoenix 是“大脑基座”：它先把眼睛练好——DINOv3 骨干分别向 VGGT-Ω 学几何、向 V-JEPA 学时序变化，再由因果语义 VAE 把视觉特征压成不偷看未来的紧凑潜空间；然后在这个潜空间里同时学习“世界接下来会变成什么样”和“我的动作应该是什么”，视频专家和动作专家通过 MoT 联合注意力互相读取信息。第二级 Phoenix-ILA 解决“最后一厘米”：轨迹看着对不等于接触有效，它把运动、触觉形变和力代理压成同一套交互潜变量，让模型直接生成“带着接触演化”的动作。第三级 Phoenix-PhysCanvas 是“脑内沙盘”：一个以动作为条件的视触觉世界模型仿真器，策略先在仿真里用 GRPO 试错改进，再上真机兑现收益。真机侧用 RTC 加分块异步执行保证连续流畅，RTX 4090 上即可实时推理。

## 核心信息

- **标题**：Phoenix: Scaling Robotic Manipulation through Visual and Interaction Representations
- **发布方**：无界动力（Anyverse Dynamics）/ OpenPhoenix Team，2026-10-21 发布并开源
- **技术报告（项目页）**：https://openphoenix-team.github.io/Phoenix-pages/
- **代码地址**：https://github.com/Anyverse-Dynamics/Phoenix-MWA
- **模型与数据**：https://huggingface.co/AnyverseDynamics
- **通讯作者**：Yupeng Zheng（zhengyupeng18@mails.ucas.ac.cn）；顾问：Qichao Zhang、Haoran Li、Dongbin Zhao
- **模型规模**：联合视频—动作骨干约 6B 可训练参数（5B 视频专家 + 1B 动作专家）；冻结的 Wan VAE（约 705M）、Phoenix Encoder（约 621M）、CS-VAE（约 72M）不计入；媒体口径为端侧 7B 完整预训练基座
- **预训练数据**：全部开源数据集，54,413 原始小时 / 约 33.8 亿帧，处理后 39,306 有效小时；机器人数据 31.09%，第一视角人类视频 63.58%，UMI 5.33%
- **六项评测**：LIBERO-Plus 94.63%、LIBERO-Pro 66.48%、RoboCasa-GR1 82.67%、RoboTwin 2.0 C2R 72.42%、Bench2Dex 45.6%、RoboDojo-RealWorld 26.11%

## 背景与问题

**动机：** 具身智能真正稀缺的不是仿真高分，而是理解物理因果、具备足够泛化性、并能将广泛操作能力转化为稳定真机执行的模型。行业主流 VLA 直接在像素或通用视觉特征上接动作头，对几何—时序结构理解薄弱；隐空间世界模型路线虽有潜力，但此前稳定规划域普遍在 4 秒以内，且“识别物体、轨迹合理、示范学会”都不保证接触有效和真机可靠。无界动力的第一性判断是：具身大脑应像人脑一样在高度抽象的隐空间直击物理因果，而非在像素层面一比一复刻世界，MWA™-Phoenix 即这一路线的完整开源基座。

**问题缺口：** 三个相互连接的缺口横在仿真与真实执行之间。其一，视觉表征层：多数表征对几何尤其是几何—时序联合理解最为缺失，模型看不清三维空间中的连续变化；其二，接触层：工具沿相似轨迹移动未必形成有效接触，抓稳、擦净、削皮需要运动与接触配合，纯运动动作目标表达不了接触演化（GPT-6 Astra 的 RoboDojo 早期评估即因真机不安全动作中止）；其三，策略优化层：示范只给名义轨迹，偏移与执行误差下缺乏“不同动作会导致什么结果”的经验，而真机试错代价高。Phoenix 体系把这三层分别交给双教师表征 + 联合世界动作建模、ILA 交互潜变量、PhysCanvas 世界模型强化学习来补。

## 论文摘要（英文原文）

> 该项目以技术报告（blog post）形式发布，无独立摘要；以下为报告 Introduction 核心段落的原文摘录。

The goal of Phoenix is to learn general robotic manipulation capabilities from large-scale experience and translate them into precise interaction skills in the physical world. To this end, we develop a unified system spanning data collection and processing, pretraining, post-training, and reinforcement learning. Phoenix-MWA is the foundation model of this system. It leverages dual-teacher distillation to combine geometric priors with temporal knowledge and a causal-semantic VAE to construct a compact visual latent space. Conditioned on observations and language instructions, the model jointly generates future visual states and actions, connecting the prediction of environmental dynamics with the learning of manipulation behavior. Moving from general manipulation to precise interaction, Phoenix-ILA focuses on the last centimeter of manipulation, combining position, force, and touch into latent interaction units. Phoenix-PhysCanvas takes a step further: an action-conditioned visual and tactile world-model simulator predicts how actions change the environment and its contact state, providing an interactive environment for policy reinforcement learning. Phoenix unifies pretraining for general capabilities, post-training for task-specific skills, and reinforcement learning for improved execution, charting a path from large-scale data to precise physical interaction.

## 论文摘要（中文翻译）

Phoenix 的目标是从大规模经验中学习通用机器人操作能力，并将其转化为物理世界中的精细交互技能。为此，团队构建了覆盖数据采集与处理、预训练、后训练和强化学习的统一系统。Phoenix-MWA 是该系统的基座模型：通过双教师蒸馏将几何先验与时序知识结合，用因果语义 VAE 构建紧凑视觉潜空间；在观测与语言指令条件下联合生成未来视觉状态与动作，把环境动态预测与操作行为学习连接起来。面向从通用操作到精细交互，Phoenix-ILA 聚焦操作的“最后一厘米”，把位置、力与触觉组合成潜在交互单元；Phoenix-PhysCanvas 更进一步：一个以动作为条件的视触觉世界模型仿真器，预测动作如何改变环境及其接触状态，为策略强化学习提供可交互环境。Phoenix 将通用能力预训练、任务技能后训练与执行改进的强化学习统一起来，画出了从大规模数据到精细物理交互的路径。

## 方法

**方法概述：** Phoenix 体系的流水线为：先用双教师蒸馏训练 Phoenix Encoder（DINOv3 ViT-L/16 + 时空 Adapter，向 VGGT-Ω 学几何、向 V-JEPA 学时序，EMA 学生权重），再用因果语义 VAE（CS-VAE）把稠密特征压缩成保留空间网格的因果潜变量；预训练阶段将 CS-VAE 潜变量与 Wan VAE 外观潜变量沿通道拼接，VideoDiT 与 ActionDiT 经 MoT 掩码联合注意力互联，以 flow matching 联合去噪未来视频与 32 步动作块；后训练阶段 Phoenix-ILA 冻结交互编解码器，把示范块离线编码为交互潜变量目标，改造动作分支生成它；Phoenix-PhysCanvas 则以动作为条件预测未来视触觉观测，与策略闭环交互并用 GRPO 更新；部署侧 RTC 加异步执行保证动作段丝滑衔接。

**核心机制：** 机制成立的关键在三层咬合。表征层：几何（物体怎么摆）与时序（观测怎么变）是操作预测最缺的两类知识，双教师蒸馏把二者同时注入同一骨干，且因果时序连接禁止编码读取未来观测，保证潜变量可用于生成建模；有效秩实验显示蒸馏后表征多样性不降反升。联合建模层：当前视觉潜变量保持干净、未来视频与动作同时加噪去噪，动作在训练的每一步都能读取世界特征，使“环境将如何变化”与“机器人应如何行动”建立显式联系，而不是各学各的。交互层：ILA 解码器不接受独立视觉输入，重建信息必须穿过交互潜变量，迫使该潜变量真正承载接触演化；PhysCanvas 让“不同动作导致什么结果”的经验在仿真中以接近零代价获取，奖励模型打分后经组内相对比较得到 GRPO 优势。

![Phoenix-MWA 整体架构](https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig0-mwa-architecture.png)

![Phoenix-MWA 双教师蒸馏、因果语义 VAE 与世界动作联合建模](https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig2-encoder-csvae-mwa.webp)

**方法拆解：**

- **Phoenix Encoder 双教师蒸馏**：以 VGGT-Ω 内的 DINOv3 初始化，VGGT-Ω 通过多层特征、深度预测与相邻帧关系提供几何监督（无需额外深度真值）；V-JEPA 教师看完整视频，学生在跨帧一致掩码区域预测教师特征获得时序监督；两个蒸馏任务交替进行并维护学生权重的 EMA。
- **CS-VAE 因果压缩**：空间 Transformer 加两级因果时序阶段把 9 帧压到 3 个时序位置且保留空间网格，首个潜变量只编码当前帧；目标函数 L = L_MSE + L_cos + β·L_KL，重建约束保留语义与空间结构，KL 把潜分布塑成适合生成建模的标准高斯。
- **联合世界—动作 flow matching**：Wan VAE 潜变量（外观与空间结构）与 CS-VAE 潜变量（几何与语义）通道拼接进 VideoDiT，动作序列进 ActionDiT，逐层 MoT 掩码联合注意力规定信息流向；T5 语言嵌入、投影后的机器人状态与可学习的具身软提示经交叉注意力条件化动作分支；训练样本配对同一区间的 32 步动作与 9 帧画面，损失 L = 0.5·L_Wan-flow + 0.5·L_CS-flow + L_action-flow，视觉编解码器全部冻结，仅更新两个专家、状态投影与具身提示（共约 6B）。
- **Phoenix-ILA 交互潜变量**：交互编码器在多视角视觉条件下联合编码同步的运动与触觉序列，时间条件化解码器在查询时刻重建动作、三维触觉形变场与力代理；冻结编解码器后把示范块编码为归一化潜目标，改造 MWA 动作分支的输入输出投影与时间位置编码，用条件 flow matching 从高斯噪声生成交互潜变量；推理无需未来触觉测量，解码回控制时栅上的关节目标序列。
- **Phoenix-PhysCanvas 世界模型 RL**：时间对齐的多视角 RGB、触觉图像与触觉位移组成统一空间画布，机器人运动提供相机对齐的几何条件，基于预训练视频模型以条件 flow matching 预测未来多模态观测；策略与仿真器从真实初始观测闭环交互，同初始条件采样多条 rollout，奖励模型评价任务完成度，组内比较得到相对优势做 GRPO 更新，更新后回真机验证。
- **数据与接口工程**：预训练全部使用开源数据（机器人 31.09%、Ego 63.58%、UMI 5.33%），统一转 LeRobot V3；质量过滤结合视觉与时序相似度去重、相机运动补偿区分 Ego 视频的局部活动与视角变化；Ego 数据做脚本级语言标注并按原始 episode 切分防泄漏，机器人数据做工作空间与末端执行器双重坐标对齐及指令改写增广；统一 80 维状态—动作空间覆盖双臂、灵巧手、躯干、升降、头部与移动底盘槽位，缺失维度零填充并以逐时间步逐维度掩码排除出损失。

![Phoenix-ILA 交互潜变量学习](https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig3-phoenix-ila.webp)

![Phoenix-PhysCanvas 强化学习后训练框架](https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig4-physcanvas-rl.webp)

![Phoenix-MWA 预训练数据池构成](https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig5-pretraining-data-pool.webp)

![统一 80 维状态与动作空间布局](https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig8-action-space-80d.webp)

**关键要点：**

- 不做任何测试数据复刻、不使用深度传感器、不依赖 Agent 框架，六个不同侧重的榜单同时登顶，说明收益来自架构与训练方法本身的泛化性，而非单点调优。
- 预训练的价值可量化：LIBERO-Plus 无预训练 88.16% → 预训练 94.63%（+6.47pp），且七个扰动类别全面上涨；未来视频预测相对 FastWAM 在 LIBERO-Plus 上 PSNR +2.56dB、LPIPS -36.84%，在 RoboTwin 2.0 C2R 上 +9.79dB、-58.97%。
- 80 维统一动作接口加掩码设计，使 12 种机械臂与灵巧手组合、26 个任务—本体设置的跨本体联合训练与迁移成为工程上可复用的标准件。

## 结果

**核心结果：**

- LIBERO-Plus 总体成功率 94.63% 登顶（七类扰动下最强对照 Qwen-RobotManip-Context 91.40%、π0.5 85.70%），机器人、语言、光照、噪声、布局五类单项最佳。
- LIBERO-Pro 66.48% 榜首（最强对照 Continuous Reasoning 64.00%、QuoVLA 62.31%），其中位置泛化 42.55% 明显高于其他方法。
- RoboCasa GR1 Tabletop 82.67% 领跑，较前代 MWA™-WALA 的 75.17% 提升 7.50pp；RoboTwin 2.0 C2R 72.42%（最强对照 InternW0-Δ 71.90%）。
- Bench2Dex 跨 12 种本体组合平均 45.6%，领先最强对照 17.3 个百分点，等变、不变、组合三种评测条件全部最优；RoboDojo 真机榜 26.11%（OpenWAM-α 24.40%、π0.5 12.80%）。
- 接触与精细操作真机增益：ILA 使削黄瓜 20%→40%、擦盘子 75%→90%，力代理误差分别降 34.05%、14.81%；PhysCanvas GRPO 使试管插拔 58.33%→75.00%、积木操作 80.00%→86.67%，三种环境条件全部改善。

![Phoenix-MWA 六项榜单总览](https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig1-benchmark-overview.webp)

**结果表：**

| 评测 | 考察重点 | Phoenix-MWA | 最强对照 | 对照分数 |
| --- | --- | --- | --- | --- |
| LIBERO-Plus | 七类扰动鲁棒性 | 94.63% | Qwen-RobotManip-Context | 91.40% |
| LIBERO-Pro | 跨任务泛化 | 66.48% | Continuous Reasoning | 64.00% |
| RoboCasa-GR1 | 24 项桌面长时序 | 82.67% | CF-WAM | 82.50% |
| RoboTwin 2.0 C2R | 随机化双臂协同 | 72.42% | InternW0-Δ | 71.90% |
| Bench2Dex | 12 本体跨任务迁移 | 45.6% | GR00T N1.5 | 28.3% |
| RoboDojo-RealWorld | 三本体真机执行 | 26.11% | OpenWAM-α | 24.40% |

## 洞察

**核心 insight：**

- 这份报告最有信息量的不是“又一个榜首”，而是预训练消融把 WAM 的价值链条拆开了：无预训练的 Phoenix-MWA 已凭几何+语义表征超过 FastWAM 的未来预测质量，预训练再叠加一层大幅增益——表征设计与大规模经验是两个可分离、可独立改进的收益来源。
- 双教师蒸馏后有效秩不降反升（预训练验证集 CLS/PatchMean +5.81%/+7.86%），反驳了“蒸馏必然窄化表征”的直觉：选对教师组合，几何先验与语义丰富度可以兼得。
- ILA 与 PhysCanvas 指向同一个判断：动作空间的表示形式本身就是改进杠杆。把接触写进动作目标（交互潜变量）和把试错搬进世界模型（GRPO 仿真）都不动基座，只改“学什么目标、在哪优化”，就在真机上换来两位数或近两位数的成功率提升。

**和已有方法的关系：**

- 相对 Fast-WAM/OpenWAM 等 WAM 路线，Phoenix 的差异在视觉前端（双教师蒸馏 + 因果压缩而非直接用视频 VAE）和完整的 ILA/PhysCanvas 后段；Bench2Dex 上相对 π0.5 的 17.3pp 差距说明该前端在跨本体迁移上收益显著。
- 相对 RTC（Physical Intelligence）只做推理调度，Phoenix 把 RTC 与异步执行纳入系统但不止于此；相对纯 VLA（π0.5、GR00T 系列），WAM 路线在随机化与真机设置下优势更明显（RoboTwin C2R、RoboDojo）。
- 延续了 MWA™（2026-06）“长时序双向物理因果链”隐空间世界模型路线，此次以开源基座 + 完整报告的形式把前代 WALA 的 RoboCasa 成绩从 75.17% 推进到 82.67%。

![双教师蒸馏后有效秩提升](https://followhub.tenstep.top/papers/phoenix-mwa-scaling-robotic-manipulation/fig9-effective-rank.webp)

**可借鉴点：**

- 数据工程可复用性极高：LeRobot V3 统一格式、按 episode 防泄漏切分、Ego/UMI 脚本级标注、双重坐标对齐、80 维统一接口加掩码，全部承诺开源，是搭建多源预训练池的直接参照。
- “冻结编解码器 + 离线编码示范为潜目标 + 改造动作分支”的 ILA 适配模式，是给任意 WAM/VLA 基座外挂新模态（力、触觉、声音）的低成本范式。
- 世界模型内 GRPO + 奖励模型的闭环，为精细操作提供了不消耗真机的后训练通道，试管任务 +16.67pp 的迁移幅度说明仿真策略改进可以较完整地兑现到真实执行。

## 风险与判断

**局限：**

- RoboDojo 真机榜绝对值仍低（26.11%），精细接触任务成功率上限 40%（削黄瓜），说明“最后一厘米”远未解决，当前更适合作为研究基座而非即插即用的产品方案。
- 评测均为自行后训练配置下的榜单对比，部分对照（如 Bench2Dex 的 ACT/DP）未必是最优调参状态；报告无第三方复现，且未给出各任务的方差与失败模式细表（PhysCanvas 实验标准差达 16.33pp，跨条件稳定性一般）。
- 数据分布重度偏向第一视角人类视频（63.58%），机器人数据仅 31.09%，对低数据量本体的适配成本未披露；编码器、数据、RTC 等分支代码标注 coming soon，当前只放出预训练主线。

**适用场景：**

- 需要开源 WAM 预训练配方与统一动作接口的研究团队：做世界动作模型、跨本体迁移、未来视频预测基线时，这是当前数据与代码开放度最高的参照。
- 接触密集与精细操作方向：ILA 的交互潜变量与 PhysCanvas 的世界模型 RL 是可直接复用的后训练组件思路。
- 商业侧已验证长时程服务场景（咖啡店饮品递送、桌面清理等），适合关注真实场景连续作业落地的团队评估。

**最终判断：**

- 值得精读并跟踪。这是 2026 年 WAM 路线最完整的开源工作之一：六项榜单同时领先、表征—联合建模—接触—RL 四层都有可量化消融，且预训练数据全部开源、权重代码开放。短期看它是 WAM 预训练与后训练的新基线；长期看其“表示即杠杆”（交互潜变量、统一动作空间）和世界模型内 RL 的范式价值大于单个分数。需要警惕的是真机精细操作成功率仍低、部分工程分支未开源，复现完整链路成本不低。

## 结果速览表

| 维度 | 配置 | 数值 |
| --- | --- | --- |
| 联合骨干规模 | 视频专家 5B + 动作专家 1B（冻结编解码器约 1.4B 不计） | 约 6B 可训练参数 |
| 预训练数据 | 全开源：机器人 + Ego + UMI | 54,413 原始小时 → 39,306 有效小时，约 33.8 亿帧 |
| LIBERO-Plus | 七类扰动 | 94.63%（无预训练 88.16%） |
| LIBERO-Pro | 四类任务变化 | 66.48% |
| RoboCasa-GR1 | 24 项桌面任务 | 82.67%（前代 WALA 75.17%） |
| RoboTwin 2.0 C2R | 50 项双臂随机化 | 72.42% |
| Bench2Dex | 12 本体 × 26 任务 | 45.6%（领先最强对照 17.3pp） |
| RoboDojo-RealWorld | 3 本体 18 项真机 | 26.11% |
| ILA 接触任务 | 削黄瓜 / 擦盘子 | 20%→40% / 75%→90%，力代理误差 -34.05% / -14.81% |
| PhysCanvas GRPO | 试管 / 积木真机 | 58.33%→75.00% / 80.00%→86.67% |
| 未来视频预测 | 对比 FastWAM | LIBERO-Plus PSNR +2.56dB；RoboTwin C2R PSNR +9.79dB |

## 相关主题

- [[Vision-Language-Action]]
- [[Robot Self-Improvement]]

## 相关页面

- 前代路线：MWA™ 隐空间世界模型（2026-06 发布）与 MWA™-WALA（RoboCasa-GR1 75.17%）
- 对照基线：[[2609.07398-openwam-an-open-modular-exploration-towards-systematic-world-action-model-pretraining|OpenWAM]]、[[2606.09811-aha-wam|AHA-WAM]]、[[2610.10528-long-wam-scaling-the-context-of-world-action-models|Long-WAM]]
