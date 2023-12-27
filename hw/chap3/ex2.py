import numpy as np

N = 3000


x = np.linspace(-1, 1, N + 1)


F0 = np.sin(np.pi * x) + x**3
F2 = -np.pi**2 * np.sin(np.pi * x) + 6 * x


h = 2 / N
D1 = np.zeros((N + 1, N + 1))

D1[0, 0] = -3
D1[0, 1] = 4
D1[0, 2] = -1

D1[N, N - 2] = 1
D1[N, N - 1] = -4
D1[N, N] = 3

for k in range(1, N):
    D1[k, k - 1] = -1
    D1[k, k + 1] = 1

D1 = D1 / (h * 2)


D2 = np.matmul(D1, D1)


F_2 = np.matmul(D2, F0)

error = np.linalg.norm(F_2 - F2)


print('误差为', error)
