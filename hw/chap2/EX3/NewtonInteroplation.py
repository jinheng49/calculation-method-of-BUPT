import numpy as np

def interpolate(xy, x):

    #获取已知点的数量
    n = xy.shape[0]

    #提取x,y坐标
    x0 = xy[:, 0]
    y0 = xy[:, 1]
    #获取要求的数量
    m = len(x)

    #结果数组y
    y = np.zeros(m)

    #差商表
    A = np.zeros((n,n))
    A[:, 0] = y0
    for j in range(1,n-1):
        for i in range(n - j):
            A[i,j] =(A[i,j-1] - A[i+1,j-1]) / (x0[i]-x0[i+j])
    
    #计算插值
    for l in range(m):
        z = x[l]
        M = np.ones(n)
        for j in range(1,n):
            M[j] = M[j-1] * (z - x0[j - 1])
        y[l] = np.sum(A[0, :] * M)

    return y


