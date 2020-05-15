# This problem was asked by Microsoft.

# You have an N by N board.
# Write a function that, given N, returns the number of possible arrangements of the board
# where N queens can be placed on the board without threatening each other,
# i.e. no two queens share the same row, column, or diagonal.


def isSafe(board, n, row, col):
    # check attack from top
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check attack from top-left
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i-1, j-1

    # check attack from top-right
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i, j = i-1, j+1

    return True


def nQueens(n, board, row):
    if row == n:    # base case: if all queens are placed, one solution has been found
        return 1
    count = 0
    for i in range(n):  # try placing current queen in all the columns one-by-one
        if isSafe(board, n, row, i):
            board[row][i] = 1   # place the queen in ith column
            # check for the queens in remaining rows
            count += nQueens(n, board, row+1)
            board[row][i] = 0   # remove the queen from ith column
    return count


# Driver Code:
for i in range(10):
    board = [[0]*i for j in range(i)]
    print('N =', i, 'Solutions =', nQueens(i, board, 0))

'''
 ===============================================================================
 Space optimised solution to N-Queens problem
 Idea is to use an array such that its
 index represents row
 value represents column
 ===============================================================================
'''


def isSafeSpaceOptimised(n, board, curRow, curCol):
    for i in range(curRow):
        diff = abs(board[i] - curCol)
        if diff == 0 or diff == curRow - i:
            return False
    return True


def nQueensSpaceOptimised(n, board, row):
    if row == n:
        return 1
    count = 0
    for col in range(n):
        if isSafeSpaceOptimised(n, board, row, col):
            board[row] = col
            count += nQueensSpaceOptimised(n, board, row+1)
            board[row] = -1
    return count

print('------------------------------------------------------')
for i in range(10):
    board = [[0]*i for j in range(i)]
    print('N =', i, 'Solutions =', nQueensSpaceOptimised(i, board, 0))
