from NewtonInteroplation import interpolate
import time
import numpy as np
import matplotlib.pyplot as plt

time0 =time.time()

 # The border to test
a = -5
b = 5

N = 10
#N = 100

# equal distance
xi = np.linspace(a,b,N+1)

# unequeal distance
#xii = np.linspace(1,N,N)
#xi = np.cos((np.pi) * (xii/N))


yi = 1 / (1 +  xi * xi)
xy = np.column_stack((xi,yi))

x1 = np.linspace(-1,1,101)
y1 = interpolate(xy, x1)
exact_y1 =1 / (1 +  x1 * x1)


time1 =time.time()
error = exact_y1 - y1
maxerror = np.max(np.abs(error))
print("CPUtime: ",str(time1 -time0))
print("Maxerror: ",str(maxerror))
plt.plot(x1,y1)
plt.show()