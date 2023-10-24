# -*- coding: utf-8 -*-
import numpy as np

N=int(1e2)

x_gauss_lobatto=np.array([-np.cos(j*np.pi/N)  for j in range(0,N+1)])           #切比雪夫高斯罗巴托点
y_gauss_lobatto=1/(1+25*x_gauss_lobatto**2)*np.sqrt(1-x_gauss_lobatto**2)          #1/(1+25*x**2)是被积函数
I_gauss_lobatto=(sum(y_gauss_lobatto)-y_gauss_lobatto[0]/2-y_gauss_lobatto[N]/2)*np.pi/N           #计算切比雪夫罗巴托高斯积分
error_gauss_lobatto=np.abs(I_gauss_lobatto-2/5*np.arctan(5))

x_gauss=np.array([-np.cos((2*j+1)*np.pi/(2*N+2))  for j in range(0,N+1)])           #切比雪夫高斯点
y_gauss=1/(1+25*x_gauss**2)*np.sqrt(1-x_gauss**2)
I_gauss=sum(y_gauss)*np.pi/(N+1)                                   #计算切比雪夫高斯积分
error_gauss=np.abs(I_gauss-2/5*np.arctan(5))

x_1_3=np.array([-1+2/N*j  for j in range(0,N+1)])           #[-1,1]等分点
y_1_3=1/(1+25*x_1_3**2)
I_1_3=(sum(y_1_3)-y_1_3[0]/2-y_1_3[-1]/2)*2/N               #公式(1.3)
error_1_3=np.abs(I_1_3-2/5*np.arctan(5))

print('error_gauss_lobatto',error_gauss_lobatto)
print('error_gauss',error_gauss)
print('equation (1.3)',error_1_3)
