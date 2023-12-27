import numpy as np  

N = 5000

b = np.random.random([N, 1])


A = np.zeros([N, N])
a0 = np.random.random([1, N])
a1 = np.hstack((a0, a0))


for k in range(0, N):
    A[k, :] = a1[0, N - k:2 * N - k]

x0 = np.linalg.solve(A, b)


print(x0)
