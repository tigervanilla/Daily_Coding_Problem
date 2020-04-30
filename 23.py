from collections import deque


def min_steps(matrix, source, destination):
    if source[0] == destination[0] and source[1] == destination[1]:
        return 0

    Q = deque()
    N, M = len(matrix), len(matrix[0])  # matrix size is N x M
    isVisited = [[False for i in range(M)] for i in range(N)]   # to keep track of visited cells
    matrix[source[0]][source[1]] = 0  # Distance of startcell from itself
    Q.appendleft(source)

    while Q:
        r, c = Q.pop()
        if isVisited[r][c]:
            continue

        isVisited[r][c] = True
        if r > 0 and matrix[r-1][c] != True:    # Cell above is not a wall
            if type(matrix[r-1][c]) == type(False) and matrix[r-1][c] == False:
                matrix[r-1][c] = 1+matrix[r][c]
            else:
                matrix[r-1][c] = min(matrix[r-1][c], 1+matrix[r][c])
            Q.appendleft((r-1, c))
        if r < N-1 and matrix[r+1][c] != True:  # Cell below is not a wall
            if type(matrix[r+1][c]) == type(False) and matrix[r+1][c] == False:
                matrix[r+1][c] = 1+matrix[r][c]
            else:
                matrix[r+1][c] = min(matrix[r+1][c], 1+matrix[r][c])
            Q.appendleft((r+1, c))
        if c > 0 and matrix[r][c-1] != True:   # Cell at left is not a wall
            if type(matrix[r][c-1]) == type(False) and matrix[r][c-1] == False:
                matrix[r][c-1] = 1+matrix[r][c]
            else:
                matrix[r][c-1] = min(matrix[r][c-1], 1+matrix[r][c])
            Q.appendleft((r, c-1))
        if c < M-1 and matrix[r][c+1] != True:  # Cell at right is not a wall
            if type(matrix[r][c+1]) == type(False) and matrix[r][c+1] == False:
                matrix[r][c+1] = 1+matrix[r][c+1]
            else:
                matrix[r][c+1] = min(matrix[r][c+1], 1+matrix[r][c])
            Q.appendleft((r, c+1))
        # print(matrix)

    if type(matrix[destination[0]][destination[1]]) == type(True):
        return -1
    else:
        return matrix[destination[0]][destination[1]]


# Driver Code:
matrix = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False],
]
print(min_steps(matrix, (3, 0), (0, 0)))
# print(matrix)
