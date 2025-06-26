import pandas as pd

df1=pd.DataFrame({
     'ID':[1,2,3,4],
     'name':['A1','A2','A3','A4'],
     'subject':['sub2','sub3','sub4','sub6'],
    'Marks':[90,100,30,50],
    },index=[1,2,3,4])

df2=pd.DataFrame({
     'ID':[2,3,4,5],
     'name':['B1','B2','B3','B4'],
     'subject':['sub1','sub3','sub2','sub6'],
    'Marks':[100,30,90,50],
    },index=[1,2,3,4])

Inner_merge=df1.merge(df2,on="Marks")
print(Inner_merge)

#perform left join on df1 and df2 based on id

left_join=df1.merge(df2,how='left',on='ID')
print(left_join)



#right jon using pd.merge
right_merge=df1.merge(df2,on="ID",how="right")
print(right_merge)

#jon based on indexes

join1=df1.join(df2,lsuffix='_l',rsuffix='_r')
print(join1)
