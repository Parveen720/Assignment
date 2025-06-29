import numpy as np

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)

#maximum value
print(arr.max())
#minimum value
print(arr.min())

#number of rows and column in array
print("(Row,Column) = ",arr.shape)

#select a specific elment in array
print(arr[0][1])

print(arr[0:2:1,0:5:1])

#sum of values in 2 D array

sum1=0
for x in arr:
    for y in x:
        sum1=sum1+y
print(sum1)

print(arr.sum())

#another method
sum2=0
for x in np.nditer(arr):
    sum2+=x
print(sum2)

#addition,substraction,division, array
print(arr)
print(arr+2)
#substraction
print(arr-2)
#divisiom
print(arr/2)
