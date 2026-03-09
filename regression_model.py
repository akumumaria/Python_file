"""
Regression, Correlation and Statistical Modeling Demo
Author: Akumu Maria

This program demonstrates:
1. Correlation analysis
2. Simple linear regression
3. Multiple regression
4. Prediction using regression models
"""

import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Sample dataset
# -----------------------------
# Study hours vs exam score

hours = np.array([1,2,3,4,5,6,7,8])
scores = np.array([50,55,60,65,70,78,85,90])


# -----------------------------
# Correlation
# -----------------------------
def correlation_analysis():

    r = np.corrcoef(hours, scores)[0,1]

    print("\n--- Correlation Analysis ---")
    print("Correlation coefficient (r):", r)

    if r > 0:
        print("Positive relationship between hours studied and exam score")
    else:
        print("Negative relationship")


# -----------------------------
# Simple Linear Regression
# y = b0 + b1x
# -----------------------------
def simple_linear_regression():

    n = len(hours)

    x_mean = np.mean(hours)
    y_mean = np.mean(scores)

    numerator = np.sum((hours-x_mean)*(scores-y_mean))
    denominator = np.sum((hours-x_mean)**2)

    b1 = numerator / denominator
    b0 = y_mean - b1*x_mean

    print("\n--- Simple Linear Regression ---")
    print("Intercept (b0):", b0)
    print("Slope (b1):", b1)

    return b0, b1


# -----------------------------
# Prediction
# -----------------------------
def prediction(b0,b1):

    new_hours = 9
    predicted_score = b0 + b1*new_hours

    print("\n--- Prediction ---")
    print(f"Predicted score if a student studies {new_hours} hours:", predicted_score)


# -----------------------------
# Multiple Regression
# -----------------------------
def multiple_regression():

    print("\n--- Multiple Linear Regression ---")

    # Example data
    # X1 = hours studied
    # X2 = sleep hours

    X = np.array([
        [1,7],
        [2,6],
        [3,6],
        [4,5],
        [5,5],
        [6,4],
        [7,4],
        [8,3]
    ])

    y = scores

    # Add column of 1s for intercept
    X_design = np.column_stack((np.ones(len(X)), X))

    # Normal equation
    beta = np.linalg.inv(X_design.T @ X_design) @ X_design.T @ y

    print("Regression coefficients:")
    print("Intercept:", beta[0])
    print("Hours coefficient:", beta[1])
    print("Sleep coefficient:", beta[2])


# -----------------------------
# Visualization
# -----------------------------
def plot_regression(b0,b1):

    predicted = b0 + b1*hours

    plt.scatter(hours,scores)
    plt.plot(hours,predicted)

    plt.title("Study Hours vs Exam Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Exam Score")

    plt.show()


# -----------------------------
# Main Program
# -----------------------------
def main():

    correlation_analysis()

    b0,b1 = simple_linear_regression()

    prediction(b0,b1)

    multiple_regression()

    plot_regression(b0,b1)


if __name__ == "__main__":
    main()