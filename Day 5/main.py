# Grouping data by categories using pandas
import pandas as pd
data = {
    "Class":["A","B","A","B","C","C"],
    "Score":[90,85,93,84,72,74],
    "Age":[15,16,15,17,16,15]
}

df = pd.DataFrame(data=data)
print("Original Dataset \n",df)

grouped = df.groupby("Class").mean()
print(grouped)

