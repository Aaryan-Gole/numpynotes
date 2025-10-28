# NumPy Full Reference Script with Comments
import numpy as np
import time
from numpy.linalg import inv, det

# ------------------ 1D and 2D Arrays ------------------
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D array : ", arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array : ", arr_2d)

# ------------------ Python List vs NumPy Array ------------------
py_list = [1, 2, 3]
print("Python list multiplication : ", py_list * 2)

np_array = np.array([1, 2, 3])
print("NumPy array multiplication : ", np_array * 2)

# ------------------ Performance Comparison ------------------
start = time.time()
py_list = [i * 2 for i in range(1000000)]
print("List operation time : ", time.time() - start)

start = time.time()
np_array = np.array([i for i in range(1000000)]) * 2
print("NumPy operation time : ", time.time() - start)

# ------------------ Creating Arrays from Scratch ------------------
zeros = np.zeros((3, 4))
print("Zeros array:\n", zeros)

ones = np.ones((2, 3))
print("Ones array:\n", ones)

full = np.full((2, 2), 7)
print("Full array:\n", full)

random = np.random.random((2, 3))
print("Random array:\n", random)

sequence = np.arange(0, 10, 2)
print("Sequence array:\n", sequence)

# ------------------ Vector, Matrix, and Tensor ------------------
vector = np.array([1, 2, 3])
print("Vector : ", vector)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix: \n", matrix)

tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Tensor: \n", tensor)

# ------------------ Array Properties ------------------
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape : ", arr.shape)
print("Dimensions : ", arr.ndim)
print("Size : ", arr.size)
print("Datatype : ", arr.dtype)

# ------------------ Array Reshaping ------------------
array = np.arange(12)
print("Original array : ", array)

reshaped = arr.reshape((2, 3))
print("Reshaped array: \n", reshaped)

flattened = reshaped.flatten()
print("Flattened array: ", flattened)

raveled = reshaped.ravel()
print("Raveled array: ", raveled)

transpose = reshaped.T
print("Transposed array: \n", transpose)

# ------------------ Boolean Masking / Filtering ------------------
data = np.array([1, 2, 3, 4, 5])
mask = data > 3
print("Boolean Masking : ", mask)
print("Filtered data (values > 3): ", data[mask])

# ------------------ Arithmetic Operations & Broadcasting ------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Addition : ", a + b)
print("Multiplication : ", a * b)
print("Broadcasting (a + 5) : ", a + 5)

# ------------------ Aggregation Functions ------------------
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Standard Deviation: ", np.std(arr))
print("Max along axis 0: ", np.max(arr, axis=0))

# ------------------ Slicing & Indexing ------------------
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("basic slicing: ", arr[2:7])
print("with step: ", arr[1:8:2])
print("negative indexing: ", arr[-3])

# ------------------ 2D Indexing ------------------
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("specific element: ", arr_2d[1,2])
print("entire row : ", arr_2d[2])

# ------------------ Sorting ------------------
unsorted = np.array([3,1,4,1,5,9,8,7])
print("sorted array: ", np.sort(unsorted))

arr_2d_unsort = np.array([[3,1], [1,2],[2,3]])
print("sorted 2d array by column : ", np.sort(arr_2d_unsort, axis=0))

# ------------------ Filtering with Mask ------------------
number = np.array([1,2,3,4,5,6,7,8,9,10])
even_number = number[number % 2 == 0]
print("even: ", even_number)

mask = number > 5
print("numbers greater than 5 : ", number[mask])

# ------------------ Fancy Indexing vs np.where ------------------
indices = [0, 2, 4]
print("fancy indexing: ", number[indices])

where_result = np.where(number > 5)
print("np.where: ", number[where_result])

condition_array = np.where(number > 5, number * 2, number)
print("np.where with condition: ", condition_array)

# ------------------ Adding & Removing Data ------------------
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
combined = np.concatenate((arr1, arr2))
print("combined: ", combined)

original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])
with_new_row = np.vstack((original, new_row))
print("with new row:\n", with_new_row)

new_col = np.array([[7], [8]])
with_new_col = np.hstack((original, new_col))
print("with new column:\n", with_new_col)

arr = np.array([1, 2, 3, 4, 5])
deleted = np.delete(arr, 2)
print("array deleted : ", deleted)

# ------------------ Array Compatibility ------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("compatibility shape: ", a.shape == b.shape)

# ------------------ Stacking Arrays ------------------
print("Vertical stacking:\n", np.vstack((a, b)))
print("Horizontal stacking:\n", np.hstack((a, b)))

# ------------------ Linear Algebra ------------------
matrix = np.array([[1, 2], [3, 4]])
print("Matrix multiplication:\n", np.dot(matrix, matrix))
print("Matrix inverse:\n", inv(matrix))
print("Matrix determinant: ", det(matrix))

# ------------------ Normalize Data ------------------
data = np.array([5, 10, 15])
normalized = (data - data.mean()) / data.std()
print("Normalized Data: ", normalized)

# ------------------ Save and Load Array ------------------
np.save('my_array.npy', data)
loaded_data = np.load('my_array.npy')
print("Loaded Data from file: ", loaded_data)

# Save as text (optional)
np.savetxt("save_demo.txt", data)

# ------------------ Random & Stats ------------------
np.random.seed(42)
print("Random float array:\n", np.random.rand(2, 3))
print("Random int array:\n", np.random.randint(0, 100, size=(3, 3)))

# ------------------ NaNs and Infs ------------------
faulty = np.array([1, np.nan, 2, np.inf])
print("is nan:", np.isnan(faulty))
print("is inf:", np.isinf(faulty))
print("nan to num:", np.nan_to_num(faulty))

# ------------------ Copy vs View ------------------
x = np.array([10, 20, 30])
y = x         # view
z = x.copy()  # copy
x[0] = 99
print("view y:", y)
print("copy z:", z)
