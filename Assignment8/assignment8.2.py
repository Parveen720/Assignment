#2-D matrix
import numpy as np

arr_2d=np.arange(2,11).reshape(3,3)
print(arr_2d)

#by split method
arr = np.arange(2, 11)
matrix = np.array(np.split(arr, 3))

print("3x3 Matrix:")
print(matrix)
