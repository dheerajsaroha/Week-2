# Exercise:- Clean a dataset by Handling missing values and renaming columns
import pandas as pd
import numpy as np
data = {
    "Name":["Alice","Bob","Catelin",np.nan,"David"],
    "Age":[25,np.nan,28,24,30],
    "Score":[85,90,np.nan,80,np.nan]
}
df = pd.DataFrame(data)
print("Original Datasets",df)

# Fill the missing value
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

print(df)

df = df.rename(columns={"Name":"Student_Name","Score":"Exam_Score"})
print(df)

df=df.dropna()
print(df)


