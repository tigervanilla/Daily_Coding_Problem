def isSafe(board, n, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i-1, j-1

    i, j = row-1, col-1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i+1, j-1

    return True


def nQueens(n, board, col):
    if col == n:
        return 1
    count = 0
    for i in range(n):
        if isSafe(board, n, i, col):
            board[i][col] = 1
            count += nQueens(n, board, col+1)
            board[i][col] = 0
    return count


# Driver Code:
n = 4
board = [[0]*n for i in range(n)]
print(board)
print(nQueens(n, board, 0))
