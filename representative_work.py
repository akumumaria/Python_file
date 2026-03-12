# enhanced_representative_work.py
# Akumu Maria
# Representative Work in Mathematical Sciences using Python
# Demonstrates algebra, calculus, statistics, linear algebra, probability, optimization, numerical methods, and plotting

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize
from sympy import symbols, diff, integrate, solve, sin, cos, Matrix

print("=== ENHANCED REPRESENTATIVE WORK IN MATHEMATICAL SCIENCES ===\n")

# ------------------------------
# 1. Algebra: Solve a system of linear equations
print("1. Algebra: Solve a system of linear equations")
A = np.array([[2, 3], [1, -1]])
b = np.array([6, 1])
solution = np.linalg.solve(A, b)
print(f"Solution (x, y): {solution}\n")

# ------------------------------
# 2. Linear Algebra: Eigenvalues and Eigenvectors
print("2. Linear Algebra: Eigenvalues and Eigenvectors")
M = np.array([[4, 2], [1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(M)
print(f"Matrix M:\n{M}")
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}\n")

# ------------------------------
# 3. Calculus: Derivative and integral
print("3. Calculus: Derivative and Integral")
x = symbols('x')
f = x**3 - 5*x**2 + 6*x

f_prime = diff(f, x)
f_integral = integrate(f, x)
print(f"Function: f(x) = {f}")
print(f"Derivative f'(x) = {f_prime}")
print(f"Indefinite Integral ∫f(x)dx = {f_integral}\n")

# Advanced Calculus: Derivative of sin(x)*cos(x)
g = sin(x)*cos(x)
g_prime = diff(g, x)
print(f"Advanced Calculus: g(x) = sin(x)*cos(x), g'(x) = {g_prime}\n")

# ------------------------------
# 4. Statistics: Mean, median, variance, correlation
print("4. Statistics: Mean, Median, Variance, Correlation")
data_x = np.array([5, 7, 6, 6, 8])
data_y = np.array([10, 6, 12, 5, 3])

mean_x = np.mean(data_x)
median_x = np.median(data_x)
var_x = np.var(data_x, ddof=1)
correlation = np.corrcoef(data_x, data_y)[0, 1]

print(f"Data X: {data_x}")
print(f"Mean: {mean_x}, Median: {median_x}, Sample Variance: {var_x}")
print(f"Correlation between X and Y: {correlation}")

slope, intercept, r_value, p_value, std_err = stats.linregress(data_x, data_y)
print(f"Linear regression: Y = {slope:.2f}*X + {intercept:.2f}, R-squared: {r_value**2:.2f}\n")

# ------------------------------
# 5. Probability: Binomial and Normal distributions
print("5. Probability: Binomial and Normal distributions")
from scipy.stats import binom, norm

# Binomial: Probability of exactly 3 successes in 5 trials with p=0.6
prob_binom = binom.pmf(3, n=5, p=0.6)
print(f"Binomial P(X=3), n=5, p=0.6: {prob_binom}")

# Normal: Probability that a value is less than 1.5 for N(0,1)
prob_norm = norm.cdf(1.5, loc=0, scale=1)
print(f"Normal P(X < 1.5), mean=0, std=1: {prob_norm}\n")

# ------------------------------
# 6. Optimization: Find minimum of a function
print("6. Optimization: Find minimum of a function")
def h(x):
    return x**4 - 3*x**3 + 2

min_result = optimize.minimize(h, x0=0)
print(f"Function h(x) = x^4 - 3x^3 + 2")
print(f"Minimum occurs at x = {min_result.x[0]:.4f}, h(x) = {min_result.fun:.4f}\n")

# ------------------------------
# 7. Numerical Methods: Solve equation numerically
print("7. Numerical Methods: Solve equation numerically")
# Solve x^3 - 5x + 1 = 0
def eq(x):
    return x**3 - 5*x + 1

root = optimize.root(eq, x0=1)
print(f"Root of equation x^3 -5x +1 = 0: x ≈ {root.x[0]:.4f}\n")

# ------------------------------
# 8. Graphing functions and data
print("8. Graphing function f(x) and scatter data")

x_vals = np.linspace(-2, 6, 100)
y_vals = x_vals**3 - 5*x_vals**2 + 6*x_vals

plt.figure(figsize=(12, 6))

# Plot cubic function
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_vals, label='f(x) = x^3 -5x^2 +6x', color='blue')
plt.title("Cubic Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

# Scatter plot of data and regression line
plt.subplot(1, 2, 2)
plt.scatter(data_x, data_y, color='red', label='Data points')
plt.plot(data_x, slope*data_x + intercept, color='green', label='Regression line')
plt.title("Data Scatter & Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

print("\n=== END OF ENHANCED REPRESENTATIVE WORK ===")