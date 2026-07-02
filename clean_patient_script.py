#!/usr/bin/env python
# coding: utf-8

# In[3]:


#ill be working on this makeup project, we have a clinical dataset of messy patient data logs,
#this scrpit cleans raw messy patient data using python and saves cleaned text files in csv format
#the structural flaws i am to fix in this data file is: 1. the seperator(|), 2. the gender incosistensies, 3. the blood pressure group strings and 4. the missing values

#ill import pandas as pd
import pandas as pd 
#now ill load the raw data file and tell panda that it uses (|) as a seperator so my output comes up as a table format
#the df is used in panda
df=pd.read_csv("raw_patient_logs.txt", sep="|")

#check for duplicate patient and store them in a seperate csv file
duplicate_rows=df[df.duplicated(subset=["Patient_ID"], keep="first")]
if not duplicate_rows.empty:
    duplicate_rows.to_csv("duplicate_p_rows.csv", index=False)
    print(f"Warning: {len(duplicate_rows)} duplicate rows found. saved to duplicate_p_rows.csv")
df=df.drop_duplicates(subset=["Patient_ID"], keep="first")    

# i work on the gender inconsistensies(M,uppercase etc), ill be using dictonaries
#normalize case/whitespaces first so the map only needs simple lowercase keys
df["Gender"]=df["Gender"].astype(str).str.strip().str.lower()

gender_map={
    "male": "Male", "m": "Male",  
    "female": "Female", "f": "Female",  
}
df["Gender"]=df["Gender"].map(gender_map)

#catch any values that didnt match the map(typos, unexpected labels) instead of losing them silently
#for this dataset , no rows are expected to fail here, this is a safety net for future/reused data
unmapped_gender= df[df["Gender"].isna()]
if not unmapped_gender.empty:
    unmapped_gender.to_csv("unmapped_gender_rows.csv", index=False)
    print(f"Warning: {len(unmapped_gender)} rows had unrecognised gender values. saved to unmapped_gender.csv   ")
df=df.dropna(subset=["Gender"])    

#convert the blood presure values into actual values that python and r can read\calc   
#ill use the "replace ", method and .astype(str) to convert that column to a text so we can replace the"mmhg" and "missing" text
#if all our number\value in that column has the text "mmHg" then we will not use the .astype(str) method to convert 
df["Blood_Pressure_mmHg"]=(
    df["Blood_Pressure_mmHg"]
    .astype(str)     
    .str.replace("mmHg", "", case=False)     
    .str.strip()
)


#saving rows that are marked "missing"
missing_patients=df[df["Blood_Pressure_mmHg"].str.lower()=="missing"]      
missing_patients.to_csv("missing_p_row.csv", index=False)
df["Blood_Pressure_mmHg"]=df["Blood_Pressure_mmHg"].str.lower()    
df=df[df["Blood_Pressure_mmHg"]!="missing"] 

# fixing "missing" text in the blood pressure column,  by converting it to nan(number/numeric), that way Py  will remove the pt 8 section cause  R cant read it.

df["Blood_Pressure_mmHg"]=pd.to_numeric(df["Blood_Pressure_mmHg"], errors="coerce") 
df =df.dropna(subset=["Blood_Pressure_mmHg"])

#fixing Age column, converting age to numeric and storing missing age it into a csv file
df["Age"] = pd.to_numeric(df["Age"], errors = "coerce")
missing_age=df[df["Age"].isna()]
if not missing_age.empty:
    missing_age.to_csv("missing_age_rows.csv", index=False)
    print(f"Warning: {len(missing_age)} rows had unrecognised gender values. saved to unmapped_gender.csv   ")
df=df.dropna(subset=["Age"])   

#finnaly save the clean data to csv file format for R visualixation
df.to_csv("clean_p_logs.csv", index=False)  
print("success: clean_patient_logs has been built and saved.")
print("success: missing_p_row has been built and saved.")
if not unmapped_gender.empty:
    print("success: unmapped_gender_rows.csv has been built and saved")
if not missing_age.empty:
    print("success: missing_age_rows.csv has been built and saved") 
if not duplicate_rows.empty:  
    print("success: duplicate_p_rows.csv has been built and saved") 


df     


