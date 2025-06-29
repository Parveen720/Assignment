#combine a 1d and 2d array
import numpy as np

arr1=np.array([1,2,3,4,5])

arr2=np.array([[1,2,3,4,4],[6,7,8,9,10]])

num=np.concatenate((arr1.reshape(1,5),arr2))
print(num)
