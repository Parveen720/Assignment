import numpy as np

arr1=np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
arr2=np.array([9,-6,17])

#using inverse

arr1_1=np.linalg.inv(arr1)
res=np.dot(arr1_1,arr2)
print(res)


