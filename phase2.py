# numpy array operations
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("basic slicing: ",arr[2:7])
print("with step: ",arr[1:8:2])
print("negative indexing: ",arr[-3])

# 2d array operation
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("specific element: ",arr_2d[1,2])
print("entire row : ",arr_2d[2])

# sorting
unsorted = np.array([3,1,4,1,5,9,8,7])
print("sorted array: ", np.sort(unsorted))

arr_2d_unsort = np.array([[3,1], [1,2],[2,3]])
print("sorted 2d array by column : ",np.sort(arr_2d_unsort,axis=0)) #axis = 0 for top to bottom bcz when data is given like revenue sheet ,axis = 1 for row (less used)

# filtering
number = np.array([1,2,3,4,5,6,7,8,9,10])
even_number = number[number % 2 == 0]
print("even: ",even_number)

# filter with mask
mask = number > 5
print("numbers greater than 5 : ",number[mask])

#fancy indexing vs np.where()
indices = [0,2,4]
print(number[indices])

where_result = np.where(number>5) #mp.where used for condition clause (if-else loop)
print("NP where: ",number[where_result])

condition_array = np.where(number>5,number*2,number)
print(condition_array)
''' if(number > 5) {
    number * 2
} else {
    number
}   '''

# adding & removing data
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# wrong way
# combined = arr1 + arr2
# print(combined)

combined = np.concatenate((arr1,arr2))
print(combined)

# array compatability

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])
print("compatibility shape : ",a.shape == b.shape)

original = np.array ([[1,2],[3,4]])
new_row = np.array([[5,6]])

with_new_row = np.vstack((original,new_row)) #vstack add the row
print(original)
print(with_new_row)

new_col = np.array([[7], [8]])
with_new_col = np.hstack((original, new_col))
print("with new column: ", with_new_row)

arr = np.array([1,2,3,4,5])
deleted = np.delete(arr, 2) #index number will be deleted
print("array deleted : ",deleted)