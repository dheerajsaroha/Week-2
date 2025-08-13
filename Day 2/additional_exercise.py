# Create a 3d random array and compute its statistics
import numpy as np

# Create a 3D random array
arr = np.random.rand(3, 3, 3)  # 3x3x3 array of random floats in the range [0.0, 1.0)
print("3D Random Array:\n", arr)
print("Sum of all elements in 3D array:", np.sum(arr))
print("Mean of all elements in 3D array:", np.mean(arr))
print("Standard deviation of all elements in 3D array:", np.std(arr))
print("Variance of all elements in 3D array:", np.var(arr))
print("Minimum of all elements in 3D array:", np.min(arr))
print("Maximum of all elements in 3D array:", np.max(arr))
print("Cumulative sum of all elements in 3D array:", np.cumsum(arr))
print("Cumulative product of all elements in 3D array:", np.cumprod(arr))
print("Unique elements in 3D array:", np.unique(arr))
print("Count of unique elements in 3D array:", np.unique(arr, return_counts=True))
print("Indices of unique elements in 3D array:", np.unique(arr, return_index=True))
print("Sorted 3D array:", np.sort(arr, axis=None))  # Sort all elements
print("Sorted along axis 0 in 3D array:", np.sort(arr, axis=0))  # Sort along first dimension
print("Sorted along axis 1 in 3D array:", np.sort(arr, axis=1))  # Sort along second dimension
print("Sorted along axis 2 in 3D array:", np.sort(arr, axis=2))