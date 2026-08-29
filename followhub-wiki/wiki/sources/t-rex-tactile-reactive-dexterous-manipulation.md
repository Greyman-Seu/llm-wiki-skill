---
id: "t-rex-tactile-reactive-dexterous-manipulation"
slug: "t-rex-tactile-reactive-dexterous-manipulation"
title: "T-Rex: Tactile-Reactive Dexterous Manipulation"
type: source
material_type: paper
source_type: paper
source_kind: "arxiv_html_url"
source_input: "https://arxiv.org/html/2606.17055v2"
source_url: "https://arxiv.org/abs/2606.17055v2"
html_url: "https://arxiv.org/html/2606.17055v2"
pdf_url: "https://arxiv.org/pdf/2606.17055v2"
code_url: "https://tactile-rex.github.io/"
translation_url: "https://hjfy.top/arxiv/2606.17055"
created: "2026-08-20"
updated: "2026-08-29"
date: "2026-06-15"
publish_date: "2026-06-15"
arxiv_id: "2606.17055"
domain: "Physical/Embodied Intelligence"
primary_domain_slug: "Physical/Embodied Intelligence"
domain_slugs:
  - "Physical/Embodied Intelligence"
domains:
  - "Physical/Embodied Intelligence"
authors:
  - "Dantong Niu"
  - "Zhuoyang Liu"
  - "Zekai Wang"
  - "Boning Shao"
  - "Zhao-Heng Yin"
  - "Anirudh Pai"
  - "Yuvan Sharma"
  - "Stefano Saravalle"
  - "Ruijie Zheng"
  - "Jing Wang"
  - "Ryan Punamiya"
  - "Mengda Xu"
  - "Yuqi Xie"
  - "Yunfan Jiang"
  - "Letian Fu"
  - "Konstantinos Kallidromitis"
  - "Matteo Gioia"
  - "Junyi Zhang"
  - "Jiaxin Ge"
  - "Haiwen Feng"
  - "Fabio Galasso"
  - "Wei Zhan"
  - "David M. Chan"
  - "Yutong Bai"
  - "Roei Herzig"
  - "Jiahui Lei"
  - "Li Fei-Fei"
  - "Ken Goldberg"
  - "Jitendra Malik"
  - "Pieter Abbeel"
  - "Yuke Zhu"
  - "Danfei Xu"
  - "Linxi Fan"
  - "Trevor Darrell"
affiliation: "UC Berkeley; NVIDIA; Stanford University; Panasonic; Sapienza University of Rome; ItalAI"
related_organizations:
  - "UC Berkeley"
  - "NVIDIA"
  - "Stanford University"
  - "Panasonic"
  - "Sapienza University of Rome"
  - "ItalAI"
related_companies:
  - "NVIDIA"
  - "Panasonic"
  - "ItalAI"
tags:
  - "tactile-representation"
keywords:
  - "tactile-reactive manipulation"
  - "dexterous manipulation"
  - "vision-language-action"
  - "asynchronous control"
summary: "以人类视频预训练、触觉同步机器人中训练和异步快慢专家，把高频触觉闭环接入双手灵巧 VLA。"
links:
  original: "https://arxiv.org/abs/2606.17055v2"
  arxiv: "https://arxiv.org/abs/2606.17055v2"
  html: "https://arxiv.org/html/2606.17055v2"
  pdf: "https://arxiv.org/pdf/2606.17055v2"
  project: "https://tactile-rex.github.io/"
  github: ""
  hjfy: "https://hjfy.top/arxiv/2606.17055"
  doi: ""
raw_refs:
  - "https://arxiv.org/abs/2606.17055v2"
  - "https://arxiv.org/html/2606.17055v2"
  - "https://arxiv.org/pdf/2606.17055v2"
images:
  - "https://arxiv.org/html/2606.17055v2/teaser_v6_0609.png"
  - "https://arxiv.org/html/2606.17055v2/model_v2_0524.png"
  - "https://arxiv.org/html/2606.17055v2/data_efficiency_v2_0529.png"
hero_image: "https://arxiv.org/html/2606.17055v2/teaser_v6_0609.png"
image_paths: []
related_topics:
  - "tactile-representation"
  - "vision-language-action"
related_syntheses:
  - "tactile-force-into-pretrained-robot-policies"
confidence: EXTRACTED
status: analyzed
---

# T-Rex: Tactile-Reactive Dexterous Manipulation

## 太长不看

