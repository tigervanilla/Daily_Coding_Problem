'''
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''
from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 1, 2, 3],
        [4, 5, 6, 7, 1],
        [2, 3, 4, 5, 6],
        [7, 0, 0, 0, 0],
    ]
    result = 0
    while result == 0:
        row = rand5() - 1
        col = rand5() - 1
        result = matrix[row][col]
    return result


# Driver Code:
freq = [0]*7
for i in range(7):
    freq[rand7() - 1] += 1
print(freq)
