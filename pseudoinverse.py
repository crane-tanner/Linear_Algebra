import numpy as np
import matplotlib.pyplot as plt

# Compute pseudoinverse and make images of A, A^*, and AA^*
m = 5
#M = np.random.randint(-5,7,(m,m))
M = np.random.randn(m,m+2)

#M[:,0] = M[:,1]
M_pinv = np.linalg.pinv(M)
MM_inv = M @ M_pinv

fig,ax = plt.subplots(1,3)


ax[0].imshow(M)
ax[0].set_title('M')

ax[1].imshow(M_pinv)
ax[1].set_title('M-Pseudoinverse')

ax[2].imshow(MM_inv)
ax[2].set_title('A*A-Pseudoinverse')

plt.show()