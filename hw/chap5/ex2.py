import numpy as np
import time
def jacobi(A,b,tol=1e-14, max_iter=1000):
    N = len(b)
    x0 = np.zeros(N)
    for k in range(max_iter):
        x = np.zeros(N)
        for i in range(N):
             x[i] = (b[i] - np.dot(A[i, :i], x0[:i]) - np.dot(A[i, i+1:], x0[i+1:])) / A[i, i]
        
        if np.linalg.norm(x - x0) < tol:
            break
        x0 = x.copy()

    return x

def gauss_seidel(A, b, tol=1e-14, max_iter=1000):

    N = len(b)
    x0 = np.zeros(N)  

    for k in range(max_iter):
        x = np.zeros(N)
        for i in range(N):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x0[i+1:])) / A[i, i]

        if np.linalg.norm(x - x0) < tol:
            break

        x0 = x.copy()

    return x

def test_method(solver, A, b, method_name):
    start_time = time.time()
    solution = solver(A, b)
    end_time = time.time()
    
    error = np.linalg.norm(np.dot(A, solution) - b)
    
    print(f"{method_name} 方法:")
    print(f"误差: {error}")
    print(f"运行时间: {end_time - start_time:.6f} 秒")
    print("="*30)


N = 100


A = -2 * np.eye(N)
for k in range(N - 1):
    A[k, k + 1] = 1
    A[k + 1, k] = 1
b = np.ones(N)

test_method(jacobi, A, b, "Jacobi")
test_method(gauss_seidel, A, b, "Gauss-Seidel")