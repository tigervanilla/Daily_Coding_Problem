from pprint import pprint


def findEmptyLocation(grid, L):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                L[0], L[1] = i, j
                return True
    return False


def usedInRow(grid, r, num):
    return num in grid[r]


def usedInCol(grid, c, num):
    for i in range(9):
        if grid[i][c] == num:
            return True
    return False


def usedInBox(grid, r, c, num):
    for i in range(3):
        for j in range(3):
            if grid[r+i][c+j] == num:
                return True
    return False


def isLocationSafe(grid, r, c, num):
    row = usedInRow(grid, r, num)
    col = usedInCol(grid, c, num)
    box = usedInBox(grid, r - r % 3, c - c % 3, num)
    return not (row or col or box)


def sudoku(grid):
    L = [0, 0]
    if not findEmptyLocation(grid, L):
        return True

    r, c = L
    for num in range(1, 10):
        if isLocationSafe(grid, r, c, num):
            grid[r][c] = num
            if sudoku(grid):
                return True
            grid[r][c] = 0
    return False


# Driver Code
grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

if sudoku(grid):
    pprint(grid)
else:
    print('No Solution Exists')
