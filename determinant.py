from sympy import *

M = Matrix([
    [1,0,1],
    [2,1,0],
    [1,0,2]
])

det = M.det()
tr = M.trace()
eigvals = M.eigenvals()

print("Determinant:", det)
print('\n')
print("Trace:", tr)
print("\n")
print("Eigenvalues:", eigvals)

# For any nxn matrix, the trace is equal to the sum of its eigenvalues,
# and the determinant is equal to the product of its eigenvalues