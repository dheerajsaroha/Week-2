# Create a dataframe from a dictionary and add a new calculated column
import pandas as pd
data = {"Name":["Arun","Sachin","Dheeraj","Nitin","Anurag","Ashish","Amit","Bhanu"],"Age":[27,24,22,22,25,23,25,22],"Address":["Samalkha","Gurugram","Hisar","Gurugram","Gurugram","Panipat","Samalkha","Panipat"]}
print(data)
print(type(data))
df = pd.DataFrame.from_dict(data)
print(type(df))

filtered_data = df[(df["Address"]=="Gurugram")|(df["Address"]== "Panipat")]
print("Filtered Data\n",filtered_data)

df['Job_Field'] = ["Electrical","IT Sector","IT Sector","IT Sector","Accounting","SalesMan","Farmer","Medical"]

print(df)

