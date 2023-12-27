import numpy as np
import time

def legendregauss_bisection(N, m):
    if N == 0 or m >= N:
        return None

    error = 1e-18
    h = N**(-2)
    a = -1
    b = a + h

    total_number_bisection = 0
    x_bisection = []

    for k in range(N - m):
        legendre_a = legendre(N, m, a)
        legendre_b = legendre(N, m, b)

        while legendre_a * legendre_b > 0:
            a = b
            legendre_a = legendre(N, m, a)
            
            b = a + h
            legendre_b = legendre(N, m, b)

        x_k, number = bisection(N, m, a, b, error)
        x_bisection.append(x_k)
        a = x_k + h
        b = a + h

        total_number_bisection += number  # 累加总的迭代次数

    average_number = total_number_bisection / (N - m)
    print(f'Bisection method average number of iterations: {average_number}')
    return x_bisection



def bisection(N, m, a, b, error):
    number_bisection = 0

    while (b - a) / 2 > error:
        c = (a + b) / 2
        legendre_a = legendre(N, m, a)
        legendre_c = legendre(N, m, c)

        if legendre_c == 0:
            number_bisection += 1  # 在找到根时增加迭代次数
            return c, number_bisection
        elif legendre_a * legendre_c < 0:
            b = c
        else:
            a = c

        number_bisection += 1

    return (a + b) / 2, number_bisection


def legendre(N, m, x):
    if N == 0 or m >= N:
        return 0
    elif N == 1:
        return x
    else:
        return ((2 * N - 1) * x * legendre(N - 1, m, x) - (N - 1) * legendre(N - 2, m, x)) / N

def time_legendre_method(N, m, method):
    start_time = time.time()

    if method == 'bisection':
        x_method = legendregauss_bisection(N, m)
    else:
        x_method = None  # Add other methods here if needed

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Time taken for {method} method: {elapsed_time} seconds')

    return x_method

N_value = 10
m_value = 1

x_bisection = time_legendre_method(N_value, m_value, 'bisection')
print(f'Roots found by bisection method: {x_bisection}')
