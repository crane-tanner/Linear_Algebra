import numpy as np
import matplotlib.pyplot as plt

#Solving system: Ax = b; x = (A^TA)^-1 * (A^T*b)
# A = np.array([[2,1,-1],[3,4,2],[1,-5,-2]])
# b = np.array([1,13,0])
#
# x1 = np.linalg.inv(A.T@A) @ (A.T@b)
# print(x1)

# Other way
# x2 = np.linalg.solve(A,b)
# print(x2)

X1 = np.array([[3,-1],[-1,1]])
y1 = np.array([6,2])

X2 = np.array([[3,-1],[1.5,-0.5]])
y2 = np.array([6,3])

X3 = np.array([[3,-1],[1.5,-0.5]])
y3 = np.array([6,2])

# System 1

# xlim = np.array([0,10])
# yy1 = -X1[0,0]/X1[0,1]*xlim + y1[0]/X1[0,1]
# yy2 = -X1[1,0]/X1[1,1]*xlim + y1[1]/X1[1,1]
#
# b = np.linalg.solve(X1,y1)
# print(b)
#
# plt.plot(xlim, yy1, 'b', label='eq1')
# plt.plot(xlim, yy2, 'r', label='eq2')
# plt.plot(b[0], b[1], 'ko', markersize=9, label='Solution')
# plt.grid()
# plt.legend()
# plt.show()

# System 2 (Infinitely many solutions; Same line)

xlim = np.array([0,10])
yy1 = -X2[0,0]/X2[0,1]*xlim + y2[0]/X2[0,1]
yy2 = -X2[1,0]/X2[1,1]*xlim + y2[1]/X2[1,1]

# b = np.linalg.solve(X2,y2) # equations are not linearly independent
# print(b)

plt.plot(xlim, yy1, 'b', label='eq1')
plt.plot(xlim, yy2, 'r--', label='eq2')
#plt.plot(b[0], b[1], 'ko', markersize=9, label='Solution')
plt.grid()
plt.legend()
plt.show()

# System 3 (Parallel lines, no solution)

# xlim = np.array([0,10])
# yy1 = -X3[0,0]/X3[0,1]*xlim + y3[0]/X3[0,1]
# yy2 = -X3[1,0]/X3[1,1]*xlim + y3[1]/X3[1,1]
#
# b = np.linalg.solve(X3,y3)
# print(b)
#
# plt.plot(xlim, yy1, 'b', label='eq1')
# plt.plot(xlim, yy2, 'r', label='eq2')
# plt.plot(b[0], b[1], 'ko', markersize=9, label='Solution')
# plt.grid()
# plt.legend()
# plt.show()
