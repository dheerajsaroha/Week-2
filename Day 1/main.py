import numpy as np

arr = np.array([1,2,3,4,5])
print(arr[0:4])

zeroes = np.zeros((3,3))
print(zeroes)
print("\n//////////////////////\n")
ones = np.ones((2,4))
print(ones)

array_range=np.arange(1,10)
print(array_range)

print("Use of linspace function")
arr_linspace = np.linspace(1,10,9)
print(arr_linspace)

# change shape
np_arr = np.array([1,2,3,4,5,4,6,7,8])
shape_changed = np_arr.reshape((3,3))
print(shape_changed)

# expanded array or adding dimension
arr = np.array([1,2,3])
print(arr)
expanded = arr[:,np.newaxis]
print(expanded)