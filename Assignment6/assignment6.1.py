import pandas as pd

df=pd.DataFrame({
    'col1':range(6),
    'col2':['A','A','B','B','C','C'],
    'date':pd.to_datetime(["22-07-2025","23-07-2025"]*3)
})

print(df)
res=df.pivot(index="date",columns="col2",values="col1")
print(res)

dates = ["2025-06-25","2025-06-24","2025-06-23","2025-06-22"]
s = pd.Series(dates)
s = pd.to_datetime(s)
print(s)