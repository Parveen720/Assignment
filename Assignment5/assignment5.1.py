import pandas as pd

dic={1:'A',2:'B',3:'C',4:'D',5:'E'}

df=pd.Series(dic)
print(df)

#creating a panda series from list

list1=[1,2,3,4,5,6]

myvar=pd.Series(list1)
print(myvar)
#give index which we want
myvar=pd.Series(list1,index=['a','b','c','d','e','f'])
print(myvar)

#Access the element in python series
print(myvar['a'])

print(myvar.iloc[0])
print(myvar.iloc[1:3])
# print(df[0])
# print(df[1])
print(myvar.iloc[[0,1,2]])
print(myvar.loc['a':'d'])


