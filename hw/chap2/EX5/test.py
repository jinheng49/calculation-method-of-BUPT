import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as skl

# 生成N个随机数提供value
N = 100
x = np.sort(np.random.random(N) * 2 - 1)

y = np.zeros(N)
for k in range(0,N):
    y[k]=np.sin(np.pi*x[k]/2-np.pi/2)   #计算y的值
    y[k] = y[k] + (np.random.random() * 2 - 1) * 0.2  #在y上增加扰动

#数据表
data = np.zeros([N,2])
for k in range(0, N):
    data[k,0] = x[k]
    data[k,1] = x[k]**2

label = np.array([y]).T

lr = skl.LinearRegression()
lr.fit(data, label)
y_train_predict=lr.predict(data)

''' 测试模型 '''
M=100
xi=np.sort(np.random.random(M)*2-1)       #[-1,1]随机生成M个点，从小到大排序

y_exact=np.zeros([M,1])
for k in range(0,M):
    y_exact[k]=np.sin(np.pi*xi[k]/2-np.pi/2)


#构建数据进行拟合
data_test=np.zeros([M,2])
for k in range(0,M):
    data_test[k,0]=xi[k]
    data_test[k,1]=xi[k]**2
    
y_predict=lr.predict(data_test)


# 计算误差

Error_test=np.sqrt(np.sum((y_predict-y_exact)**2)/len(y_exact))
print('Error_test',Error_test)


#作图

#训练集
fig2 = plt.figure('fig1')
plt.plot(x,y,'r+',lw=1)    #原数据
plt.plot(x,y_train_predict,'b',lw=1)    #模型

#测试
fig2 = plt.figure('fig2')
plt.plot(xi,y_predict,'b',lw=1)   #预测解
plt.plot(xi,y_exact,'r+',lw=1)     #精确值


plt.show()
