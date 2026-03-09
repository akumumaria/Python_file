"""
Advanced Network Modeling and Mathematical Analysis
Author: Akumu Maria

Demonstrates:
1. Graph centrality analysis
2. Linear regression modeling
3. Singular Value Decomposition (SVD)
4. Statistical error analysis
5. Visualization of data relationships
"""

import numpy as np
import matplotlib.pyplot as plt
import heapq


# -----------------------------
# Graph Data
# -----------------------------
# Adjacency matrix for a weighted network

A = np.array([
    [0, 3, 0, 0, 5],
    [3, 0, 4, 0, 2],
    [0, 4, 0, 7, 0],
    [0, 0, 7, 0, 6],
    [5, 2, 0, 6, 0]
])


# -----------------------------
# Degree Centrality
# -----------------------------
def degree_centrality(graph):

    degrees = np.sum(graph > 0, axis=1)

    print("\n--- Degree Centrality ---")
    print("Degrees:", degrees)

    return degrees


# -----------------------------
# Dijkstra Shortest Path
# -----------------------------
def dijkstra(graph, start):

    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]

    while pq:

        current_dist, node = heapq.heappop(pq)

        for neighbor in range(n):

            weight = graph[node][neighbor]

            if weight > 0:

                distance = current_dist + weight

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

    return dist


# -----------------------------
# Singular Value Decomposition
# -----------------------------
def svd_analysis(graph):

    print("\n--- Singular Value Decomposition ---")

    U, S, V = np.linalg.svd(graph)

    print("Singular values:")
    print(S)

    return S


# -----------------------------
# Regression Modeling
# -----------------------------
def regression_model():

    print("\n--- Regression Modeling ---")

    # Example dataset
    x = np.array([1,2,3,4,5,6,7,8])
    y = np.array([3,5,7,9,11,13,15,17])

    X = np.column_stack((np.ones(len(x)), x))

    beta = np.linalg.inv(X.T @ X) @ X.T @ y

    intercept = beta[0]
    slope = beta[1]

    print("Regression equation:")
    print(f"y = {intercept:.2f} + {slope:.2f}x")

    y_pred = intercept + slope*x

    return x, y, y_pred


# -----------------------------
# Model Evaluation
# -----------------------------
def model_evaluation(y, y_pred):

    residuals = y - y_pred

    mse = np.mean(residuals**2)

    ss_total = np.sum((y - np.mean(y))**2)
    ss_res = np.sum(residuals**2)

    r2 = 1 - ss_res/ss_total

    print("\n--- Model Evaluation ---")
    print("Mean Squared Error:", mse)
    print("R^2:", r2)


# -----------------------------
# Visualization
# -----------------------------
def plot_regression(x, y, y_pred):

    plt.scatter(x, y)
    plt.plot(x, y_pred)

    plt.title("Regression Model")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()


# -----------------------------
# Main Program
# -----------------------------
def main():

    print("Adjacency Matrix:")
    print(A)

    # Network analysis
    degree_centrality(A)

    distances = dijkstra(A, 0)
    print("\nShortest paths from node 0:", distances)

    # Linear algebra
    svd_analysis(A)

    # Regression modeling
    x, y, y_pred = regression_model()

    # Model evaluation
    model_evaluation(y, y_pred)

    # Visualization
    plot_regression(x, y, y_pred)


if __name__ == "__main__":
    main()