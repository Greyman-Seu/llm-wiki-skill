---
id: "pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities"
slug: "pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities"
title: "π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities"
type: source
material_type: "paper"
source_type: "paper"
created: "2026-05-11"
updated: "2026-05-16"
date: "2026-04-16"
authors:
  - "Bo Ai"
  - "Ali Amin"
  - "Raichelle Aniceto"
  - "Ashwin Balakrishna"
  - "Greg Balke"
  - "Kevin Black"
  - "George Bokinsky"
  - "Shihao Cao"
  - "Thomas Charbonnier"
  - "Vedant Choudhary"
  - "Foster Collins"
  - "Ken Conley"
  - "Grace Connors"
  - "James Darpinian"
  - "Karan Dhabalia"
  - "Maitrayee Dhaka"
  - "Jared DiCarlo"
  - "Danny Driess"
  - "Michael Equi"
  - "Adnan Esmail"
  - "Yunhao Fang"
  - "Chelsea Finn"
  - "Catherine Glossop"
  - "Thomas Godden"
  - "Ivan Goryachev"
  - "Lachlan Groom"
  - "Haroun Habeeb"
  - "Hunter Hancock"
  - "Karol Hausman"
  - "Gashon Hussein"
  - "Victor Hwang"
  - "Brian Ichter"
  - "Connor Jacobsen"
  - "Szymon Jakubczak"
  - "Rowan Jen"
  - "Tim Jones"
  - "Gregg Kammerer"
  - "Ben Katz"
  - "Liyiming Ke"
  - "Mairbek Khadikov"
  - "Chandra Kuchi"
  - "Marinda Lamb"
  - "Devin LeBlanc"
  - "Brendon LeCount"
  - "Sergey Levine"
  - "Xinyu Li"
  - "Adrian Li-Bell"
  - "Vladislav Lialin"
  - "Zhonglin Liang"
  - "Wallace Lim"
  - "Yao Lu"
  - "Enyu Luo"
  - "Vishnu Mano"
  - "Nandan Marwaha"
  - "Aikys Mongush"
  - "Liam Murphy"
  - "Suraj Nair"
  - "Tyler Patterson"
  - "Karl Pertsch"
  - "Allen Z. Ren"
  - "Gavin Schelske"
  - "Charvi Sharma"
  - "Baifeng Shi"
  - "Lucy Xiaoyang Shi"
  - "Laura Smith"
  - "Jost Tobias Springenberg"
  - "Kyle Stachowicz"
  - "Will Stoeckle"
  - "Jiaming Tang"
  - "Jimmy Tanner"
  - "Shalom Tekeste"
  - "Marcel Torne"
  - "Kyle Vedder"
  - "Quan Vuong"
  - "Anna Walling"
  - "Haohuan Wang"
  - "Jason Wang"
  - "XuDong Wang"
  - "Chris Whalen"
  - "Samuel Whitmore"
  - "Blake Williams"
  - "Charles Xu"
  - "Sukwon Yoo"
  - "Lili Yu"
  - "Wuming Zhang"
  - "Zhuoyang Zhang"
  - "Ury Zhilinsky"
domains:
  - "Physical/Embodied Intelligence"
tags:
  - "robot-foundation-model"
summary: ""
links:
  original: "https://www.pi.website/pi07"
  arxiv: "https://arxiv.org/abs/2604.15483"
  pdf: "https://www.pi.website/download/pi07.pdf"
  project: ""
  github: ""
  hjfy: ""
  doi: ""
raw_refs:
  - "https://www.pi.website/download/pi07.pdf"
related_topics:
  - "vision-language-action"
  - "human-to-robot-transfer"
related_syntheses:
  - "current-vla-landscape-foundation-control-memory-and-transfer"
confidence: EXTRACTED
hero_image: "https://followhub.tenstep.top/papers/pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities/figure-hero.png?v=20260511a"
images: 3
image_paths:
status: analyzed
---
# π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities

## 太长不看

π0.7 的关键价值不只是把模型继续做大，而是把“可控的通才机器人策略”往前推了一步。它试图解决的核心问题是：当训练数据越来越杂时，机器人基础模型怎样既能吃下示范、失败轨迹、人类视频和网页数据，又不在推理时退化成平均化、含糊的动作。作者给出的答案是把“怎么做”也写进 prompt，包括子任务语言、子目标图像、质量/速度/错误等 episode metadata，让模型学会在多模态上下文里被 steer。

## 直观理解

可以把 π0.7 理解成一个面向具身智能的“提示可控型 VLA”。传统 VLA 往往只知道任务目标，而 π0.7 还显式接收策略线索和阶段性目标，所以它不只是知道“做什么”，还更知道“按什么方式做”。这使它更容易利用 heterogeneous data，并把不同来源学到的技能重新组合到新任务上。