T-Rex 的关键贡献不是把触觉当作又一种静态输入，而是让现有 VLA 的低频视觉动作规划与高频触觉修正协同工作。它用 22889 小时人类第一视角视频预训练、100 小时触觉同步机器人数据中训练和约 100 条任务示范后训练，在 12 个真实双手灵巧任务上达到 65% 平均成功率，相比最强基线 EgoScale 的 35% 高出 30 个百分点。结果很强，但目前仍是单一硬件平台上的研究级验证。

## 直观理解

可以把 T-Rex 想成一位先看清全局、再靠手感随时纠偏的操作者：慢速动作专家约 5 Hz 生成一段大方向正确的动作，快速触觉专家约 20 Hz 复用已缓存的视觉语言上下文，只根据最新十指触觉把尚未完全去噪的动作继续修细；因此视觉规划不必每次重算，触觉却能在滑移、挤压、插入和摩擦发生时及时闭环响应。

![主要图](https://arxiv.org/html/2606.17055v2/teaser_v6_0609.png)

*主要图*

## 核心信息

- **作者**：Dantong Niu、Zhuoyang Liu、Zekai Wang、Boning Shao、Zhao-Heng Yin、Anirudh Pai、Yuvan Sharma、Stefano Saravalle、Ruijie Zheng、Jing Wang、Ryan Punamiya、Mengda Xu、Yuqi Xie、Yunfan Jiang、Letian Fu、Konstantinos Kallidromitis、Matteo Gioia、Junyi Zhang、Jiaxin Ge、Haiwen Feng、Fabio Galasso、Wei Zhan、David M. Chan、Yutong Bai、Roei Herzig、Jiahui Lei、Li Fei-Fei、Ken Goldberg、Jitendra Malik、Pieter Abbeel、Yuke Zhu、Danfei Xu、Linxi Fan、Trevor Darrell
- **作者单位**：UC Berkeley、NVIDIA、Stanford University、Panasonic、Sapienza University of Rome、ItalAI
- **来源类型**：arxiv_html_url
- **输入来源**：https://arxiv.org/html/2606.17055v2
- **原文链接**：https://arxiv.org/abs/2606.17055v2
- **HTML 正文**：https://arxiv.org/html/2606.17055v2
- **PDF 地址**：https://arxiv.org/pdf/2606.17055v2
- **代码地址**：https://tactile-rex.github.io/
- **中英翻译地址**：https://hjfy.top/arxiv/2606.17055
- **发布日期**：2026-06-15
- **主题域**：Physical/Embodied Intelligence

## 背景与问题

**动机：** 视觉适合判断“物体在哪里、任务做到哪一步”，却不擅长判断手指接触后正在发生什么。插钥匙时的轻微卡阻、抽卡片时的摩擦变化、挤牙膏时的受力程度，以及易碎物体开始滑落的瞬间，都可能被手掌和物体遮挡，而且变化速度快于大型视觉模型的推理频率。人类之所以能稳定完成这些任务，是因为会根据连续触觉快速调整握力和运动方向。现有 VLA 通常约 5 Hz 地生成动作，主要依赖图像和语言；有些方法虽然拼接了当前力值，但单帧触觉不能表达“力正在增大还是减小”“接触是否开始滑移”这类动态。因此，机器人需要的不是“看见一次触觉”，而是一条能在视觉规划之间持续工作的高频触觉反馈回路。

**问题缺口：** 要把这条反馈回路接到 VLA 上，需要同时解决四件事。第一，已有的人类视频预训练有丰富的语义和手部运动先验，却没有机器人触觉；从零收集同等规模的同步视触机器人数据又不可行。第二，视觉规划和触觉反应存在频率错配：如果每次触觉变化都重跑视觉骨干，计算开销太大；如果仍按视觉频率更新，机器人又来不及纠正滑移和受力。第三，原始触觉同时包含十个指尖的六轴力时间序列与空间形变图，简单 MLP 或单帧编码会丢失接触演化。第四，领域缺少覆盖双手多指、可变形物体、精细插入和力控制的统一真实评测。T-Rex 因而要回答的是：能否保留大规模 VLA 的全局能力，只用 100 小时机器人中训练数据学会接触物理，并让一个轻量触觉专家在不重算视觉的情况下实时修正动作。

## 论文摘要（英文原文）

The ability to react dynamically to tactile signals has long been considered crucial to agile human-level dexterity. Yet contemporary learning-based Vision-Language-Action (VLA) models for robotic manipulation generally either overlook the tactile modality or are limited to encoders with static cues, due in part to the scarcity of diverse training data and standardized evaluation, architectural constraints in current VLA models, and limitations of static tactile encoders. In this paper, we push the frontier of tactile-reactive manipulation by addressing all of these limitations. We propose a large-scale, 100-hour tactile-rich dataset collected via a novel, data-efficient recipe that prioritizes elementary motor primitives. To effectively exploit naturally high-frequency touch signals without sacrificing the existing capabilities of existing VLAs, we introduce a variable-rate Mixture-of-Transformers (MoT) architecture equipped with a novel temporal tactile VQ-VAE encoder. We demonstrate the effectiveness of tactile-reactive policies on 12 manipulation tasks requiring delicate force control and deformable object manipulation, achieving over 30% higher average success rate than the strongest baseline.

## 论文摘要（中文翻译）

动态响应触觉信号长期以来一直被认为是实现类人敏捷灵巧性的关键。然而，当代用于机器人操作的学习式视觉语言动作模型通常忽略触觉模态，或者仅限于使用静态线索的编码器；其原因包括缺少多样化训练数据和标准化评测、现有 VLA 架构的约束，以及静态触觉编码器本身的局限。本文针对这些问题推进触觉响应操作：作者提出一个大规模、100 小时的触觉丰富数据集，并用优先覆盖基本运动原语的数据高效采集方案构建它。为了利用天然高频的触觉信号，同时不牺牲现有 VLA 的能力，作者提出可变速率 Mixture-of-Transformers 架构，并配备新的时序触觉 VQ-VAE 编码器。在 12 个需要精细力控制和可变形物体操作的任务上，触觉响应策略相对最强基线的平均成功率高出 30 个百分点以上。

## 方法

**方法概述：** T-Rex 的整体流程可以按“先学会看和规划，再学会接触，最后适配任务”来理解。

1. **人类视频预训练**：先用 22,889 小时第一视角人类视频训练潜变量专家和动作专家。头戴相机画面与语言让模型学会识别物体和动作语义；人类手臂、手部运动经过重定向后变成统一动作监督。此时模型具备广泛的视觉运动先验，但还没有触觉专家，也不知道机器人真实接触时的力学反馈。
2. **触觉机器人中训练**：再加入 100 小时、7,755 条双手机器人轨迹。数据不是围绕 12 个最终任务重复采集，而是让 207 个物体与 22 种运动原语形成 502 个可执行组合，例如按、擦、滑、拧、挤和插入。每条轨迹同步记录三路 RGB、双臂与 44 自由度双手状态、十个指尖的六轴力和形变深度图。这个阶段把人类视频先验对齐到机器人动作，并训练新的触觉专家学习“当前接触变化应该怎样修正动作”。
3. **任务后训练**：对于开锁、抽卡、挤牙膏等复杂任务，再用约 100 条任务示范微调。中训练已经提供通用接触原语，所以后训练主要学习如何组合原语，而不是从头学习摩擦和受力。
4. **异步执行**：部署时，动作专家约 5 Hz 运行一次，先根据图像和语言生成长度 16 的动作块；触觉专家约 20 Hz 插入执行，读取最新触觉并修改尚未执行的动作。视觉语言特征只在慢速阶段计算一次并缓存，因此快回路不需要反复运行昂贵视觉骨干。

**核心机制：** 两个动作专家不是各自预测一套互相独立的控制命令，而是共同完成同一条 flow-matching 去噪轨迹。模型从随机噪声开始生成一个长度 16、每步 62 维的双臂双手动作块，总共做 10 次 Euler 去噪。1.41B 参数的动作专家先执行前 6 步，把噪声变成方向基本正确的中间动作，并把图像、语言、未来视觉表示和中间动作的 key-value cache 保存下来。随后 0.62B 参数的触觉专家不再读取原始图像，而是在动作块偏移 0、4、8、12 时取得最新触觉，复用缓存完成后 4 步去噪。这样，慢专家决定“手要往哪里去、任务处在哪一步”，快专家处理“现在是否打滑、力是否过大、接触位置是否需要微调”。训练时还随机加入 0、4、8、12 帧的触觉延迟，让模型适应部署时视觉缓存与实时触觉不同步的问题。

**方法拆解：**

- **触觉如何编码**：每个指尖最近 16 帧的六轴力序列先经过 1D 卷积 VQ-VAE，压缩成描述力变化趋势的离散 token；当前时刻的六轴力另走一条线性投影，避免压缩过程丢失瞬时接触；当前形变深度图由卷积网络提取空间接触形状。三类特征拼成触觉 token，分别覆盖“过去怎样变化、现在有多大力、接触发生在哪里”。
- **三个专家怎样分工**：潜变量专家根据视觉与语言预测未来视觉表示，为动作提供时间上下文；动作专家负责低频、全局的动作块规划；触觉专家负责高频、局部的动作细化。三者处在 Mixture-of-Transformer-Experts 骨干中，通过共享注意力交换上下文，但保持各自参数和输入职责。
- **动作如何生成**：策略输入三路 RGB、语言、力历史和形变图，输出长度 16 的 62 维动作块。双臂采用相对末端位姿增量，手指采用绝对关节目标；动作专家完成去噪区间 1.0 到 0.4，触觉专家完成 0.4 到 0。
- **快回路怎样节省计算**：动作专家运行后缓存视觉语言 KV 与中间动作；触觉更新时只执行更小的触觉专家及 4 个 Euler 步。视觉塔、潜变量专家和动作专家都不重复前向，因此触觉能够约 20 Hz 更新，而全局规划保持约 5 Hz。
- **训练目标怎样保持一致**：动作专家和触觉专家在不同时间区间回归同一个 flow velocity target，避免快回路变成与主策略分离的控制器；总损失还加入未来视觉预测项。慢专家仍在完整噪声区间训练，所以即使没有快专家也保留独立生成动作的能力。
- **数据为什么可能高效**：100 小时中训练数据按“物体 × 运动原语”覆盖接触分布，而非只覆盖最终任务。论文假设擦、滑、压、拧等接触原子能力能够被复杂任务复用，后训练只需少量示范学习组合和语言条件。

**关键要点：**

- 触觉的价值主要来自动态闭环，而不是把单步力向量拼到 VLA 状态中；π0.5 直接拼接触觉后平均成功率反而从 17% 降到 6%。
- 人类视频预训练与触觉机器人中训练是互补的：前者提供语义和粗粒度视觉运动先验，后者把先验落到可执行的接触动力学。
- 异步结构本身贡献约 5 个百分点，而完整触觉模态贡献约 23 个百分点；主要收益来自正确利用动态触觉，异步执行是进一步提升效率与反应速度的接口。

![方法图](https://arxiv.org/html/2606.17055v2/model_v2_0524.png)

*方法图*

## 结果

**核心结果：** - 12 个真实触觉响应任务、每项 16 次随机位置和朝向评测中，T-Rex 平均成功率 65%，最强基线 EgoScale 为 35%，绝对高 30 个百分点。
- 去掉全部触觉后，六项代表任务平均成功率从 65% 降到 42%；仅保留简化 MLP 力与形变为 58%，仅形变为 54%，证明时序力与空间形变均有贡献。
- 把异步触觉细化改为同步执行，六项任务平均成功率从 65% 降到 60%；提升存在但小于触觉模态本身的 23 个百分点贡献。
- 训练配方消融中，无人类预训练且无触觉中训练为 18%，只加人类预训练为 34%，只加触觉中训练为 45%，两者同时使用达到 65%。
- 模型在 24 张 H100 上进行监督微调；动作专家和潜变量专家各 1.41B 参数，触觉专家 0.62B 参数，因此结果尚不能视为低成本部署证明。

**结果表：** | 对比 / 消融 | 平均成功率 | 相对完整模型 | 说明 |
| --- | ---: | ---: | --- |
| T-Rex 完整模型 | **65%** | — | 12 任务主结果；消融平均取 6 个代表任务 |
| EgoScale | 35% | -30 个百分点 | 12 任务最强基线 |
| 无触觉 | 42% | -23 个百分点 | 触觉闭环是最大增益来源 |
| 同步触觉细化 | 60% | -5 个百分点 | 异步快慢回路有独立贡献 |
| 无人类预训练、无触觉中训练 | 18% | -47 个百分点 | 两阶段先验均缺失 |
| 仅人类预训练 | 34% | -31 个百分点 | 有视觉运动先验，缺接触落地 |
| 仅触觉中训练 | 45% | -20 个百分点 | 接触数据比单独人类预训练贡献更直接 |

![结果图](https://arxiv.org/html/2606.17055v2/data_efficiency_v2_0529.png)

*结果图*

## 洞察

**核心 insight：** - 真正值得记住的是快慢回路的接口设计：不是另起一个完全独立的反射控制器，而是在同一条 flow matching 轨迹上分段去噪，使低频规划与高频触觉修正共享动作分布。
- 中训练数据按运动原语乘物体组织，而不是按 12 个下游任务收集，这是低数据迁移的关键假设：先覆盖接触原子能力，再用少量任务示范组合。
- 触觉表示要同时保留历史变化和瞬时接触；VQ-VAE 压缩力序列解决时序动态，直接力投影避免离散压缩丢掉当前信号，形变图补空间结构。

**和已有方法的关系：** - 相对 RDP 等任务专用快慢视触策略，T-Rex 把异步触觉修正纳入经过大规模预训练的基础模型，并面向双手多指操作。
- 相对把触觉直接拼进 VLA 状态的做法，T-Rex 用独立触觉专家、专门时空编码器和分段去噪给触觉明确的控制职责。
- 相对 Heterogeneous Tactile Transformer 关注跨传感器共享 backbone，T-Rex 关注触觉表示怎样进入动作生成闭环；两者分别解决表示迁移和策略响应。

**可借鉴点：** - 对频率差异大的多模态系统，可缓存慢模态上下文，让快模态专家只运行轻量残差更新，并在训练时显式模拟缓存延迟。
- 中训练数据可以按可组合运动原语设计覆盖率，用较少小时数替代为每个下游任务收集大规模专用数据。

## 风险与判断

**局限：** - 所有主结果都来自固定基座的 Dexmate Vega-1 与 Sharpa Wave 双手，跨机器人、跨手型、跨触觉传感器的泛化没有验证。
- 12 个任务每项仅 16 次评测，而且多阶段任务允许按进度给部分分；65% 是平均进度型成功率，不等同于 65% 完整任务全成功。
- 训练依赖 22889 小时人类视频、100 小时机器人数据与 24 张 H100，数据和算力门槛仍高；论文承诺开源数据，但实际复现成本未知。
- 失败案例仍包括碰撞、滑落、定位不准、多指误触、用力过度与滑动错位，说明触觉不能替代精细视觉对齐、在线纠错和更好的行为分布覆盖。
- 触觉硬件仍受传感器形变、跨设备标定漂移和缺少掌面密集感知限制；长时程紧公差任务可能仍需在线强化学习。

**适用场景：** - 适合需要滑移、摩擦、挤压、插入、抽取、旋拧和可变形物体处理的固定平台双手灵巧操作研究。
- 适合已有视觉语言动作基座、具备同步多指触觉数据，并希望用少量下游示范完成接触密集技能适配的实验室系统。

**最终判断：** - T-Rex 是当前触觉 VLA 路线中值得重点跟踪的系统型工作：65% 对 35% 的同协议结果与触觉消融都说明动态触觉闭环确有实质价值。
- 但它更像强研究原型而非通用部署方案；在跨硬件、完整任务成功率、传感器漂移、在线恢复和计算成本得到独立验证前，不应把结论外推为通用灵巧操作已经解决。

## 结果速览表

| 对比 / 消融 | 平均成功率 | 相对完整模型 | 说明 |
| --- | ---: | ---: | --- |
| T-Rex 完整模型 | **65%** | — | 12 任务主结果；消融平均取 6 个代表任务 |
| EgoScale | 35% | -30 个百分点 | 12 任务最强基线 |
| 无触觉 | 42% | -23 个百分点 | 触觉闭环是最大增益来源 |
| 同步触觉细化 | 60% | -5 个百分点 | 异步快慢回路有独立贡献 |
| 无人类预训练、无触觉中训练 | 18% | -47 个百分点 | 两阶段先验均缺失 |
| 仅人类预训练 | 34% | -31 个百分点 | 有视觉运动先验，缺接触落地 |
| 仅触觉中训练 | 45% | -20 个百分点 | 接触数据比单独人类预训练贡献更直接 |

## 相关主题

- [[Tactile Representation]]：T-Rex 把时序力与空间形变表示接入高频动作细化，回答了触觉 backbone 如何进入策略闭环。
- [[Vision-Language-Action]]：T-Rex 为 VLA 补上异步高频触觉响应路线。
<!-- confidence: INFERRED -->

## 相关页面

- [[Heterogeneous Tactile Transformer]]
- [[Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks]]
- [[Vision-Language-Action]]
- [[tactile-force-into-pretrained-robot-policies|触觉与力觉如何进入预训练机器人策略：表示、持续适配与执行闭环]]
