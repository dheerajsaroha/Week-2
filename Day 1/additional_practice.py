# First Exercise
import numpy as np
from random import *
# Create a 4x4 matrix (example with random integers)
# You can also manually input values or use a predefined matrix
matrix = np.random.randint(1, 10, size=(4, 4)) 

print("The 4x4 Matrix:")
print(matrix)

# Calculate the sum of each row
row_sums = np.sum(matrix, axis=1)
print("\nSum of each row:")
print(row_sums)

# Calculate the sum of each column
column_sums = np.sum(matrix, axis=0)
print("\nSum of each column:")
print(column_sums)

# Second Exercise
# Write a program to normalize an array(scale values b/w 0 and 1)
def normalized_array(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)

    if max_val == min_val:
        return np.zeros_like(arr,dtype=float)
    
    normalized_arr = (arr-min_val)/(max_val-min_val)
    return normalized_arr
original_array = np.array([10, 25, 5, 40, 15])
normalized_array = normalized_array(original_array)

print("Original Array: ",original_array)
print("Normalized Array: ",normalized_array)

# Third Exercise
# Generate a random array and find the minimum  and maximum values
random_array = np.random.randint(1, 101, 10)
print("Generated Array:", random_array)

print("Max Values :",np.max(random_array))
print("Min Values :",np.min(random_array))