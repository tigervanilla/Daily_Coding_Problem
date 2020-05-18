from pprint import pprint

'''
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life.
It should be able to be initialized with a starting list of live cell coordinates
and the number of steps it should run for.
Once initialized, it should print out the board state at each step.
Since it's an infinite board, print out only the relevant coordinates,
i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
'''

def conwayGameOfLife(grid, m, n):
    future = [[0]*n for i in range(m)]

    # loop through every cell
    for i in range(1, m-1):
        for j in range(1, n-1):
            # find no. of alive neighbours
            aliveNeightbours = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    aliveNeightbours += grid[i+k][j+l]
            # the cell needs to be subtracted from
            # its neighboursas it was counted before
            aliveNeightbours -= grid[i][j]

            # implement the rules of game

            # cell is lonely and dies
            if grid[i][j] == 1 and aliveNeightbours < 2:
                future[i][j] = 0
            
            # cell dies due to over population
            elif grid[i][j] == 1 and aliveNeightbours > 3:
                future[i][j] = 0
            
            # a new cell is born
            elif grid[i][j] == 0 and aliveNeightbours == 3:
                future[i][j] = 1

            # remains the same
            else:
                future[i][j] = grid[i][j]
    print('Future')
    pprint(future)


# Driver code:
grid = [ 
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] 
]
print('Starting')
pprint(grid)
conwayGameOfLife(grid, 10, 10)