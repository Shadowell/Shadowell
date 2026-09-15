<p align="right">
  <a href="README.md">English</a> |
  <strong>简体中文</strong>
</p>

# 冯杰

**大数据开发工程师 · AI Agent 与量化系统研究者**

我的主业是大数据开发，拥有 **9 年生产级大数据开发经验**，长期参与 PB 级离线数仓、
大规模实时计算、任务治理、数据质量与性能优化。

在主业之外，我持续研究 **AI Agent、量化系统和端到端 AI 产品**。这些工作用于探索模型如何接入
真实数据与工具，并通过持久状态、证据、评测、权限、人工确认和运行验证形成可持续迭代的系统。

**熟悉的市场：永续合约、A 股。量化研究尤其聚焦永续合约**，将数据工程能力用于行情处理、策略验证、模拟交易与风险监控。

[English](README.md) · [邮箱](mailto:jie.f@outlook.com)

## 主业｜大数据开发

| 核心方向 | 能力范围 |
| --- | --- |
| **离线数仓** | 维度与分层建模、公共层、指标口径、跨区域同步与历史回补 |
| **实时计算** | Flink/Kafka 链路、大状态 Checkpoint、吞吐与延迟优化、故障恢复 |
| **任务治理** | 依赖、资源、灰度、SLA、补数、迁移与可观测性 |
| **数据质量** | 真实数据校验、血缘与审计、异常定位、可复现计算与稳定性治理 |

核心技术栈：`Flink` · `Kafka` · `Spark` · `Hive` · `Hadoop` · `HBase` · `Airflow` ·
`MySQL` · `PostgreSQL` · `ClickHouse` · `Python` · `Java` · `Scala`

## 副业研究｜AI Agent、量化与 AI 产品

| 在研方向 | 当前工作 |
| --- | --- |
| **永续合约量化研究 · 重点** | 多空策略、交易所行情、回测与 Paper 验证；关注杠杆、保证金、资金费率、手续费与滑点对策略表现的影响 |
| **A 股量化研究** | 行情与数据质量、选股与策略研究、可复现回测、模拟交易和市场监控 |
| **AI Agent 与自主研究** | 受治理运行时、工具编排、持久目标与证据、程序合成、评测和失败恢复 |
| **AI 产品与运营系统** | AI 视频生产、GPU/模型接入、内容运营、人工审核、测试、部署与可观测性 |

这些方向仍在持续研究和迭代。我会明确区分本地验证、研究实验、Paper、比赛结果与生产效果，
不把过程状态包装成未经验证的成果。

## 代表成果与能力证明

### 大数据工程成果

| 规模 | 工程成果 |
| --- | --- |
| **600+TB/日** | 支撑 10 个国际站点分析业务的生产数据链路 |
| **1000+ 任务** | 调度迁移中的依赖、资源、灰度、SLA、回补与恢复治理 |
| **百亿事件/日** | 基于 Flink、Kafka、MySQL 与 HBase 建设实时数仓链路 |
| **PB 级数仓** | 分层建模、公共层、指标口径、跨区域同步与数据质量治理 |

### AI Agent 研究系统

#### [HyperTrade](https://github.com/Shadowell/HyperTrade)

面向量化研究的受治理 Agent 运行时，将开放式研究目标收敛为持久、可复查的任务。

- 持久化目标、计划、步骤、证据、预算和完成条件
- 组合 MCTS 与 MAP-Elites，进行多样化策略代码探索
- 引入红队压力测试、市场 Regime 归因和结构化否定约束
- 将研究、回测、Paper Trading 与真实效果隔离在明确的控制边界之后

#### [HyperARC](https://arcprize.org/competitions/2026) · 私有研究项目

**比赛：** [ARC-AGI-2](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-2) ·
[ARC-AGI-3](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3)

覆盖 ARC-AGI-1/2 程序合成与 ARC-AGI-3 交互式 Agent 实验的研究系统。

