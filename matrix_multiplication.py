import numpy as np
# A = np.random.randn(2,3)
# B = np.random.randn(3,4)
#
# print(A@B)
# print("-----------------------------n--------------------------------------------------------------------")
# print(np.shape(A@B))
A = np.random.randn(2,1)
B = np.random.randn(1,2)

def matrix_mul(z,y):
    sizez = np.shape(z)
    sizey = np.shape(y)
    #check if matrix multi. is valid
    if sizez[1] != sizey[0]:
        raise ValueError("Inner dimensions don't match")
    #initialize size of resultant matrix using product of outer dimensions
    c = np.zeros((sizez[0], sizey[1]))
    #compute
    for i in range(sizez[0]):
        for j in range(sizey[1]):
            c[i,j] = np.dot(z[i,:], y[:,j])

    return c

print(matrix_mul(A,B))
print(A@B) # for comparison