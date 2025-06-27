import csv

import pandas as pd

df=pd.read_csv('annual.csv')
# print(df.to_string())

#print first 10 line of head
print(df.head(10).to_string())
#print 10 tail line of data
print(df.tail(10).to_string())
#to print all the columns of the data
print(df.columns)
#print the shape of the data
print(df.shape)

print(df.describe())

# print(df.info)
print(df.columns)

print(df['Variable_name'])
#filter data on condition
print(df['Variable_code']<'H20')