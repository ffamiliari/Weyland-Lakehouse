# Weyland Lakehouse

Consumption-based SaaS analytics platform built on Databricks using PySpark, Delta Lake and Medallion Architecture.

---

## Overview

Weyland Lakehouse simulates a modern SaaS data platform where customer growth is driven by platform consumption.

The project transforms raw customer, subscription and compute usage data into business-ready analytics tables using a modern Lakehouse architecture inspired by real-world Databricks implementations.

The objective is not only to build technical pipelines, but also to understand how modern data platforms support business analytics, customer adoption and revenue expansion.

---

## Objectives

This project was built to learn and demonstrate:

- Databricks
- PySpark
- Delta Lake
- Medallion Architecture
- Consumption-based SaaS analytics
- Business-oriented data engineering
- Modern Lakehouse concepts

---

## Business Context

Modern SaaS and AI platforms increasingly rely on usage-based pricing models.

Instead of relying only on fixed subscriptions, revenue growth is increasingly driven by:

- compute consumption
- query execution
- storage usage
- pipeline activity
- platform adoption

This project simulates how a modern data platform can analyze these signals to identify:

- customer expansion opportunities
- adoption trends
- under-utilization risk
- churn risk

---

## What is a Lakehouse?

A Lakehouse combines:

- the flexibility of a Data Lake
- the reliability and analytics capabilities of a Data Warehouse

This architecture allows organizations to support:

- data engineering
- analytics
- machine learning
- AI workloads

within a unified platform.

---

## Medallion Architecture

The project follows the Medallion Architecture:

```text
Bronze → Silver → Gold
```

### Bronze Layer
Stores raw ingested data with minimal transformation.

### Silver Layer
Cleans, standardizes and validates business entities.

### Gold Layer
Produces business-ready analytics tables optimized for reporting and SQL analysis.

---

## Planned Data Flow

```text
Raw SaaS Data
    ↓
Bronze Layer
    ↓
Silver Layer
    ↓
Gold Layer
    ↓
Business Insights & Analytics
```

---

## Simulated SaaS Datasets

The platform simulates four core datasets:

| Dataset | Description |
|---|---|
| customers | customer master data |
| subscriptions | SaaS subscription contracts |
| usage_events | product usage activity |
| compute_consumption | compute and storage consumption |

---

## Planned Gold-Level Business Outputs

The project will generate analytics tables for:

- customer consumption metrics
- customer adoption scoring
- revenue expansion analysis
- customer health indicators
- churn and under-utilization risk

---

## Technologies

- Databricks
- PySpark
- Delta Lake
- Databricks SQL
- Git
- GitHub

---

## Project Structure

```text
weyland-lakehouse/
│
├── data/
│   └── raw/
│
├── docs/
│   ├── architecture.md
│   ├── business_model.md
│   └── data_dictionary.md
│
├── notebooks/
│   ├── 01_bronze_ingestion.py
│   ├── 02_silver_transformation.py
│   ├── 03_gold_business_metrics.py
│   └── 04_business_insights.sql
│
├── screenshots/
│
├── README.md
└── .gitignore
```

---

## Learning Goals

The objective is to progressively understand:

- how modern Lakehouse platforms work
- how Delta Lake improves reliability
- how Medallion Architecture structures data pipelines
- how consumption-based SaaS companies operate
- how business analytics and data engineering connect together

---

## Future Improvements

Planned future additions include:

- Databricks dashboards
- streaming ingestion
- advanced customer health scoring
- predictive churn modeling
- AI-driven analytics