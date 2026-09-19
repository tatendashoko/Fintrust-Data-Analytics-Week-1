# FinTrust Digital Bank — Week 1 (Data Analytics Track)

AnalystLab Africa Data Analytics

## What this repo contains

| Path | Contents |
|---|---|
| `submission/` | The Week 1 write-up (Business Understanding, Data Understanding, Analytical Questions, KPI Table, Dashboard Wireframe) |
| `scripts/data_profiling.py` | The script that produced every number in the Data Understanding section (row counts, missing values, duplicates, cross-tabs) |
| `data/` | The two source CSVs supplied for the project (see note below) |

## How to reproduce the numbers

```bash
pip install pandas
python scripts/data_profiling.py
```

This prints the shape, data types, missing-value counts, duplicate checks,
categorical breakdowns, numeric summary statistics, date range, and the
risk-rate cross-tabs referenced in the submission. No data is modified —
this is a read-only profiling pass, in line with the Week 1 brief (clean
in Week 2, not now).

## Status

Week 1 of 4 — business and data understanding, plus planning. No dashboard
build or data cleaning yet; both are scoped for Week 2 onward.