- 网格变换 DSL、候选生成、精确匹配验证与受限代码执行
- 视觉状态抽象、动作历史、技能路由与轨迹评测
- 严格区分本地诊断与官方基准结果，并保留可复现实验证据

Agent 工程能力：`任务规划` · `Tool Calling` · `MCP` · `JSON Schema` · `状态机` ·
`记忆` · `评测` · `人工确认` · `失败恢复` · `审计`

### Kaggle 竞赛研究

- **[RSNA Knee Abnormality Detection](https://www.kaggle.com/competitions/rsna-knee-abnormality-detection)**：正在参与的医学影像竞赛，围绕膝关节 MRI 与影像报告的多模态异常检测开展研究。
- **[Kaggriculture](https://www.kaggle.com/competitions/kaggriculture)**：正在参与的农业经营策略竞赛，围绕资源分配、市场决策与 Agent 策略评测开展研究。

### 量化研究｜永续合约与 A 股

**永续合约是我的量化研究重点，A 股是另一条熟悉且持续投入的研究方向。**

- **BitPro · 私有产品**：以**永续合约研究与模拟交易**为重点的数字资产研究平台，覆盖交易所行情、多空策略、策略版本、异步回测、Paper 验证、受控执行与监控

  <a href="https://shadowell.github.io/Shadowell/strategy/"><img src="./assets/bitpro-paper-performance.png" alt="打开 BitPro Paper 动态指标页" width="100%" /></a><br />
  <sub>Paper 收益快照 · 每 10 分钟定时更新（调度与图片缓存可能延迟） · 点击进入动态页面</sub>

我把行情数据质量、计算可复现性、成本、成交明细和审计记录视为研究前提；展示研究证据，
不包装未经验证的收益。

**A 股研究与工程实践：**

- [Alpha](https://github.com/Shadowell/Alpha)：开源 A 股研究系统，包含可信行情接入、可复现工作流、CI 与公开 Release
- [StockPro](https://github.com/Shadowell/StockPro)：实时 A 股研究与监控平台，覆盖数据质量、策略生命周期、回测、Paper Trading 与运行检查
- [QuantBase](https://github.com/Shadowell/QuantBase)：覆盖真实行情、Backtrader 验证、模拟交易、信号审计与风险优先研发的研究工作台

### AI 产品与独立产品

- **Zora · 私有产品**：串联故事、角色、分镜、视频生成、配音、合成、质量审核和发布的 AI 动画工作台
- **FrameLab · 私有产品**：集成模型 API、ComfyUI/GPU Worker、异步任务、存储、积分、审核、测试与部署的 AI 视频平台

我会根据能力边界选择 Codex、Cursor、GLM、Grok 等模型和工具；由我负责业务判断、需求拆解、
约束、验收标准，并通过真实数据、自动化测试、运行日志和用户可见结果验证交付。

#### 独立运营的微信小程序

##### 配料君

持续运营与迭代的食品配料分析与健康认知小程序，覆盖数据整理、产品迭代与微信搜一搜推广。

<img src="./assets/wechat-mini-program-peiliaojun.png" alt="配料君微信小程序码" width="320" />

##### 野钓潮汐

面向钓鱼爱好者的潮汐与天气小程序，整合潮汐与气象时序数据、后端服务和移动端产品体验。

<img src="./assets/wechat-mini-program-tidenow.png" alt="野钓潮汐微信小程序码" width="320" />

这两个小程序都是持续运营和迭代的真实产品，不是一次性 Demo。

> 雇主源代码、业务数据和内部实现细节保持保密；私有项目只展示能力与已验证结果，不公开仓库内容。

## 当前关注方向

- 可靠的离线、实时与数据治理体系，以及面向模型和 Agent 工作负载的数据底座
- 具备证据、评测、记忆和安全工具调用的受治理 Agent 运行时
- 永续合约多空策略与成本、风险研究，以及 A 股策略和数据研究，以真实数据与 Paper 验证推进
- 包含人工审核和可观测交付的 AI 视频与内容生产系统
