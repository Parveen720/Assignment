import numpy as np

arr=np.array([[1,-2,3],[4,-2,-3],[-2,9,-20]])

arr[arr<0]=0
print(arr)

#or another method
arr=np.where(arr<0,0,arr)
print(arr)

#Question 6
#create a nupy 1-d array

arr1=np.array([3,4])
arr2=np.array([1,0])
arr=np.concatenate((arr1,arr2),axis=0)
new=arr.flatten()
print(new)
sum1=np.sum(arr1)
sum2=np.sum(arr2)
avg=(sum1+sum2)/2
print(avg)
print(np.mean(new))
print(np.median(new))

