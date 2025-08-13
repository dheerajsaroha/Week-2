import numpy as np
## Example of broadcasting in NumPy
# arr = np.array([1, 2, 3])

# print("Scaler Broadcasting",arr+10)

# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print("Matrix Broadcasting", matrix + arr)

# # Aggregate Functions

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print("Sum of all elements:", np.sum(arr))
# print("Sum along axis 0:", np.sum(arr, axis=0))  # Sum along columns
# print("Sum along axis 1:", np.sum(arr, axis=1))  # Sum alongs rows
# print("Mean of all elements:", np.mean(arr))
# print("Mean along axis 0:", np.mean(arr, axis=0))  # Mean along columns
# print("Mean along axis 1:", np.mean(arr, axis=1))
# print("Standard deviation of all elements:", np.std(arr))
# print("Standard deviation along axis 0:", np.std(arr, axis=0))  # Standard deviation along columns
# print("Standard deviation along axis 1:", np.std(arr, axis=1))  # Standard deviation along rows
# print("Variance of all elements:", np.var(arr))
# print("Variance along axis 0:", np.var(arr, axis=0))  # Variance along columns
# print("Variance along axis 1:", np.var(arr, axis=1))
# print("Minimum of all elements:", np.min(arr))
# print("Minimum along axis 0:", np.min(arr, axis=0))  # Minimum along columns
# print("Minimum along axis 1:", np.min(arr, axis=1))
# print("Maximum of all elements:", np.max(arr))
# print("Maximum along axis 0:", np.max(arr, axis=0))  # Maximum along columns
# print("Maximum along axis 1:", np.max(arr, axis=1))
# print("Cumulative sum of all elements:", np.cumsum(arr))
# print("Cumulative sum along axis 0:", np.cumsum(arr, axis=0))  # Cumulative sum along columns
# print("Cumulative sum along axis 1:", np.cumsum(arr, axis=1))  # Cumulative sum along rows
# print("Cumulative product of all elements:", np.cumprod(arr))
# print("Cumulative product along axis 0:", np.cumprod(arr, axis=0))  # Cumulative product along columns
# print("Cumulative product along axis 1:", np.cumprod(arr, axis=1))  # Cumulative product along rows
# print("Unique elements:", np.unique(arr))
# print("Count of unique elements:", np.unique(arr, return_counts=True))
# print("Indices of unique elements:", np.unique(arr, return_index=True))
# print("Sorted array:", np.sort(arr, axis=None))  # Sort all elements
# print("Sorted along axis 0:", np.sort(arr, axis=0))  # Sort along columns
# print("Sorted along axis 1:", np.sort(arr, axis=1))

# Boolean Indexing and Filtering
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr)
print("Elements greater than 3:\n",arr[arr>3])
print("Elements which are even:\n",arr[arr%2==0])

# Random Number Generation
# To generate random number we use np.random module
np.random.seed(19)  # Set seed for reproducibility
random_arr = np.random.rand(3, 3)  # Generate a 3x3 array of random floats in the range [0.0, 1.0)
print("Random array:\n", random_arr)

random_int_arr = np.random.randint(1, 10, size=(3, 3))  # Generate a 3x3 array of random integers between 1 and 10
print("Random integer array:\n", random_int_arr)