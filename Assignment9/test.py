import pandas as pd
import numpy as np

#for column=column.sort() for row=sort_index()

data={'Name':['ABC','zyx','PQR'],'age':[70,85,34]}
df=pd.DataFrame(data)
print(df)

res=df.sort_values(by='age')
print(res)
print(df)