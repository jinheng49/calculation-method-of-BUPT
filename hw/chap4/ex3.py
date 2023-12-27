def func(x):
    return x**3 - x - 1

def func_derivative(x):
    return 3 * x**2 - 1

def newton_method(initial_guess, tolerance=1e-10, max_iterations=1000):
    x = initial_guess
    for _ in range(max_iterations):
        x_new = x - func(x) / func_derivative(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Newton method did not converge")

def secant_method(x0, x1, tolerance=1e-10, max_iterations=1000):
    for _ in range(max_iterations):
        x_new = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(x_new - x1) < tolerance:
            return x_new
        x0, x1 = x1, x_new
    raise ValueError("Secant method did not converge")

# Initial guesses
initial_guess_newton = 1.0
initial_guess_secant_0 = 1.0
initial_guess_secant_1 = 2.0

# Solve using Newton method
result_newton = newton_method(initial_guess_newton)
print(f"Newton Method: Root found at x = {result_newton}")

# Solve using Secant method
result_secant = secant_method(initial_guess_secant_0, initial_guess_secant_1)
print(f"Secant Method: Root found at x = {result_secant}")
