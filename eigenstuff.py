import numpy as np
import matplotlib.pyplot as plt

# Av = w; Av = \lambdaV
# Diagonalization: AV = V\lamda where A - matrix, V - E.vectors, \lambda - E.values ;
# A = A\lambdaV^-1 ( A = PDP^-1 in more familiar notation)

M = np.random.randint(-5,6, (5,5))
M = M@M.T
eigvals, eigvecs = np.linalg.eig(M)
print("Eigenvalues:", np.diag(eigvals))
print("\n")
print("Eigenvectors:", eigvecs)
Mv = M@eigvecs[:,0] # matrix * 1st eigenvector
lv = eigvals[0]*eigvecs[:,0] # lambda (1st eigenvalue) * 1st eigenvector
print("\n")
print(Mv) # this equivalence is the algebraic meaning of eigendecomposition
print("\n")
print(lv)

fig,ax = plt.subplots(1,3)
ax[0].imshow(M)
ax[0].set_title("The matrix")

ax[1].imshow(np.diag(eigvals))
ax[1].set_title("Eigenvalues")

ax[2].imshow(eigvecs)
ax[2].set_title("Eigenvectors")


plt.show()