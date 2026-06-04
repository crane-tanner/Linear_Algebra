import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


ein=Image.open('einstein.jpg')
ein = np.mean(ein,2)
#print(np.shape(ein))

U,s,v = np.linalg.svd(ein)

#randorder = np.random.permutation(len(s))
S = np.zeros(np.shape(ein))
for i in range(10,len(s)):
    S[i,i] = s[i]

rein = U@S@v #reconstructed image

plt.subplot(1,2,1)
plt.imshow(ein)
plt.axis('off')
plt.title('Original')
plt.show()

plt.subplot(1,2,2)
plt.imshow(rein)
plt.axis('off')
plt.title('Reconstructed')
plt.show()