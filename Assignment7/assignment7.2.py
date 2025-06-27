import pandas as pd

data_series=pd.to_datetime(['2023-01-01','2023-06-15','2023-12-31'])
print(data_series)

#allow to extract parts of date
df=pd.DataFrame({
    'date':pd.to_datetime(['2023-01-01','2023-06-15','2023-12-31'])
})
df['year']=df['date'].dt.year
df['month']=df['date'].dt.month
df['weekday']=df['date'].dt.day_name()
print(df)
#to generate a range
rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
print(rng)

#pd.timestamp

ts=pd.Timestamp('2023-01-31 15:30')
print(ts)

ts=pd.Series([1,2,3,4],index=pd.date_range('2023-01-01',periods=4,freq='D'))
ts.resample('2D').sum()
print(ts)
