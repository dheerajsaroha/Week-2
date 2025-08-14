# Select specific columns and Filter rows
import pandas as pd

data = pd.read_csv("Iris.csv")
print(data[data["Species"]=="Iris-setosa"])
print(data.loc[:,"Species"])
print(data.iloc[:,0])

selected_columns =data[["Species","SepalLengthCm","PetalLengthCm"]]
print("Selected Columns:\n",selected_columns)

# Filter the rows
filtered_rows = data[(data["SepalLengthCm"] > 5.0)&(data["PetalLengthCm"] > 1.5) & (data["Species"] == "Iris-setosa")]
print("Filtered Rows\n",filtered_rows)