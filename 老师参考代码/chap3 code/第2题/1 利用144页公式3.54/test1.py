# -*- coding: utf-8 -*-
import numpy as np

N=3000

x=[]
for k in range(0,N+1):
    x.append(-1+2/N*k)           #等分点

F0=[]
F2=[]

for k in range(0,N+1):
    F0.append(np.sin(x[k])+x[k]**3)            #函数0阶导
    F2.append(-np.sin(x[k])+6*x[k])            #函数2阶导

F0=np.array([F0]).transpose()        
F2=np.array([F2]).transpose()

'''按照144页3.54构建一阶微分矩阵'''
D1=np.zeros([N+1,N+1])

h=2/N

D1[0,0]=-3
D1[0,1]=4
D1[0,2]=-1

D1[N,N-2]=1
D1[N,N-1]=-4
D1[N,N]=3

for k in range(1,N):
    D1[k,k-1]=-1
    D1[k,k+1]=1

D1=D1/h/2
'''按照144页3.54构建一阶微分矩阵'''


D2=np.matmul(D1,D1)            #用一阶微分矩阵的平方近似二阶微分矩阵

F_2=np.matmul(D2,F0)           #函数2阶导数值解

error=np.linalg.norm(F_2-F2)      #函数2阶导数值解和精确解差的范数，误差
print('误差为',error)




#import matplotlib.pyplot as plt  
#
#fig1 = plt.figure('fig1')
#plt.plot(x,F2,c='b',lw=3)
#
#fig2 = plt.figure('fig2')
#plt.plot(x,F_2,c='b',lw=3)




