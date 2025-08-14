import pandas as pd
# Series is one dimensional labeled array ability to store any type of data with better computational efficiency
s= pd.Series([10,20,30],index=["a","b","c"])
print(s)

# Dataframe in data structure provide two dimensional data or we can say that data will be in tabular form
data = pd.DataFrame({"name":["Anmol","Amit"],"age":[23,26]})
print(data)

data = pd.read_csv("machine-readable-business-employment-data-mar-2025-quarter.csv")
print(data)

print(data.head())
print(data.tail())
print(data.info())
print(data.describe())

print(data[data["Series_title_3"] == "Actual"])

