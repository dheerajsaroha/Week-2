#  Filterning and aggregating
import numpy as np

# Example of broadcasting in NumPy
arr = np.array([1, 2, 3])   
print("Scaler Broadcasting", arr + 10)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix Broadcasting", matrix + arr)
# Aggregate Functions
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Sum of all elements:", np.sum(arr))

# Generate random datasets
datsets = np.random.randint(1,51,size=(3, 3))  # Generate a 3x3 array of random floats in the range [0.0, 1.0)
print("Random dataset:\n", datsets)

# Filter value greater than 25 and replace with 0
datsets[datsets > 25] = 0
print("Filtered dataset (values > 25 replaced with 0):\n", datsets)

# calculate summary statistics
print("Sum of all elements:", np.sum(datsets))
print("Mean of all elements:", np.mean(datsets))
print("Standard deviation of all elements:", np.std(datsets))
print("Variance of all elements:", np.var(datsets))
print("Minimum of all elements:", np.min(datsets))
print("Maximum of all elements:", np.max(datsets))
print("Cumulative sum of all elements:", np.cumsum(datsets))
print("Cumulative product of all elements:", np.cumprod(datsets))
print("Unique elements:", np.unique(datsets))
print("Count of unique elements:", np.unique(datsets, return_counts=True))
print("Indices of unique elements:", np.unique(datsets, return_index=True))
print("Sorted array:", np.sort(datsets, axis=None))  # Sort all elements
print("Sorted along axis 0:", np.sort(datsets, axis=0))  # Sort along columns
print("Sorted along axis 1:", np.sort(datsets, axis=1))
# Boolean Indexing and Filtering
print("Original array:\n", arr)
print("Elements greater than 3:\n", arr[arr > 3])
print("Elements which are even:\n", arr[arr % 2 == 0])
# Random Number Generation
np.random.seed(19)  # Set seed for reproducibility
random_arr = np.random.rand(3, 3)  # Generate a 3x
# array of random floats in the range [0.0, 1.0)
print("Random array:\n", random_arr)
