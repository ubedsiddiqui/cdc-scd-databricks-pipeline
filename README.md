# cdc-scd-databricks-pipeline 

# 🔄 Real-Time CDC & SCD Pipeline with Databricks

## Overview
This project demonstrates how to handle **Change Data Capture (CDC)** and **Slowly Changing Dimensions (SCD Type 1 & 2)** in a real-time data pipeline using **Databricks Delta Live Tables (DLT)**.

## Pipeline Flow
1. **Landing Layer**: Ingest customer & account data as streaming tables.
2. **Bronze Layer**: Apply data quality checks & prepare raw data.
3. **Silver Layer**:  
   - `apply_changes` → SCD Type 1 & Type 2 for customer data  
   - `auto_cdc` → CDC for account data
4. **Gold Layer**: Provide history-tracked and current views for analytics.

## Outputs
- ✅ Real-time CDC applied to account transactions  
- ✅ SCD1 (overwrite) and SCD2 (historical tracking) on customer table  
- ✅ Dashboard with both active & historical records  


