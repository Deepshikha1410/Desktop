#use the titanic-tested.csv dataset.find out tthe number of nulls in each columns. replace nulls in the age column with the average age. find how many male and female records exist in the dataset. 
import pandas as pd
import numpy as np

df = pd.read_csv('titanic-tested.csv')

# Find the number of nulls in each column
print(df.isnull().sum())

# Replace nulls in the age column with the average age
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Find how many male and female records exist in the dataset
print(df['Sex'].value_counts())
