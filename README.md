# -Make-Up-Clinical-Trial-data-pipeline
This project includes an automated Python pipeline to clean messy clinical logs using Python(Pandas) and using R ggplot2 visualization engine to analyze drug trial trends

## 📌 Project Overview & The Challenge
In clinical trials, data integrity is everything. Missing data points, incorrectly formatted patient logs, and edge-case age inputs can skew efficacy reporting and delay regulatory approvals. 

This project simulates a realistic data-cleaning pipeline that isolates corrupted patient rows, fixes data anomalies, and provides a polished analytical report on patient responses to experimental drug treatments.

### Key Objectives:
*   **Data Quality Assurance:** Programmatically identify and isolate rows missing critical age records or general patient demographics.
*   **Pipeline Automation:** Build a reproducible Python script using Pandas to transform raw text files into clean Excel reports.
*   **Exploratory Data Analysis (EDA):** Use R's `ggplot2` engine to visually track distribution patterns, patient responses, and trial compliance trends.

## 🛠️ Data Pipeline Architecture

1.  **Ingestion:** Reads the unformatted, raw data file (`raw_patient_logs.txt`).
2.  **Validation & Quality Control:** 
    *   Filters out rows missing crucial demographics and outputs them to `missing_p_row.xls`.
    *   Flags and extracts rows with invalid/missing age inputs to `missing_age_rows.xls`.
3.  **Transformation:** Cleans types, normalizes string data, and structures the records into a finalized, production-ready dataset (`clean_p_log.xls`).
4.  **Analytics & Visualization:** Feeds the clean dataset into `Patient_logs_visualization` via R to map out key drug trial trends.


## 📁 Repository Directory Structure
📁 Make-Up-Clinical-Trial-data-pipeline/
│
├── 📁 images/
│   
│
├── 📁 data/
│   ├── 📄 raw_patient_logs.txt
│   ├── 📁 cleaned/
│   │   └──  Excel clean_p_log.xls
│   └── 📁 errors/
│       ├── 📑 missing_age_rows.xls
│       └── 📑 missing_p_row.xls
│
├── 🐍 clean_patient_script.py
├── 📊 Patient_logs_visualization.R
└── 📝 README.md


## 📊 Analytics & Key Findings

> **Note:** Below are the visualizations highlights generated during the exploratory phase of the clean dataset.

### 1. Clinical Drugs Efficacy
implemented box plot graph(geom_boxplot) split by Treatment_Group to see if the average blood pressure drops for patients taking Drug A & B compared to patients     on Placebo

#### Visualizing the Demographic Spread:
![Patient Age Distribution](images/age_distribution.png) 
*(How to add this: Create a folder named `images` in your repository, upload your plot image as `age_distribution.png`, and this link will display it automatically!)*

### 2. Patient Distribution and Demographics
*   *Insert your analytical observation here. e.g., "After cleaning the text discrepancies, the R analysis revealed a distinct, positive trend in recovery speed for the primary trial group relative to the control group."*

#### Visualizing the Drug Trial Performance:
![Trial Trends Plot](images/trial_trends.png)



# 🔬 Make-Up Clinical Trial Data Pipeline & Analytics

[![Python](https://img.shields.io/badge/Python-3.8+-blue.Automated)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Library-Pandas-orange)](https://pandas.pydata.org)
[![R](https://img.shields.io/badge/R-ggplot2-blue)](https://ggplot2.tidyverse.org)

An end-to-end data engineering and analytics pipeline built to handle, clean, and visualize messy, real-world clinical drug trial logs. This project takes raw, unformatted patient logs, transforms them into high-quality clinical data datasets, and uncovers actionable insights on drug trial trends.




## 🚀 How To Run the Pipeline Locally

### Prerequisites
Make sure you have both Python (with Pandas) and R installed on your local environment.

### Step 1: Run the Cleaning Pipeline
Execute the Python script to clean the raw logs and generate the isolated error logs and final clean file.
```bash
python clean_patient_script.py

