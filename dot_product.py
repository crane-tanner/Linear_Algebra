import numpy as np

v = np.arange(10,22,3)
w = np.arange(5,15, 3)

# dp1 = 0
# algorithm for dot product in code
# for i in range(0, len(v)):
#     dp1 = dp1 + v[i]*w[i]
# using built-in numpy functions
# dp2 = np.sum(np.multiply(v,w))
# dp3 = np.dot(v,w)
#
print(v,w)

def dot_product(u,p):
    if len(u) == len(p):
        print("Valid operation...")
        print("DP:", np.dot(u,p))
    else:
        print("Vectors not compatible for dot product")


dot_product(v,w)

