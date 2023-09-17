
import math

N = 100000
x = []
y = []
dx = []
su = 0
result = 0
for k in range(0, N):
    x.append(1.0*k/N)

for k in range(0, N-1):
    y.append(math.exp(x[k]))
    dx.append(x[k+1]-x[k])


for k in range(0, N-1):
    su = dx[k] * y[k]
    result = result + su

print("Integral Result:", result)
print("e minus 1:", math.e-1)
print("Absolute error:", math.e-1-result)


