---
id: "turbovla-real-time-vision-language-action-model"
slug: "turbovla-real-time-vision-language-action-model"
title: "TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM"
type: source
material_type: "paper"
source_type: "paper"
created: "2026-08-10"
updated: "2026-08-10"
date: "2026-07-29"
authors: ["Hengyi Xie", "Chenfei Yao", "Xianjin Wu", "Xuanyang Xi", "Yiping Tang", "Di Xu", "Yingying Zhu", "Dingkang Liang", "Xiang Bai", "Han Ding"]
affiliation: "Huazhong University of Science and Technology; Huawei Technologies"
related_organizations: ["Huazhong University of Science and Technology", "Huawei Technologies"]
domains: ["Physical/Embodied Intelligence"]
tags: ["vision-language-action", "robot-manipulation", "efficient-inference"]
summary: "用轻量视觉—语言交互替换 LLM 居中的 V→L→A 路径，在 0.2B 参数下实现 31.2 ms、0.9 GB VRAM 的 VLA 推理。"
links:
  original: "https://arxiv.org/abs/2607.27205"
  arxiv: "https://arxiv.org/abs/2607.27205"
  pdf: "https://arxiv.org/pdf/2607.27205"
  project: "https://H-EmbodVis.github.io/TurboVLA"
  github: "https://github.com/H-EmbodVis/TurboVLA"
  hjfy: "https://hjfy.top/arxiv/2607.27205"
raw_refs: ["https://arxiv.org/html/2607.27205v1"]
related_topics: ["vision-language-action"]
confidence: EXTRACTED
hero_image: "https://arxiv.org/html/2607.27205v1/x2.png"
images: 1
image_paths: ["https://arxiv.org/html/2607.27205v1/x2.png"]
source_url: "https://arxiv.org/abs/2607.27205"
html_url: "https://arxiv.org/html/2607.27205"
pdf_url: "https://arxiv.org/pdf/2607.27205"
translation_url: "https://hjfy.top/arxiv/2607.27205"
status: analyzed
---
# TurboVLA：把 VLA 的执行路径从「过 LLM」改成「直接控制」

## 太长不看

TurboVLA 主张：执行级机器人操作不必每一步都经过大语言模型。它以视觉编码器、轻量文本编码器、双向交叉注意力和动作块解码器直接形成 `V + L → A`，在 LIBERO 达到 97.7% 平均成功率，同时在 RTX 4090 上仅用 0.2B 参数、31.2 ms 推理延迟和 0.9 GB 显存。

## 直观理解

传统 VLA 像是每次抬手前都先让一个大语言模型把画面“翻译”一遍；TurboVLA 则保留语言对视觉的条件化，但把这件事缩成少量跨注意力层，再直接输出一段连续动作。它牺牲的是开放式推理能力的假设空间，换来更高的闭环控制频率和更低的边缘部署门槛。

## 核心信息

