from wsgiref.util import request_uri

import pandas as pd
import numpy as np
# from pandas.conftest import axis_1

#3-D array
#first axis=depth
#seccond axis=row

arr=np.array([[[1,2,3],[3,4,5]],[[3,4,5],[6,7,8]]])
print(arr)
#creating an indexing
print(arr.shape)
#it gives set,row and column in 3d array

element=arr[0,1,2]
print(element)

print (arr[0:,1:,0:])
print(arr[0:1:1,1:2:1,0:1:1])

x=np.zeros((2,3,4))
# print(x)
x[1,2,3]=11
# print(x)

#cahnge in view change  the original data but chnage in copy data do'not affect the original data

arr=np.array([1,2,3,4,5])
x=arr.copy()
print(x)
x[3]=11
print(x)
print(arr)

#view
x=arr.view()
x[2]=100
print(x)
print(arr)

x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)
arr=np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)

#to change the dimension of the array
#base basically give the original array from which it will form
#ndmin to create dimension
arr=np.array([[1,2,3,4,5],[2,3,4,5,6]],ndmin=4)
print(arr)

arr=np.array([[1,2,3,4,5,6],[1,2,3,4,5,7]])
arr1=arr.reshape(2,3,2)
print(arr1)
#converting array to one dimension
new_array=arr1.reshape(-1)
print(new_array)

#iterate over array
#1D array
arr=np.array([1,2,3,4,5])
for x in arr:
    print(x,end=" ")
print()
arr=np.array([[1,2,3,4],[2,3,4,5]])
for x in arr:
    print(x)
    for y in x:
        print(y,end=" ")


arr=np.array([[[11,12,13],[12,13,14]],[[12,13,14],[13,14,15]]])
print(arr)
for x in arr:
    print(x)
    for y in x:
        print(y,end=" ")
        for z in y:
            print(z,end=" ")


#nditer used to print elment of array

for x in np.nditer(arr):
    print(x,end=" ")
print()
a=np.array([[12,32,43,53],[32,32,12,32],[54,65,32,53]],dtype="f")
print(a)
print(a.reshape(6,2))
#converting array in 1d using ravel()

print(a.ravel())

#unique element in the array

print(np.unique(a))

#minimum and maximum value in the array
print(a.min(),a.max())

print(a.sum())

print(a.sum(0))

#to find standard devaiartion

print(np.std(a))

#to find square root of the elment
print(np.sqrt(a))
print(a)

#operation on two numpy array
a=np.array([[1,2,3],[2,3,4]])
b=np.array([[3,1,5],[4,6,7]])
print(a+b)
print(a*b)
# try:
#     print(a/b)
# except ZeroDivisionError:
# #     print("error")
# # x=a.dot(b)
# # print(x)

#other operations
#increase pad with betwwn elment
padding_array=np.pad(a,pad_width=2,mode='constant')
print(padding_array)

transpose_array=np.transpose(a)
print(transpose_array)

a=np.array([[1,2,3],[2,3,4]])
b=np.array([[3,1,5],[4,6,7]])
result=np.concat((a,b))
print(result)

result=np.concatenate((a,b),axis=1)
print(result)

#split array in multiple arrays

result=np.split(a,1)
print(result)


#adding and removing elments
res=np.resize(a,(3,2))
print(res)

b=np.resize(a,(3,3))
print(b)

#append the values
# print(np.append(a,[[7,8,9]],axis=0))

print(np.insert(a,3,[11,12]))

#index se phle append kar dega original array m

print(np.delete(a,5))

#rearranging elements

a=np.arange(12).reshape(3,4)
print(a)
#rearanging elments

#flip()
a=np.array([[1,4,3],[2,3,9]])
res=np.flip(a,axis=0)
print(res)

# res=np.sort(a)
# print(res)

#argmax() return index of maximum values
max_index=np.argmax(a,axis=1)
print(max_index)
arr=np.arange(12)
print(arr[::-1])


result=np.split(a,1)
print(result)






