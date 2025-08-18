# Create a heatmap with seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Iris.csv")
data = pd.DataFrame(data=data)
del data["Species"]
print(data)

# Calculate corelation matrix
corelation_matrix = data.corr()

# PLot heatmap
sns.heatmap(corelation_matrix,annot=True,cmap="coolwarm")
plt.title("Corelation Heatmap")
plt.show()