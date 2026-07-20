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

   

2. Visualization & Reporting (R/ggplot2):
 - implemented box plot graph(geom_boxplot) split by Treatment_Group to see if the average blood pressure drops for patients taking Drug A & B compared to patients     on Placebo
 - implemented scatter plot with linear modelling trends(geom_smooth) to show if the drug loses control/efficacy as pateint gets older
 - implemnted demographic faceting (facet_wrap) to indentify if biological sex alter drugs impact

 3. Patient Directory Breaakdown
 - raw_ptient_logs.txt: uncleaned initial text file logs from clinical database entries
 - clean_patient_logs.py: cleaned automated python script and logic
 - clean_patient_csv: finalized comma sepperated structured dataset
 - patient_logs_visulization.R: R code housing the plotting engine and visualization.



# 🔬 Make-Up Clinical Trial Data Pipeline & Analytics

[![Python](https://img.shields.io/badge/Python-3.8+-blue.Automated)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Library-Pandas-orange)](https://pandas.pydata.org)
[![R](https://img.shields.io/badge/R-ggplot2-blue)](https://ggplot2.tidyverse.org)

An end-to-end data engineering and analytics pipeline built to handle, clean, and visualize messy, real-world clinical drug trial logs. This project takes raw, unformatted patient logs, transforms them into high-quality clinical data datasets, and uncovers actionable insights on drug trial trends.

---


---



---

## 📁 Repository Directory Structure

*   `raw_patient_logs.txt` — The initial messy data file directly from clinical entry logs.
*   `clean_patient_script.py` — The core automated Python cleaning script utilizing Pandas.
*   `clean_p_log.xls` — The resulting polished dataset used for downstream analysis.
*   `missing_age_rows.xls` & `missing_p_row.xls` — Isolated error reports generated for data auditing teams.
*   `Patient_logs_visualization...` — The R script containing the visualization engine.

---

## 📊 Analytics & Key Findings

> **Note:** Below are the visualizations and statistical highlights generated during the exploratory phase of the clean dataset.

### 1. Patient Distribution and Demographics
*   *Insert what you noticed here. e.g., "The data showed a heavy concentration of trial participants within the 25–40 age bracket, allowing us to accurately gauge side-effect trends among younger cohorts."*

#### Visualizing the Demographic Spread:
![Patient Age Distribution](images/age_distribution.png) 
*(How to add this: Create a folder named `images` in your repository, upload your plot image as `age_distribution.png`, and this link will display it automatically!)*

### 2. Clinical Efficacy and Treatment Trends
*   *Insert your analytical observation here. e.g., "After cleaning the text discrepancies, the R analysis revealed a distinct, positive trend in recovery speed for the primary trial group relative to the control group."*

#### Visualizing the Drug Trial Performance:
![Trial Trends Plot](images/trial_trends.png)

---

## 🚀 How To Run the Pipeline Locally

### Prerequisites
Make sure you have both Python (with Pandas) and R installed on your local environment.

### Step 1: Run the Cleaning Pipeline
Execute the Python script to clean the raw logs and generate the isolated error logs and final clean file.
```bash
python clean_patient_script.py

