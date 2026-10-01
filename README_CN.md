<p align="right">
  <a href="README.md">English</a> |
  <strong>简体中文</strong>
</p>

## 关于我

我是一名专注于**量化研究基础设施、数据 Pipelines 与 AI 驱动交易系统**的**大数据开发工程师**。

致力于构建实用且贯穿研发与交易全生命周期的端到端量化基础设施与大数据平台。

> **终极目标与核心理念**：依托自主推理与控制（ARC）的核心理念，我的最高目标是打造具备自演进能力的自主 Agent 系统，使其能够在极其复杂的金融环境中实现独立的环境探索、持续的策略探索与稳健的交易执行。

### 端到端量化全生命周期

```text
[ 行情数据 Pipeline ]  ──>  [ 因子挖掘与特征工程 ]  ──>  [ 策略研发 & Alpha 探索 ]
                                                                   │
[ 自动化执行与风控 ]  <──  [ 模拟交易与信号审计 ]  <──  [ 向量化/事件驱动回测  ]
```

| 阶段 | 核心任务 | 底层工具与架构 |
| :--- | :--- | :--- |
| **01. 行情数据** | Tick/Bar 实时流处理、历史盘口数据清洗与高吞吐时序存储 | `Flink` · `Kafka` · `ClickHouse` |
| **02. 因子挖掘** | 截面多因子挖掘、微观特征工程与因子有效性检验 | `PySpark` · `DolphinDB` · `NumPy` |
| **03. 策略研发** | 多因子 Alpha 模型、K线形态预测与 ARC 智能体策略搜寻 | `MCTS` · `Chronos` · `红蓝对抗` |
| **04. 策略回测** | 向量化快速初筛、事件驱动高精度撮合与滑点/手续费成本建模 | `Backtrader` · `自研撮合内核` |
| **05. 模拟与风控**| 零触碰模拟盘自动部署、实时信号审计与组合敞口动态风控 | `Paper Trading` · `执行网关` |

### 核心基础设施与技术栈

<p>
  <img src="https://img.shields.io/badge/Apache%20Flink-E6526F?style=flat-square&logo=apacheflink&logoColor=white" alt="Flink"/>
  <img src="https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white" alt="Kafka"/>
  <img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white" alt="Spark"/>
  <img src="https://img.shields.io/badge/Apache%20Hive-FDEE21?style=flat-square&logo=apachehive&logoColor=black" alt="Hive"/>
  <img src="https://img.shields.io/badge/Apache%20Hadoop-66CCFF?style=flat-square&logo=apachehadoop&logoColor=black" alt="Hadoop"/>
  <img src="https://img.shields.io/badge/Apache%20HBase-900000?style=flat-square&logo=apache&logoColor=white" alt="HBase"/>
  <img src="https://img.shields.io/badge/Apache%20Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white" alt="Airflow"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/ClickHouse-FFCC00?style=flat-square&logo=clickhouse&logoColor=black" alt="ClickHouse"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white" alt="Java"/>
  <img src="https://img.shields.io/badge/Scala-DC322F?style=flat-square&logo=scala&logoColor=white" alt="Scala"/>
</p>

- **实时计算与流处理**：`Apache Flink` · `Kafka` · `Tick/Bar 流处理` · `Flink SQL` · `大状态 Checkpoint 调优`
- **PB 级离线数仓与批处理**：`Apache Spark` · `Hive` · `Hadoop` · `ODS ➔ DWD ➔ DWS 分层建模`
- **任务调度与链路治理**：`Airflow` · `自研分布式调度系统` · `千级任务 DAG 依赖治理` · `SLA 保障 & 自动补算/重跑`
- **存储、时序与量化执行**：`ClickHouse` · `HBase` · `PostgreSQL` · `MySQL` · `执行网关` · `实时风控`

---

## GitHub 研发活跃度与技术指标

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=Shadowell&theme=tokyonight&no-frame=true&margin-w=4&margin-h=4&column=7" alt="GitHub Trophies" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Shadowell&theme=tokyo-night&hide_border=true&area=true" alt="Activity Graph" width="98%" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Shadowell&show_icons=true&theme=tokyonight&hide_border=true" alt="GitHub Stats" width="48%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Shadowell&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" width="48%" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Shadowell&theme=tokyonight&hide_border=true" alt="GitHub Streak" width="98%" />
</p>

---

## 我在构建的项目

我正在积极开发和维护一系列量化研究工具与生产级软件：

### [HyperTrade](https://github.com/Shadowell/HyperTrade)

面向多资产量化研究与策略孵化的受治理 Agent Runtime，由通用 **ARC (Autonomous Research Core)** 控制内核驱动，实现从自然语言目标到自演进策略研发与模拟盘自动上线的全流程闭环：

- **MCTS & MAP-Elites 搜寻引擎**：基于蒙特卡洛树搜索与质量-多样性（Quality-Diversity）网格，在策略代码 AST 节点树上高维探索解空间，防止早熟收敛。
- **红蓝对抗博弈 (Adversarial Red-Teaming)**：蓝队生成策略与代码突变，红队施加黑天鹅、流动性踩踏与宽止损陷阱攻防测试，确保策略健壮性。
- **多 Regime 定量因果归因 & Reflexion 账本**：拆解牛熊震荡市场下的性能表现，提取结构化否定约束注入进化 Prompt。
- **Voyager 技能蒸馏与模拟盘孵化**：自动提取优良子函数注册为不可变技能库，通过攻防测试的策略自动部署上线模拟盘运行。

### [HyperARC](https://github.com/Shadowell/HyperARC)

面向 ARC-AGI (1, 2 & 3 / ARC Prize 2026) 基准套件的通用自主程序合成与 AGI 推理引擎，源自 HyperTrade 的高吞吐 MCTS 搜寻与工业级控制架：

- **通用 ARC 测评基准集成**：统一支持 ARC-AGI-1、ARC-AGI-2 及 ARC-AGI-3 标准任务模型 (`ARCTask`) 与自动化数据集加载器。
- **并行 MCTS 程序搜寻**：多线程 AST 树节点突变与并行 Rollout 求解引擎，高维探索二维空间图形变换解空间。
- **2D 网格 DSL 算子原语**：内置旋转、镜像、颜色替换、边界框裁剪等原子级图形变换 DSL Primitive。
- **自愈控制架与像素级匹配**：具备自愈错误恢复机制（`HyperARCHarness`），要求合成程序在训练集上达成 100% 像素完全精确匹配后应用于测试集。

### [StockPro](https://github.com/Shadowell/StockPro)

A股研究与监控平台，涵盖实时行情接入、AI 股票评估、因子研究、策略研发与模拟交易。

### [QuantBase](https://github.com/Shadowell/QuantBase)

开源量化研究工作台，专注于真实市场数据分析、稳健的回测引擎、模拟交易验证、信号审计与风控优先的策略开发。

### [Alpha](https://github.com/Shadowell/Alpha)

自演进 A股选股系统，结合 Kronos K线预测模型、Hermes Agent 循环与多阶段漏斗筛选流程。

### [配料君 (微信小程序)](#%E5%B0%8F%E7%A8%8B%E5%BA%8F%3A%2F%2F%E9%85%8D%E6%96%99%E5%90%9B%2FBxq9NHM7YIjXgxe)

持续运营与迭代的食品配料分析与健康认知微信小程序，涵盖数据整理、产品迭代与微信搜一搜推广。

<img src="./assets/wechat-mini-program-peiliaojun.png" alt="配料君微信小程序码" width="320" />

该小程序是持续运营和迭代的真实产品，不是一次性 Demo。
