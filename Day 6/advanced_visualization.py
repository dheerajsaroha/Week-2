import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.rand(5,5)
df = pd.DataFrame({
    "Grade":["A","B","C","D"],
    "score":[90,80,70,50]
})

# sns.heatmap(data,annot=True,cmap="coolwarm")
# plt.title("Heatmap")


sns.pairplot(df)
plt.title("PairPlot")
plt.show()