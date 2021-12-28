import numpy as np

a = np.array([1,2,3,4,5,6]);
print(a)
b = np.array([1,2,3,4,5,6]);
print(b)

sumarr = a+b
print(sumarr)

prodarr = a*b
print(prodarr)

div = a/b
print(div)

a_t = a.T;
b_t = b.T;

print(a_t)
print(b_t)

matmult = np.dot(a_t,b_t)
matmult2 = np.dot(a,b_t)
matmult3 = np.dot(a_t,b)
matmult4 = np.dot(a,b)

#Be careful if you want to multiply matrices... .dot is a dot product operator

print(matmult)
print(matmult2)
print(matmult3)
print(matmult4)

#All of the above generate the same answer, 91.

mat = np.array([[1,2,3],[4,5,6]])
print(mat)
