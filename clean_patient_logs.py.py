#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ill be working on this makeup project, we have a clinical dataset of messy patient data logs,
#ill be cleaning it using python and saving cleaned text files in csv format
#the structural flaws i am to fix in this data file is: 1. the seperator(|), 2. the gender incosistensies, 3. the blood pressure group strings and 4. the missing values
# 

#now lets get work,
#ill import pandas as pd
import pandas as pd 
#now ill load the raw data file and tell panda that it uses (|) as a seperator so my output comes up as a table format
#the df is used in panda
df=pd.read_csv("raw_patient_logs.txt", sep="|") 

#next ill work on the gender inconsistensies(M,uppercase etc), ill be using dictonaries
gender_map={
    "Male":"Male", "male":"Male", "M":"Male",
    "Female":"Female", "female":"Female",  
}
df["Gender"]=df["Gender"].map(gender_map)

#now that the inconsistensies have been fixed, ill convert the blood presure values into actual values that python and r can read\calc
#ill use the "replace ", method and .astype(str) to convert that column to a text so we can replace the"mmhg" and "missing" text
#if all our number\value in that column has the text "mmHg" then we will not use the .astype(str) method to convert 
df["Blood_Pressure_mmHg"]=df["Blood_Pressure_mmHg"].astype(str).str.replace("mmHg", "", case=False)  

#now i fix the "missing" text in the blood pressure colume, by converting it to nan(number), that way py  will remove the pt 8 section cause  r cant read it.
#I will to store that "missing" blood_pressure_mmHg column in a diff text file for future reference  
missing_patients=df[df["Blood_Pressure_mmHg"]=="missing"]   
missing_patients.to_csv("missing_patient_rep.csv", index=False)
df=df[df["Blood_Pressure_mmHg"]!="missing"]
df["Blood_Pressure_mmHg"]=pd.to_numeric(df["Blood_Pressure_mmHg"]) 
df =df.dropna(subset=["Blood_Pressure_mmHg"]) 

#finnaly ill save the clean data to csv file format for r visualixation
df.to_csv("clean_patient_logs.csv", index=False)
print("success: clean_patient_logs has been built and saved.")
print("success: missing_patient_logs has been built and saved.")

df     



# In[ ]:




