import numpy as np
import matplotlib.pyplot as plt

v1 = np.random.randn(50)
v2 = np.random.randn(80)

op = np.outer(v1,v2)

plt.imshow(op)
plt.show()

# The outer product is not matrix commutative, (v1,v2) \neq (v2,v1), because switching order changes the matrix dimension (transpose)

s = 5
result1 = s*np.outer(v1,v2)
result2 = np.outer(s*v1,v2)
result3 = np.outer(v1,s*v2)
result4 = np.outer(v1,v2)*s

print(result1-result2)
print(result1-result3)
print(result1-result4)
# The outer product is, however, scalar multiplication commutative