import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz

# I = np.eye(2) # identity matrix
# print(I)
# print(np.zeros((2,2))) # matrix with all 0 entries
# D = np.diag([2,3, 4]) # diagonal matrix with specified entries
# d = np.diagonal(D) # function returns the diagonal of the matrix as a vector
# print(d)
#
# T = np.random.randn(8,8)
# plt.imshow(np.triu(T)) # upper triangular matrix with all 0s below diagonal
# plt.imshow(np.tril(T)) # lower triangular matrix with all 0s above the diagonal
# plt.show()

r_integer_mat = np.random.randint(-4,5, (4,4))
I = np.eye(4)
upperT = np.triu(np.random.randn(4,4))
print("Random integer matrix:\n", r_integer_mat)
print('-------------------------------------------------')
print("Product of random integer matrix with Identity matrix:\n",r_integer_mat@I)
print('-------------------------------------------------')
print("Upper Triangular matrix:\n", upperT)
print('-------------------------------------------------')
print("Product of Random integer matrix and upper triangular:", r_integer_mat@upperT)

# plt.imshow(r_integer_mat@upperT)
# plt.show()

#Toesplitz Matrix
toe = toeplitz(np.arange(1,6))
plt.imshow(toe)
plt.show()