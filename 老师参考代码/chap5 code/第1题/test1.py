# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np  


N=5000
b=np.random.random([N,1])

A = np.zeros([N,N])
a0 = np.random.random([1,N])
a1 = np.hstack((a0,a0))


for k in range(0,N):
    A[k,:]=a1[0,N-k:2*N-k]

x0 = np.linalg.solve(A,b)

Lambda = np.fft.fftn(A[:,0])
inv_lambda = np.diag(1/Lambda)
x1 = np.fft.ifftn(np.dot(inv_lambda,np.fft.fftn(b)))


#print(x0)
#print(x1)
 
print('error',np.linalg.norm(x0-x1))