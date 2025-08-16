import pandas as pd
data = pd.read_csv("accounts.csv")

df = pd.DataFrame(data=data)
print(df)

grouped = df.groupby("sales_rep_id").agg(
    {"lat":["mean","max","min",],
     "long":["mean","max","min"]
     }
)
print("Grouped by:\n",grouped)

