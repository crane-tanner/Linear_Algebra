import numpy as np
from sympy import transpose
import matplotlib.pyplot as plt

# row_vec = np.random.randn(1,10)
# print(np.shape(row_vec))
#
# new_vec = np.transpose(row_vec)
# new2 = row_vec.T
# print(np.shape(new2))

# mat = np.random.randn(8,4)
# mat_T = mat.T
# print(np.shape(mat))
# print(np.shape(mat_T))
#
# fig,ax = plt.subplots(1,20)
# ax[0].imshow(mat)
# ax[0].set_title('M')
#
# ax[1].imshow(mat_T)
# ax[1].set_title('M^T')
#
# for i in ax:
#     i.set_xticks([])
#     i.set_yticks([])
#
# plt.show()

# Symmetric is A = A^T
m = 5
n = 9

amat = np.random.randn(m,n)
amat_T = amat.T
new_m = amat@amat_T # taking a matrix and multiplying by its transpose results in a square matrix
print(np.shape(new_m)) # show square matrix
print(new_m - new_m.T) # showing symmetry

