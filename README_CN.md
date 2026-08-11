<p align="right">
  <a href="README.md">English</a> |
  <strong>简体中文</strong>
</p>

# 冯杰

**大数据开发工程师 · 数据架构 · 高可靠数据系统**

拥有 **9 年大数据开发经验**，长期从事 PB 级离线数仓、大规模实时计算、任务治理、数据质量与性能优化。

目前在 Shopee 负责 **600+TB/日**生产数据链路，覆盖 **10 个国际站点**。擅长将复杂业务规则沉淀为稳定的数据模型、可复用公共层、可追踪 SLA 和可恢复的数据交付流程。

[English](README.md) · [邮箱](mailto:jie.f@outlook.com)

## 生产规模与成果

| 规模 | 工程成果 |
| --- | --- |
| **600+TB/日** | 支撑 10 个国际站点分析业务的生产数据链路 |
| **1000+ 任务** | 调度迁移中的依赖、资源、灰度、SLA、回补与恢复治理 |
| **百亿事件/日** | 基于 Flink、Kafka、MySQL 与 HBase 建设实时数仓链路 |
| **PB 级数仓** | 分层建模、公共层、指标口径、跨区域同步与数据质量治理 |

## 核心能力

- **离线数仓**：Hadoop、Hive、Spark、Spark SQL、维度建模、ODS/DWD/DWS 分层、公共层设计
- **实时计算**：Flink、Flink SQL、Kafka、HBase、窗口聚合、大状态 Checkpoint、内存与反压排查
- **任务与 SLA 治理**：Airflow、分布式调度、DAG 依赖治理、灰度迁移、监控、回补与恢复
- **数据可靠性**：指标口径、数据质量、对账、去重、历史回补、可观测性与故障诊断
- **存储与服务**：MySQL、PostgreSQL、ClickHouse、REST API、Python、Java、Scala
- **AI 协作研发**：使用 Codex、Cursor 辅助需求拆解、实现、测试、排障和交付验收

## 脱敏工程案例

### 大规模任务迁移与 SLA 治理

推动 1000+ 离线任务从 Airflow 迁移至自研调度系统，覆盖依赖梳理、资源配置、灰度迁移、SLA 对齐、数据回补、监控与异常恢复，使核心数据产出提前 2 小时以上。

### 百亿事件级实时数仓

从接入、明细加工、窗口聚合到指标服务建设实时数据链路，推动 ODS → DWD → DWS 分层规范落地，并使 Kafka 数据复用率提升 80%。

### 数据可靠性与性能优化

具备跨区域同步、大规模流量去重、历史回补、大状态 Checkpoint 调优、内存问题定位和失败恢复经验，覆盖离线与实时工作负载。

> 以上仅展示脱敏后的架构思路和工程成果，不公开雇主源代码、业务数据或内部实现细节。

## 独立工程项目

- [Alpha](https://github.com/Shadowell/Alpha)：开源 A 股研究系统，包含可信行情接入、可复现工作流、CI 与公开 Release
- [StockPro](https://github.com/Shadowell/StockPro)：实时 A 股研究与监控平台，强调数据质量和受控仿真流程
- [QuantBase](https://github.com/Shadowell/QuantBase)：覆盖真实行情、回测、模拟交易、信号审计与风险优先验证的研究工作台
- [CommentX](https://github.com/Shadowell/CommentX)：覆盖审核、排期、多平台分发与受控执行的内容运营工作台

这些项目用于证明产品意识和端到端交付能力；我的核心职业方向仍是 **大数据开发与数据架构**。

## 当前关注方向

- 高可靠离线与实时数据系统
- 数据架构、治理与可观测性
- 以明确目标和验收标准驱动的 AI 协作研发
- 具备测试、CI、Release 与能力边界说明的开源维护
