"""
Numerical Methods and Algebra Demonstration
Author: Akumu Maria

This program demonstrates several mathematical techniques:
1. Solving systems of linear equations
2. Newton-Raphson root finding
3. Numerical differentiation
4. Numerical integration
"""

import numpy as np


# -----------------------------
# 1. Solve Linear Equations
# Ax = b
# -----------------------------
def solve_linear_system():
    print("\n--- Solving Linear System ---")

    A = np.array([
        [2, -1, 3],
        [4, 2, -2],
        [1, 1, 1]
    ])

    b = np.array([5, 2, 6])

    solution = np.linalg.solve(A, b)

    print("Coefficient Matrix A:\n", A)
    print("Constant Vector b:", b)
    print("Solution Vector x:", solution)


# -----------------------------
# 2. Newton-Raphson Method
# Root finding for f(x)
# -----------------------------
def newton_raphson(f, df, x0, tolerance=1e-6, max_iter=100):
    print("\n--- Newton-Raphson Root Finding ---")

    x = x0

    for i in range(max_iter):
        x_new = x - f(x) / df(x)

        if abs(x_new - x) < tolerance:
            print(f"Root found after {i+1} iterations: {x_new}")
            return x_new

        x = x_new

    print("Did not converge")
    return None


# Example function: f(x) = x^3 - x - 2
def f(x):
    return x**3 - x - 2


def df(x):
    return 3*x**2 - 1


# -----------------------------
# 3. Numerical Differentiation
# -----------------------------
def numerical_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)


# -----------------------------
# 4. Numerical Integration
# Trapezoidal Rule
# -----------------------------
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    total = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        total += func(a + i*h)

    return h * total


# Example function for integration
def g(x):
    return x**2 + 2*x + 1


# -----------------------------
# Main Program
# -----------------------------
def main():

    # Linear Algebra
    solve_linear_system()

    # Root finding
    newton_raphson(f, df, x0=1.5)

    # Numerical derivative
    x = 2
    derivative = numerical_derivative(g, x)
    print(f"\nNumerical derivative of g(x) at x={x}: {derivative}")

    # Numerical integration
    integral = trapezoidal_rule(g, 0, 5, 100)
    print(f"Approximate integral of g(x) from 0 to 5: {integral}")


if __name__ == "__main__":
    main()