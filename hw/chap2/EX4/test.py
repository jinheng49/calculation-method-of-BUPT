import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.interpolate as spi

time0 =time.time()

# The border to test
a = -1
b = 1

N = 10
#N = 30

# 数据点
xi = np.linspace(a,b,N+1)
yi = 1 / (1 +  25 *xi * xi)


# 插值的点
x = np.linspace(-1,1,11)
exact_y = 1 / (1 +  25 *x * x)

ipo3=spi.splrep(xi,yi,k = 3)
y = spi.splev(x,ipo3)


plt.plot(xi, yi,'o')
plt.plot(x,y)
time1 =time.time()
error = exact_y - y
maxerror = np.max(np.abs(error))
print("CPUtime: ",str(time1 -time0))
print("Maxerror: ",str(maxerror))
plt.show()