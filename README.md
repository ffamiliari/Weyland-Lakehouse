# Weyland Lakehouse

Consumption-based SaaS analytics platform built on Databricks using PySpark, Delta Lake and Medallion Architecture.

---

## Overview

Weyland Lakehouse simulates a modern SaaS data platform where customer growth is driven by platform consumption.

The project transforms raw customer, subscription and compute usage data into business-ready analytics tables using a modern Lakehouse architecture.

---

## Objectives

This project was built to learn and demonstrate:

- Databricks
- PySpark
- Delta Lake
- Medallion Architecture
- Consumption-based SaaS analytics
- Business-oriented data engineering

---

## Business Context

Modern SaaS platforms increasingly rely on usage-based revenue models.

Understanding platform consumption is critical to:

- identify expansion opportunities
- detect under-utilization
- measure customer adoption
- estimate churn risk
- analyze revenue growth

---

## Architecture

The project follows the Medallion Architecture:

- Bronze → raw ingestion
- Silver → cleaned and standardized data
- Gold → business-ready analytics

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
│
├── notebooks/
│
├── screenshots/
│
├── README.md
└── .gitignore
```

---

## Planned Business Outputs

The project will generate Gold-level business tables for:

- customer consumption metrics
- customer adoption scoring
- expansion revenue analysis
- churn and under-utilization risk

---

## Learning Goals

The objective is not only to build a technical pipeline, but also to understand:

- how modern Lakehouse platforms work
- how consumption-based SaaS businesses operate
- how data engineering supports business analytics
- how PySpark and Delta Lake are used in real-world architectures