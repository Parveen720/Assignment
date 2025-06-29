#reverse a numpy array
import numpy as np

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)

#reverse

print(arr[::-1,::-1])
#reverse 2-D array
print(np.flip(arr))

#flipping in each columns in row without flipping the row
print(np.flip(arr,axis=1))