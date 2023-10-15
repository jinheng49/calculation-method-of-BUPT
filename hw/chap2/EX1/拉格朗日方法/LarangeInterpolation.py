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

    for i in range(m):
        s = 0
        for j in range(n):
            l = 1
            for k in range(n):
                if(k != j):
                    l *= (x[i]-x0[k]) / (x0[j] - x0[k])
            s += l * y0[j]
        y[i] = s
    
    return y
        
            


