# -Make-Up-Clinical-Trial-data-pipeline
This project includes an automated Python pipeline to clean messy clinical logs and using R ggplot2 visualization engine to analyze drug trial trends
## Data Pipeline Architecture
1. Cleaning & Quality control (Python/Pandas):
 - Standardized uneven patient string keys, (Pt-01 and Pt-02).
 - Handled corrupted case formatting and isolated incomplete records.
 - Saved the clean uniformed outputs

2. Visualization & Reporting (R/ggplot2):
 - implemented box plot graph(geom_boxplot) split by Treatment_Group to see if the average blood pressure drops for patients taking Drug A & B compared to patients     on Placebo
 - implemented scatter plot with linear modelling trends(geom_smooth) to show if the drug loses control/efficacy as pateint gets older


 3. Patient Directory Breaakdown
 - raw_ptient_logs.txt: uncleaned initial text file logs from clinical database entries
 - clean_patient_logs.py: cleaned automated python script and logic
 - clean_patient_csv: finalized comma sepperated structured dataset
 - patient_logs_visulization.R: R code housing the plotting engine and visualization.         
