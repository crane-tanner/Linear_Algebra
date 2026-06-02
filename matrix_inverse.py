import numpy as np
import matplotlib.pyplot as plt
# Inverse: Ax = b; A^-1Ax = A^-1b; Ix = A^-1b; x =A^-1b
# A matrix is invertible if it's square and if it is full rank (A condition for invertibility)

m = 5
A = np.random.randint(-5,6, (m,m))
Ainv = np.linalg.inv(A)
print(A)
print('\n')
print(Ainv)

fig,ax = plt.subplots(1, 3)

ax[0].imshow(A)
ax[0].set_title('A')

ax[1].imshow(Ainv)
ax[1].set_title('A-Inverse')

ax[2].imshow(A@Ainv)
ax[2].set_title('AA-Inverse')

plt.show()