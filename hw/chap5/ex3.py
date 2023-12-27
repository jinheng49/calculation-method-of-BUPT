import numpy as np
import time


def gauss_seidel_inv(A, b):
    N = A.shape[0]
    
    x0 = b.copy()
    x = np.zeros(N)
    
    # Gauss-Seidel iteration
    for k in range(N):
        x[k] = 1 / A[k, k] * (b[k] - np.dot(A[k, :k], x[:k]) - np.dot(A[k, k+1:], x0[k+1:]))
    
    # Convergence check
    while np.linalg.norm(x - x0) > 1e-10:
        x0 = x.copy()
        for k in range(N):
            x[k] = x0[k] + 1 / A[k, k] * (b[k] - np.dot(A[k, :k], x[:k]) - np.dot(A[k, k:], x0[k:]))
    
    return x

def jacobi_inv(A, b):
    N = A.shape[0]
    
    x0 = b.copy()
    x = np.zeros(N)
    
    # Jacobi iteration
    for k in range(N):
        x[k] = 1 / A[k, k] * (b[k] - np.dot(A[k, :], x0) + A[k, k] * x0[k])
    
    # Convergence check
    while np.linalg.norm(x - x0) > 1e-10:
        x0 = x.copy()
        for k in range(N):
            x[k] = 1 / A[k, k] * (b[k] - np.dot(A[k, :], x0) + A[k, k] * x0[k])
    
    return x

N = 100

def test_method(solver, A, b, method_name):
    start_time = time.time()
    solution = solver(A, b)
    end_time = time.time()
    
    error = np.linalg.norm(np.dot(A, solution) - b)
    
    print(f"{method_name} 方法:")
    print(f"误差: {error}")
    print(f"运行时间: {end_time - start_time:.6f} 秒")
    print("="*30)

A = -2 * np.eye(N)
for k in range(N - 1):
    A[k, k + 1] = 1
    A[k + 1, k] = 1
b = np.ones(N)

test_method(gauss_seidel_inv, A, b, "gauss_seidel_invi")
test_method(jacobi_inv, A, b, "jacobi_inv")