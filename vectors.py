import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
#from IPython.display import display, Math
from mpl_toolkits.mplot3d import Axes3D
from sympy.printing.pretty.pretty_symbology import line_width

# row_vec = np.array([4,2])
# col_vec = np.array([[-2],[3]])
# print(row_vec)
# print(col_vec)
#
# display(Math(sym.latex(sym.sympify(row_vec))))
# display(Math(sym.latex(sym.sympify(col_vec))))
#
# plt.plot([0, row_vec[0]], [0, row_vec[1]], 'r', label='row vector')
# plt.plot([0, col_vec[0]], [0, col_vec[1]], 'b', label='column vector')
#
# plt.axis('square')
# plt.axis(-5,5,-5,5)
# plt.grid()
# plt.legend()
# plt.show()

v = np.array([3,0,-4])
u = np.array([-1,1,3])

fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')

ax.plot([0, v[0]], [0, v[1]], [0,v[2]], 'b', linewidth=3)
ax.plot([0, u[0]], [0, u[1]], [0,u[2]], 'r', linewidth=3)
ax.plot([-5,5], [0,0], [0,0], '--', color=[.7,.7,.7])
ax.plot([0,0], [-5,5], [0,0], '--', color=[.7,.7,.7])
ax.plot([0,0], [0,0], [-5,5], '--', color=[.7,.7,.7])

ax.set_xlim3d(-5,5)
ax.set_ylim3d(-5,5)
ax.set_zlim3d(-5,5)

plt.show()