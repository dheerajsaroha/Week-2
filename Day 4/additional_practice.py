# Drop columns with more than 50% missingvalues

import pandas as pd

# Create a sample DataFrame with missing values
data = {'A': [1, 2, None, 4, 5],
        'B': [None, None, None, 4, 5],
        'C': [1, 2, 3, 4, None],
        'D': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Calculate the percentage of missing values for each column
missing_percentage = df.isnull().mean()
print("Missing Percentage",missing_percentage)

# Identify columns with more than 50% missing values
columns_to_drop = missing_percentage[missing_percentage > 0.5].index

# Drop the identified columns
df_cleaned = df.drop(columns=columns_to_drop)

print("Original DataFrame:")
print(df)
print("\nCleaned DataFrame (columns with >50% missing values dropped):")
print(df_cleaned)

# Merge three datasets and analyze relationships b/w them
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
         'Mobile No': [97, 91, 58, 76]}

data2 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
         'Age': [22, 32, 12, 52],
         'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
         'Salary': [1000, 2000, 3000, 4000]}

# df = pd.DataFrame(data1,index=[0,1,2,3])
# df1 = pd.DataFrame(data2,index=[2,3,6,7])
df= pd.DataFrame(data1,index=[0,1,2,3])
df1 = pd.DataFrame(data2,index=[2,3,4,5])
print(df,"\n\n",df1)
concat_dataset = pd.concat([df,df1],join="inner")
print("\n",concat_dataset)


