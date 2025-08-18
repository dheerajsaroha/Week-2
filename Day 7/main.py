# Exploratory Data Analysis

# Step 1: Applying Data Manipulation and Data Visualization for EDA
# Task - 1: Perform data cleaning,Aggregation and Filtering
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

# inspect data
print(df.info())
print(df.describe())

# Handle missing value
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# remove duplicates
df = df.drop_duplicates()

# Filter Data : Passenger in first class
first_class =df[df["Pclass"] == 1]
print("First Class Passenger :\n",first_class.head())

# Task 2: Generate visualizations illustrate key insights

# # Bar chart : Survival Rate by class
# survival_by_class = df.groupby("Pclass")["Survived"].mean()
# survival_by_class.plot(kind="bar",color="skyblue")
# plt.title( "Survival Rate by class")
# plt.ylabel("Survival Rate")
# plt.show()

# # Histogram for Age distributiion
# sns.histplot(df["Age"],kde=True,bins = 20,color="purple")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# ScatterPlot
plt.scatter(df["Age"],df["Fare"],alpha=0.5,color = "green")
plt. title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()