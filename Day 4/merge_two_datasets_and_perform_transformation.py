import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID":[1,2,3,4],
    "Name":["Nitin","Anurag","Rituraj","Sagar"],
    "Age":[22,25,24,25]
})

df2 = pd.DataFrame({
    "ID":[1,2,3,4],
    "Score":[80,85,75,78]

})

print("First Dataset \n",df1)
print("Second Dataset \n",df2)

# Merged the dataset

merged_datset = pd.merge(df1,df2,how="inner",on="ID")
print("Merged Dataset\n",merged_datset)

merged_datset["Score_Percentage"]= (merged_datset["Score"]/100)*100
print("Transformed Dataset\n",merged_datset)