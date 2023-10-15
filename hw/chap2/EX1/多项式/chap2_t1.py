import numpy as np

def interpolate(xy, x):

    #获取已知点的数量
    n = xy.shape[0]

    #提取x,y坐标
    x0 = xy[:, 0]
    y0 = xy[:, 1]
    #获取要求的数量
    m = len(x)


   # 基函数系数矩阵
    A = np.zeros((n,n))
    for k in range(0,n):
        z = x0[k]
        A[k,0] = 1
        for j in range(1,n):
            A[k, j] = A[k, j-1] * z
    

    #系数矩阵
    a = np.linalg.solve(A,y0)

    #计算结果
    y = np.zeros(m)
    for l in range(m):
        z = x[l]
        M = np.zeros(n)
        M[0]  = 1
        for j in range(1, n):
            M[j] = M[j - 1] * z
        y[l] = np.sum(M * a) 
    return y
 