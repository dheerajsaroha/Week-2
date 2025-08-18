import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3, 6)
# Lines Plot
years= [2010,2011,2012,2013]
sales=[100,120,150,135]
# plt.plot(years,sales,label="sales trend",color="blue",marker="o")
# plt.title("Line Plot")
# plt.show()
# Bar plot
categories = ["Clotthes","Electronics","Groceries"]
revenue = [250,400,200]
# plt.bar(categories,revenue,color="green")
# plt.title("Revenue by Category")
# plt.show()

# Scatter Plot
hour_studied=[1,2,3,4,5]
exam_scores=[50,55,65,70,85]
# plt.scatter(hour_studied,exam_scores,color = "red")
# plt.title("Studies hour vs Exam scores")
# plt.xlabel("Hour Studies")
# plt.ylabel("Exam Score")
# plt.show()

axs[0, 1].plot(years, sales)
axs[0, 1].set_title('Line Plot')
axs[2, 1].scatter(hour_studied, exam_scores)
axs[2, 1].set_title('Hour Studied vs Exam Score')

axs[1, 0].bar(categories,revenue)
axs[1, 0].set_title('Categories based Revenue')

plt.show()



