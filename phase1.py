import numpy as np

arr_1d = np.array([1,2,3,4,5])
print("1D array : ",arr_1d)

arr_2d = np.array([ [1,2,3], [4,5,6] ])
print("2D array : ",arr_2d) 

# list vs numpy array
py_list = [1,2,3]
print("python list multiplication : ", py_list * 2)

np_array = np.array([1,2,3]) #element wise multiplication
print("python array multiplication ",np_array * 2)

import time
start = time.time()
py_list = [i*2 for i in range (1000000)]
print("list operation time : ",time.time() - start)

start = time.time()
np_array = np.array(1000000) * 2
print("numpy operation time : ",time.time() - start)

# creating array from scratch
zeros = np.zeros((3,4))
print("zeros array: \n",zeros)

ones = np.ones((2,3))
print("ones aray: \n",ones)

full = np.full((2,2),7)
print("full array: \n",full)

random = np.random.random((2,3))
print("random array: \n", random)

sequence = np.arange(0,10,2) #non inclusive outer boundary = n-1 (10-1=9)
print("sequence array : \n",sequence)

# vector,matrix and tensor

vector = np.array([1,2,3])
print("vector : ", vector)

matrix = np.array([[1,2,3],[4,5,6]])
print("matrix: ", matrix)

# tensor have more dimension
tensor = np.array([[[1,2], [3,4]],
                   [[5,6], [7,8]]])
print("tensor: ",tensor)

# array properties 
arr = np.array([[1,2,3],
                [4,5,6]])
print("shape : ", arr.shape)
print("dimension ",arr.ndim)
print("size: ",arr.size)
print("datatype: ",arr.dtype)

# array reshaping
array = np.arange(12)
print("original array : ",array)

reshaped = arr.reshape((2, 3))
print("reshaped array: ",reshaped)

flattened = reshaped.flatten()
print("flattened array: ",flattened)

# ravel (return view (original), instead of copy)
raveled = reshaped.ravel()
print("\n raveled array: ",raveled)

# transpose
transpose = reshaped.T
print("\n transposed array: ",transpose)

