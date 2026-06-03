import numpy as np
import matplotlib.pyplot as plt

M = np.array([[.5,1],
            [1,.5]])

vcomp = np.linspace(-2,2,80)
for a in vcomp:
    v = np.array([1, a])
    Mv = M@v # transformed vector

    plt.plot([0,v[0]], [0,v[1]], color=[1-abs(a)/4,.5,abs(a)/2], alpha=.8)
    plt.plot([0,Mv[0]], [0,Mv[1]],color=[1-abs(a)/2,abs(a)/4, .5])

plt.axis('square')
plt.axis('off')
#plt.legend()

plt.show()