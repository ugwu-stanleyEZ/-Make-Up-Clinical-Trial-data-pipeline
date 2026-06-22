#now that im done cleaning my data in python ill be visualizing it here
#before i start plotting ill let R confirm that it sees the data in exactly the way it was saved on python, ill do that using tidyverse and (glimpse)

library(tidyverse)
#loading the cleaned data file in R
clean_patient_log<- read_csv("clean_patient_logs.csv")
#now to ensure i have the data tupe and bloodpressure  double/numeric type
glimpse(clean_patient_log)

#now that im done cleaning my data in python ill be visualizing it here
#before i start plotting ill let R confirm that it sees the data in exactly the way it was saved on python, ill do that using tidyverse and (glimpse)

library(tidyverse)
#set the plot width and heigth (in inches)
options(repr.plot.width = 6, repr.plot.height =4)

#loading the cleaned data file in R
clean_patient_log<- read_csv("clean_patient_logs.csv")
#now to ensure i have the data tupe and bloodpressure  double/numeric type
#glimpse(clean_patient_log)

#now that ive checked my data type and everything looks ggod on R, ill start plotting using "ggplot". my preffeerd graph for this plot
#is boxplot
ggplot(
    clean_patient_log, aes(x=Treatment_Group, y=Blood_Pressure_mmHg))+
    geom_boxplot(aes(fill=Treatment_Group), alpha=0.7)+
    geom_jitter(width=0.1, size=2)+ theme_minimal()+ 
    #now ill include the graph labels
    labs(title="Patient Blood Pressure Across Treatment Groups",
        x="Treatment Group",
        y="Blood Pressure (mmHg)")

  
    

#ill be creating another graph, this time around a scatter plot, here i can visually prove if blood presure climbs as the patients get older

ggplot(
    clean_patient_log, aes(x=Age, y=Blood_Pressure_mmHg))+
    geom_point(aes(color=Treatment_Group), size=3  )+
    geom_smooth(method="lm", se=FALSE, color="black" )+ 
    theme_bw()+
    labs(
        title="Correlation Between Patient Age and Blood Pressure",
        x="Patient Age (Years)",
        y="Blood Pressure (mmHg)"
    )

#finally ill be ploting a visualization to determine if biological sex alter the drugs impact
options(repr.plot.width = 6, repr.plot.height =4)

#ill be using facet_wrap to split my graph into groups
ggplot(
    clean_patient_log, aes(x=Age, y=Blood_Pressure_mmHg))+
    geom_point(aes(color=Treatment_Group), size=4  )+
    geom_smooth(method="lm", se=FALSE, color="black", size=0.8 )+
    facet_wrap(~Gender)+ 
    theme_grey()+
    theme(
        plot.background=element_rect(fill="#f0f0f0", color=NA),
        panel.background=element_rect(fill="#e0e0e0", color=NA)   
    )+
    labs(
        title=" Blood Pressure Trends splits by Biological Sex",
        subtitle="Analyzing Age and Treatment Interaction amomg Genders",  
        x="Patient Age (Years)",
        y="Blood Pressure (mmHg)"
    )


