import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6],[2,4,6]])
vector = np.array([1, 2, 3])

print("Addition of matrix and vector:\n", matrix + vector)

result_mul = matrix * vector
print("Element-wise multiplication of matrix and vector:\n", result_mul)
