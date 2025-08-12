import numpy as np

# basic array operation
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
print(arr1 + arr2)
print(arr2 - arr1)
print(arr1 * arr2)
print(arr2 / arr1)
print(np.sum(arr1))
print(np.mean(arr2))
print(np.sqrt(arr2))
print(np.square(arr2))
print(np.max(arr1))
print(np.std(arr1))

# Array indexing and slicing

arr = np.array([1,2,4,5,2,3,6,7,8])
# indexing
print(arr[-1])

# slicing
print(arr[:4])
print(arr[2:4])
print(arr[:])

# reshaping
arr = arr.reshape(3,3)
print(arr)