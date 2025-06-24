import pandas as pd

list_of_tuple=[(1,2,3),
               (4,5,6),
               (7,8,9)
               ]
df=pd.DataFrame(list_of_tuple)
print(df)
#iterate through dataframes

for idx,row in df.iterrows():
    print(idx,row[1],row[2])


for row in df.itertuples():
    print(row)

#selecting rows on based of condition

res=df[df[0]!=4]  #col index and remove row
print(res)

#selecting any row using iloc
res=df.iloc[0]
print(res)

#limited row selection with given column
res=df.iloc[0:1,1:3]
print(res)

#drop row on the basis of given condition
res=df[df[0]!=4]
print(res)
#insertion row at given position

#row converted into list
res=df[0].tolist()
print(res)