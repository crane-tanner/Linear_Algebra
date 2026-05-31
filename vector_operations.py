import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from IPython.display import display, Math

# scalar multiplication
# v = np.array([.5,1])
# s= [1, -.5, 2, .5]
#
# for s_i in s:
#     s_v = s_i*v
#     plt.plot([0, s_v[0]], [0, s_v[1]], 'o-', linewidth=3, label='$\\lambda%g$' %s_i)
#
# plt.axis('square')
# plt.grid()
# plt.legend()
# plt.show()

# vector addition

v1 = np.array([-1,2])
v2 = np.array([1,1])

v3a = v1 + v2
v3b = np.add(v1,v2)
v3c = np.zeros(2)

for i in range(0,2):
    v3c = v1[i] + v2[i]

print(v3a, v3b, v3c)

plt.plot([0,v3a[0]], [0, v3a[1]],'b', linewidth=3, label='$v_3$')
plt.plot([0,v1[0]], [0, v1[1]],'g', linewidth=3, label='$v_1$')
plt.plot([0,v2[0]]+v1[0], [0, v2[1]] + v1[1],'r',linewidth=3, label='$v_2$', )

plt.axis('square')
plt.axis([-2,5,-2,5])
plt.grid()
plt.legend()

plt.show()