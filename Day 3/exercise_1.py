# Load and explore a sample datasets
import pandas as pd

data = pd.read_csv("Iris.csv")
print(data)

print(data.head(5))
print(data.tail(5))

print(data.info())
print(data.describe())

