# Create a 3x3 matrix and perform operations
import numpy as np
matrix =np.array([[2,3,4],[1,5,6],[3,6,2]])
# matrix = matrix.reshape(3,3)
print(matrix)
print("\n\n")
# transpose of matrix
print(matrix.T)
print(matrix.transpose())

print("Another Matrix\n")
another_matrix = np.array([[1,1,4],[2,3,7],[9,6,5]])
print(another_matrix)

print("Operation to perform on matrix")
print("Addition of Matrix\n",matrix + another_matrix,"\n")
print("Multiplication of Matrix\n",matrix * another_matrix,"\n")
