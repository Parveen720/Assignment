#replace nan

import numpy as np

arr=np.array([[6,-8,73,-110],[np.nan,-8,0,94]])

np.nan_to_num(arr,nan=0,copy=False)
print(arr)

#cahnging 3 rows and columns

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr[:,[0,1,2]]=arr[:,[1,2,0]]
print(arr)

arr[[0,1,2],:]=arr[[2,1,0],:]
print(arr)



#Question 2 move axes of 3d array to new positions

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
move_axes=arr.transpose()
print(move_axes)

# Question 3 replace nan value with average of column

arr=np.array([[6,-8,np.nan,-110],[np.nan,-8,0,94]])

mean=np.nanmean(arr,axis=0)
nan_idx=np.where(np.isnan(arr))

arr[nan_idx]=mean[nan_idx[1]]

print(arr)
