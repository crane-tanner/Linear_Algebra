import numpy as np
import matplotlib.pyplot as plt

# Eigen-decomposition exercise
# M = np.array([[1,2], [2,1]])
# print("M=",M)
# print("\n")
# eigvals, eigvecs = np.linalg.eig(M)
# print("Eigenvalues:", eigvals)
# print("\n")
# print("Eigenvectors:", eigvecs)
# print("\n")
#
# Mv = M@eigvecs[:,1]
# lv = eigvals[1]*eigvecs[:,1]
# print("Mv:", Mv)
# print("\n")
# print("lv:", lv)
#
# plt.plot([0,Mv[0]], [0,Mv[1]], 'b', label="Mv", linewidth=4)
# plt.plot([0,lv[0]], [0,lv[1]], 'r:', label="lv", linewidth=4)
#
# plt.axis("square")
# plt.grid()
# plt.legend()
# plt.show()

m = 6
A = np.random.randn(m,m)
A = A@A.T

d,v = np.linalg.eig(A)
dps = np.zeros([m,m])

print(np.round(v,1))
for i in range(m):
    for j in range(m):
        dps[i,j] = np.dot(v[:,i], v[:,j])

print(np.round(dps,2)) # identity matrix
