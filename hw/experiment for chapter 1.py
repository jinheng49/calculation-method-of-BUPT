from sympy import Integral, Symbol
from sympy import E
x = Symbol('x')
result = Integral(E**x, (x, 0, 1)).doit()
print("Integral_result:", result)