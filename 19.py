# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix
# where the nth row and kth column represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

from sys import maxsize


def paint_houses(cost_matrix):
    n = len(cost_matrix)    # number of houses
    k = len(cost_matrix[0])  # number of colors
    dp = [[0]*k for i in range(n)]       # to store the minimum cost

    if (not cost_matrix) or (n > 1 and k < 2):
        return -1

    # for house #0
    dp[0] = cost_matrix[0]

    # to store the least two costs of painting till he previous house
    min_cost, min_cost_index = maxsize, -1
    second_min_cost, second_min_cost_index = maxsize, -1

    # find the least two costs of house #0
    for i in range(k):
        if dp[0][i] < min_cost:
            second_min_cost, second_min_cost_index = min_cost, min_cost_index
            min_cost, min_cost_index = dp[0][i], i
        elif dp[0][i] < second_min_cost:
            second_min_cost, second_min_cost_index = dp[0][i], i

    # for houses #1 to #n-1
    for i in range(1, n):
        cur_min = cur_min2 = maxsize    # least cost of painting till the current house
        cur_min_index = cur_min2_index = -1

        for j in range(k):
            dp[i][j] = cost_matrix[i][j] + (min_cost if j != min_cost_index else second_min_cost)

            if dp[i][j] < cur_min:
                cur_min2, cur_min2_index = cur_min, cur_min_index
                cur_min, cur_min_index = dp[i][j], j
            elif dp[i][j] < cur_min2:
                cur_min2, cur_min2_index = dp[i][j], j

        min_cost, min_cost_index = cur_min, cur_min_index
        second_min_cost, second_min_cost_index = cur_min2, cur_min2_index

    return min_cost


# Driver code:
test_case1 = [
    [5, 8, 6],
    [19, 14, 13],
    [7, 5, 12],
    [14, 15, 17],
    [3, 20, 10],
]
print(paint_houses(test_case1))


# Explanaion:
Lets say we have n=4 houses and k=3 colors
cost_matrix = [
    [4, 20, 3],
    [10, 4, 6],
    [33, 10, 7],
    [1, 9, 1]
]
initialize a 2D matrix dp such that
dp[i][j] denotes the cost of painting ith house with jth color + minimum cost to paint 0 to i-1 houses

For house 0:
dp = [
    [4, 20, 3],
    [],
    [],
    [],
]

For house 1:
dp = [
    [4, 20, 3],
    [13, 7, 10],    # ie [10+min(20,3), 4+min(4,3), 6+min(4,20)]
    [],
    p[,]
]

For house 2:
dp = [
    [4, 20, 3],
    [13, 7 , 10]
    [40, 20, 14],   # ie [33+min(7,10), 10+min(13,10), 7+min(13,7)]
    [],
]

For house 3:
dp = [
    [4, 20, 3],
    [13, 7, 10],
    [40, 20, 14],
    [15, 23, 21],   # ie [1+min(20,14), 9+min(40,14), 1+min(40,20)]
]

therefor ans = 15