'''
This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k,
determine whether each node in the graph can be colored
such that no two adjacent nodes share the same color using at most k colors.
'''


def isSafe(adjMatrix, color, node):
    n = len(adjMatrix)
    for i in range(n):
        if i != node and adjMatrix[node][i] == 1 and color[node] == color[i]:
            return False
    return True


def mColoring(adjMatrix, K, color, node):
    if node == len(adjMatrix):
        return True
    for j in range(1, K+1):
        color[node] = j
        if isSafe(adjMatrix, color, node) and mColoring(adjMatrix, K, color, node+1):
            return True
        color[node] = -1
    return False


# Driver Code:
adjMatrix = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
]

color = [-1]*5

K = 3

if mColoring(adjMatrix, K, color, 0):
    print(color)
else:
    print('No Solution Exists')
