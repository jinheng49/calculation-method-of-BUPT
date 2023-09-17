import time
import math


def Factorial(n):
    global y
    y = []
    f(n)
    return y


def f(n):
    if n == 1:
        z = 1
    else:
        z = n * f(n - 1)

    y.append(z)
    return z


################################# The first way to calculate e

time0 = time.time()
T = int(2e6)
n1 = 1e10
for i in range(1, T):
    e1 = (1+1/n1)**n1
time1 = time.time()

runtime1 = time1 - time0
error1 = math.e - e1

################################# The second way to calculate e

# The number of factorials
n2 = 9
for j in range(1, T):
    ff = Factorial(n2)
    e2 = 1
    for k in range(0, n2):
        e2 = e2 + 1 / ff[k]

time2 = time.time()

print('cputime1:', time1-time0)
print('e1', e1)
print('error1', math.fabs(math.e-e1))

print('\n')

print('cputime2', time2-time1)
print('e2', e2)
print('error2', math.fabs(math.e-e2))





