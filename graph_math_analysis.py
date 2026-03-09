"""
Graph Algorithms and Mathematical Data Analysis
Author: Akumu Maria

This program demonstrates:
1. Graph representation using adjacency matrices
2. Breadth-First Search (BFS)
3. Dijkstra's Shortest Path Algorithm
4. Spectral graph analysis using eigenvalues
5. Statistical analysis of graph properties
6. Visualization of graph structure
"""

import numpy as np
import matplotlib.pyplot as plt
import heapq


# -----------------------------
# Graph Representation
# -----------------------------
# Weighted adjacency matrix
A = np.array([
    [0, 4, 0, 0, 0, 0],
    [4, 0, 8, 0, 0, 0],
    [0, 8, 0, 7, 2, 4],
    [0, 0, 7, 0, 9, 14],
    [0, 0, 2, 9, 0, 10],
    [0, 0, 4, 14, 10, 0]
])


# -----------------------------
# Breadth First Search
# -----------------------------
def bfs(graph, start):

    visited = [False]*len(graph)
    queue = [start]
    visited[start] = True

    order = []

    while queue:
        node = queue.pop(0)
        order.append(node)

        for i in range(len(graph[node])):
            if graph[node][i] != 0 and not visited[i]:
                queue.append(i)
                visited[i] = True

    return order


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
# Spectral Graph Analysis
# -----------------------------
def spectral_analysis(graph):

    print("\n--- Spectral Graph Analysis ---")

    eigenvalues, eigenvectors = np.linalg.eig(graph)

    print("Eigenvalues of adjacency matrix:")
    print(eigenvalues)

    return eigenvalues


# -----------------------------
# Degree Statistics
# -----------------------------
def graph_statistics(graph):

    degrees = np.sum(graph > 0, axis=1)

    print("\n--- Graph Statistics ---")
    print("Node degrees:", degrees)

    mean_degree = np.mean(degrees)
    variance_degree = np.var(degrees)

    print("Mean degree:", mean_degree)
    print("Variance of degrees:", variance_degree)

    return degrees


# -----------------------------
# Graph Visualization
# -----------------------------
def visualize_graph(graph):

    n = len(graph)

    angles = np.linspace(0, 2*np.pi, n, endpoint=False)

    x = np.cos(angles)
    y = np.sin(angles)

    plt.scatter(x, y)

    for i in range(n):
        plt.text(x[i], y[i], str(i), fontsize=12)

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                plt.plot([x[i], x[j]], [y[i], y[j]])

    plt.title("Graph Visualization")
    plt.axis("equal")
    plt.show()


# -----------------------------
# Main Program
# -----------------------------
def main():

    print("Adjacency Matrix:")
    print(A)

    # BFS
    order = bfs(A, 0)
    print("\nBFS Traversal:", order)

    # Shortest paths
    distances = dijkstra(A, 0)
    print("\nShortest distances from node 0:", distances)

    # Graph statistics
    graph_statistics(A)

    # Spectral analysis
    spectral_analysis(A)

    # Visualization
    visualize_graph(A)


if __name__ == "__main__":
    main()