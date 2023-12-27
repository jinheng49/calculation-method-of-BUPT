import numpy as np

def legendre(n, m, x):
    if n == 0 or m >= n:
        return None
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legendre(n - 1, m, x) - (n - 1) * legendre(n - 2, m, x)) / n

def bisection(n, m, a, b, error):
    number_bisection = 0
    z = []

    for k in range(n - m):
        legendre_a = legendre(n, m, a)
        legendre_b = legendre(n, m, b)

        while legendre_a * legendre_b > 0:
            a = b
            legendre_a = legendre_b

            b = a + error
            legendre_b = legendre(n, m, b)

        z_k, number = bisection_helper(n, m, a, b, error)
        z.append(z_k)
        a = z_k + error
        b = a + error

        number_bisection += number

    average_number = number_bisection / (n - m)
    print(f'二分法平均计算次数为 {average_number} 次')
    return z

def bisection_helper(n, m, a, b, error):
    number = 0

    while (b - a) / 2 > error:
        c = (a + b) / 2
        legendre_a = legendre(n, m, a)
        legendre_c = legendre(n, m, c)

        if legendre_c == 0:
            return c, number
        elif legendre_a * legendre_c < 0:
            b = c
        else:
            a = c

        number += 1

    return (a + b) / 2, number

# Example usage
n_value = 5
m_value = 2
result = legendregauss_bisection(n_value, m_value)
print(f'Legendre-Gauss结果为: {result}')
