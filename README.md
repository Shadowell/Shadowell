<p align="right">
  <strong>English</strong> |
  <a href="README_CN.md">简体中文</a>
</p>

# Jie Feng

**Big Data Engineer · Data Architecture · Reliable Data Systems**

Big Data Engineer with **9 years of hands-on development experience** across PB-scale offline data warehouses, large-scale streaming pipelines, workflow governance, data quality, and performance optimization.

At Shopee, I work on production data paths processing **600+ TB per day** across **10 international sites**. My focus is turning complex business rules into stable data models, reusable shared layers, traceable SLAs, and recoverable delivery workflows.

[中文主页](README_CN.md) · [Email](mailto:jie.f@outlook.com)

## Production Impact

| Scale | Engineering outcome |
| --- | --- |
| **600+ TB/day** | Production data paths serving analytics across 10 international sites |
| **1,000+ jobs** | Dependency, resource, rollout, SLA, backfill, and recovery governance during scheduler migration |
| **10B events/day** | Real-time warehouse path built with Flink, Kafka, MySQL, and HBase |
| **PB-scale DWH** | Layered modeling, shared data layers, metric consistency, cross-region synchronization, and data quality |

## Core Competencies

- **Offline Data Warehousing** — Hadoop, Hive, Spark, Spark SQL, dimensional modeling, ODS/DWD/DWS layers, shared-layer design
- **Real-Time Computing** — Flink, Flink SQL, Kafka, HBase, window aggregation, large-state checkpoints, memory and backpressure diagnosis
- **Workflow & SLA Governance** — Airflow, distributed scheduling, DAG dependency governance, staged migration, monitoring, backfills, recovery
- **Data Reliability** — metric definitions, data quality, reconciliation, deduplication, historical backfills, observability, incident diagnosis
- **Storage & Services** — MySQL, PostgreSQL, ClickHouse, REST APIs, Python, Java, Scala
- **AI-Assisted Engineering** — Codex and Cursor for requirement decomposition, implementation, testing, troubleshooting, and delivery verification

## Selected Engineering Case Studies

### Large-Scale Job Migration & SLA Governance

Migrated and governed 1,000+ offline jobs from Airflow to an in-house scheduler. The work covered dependency mapping, resource configuration, staged rollout, SLA alignment, backfills, monitoring, and recovery—moving critical data availability forward by more than two hours.

### 10B-Event-Per-Day Real-Time Data Warehouse

Built a real-time data warehouse path from ingestion and detail processing to window aggregation and metric serving. Standardized ODS → DWD → DWS modeling and increased Kafka data reuse by 80%.

### Data Reliability & Performance

Worked on cross-region synchronization, large-scale traffic deduplication, historical backfills, large-state checkpoint tuning, memory diagnosis, and failure recovery for batch and streaming workloads.

> These case studies describe architecture and engineering outcomes only. Employer source code, data, and internal implementation details remain confidential.

## Independent Engineering Work

- [Alpha](https://github.com/Shadowell/Alpha) — Open-source A-share research system with trusted market-data ingestion, reproducible workflows, CI, and a public release
- [StockPro](https://github.com/Shadowell/StockPro) — Real-time A-share research and monitoring platform with data-quality and controlled simulation workflows
- [QuantBase](https://github.com/Shadowell/QuantBase) — Research workbench for real market data, backtesting, paper trading, signal audit, and risk-first validation
- [CommentX](https://github.com/Shadowell/CommentX) — Content-operations workspace with review, scheduling, multi-platform delivery, and controlled execution

These projects demonstrate product ownership and end-to-end delivery. My primary professional focus remains **big-data engineering and data architecture**.

## Current Focus

- Reliable batch and streaming data systems
- Data architecture, governance, and observability
- AI-assisted software delivery with explicit requirements and acceptance criteria
- Open-source maintenance with tests, CI, releases, and documented operating boundaries
