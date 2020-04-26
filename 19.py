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