- **作者**：Hengyi Xie 等；华中科技大学、华为。
- **来源类型**：arXiv 论文（v1，2026-07-29）。
- **原文链接**：[abs](https://arxiv.org/abs/2607.27205)｜[PDF](https://arxiv.org/pdf/2607.27205)｜[项目页](https://H-EmbodVis.github.io/TurboVLA)｜[代码](https://github.com/H-EmbodVis/TurboVLA)。
- **问题**：LLM 居中的 `V → L → A` 在每个控制步都会带来显存和延迟成本。
- **结论**：对执行级、语言条件的操作任务，紧凑的直接跨模态交互足以取得强表现。

## 背景与问题

VLA 通常把图像投影到大语言模型的表示空间，再由该表示生成动作；即使动作采用并行的连续解码器，LLM 仍留在在线控制的关键路径上。论文的问题是：在不要求开放式规划/对话的执行阶段，是否可移除这条昂贵的中枢路径，同时维持语言 grounding 与操作成功率？

## 论文摘要（英文原文）

Vision-language-action models commonly adopt an LLM-centric V → L → A pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. We introduce TurboVLA, which directly exchanges information between independently encoded visual observations and language instructions through lightweight bidirectional vision-language interaction, then predicts continuous action chunks with a compact decoder.

## 论文摘要（中文翻译）

现有 VLA 常把视觉输入送入大语言模型表征后再解码为机器人动作。TurboVLA 让视觉与指令先独立编码，再通过轻量的双向视觉—语言交互直接形成控制表征，并由紧凑解码器预测连续动作块，从而显著降低在线推理的计算和显存成本。

## 方法

**结构：** DINOv3 提取每个相机的空间视觉 token，BERT 保留完整指令 token（而非只用 pooled embedding）；两者投影到 `d=256` 的共享维度后，经过 6 层双向 cross-attention。视觉 token 查询语言得到 instruction-conditioned vision，语言 token 查询视觉得到 scene-aware instruction；ACT 风格 Transformer 再结合机器人状态，一次预测连续动作 chunk。交互层以 grounding-pretrained 的 feature-enhancement 权重初始化。

**训练与评测：** 行为克隆、L1 动作损失，在 4 张 RTX 4090 上训练。LIBERO 使用 OpenVLA 的 modified no-noops RLDS，DINOv3 ViT-B，混合四套件训练 80k steps；每任务 50 rollout、共 2,000 次试验，预测 12 步 7-DoF 动作。RoboTwin 2.0 用官方 clean demonstrations，DINOv3 ViT-L，训练 55k steps，预测 50 步 14 维双臂绝对关节位置；每个 50 任务做 100 rollout。两者的模型尺寸和动作定义不同，不能把 31.2 ms 与 43.4 ms 当作同一设置下的直接延迟对比。

![从 LLM-centric VLA 到 TurboVLA](https://arxiv.org/html/2607.27205v1/x2.png)

*图：论文 Figure 2。核心改变是移除 LLM 作为视觉到动作的必经表示层，而不是移除语言条件。*

## 结果

| 设置 | 结果 | 含义 |
| --- | --- | --- |
| LIBERO | 97.7% 平均成功率 | 0.2B 参数、0.9 GB、31.2 ms；与更大 VLA 竞争 |
| RoboTwin 2.0（50 个双臂任务） | 60.2%，43.4 ms | 高于 π0.5 的 57.0%，且其延迟为 95.6 ms |
| AgileX Piper 真机四任务 | 92.5%、80%、90%、87.5% | 每任务 40 次试验，均优于同协议 π0.5 |

**LIBERO 的效率语境：** 对照表在单张 RTX 4090、batch=1 下测量“多模态输入到一个 action chunk”的时间与整条在线策略的峰值显存。TurboVLA 不是只把 decoder 加速：其 0.2B / 0.9GB / 31.2ms 来自同时移除了 LLM 中枢、采用轻量文本编码和并行 action chunk；但不同基线的 chunk 长度或自回归 token 数并不完全相同，结论应理解为部署轮廓上的强证据而非严格的逐 FLOP 公平赛。

**消融：** 去除语言后 LIBERO 平均成功率从 97.7% 降至 70.8%，其中 Goal 从 97.4% 降到 11.6%；以 learned task-ID 代替自然语言为 95.4%。BERT 97.7%、T5-small 97.1%、SigLIP text 95.5%，说明轻量语义编码足够但语义本身不可省。无交互/两种单向交互/双向交互分别为 95.2%、96.1%/96.5%、97.7%。交互层数 `N=2/4/6/8` 为 93.5/95.7/97.7/96.6%，主配置的 6 层不是任意选择；动作 horizon `H=8/10/12/15` 为 96.4/96.9/97.7/95.6%，过长 chunk 会增加一次预测难度。

真机实验以 LIBERO 预训练权重为起点，对每个任务用 65 条遥操作示范微调 12.5k steps；因此结果证明的是执行层的可部署性，不等同于无需任务数据的开放世界泛化。

## 洞察

- VLA 的语言能力可以按控制环路分层：任务级规划可以慢、重；执行级 grounding 和动作输出应当快、轻。
- 论文的关键不是“不要语言模型”，而是把语言模型从高频控制临界路径移开。
- 对算力受限的本地机器人，延迟、显存和成功率应被共同优化；单独报告参数量并不足以说明能否部署。
- 更准确的系统形态是“慢规划 + 快执行”：LLM 可位于任务分解、失败恢复或人机交互层，TurboVLA 类模块承担高频视觉—语言 grounding 与连续控制；这也是论文结论最可迁移的部分。

## 风险与判断

**局限：** 实验主要覆盖语言条件的执行级操作；直接 `V + L → A` 是否能承担长程规划、复杂语义推理或开放世界任务分解，论文并未证明。跨方法的效率指标虽在同一 RTX 4090 条件测量，但不同实现和动作定义仍会影响横向比较。

**适用场景：** 高频闭环抓取、桌面操作、双臂协调，以及希望在消费级 GPU 本地运行的语言条件策略。

**最终判断：** 这是一个很有工程含金量的 VLA 重构：若系统另有规划器，TurboVLA 式执行器是比“大模型每步在场”更可信的部署路线；不应把它解读为大模型在整条具身链路中已不再需要。

## 相关主题

- vision-language-action
- robot-manipulation
- efficient-inference
