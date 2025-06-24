#two dimansional list
import pandas as pd

list1=[['1','2','3'],['apple','mango','banana'],
    ['parveen','riya','yadav']]

df=pd.DataFrame(list1,index=['col1','col2','col3'])
print(df)

#dataframe from python dictionary

dic1={
    'name':['parveen','riya','yadav'],
    'fruits':['mango','apple','banana'],
    'number':[1,2,3]
}
df=pd.DataFrame(dic1,index=['col1','col2','col3'])
print(df)

#list of tuples

list_of_tuple=[('*','*','*'),('*','*','*'),('*','*','*')]

df=pd.DataFrame(list_of_tuple)
print(df)

#list of dictionary

list_of_dic=[
    {1:'parveen',2:'riya',3:'hemant'},
    {4:'himanshu',5:'heamng',6:'mohanish'},
    {7:'abhishek',8:'lakshay',9:'ashive'}
]
df=pd.DataFrame(list_of_dic)
print(df)
#where no value in id it give NAN


