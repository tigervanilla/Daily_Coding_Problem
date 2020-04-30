// This problem was asked by Google.

// You are given an M by N matrix consisting of booleans that represents a board.
// Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
// Given this matrix, a start coordinate, and an end coordinate,
// return the minimum number of steps required to reach the end coordinate from the start.
// If there is no possible path, then return null. You can move up, left, down, and right.
// You cannot move through walls. You cannot wrap around the edges of the board.

// For example, given the following board
// [[f, f, f, f],
// [t, t, f, t],
// [f, f, f, f],
// [f, f, f, f]]
// and start = (3, 0) (bottom left) and end = (0, 0) (top left),
// the minimum number of steps required to reach the end is 7,
// since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

function min(a, b) {
    return a < b ? a : b;
}

function minSteps(matrix: boolean[][], start: any[], end: any[]) {
    if (start[0] === end[0] && start[1] === end[1]) {
        return 0;
    }

    const stack: { r: number, c: number }[] = [];
    const n: number = matrix.length;
    const m: number = matrix[0].length;
    const isVisited: boolean[][] = [];
    const distance: number[][] = [];
    for (let i = 0; i < n; i++) {
        let ar = [], ar2 = [];
        for (let j = 0; j < m; j++) {
            ar.push(false);
            ar2.push(Number.MAX_VALUE);
        }
        isVisited.push(ar);
        distance.push(ar2);
    }
    distance[start[0]][end[0]] = 0;
    stack.push({ r: start[0], c: start[1] });

    while (stack.length > 0) {
        const { r, c } = stack.pop();
        if (!isVisited[r][c]) {
            isVisited[r][c] = true;
            if (r > 0 && !matrix[r - 1][c]) {
                distance[r - 1][c] = min(distance[r - 1][c], 1 + distance[r][c]);
                stack.push({ r: r - 1, c: c });
            }
            if (r < n - 1 && !matrix[r + 1][c]) {
                distance[r + 1][c] = min(distance[r + 1][c], 1 + distance[r][c]);
                stack.push({ r: r + 1, c: c });
            }
            if (c > 0 && !matrix[r][c - 1]) {
                distance[r][c - 1] = min(distance[r][c - 1], 1 + distance[r][c]);
                stack.push({ r: r, c: c - 1 });
            }
            if (c < m - 1 && !matrix[r][c + 1]) {
                distance[r][c + 1] = min(distance[r][c + 1], 1 + distance[r][c]);
                stack.push({ r: r, c: c + 1 });
            }
        }
    }

    return matrix[end[0]][end[1]] ? -1 : distance[end[0]][end[1]];
}

const matrix = [
    [false, false, false, false],
    [true, true, false, true],
    [false, false, false, false],
    [false, false, false, false],
]
console.log(minSteps(matrix, [3, 0], [0, 0]));
