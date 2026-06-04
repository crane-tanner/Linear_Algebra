import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Singular Value Decomposition
# A (mxn) = U(mxm)*\Sigma(mxn)*V^T(nxn)
# Where A is the matrix, U is the orthogonal basis for the column space of A, \Sigma singular values of A,
# V^T is the orthogonal basis for the row space of A

ein=Image.open('einstein.jpg')
ein = np.mean(ein,2)
print(np.shape(ein))


# plt.imshow(ein)
# plt.show()

U,s,v = np.linalg.svd(ein)

#fig,ax = plt.subplots(1,3)

# ax[0].imshow(U)
# ax[0].set_title('U')
#
# ax[1].imshow(np.diag(np.log(s)))
# ax[1].set_title('\\Sigma')
#
# ax[2].imshow(v)
# ax[2].set_title('V^T')

plt.plot(s, 'ks-', markerfacecolor='w')
plt.xlim([-1,50])
plt.title("Eigenspectrum of Einstein")
plt.show()