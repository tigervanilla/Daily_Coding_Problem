# This problem was asked by Amazon.

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def staircase(N, X):
    unique_ways = [0] * (N + 1)
    unique_ways[0] = unique_ways[1] = 1
    for i in range(2, N + 1):
        for j in X:
            if i - j >= 0:
                unique_ways[i] += unique_ways[i - j]
    return unique_ways[N]


# Driver Code
print(staircase(4, [1, 2]))
print(staircase(1, [1, 3, 5]))
print(staircase(2, [1, 3, 5]))
print(staircase(3, [1, 3, 5]))
print(staircase(4, [1, 3, 5]))
print(staircase(5, [1, 3, 5]))
print(staircase(6, [1, 3, 5]))
print(staircase(7, [1, 3, 5]))
print(staircase(8, [1, 3, 5]))
print(staircase(9, [1, 3, 5]))
print(staircase(10, [1, 3, 5]))