![Fig. 1 总览图](https://followhub.tenstep.top/papers/pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities/figure-hero.png?v=20260511a)

*Fig. 1：π0.7 总览图，展示 heterogeneous data、prompt 组成以及开箱即用能力与 cross-embodiment transfer。*

## 核心信息

- **作者**：Bo Ai 等 Physical Intelligence 团队
- **机构**：Physical Intelligence
- **来源类型**：pdf_url
- **输入来源**：https://www.pi.website/download/pi07.pdf
- **项目页面**：https://www.pi.website/pi07
- **PDF 地址**：https://www.pi.website/download/pi07.pdf
- **arXiv**：https://arxiv.org/abs/2604.15483
- **发布日期**：2026-04-16
- **主题域**：physical-embodied-intelligence

## 背景与问题

**动机：** 机器人基础模型一直在追求 generalist 能力，但过去很多 VLA 虽然能覆盖很多任务，却很难真正展示类似 LLM 的组合泛化。尤其当数据混入不同策略、不同质量、失败轨迹和跨 embodiment 数据后，模型很容易把这些模式平均掉，最后既不稳也不够可控。

**问题缺口：** 作者关注的不只是“怎样训练一个更强 VLA”，而是“怎样让机器人基础模型在更杂、更广的数据混合里仍然保持可控性，并把这些数据真正转化成可组合能力”。这也是具身智能走向通用化时的一个核心瓶颈。

## 论文摘要（英文原文）

We present a new robotic foundation model, called π0.7, that can enable strong out-of-the-box performance in a wide range of scenarios. π0.7 can follow diverse language instructions in unseen environments, including multi-stage tasks with various kitchen appliances, provide zero-shot cross-embodiment generalization, for example enabling a robot to fold laundry without seeing the task before, and perform challenging tasks such as operating an espresso machine out of the box at a level of performance that matches much more specialized RL-finetuned models. The main idea behind π0.7 is to use diverse context conditioning during training. This conditioning information, contained in the prompt, makes it possible to steer the model precisely to perform many tasks with different strategies. It is conditioned not just on a language command that describes what it should do, but on additional multimodal information that also describes the manner or strategy in which it should do it, including metadata about task performance and subgoal images. This enables π0.7 to use very diverse data, including demonstrations, potentially suboptimal (autonomous) data including failures, and data from non-robot sources. Our experiments evaluate π0.7 across numerous tasks with multiple robot platforms, on tasks that require speed and dexterity, language following, and compositional task generalization.

## 论文摘要（中文翻译）

作者提出了一个新的机器人基础模型 π0.7，它可以在多种场景中实现很强的开箱即用表现。π0.7 能够在未见环境中遵循多样化语言指令，包括涉及多种厨房电器的多阶段任务；能够实现 zero-shot 的跨 embodiment 泛化，例如在从未见过该任务的情况下完成叠衣服；还能在不做任务特定后训练的前提下，完成如操作咖啡机这类具有挑战性的任务，其表现可与专门经过 RL 微调的模型相匹配。π0.7 的核心思想是在训练中使用多样化的上下文条件信息。这些包含在 prompt 里的条件让模型能够被更精确地 steer，从而以不同策略执行多种任务。模型接收的不仅是描述“做什么”的语言命令，还包括描述“如何做”的额外多模态信息，例如任务执行质量相关的 metadata 和子目标图像。这样一来，π0.7 就能利用非常多样的数据，包括示范数据、包含失败在内的次优自主数据，以及非机器人来源的数据。论文在多个机器人平台和大量任务上评估了 π0.7，涵盖速度与灵巧性、语言跟随以及组合泛化等能力。

## 方法

**方法概述：** π0.7 是一个约 5B 参数的机器人基础模型，由 4B 级别的 VLM backbone、MEM 风格的视频历史编码器和 860M 的 action expert 组成。作者没有把重点放在全新架构发明上，而是把重点放在 prompt 设计和数据利用方式上。

**核心机制：** π0.7 不只接收 task instruction，而是把 context 扩展成多种模态的组合：

- **子任务语言**：给出更细粒度的当前 subtask instruction
- **子目标图像**：由轻量 world model 生成，帮助模型更明确地知道阶段性目标状态
- **episode metadata**：包含速度、质量、是否犯错等标签，让模型学习“什么样的执行方式更优”
- **控制模式标识**：区分 joint-level 与 end-effector 控制

**训练数据策略：** 这篇工作的一大特点是明确拥抱 heterogeneous data，而不是只保留高质量示范：

- 机器人示范数据
- 较低质量甚至失败的轨迹
- 来自先前模型评估或自主执行的数据
- 人类 egocentric 视频
- 通用多模态网页数据

作者的核心判断是，只要 prompt 足够细、能把行为方式 disambiguate 清楚，次优数据和非机器人数据也能成为通才能力的一部分，而不只是噪声。

**方法要点：**

- 通过 richer prompting 缓解多源数据带来的 mode averaging
- 用 subgoal image 把“想达到什么状态”显式交给策略模型
- 用 metadata 让模型能在推理时被 steer 到“更快”“更稳”“少犯错”等偏好
- 把 prior RL specialists 的经验蒸馏进一个 generalist 模型中

![Fig. 2 架构图](https://followhub.tenstep.top/papers/pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities/figure-method.png?v=20260511a)

*Fig. 2：架构总览图，说明 4B VLM backbone、MEM-style history encoder、860M action expert，以及 language / metadata / subgoal image 的关系。*

## 结果

**核心结果：**

- π0.7 在多类高灵巧、长时程任务上实现了强 out-of-the-box 表现，不依赖任务特定 post-training
- 在 espresso making、box building、laundry folding 等任务上，性能可与先前 RL specialist 模型竞争，部分任务吞吐甚至更高
- 在未见环境中的 instruction following 上，明显优于 π0.5 和 π0.6
- 在复杂 referential instruction 上，加入 world-model 生成的 subgoal image 后效果进一步提升
- 展示了 zero-shot cross-embodiment transfer，例如在目标机器人从未见过相应任务数据时也能直接迁移

![Fig. 6 结果图](https://followhub.tenstep.top/papers/pi07-a-steerable-generalist-robotic-foundation-model-with-emergent-capabilities/figure-result.png?v=20260511a)

*Fig. 6：开箱即用灵巧操作结果图，展示 π0.7 在 laundry、espresso、box building 等任务上与 specialist 路线的对比。*

**结果速览表：**

| 维度 | π0.7 的结论 |
| --- | --- |
| 开箱即用灵巧操作 | 能直接完成多种高难度 manipulation 任务 |
| 对比 RL specialist | 多项任务接近甚至超过专用策略 |
| 指令泛化 | 明显强于 π0.5 / π0.6 |
| 跨 embodiment 泛化 | 展现 zero-shot transfer 能力 |
| 组合泛化 | 能把已学技能重新组合到新任务 |

## 洞察

**核心 insight：** 这篇论文真正值得记住的不是“又一个更强的 VLA”，而是它把具身智能里的 prompt engineering 推到了更结构化的层面。作者实际上在做一件很重要的事：把训练数据中的“执行方式”也显式化，使得基础模型不只是学习任务结果，还学习任务风格、质量和阶段性目标。

**和已有路线的关系：**

- 相对传统 VLA，π0.7 更强调 steerability，而不是只强调任务覆盖面
- 相对只吃高质量 demonstration 的路线，它更愿意吸收失败轨迹和 autonomous data
- 相对只做 policy learning 的路线，它把 lightweight world model 纳入 prompt 生成链路，让图像化子目标成为机器人控制的一部分

**可借鉴点：**

- 具身智能里“数据更多”并不自动等于“泛化更强”，关键是有没有把数据差异显式编码给模型
- subgoal image 可能是连接 world model 与 low-level policy 的一条务实接口
- 从工程视角看，这篇工作说明通才策略与 specialist 策略不一定是替代关系，也可以是蒸馏关系

## 风险与判断

**局限：**

- 论文展示了强 generalization 信号，但作者自己也承认，在如此大而杂的数据集下，很难严格界定什么是真正“未见”的任务
- 许多能力可能来自对已见技能片段的 remix，而不是更强意义上的系统性推理
- 这条路线对高质量标注、prompt 设计和数据组织的要求很高，复制门槛不低

**适用场景：**

- 面向多任务 manipulation 的机器人基础模型
- 需要跨 embodiment 泛化的研究场景
- 想把 world model、language coaching、metadata control 结合进统一策略框架的系统

**最终判断：** 这是近阶段具身智能里很有代表性的一篇工作。它的重要性不只在性能，而在于明确提出并验证了一条“通过多模态可控 prompt 把 heterogeneous data 变成通才能力”的路线。

## 相关主题

- vision-language-action
- human-to-robot-transfer

## 相关页面

- [[Vision-Language-Action]]
- [[Online RL for VLA]]
- [[Long-Horizon Memory for Robot Policies]]
- [[Human-to-Robot Transfer]]
- [[当前 VLA 路线图：基座、可控性、在线精修、记忆与人类数据]]
