import pandas as pd

dataframe1 = pd.DataFrame({
    'ID':[100,101],
    'name': ['Parveen', 'Riya'],
    'marks': [99, 92]
})
dataframe2 = pd.DataFrame({
    'Id':[102,103],
    'name': ['Hemant', 'Hemang'],
    'marks': [99, 100]
})
dataframe3 = pd.DataFrame({
    'ID': [100,101,102,104],
    'Branch': ['CS', 'AI', 'IT', 'CIVIL']
})
#vertically concatination of dataframe 1 and dataframe 2
concat = pd.concat([dataframe1,dataframe2],keys=['x','y'],ignore_index=True)
print(concat)
#merge dataframe 3 with concat dataframe

merge_res=concat.merge(dataframe3,on="ID")
print(merge_res)

#join on dataframes

df=dataframe1.join(dataframe3,on="ID",lsuffix='_l',rsuffix='_r')
print(df)