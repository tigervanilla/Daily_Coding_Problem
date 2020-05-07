# This problem was asked by Facebook.

# You are given an array of non-negative integers that represents a two-dimensional elevation map
# where each element is unit-width wall and the integer is the height.
# Suppose it will rain and all spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index
# (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


def trap_water(arr):
    n = len(arr)
    left, right = [0]*n, [0]*n   # to store tallest walls on left and right of the current index
    left[0], right[n-1] = arr[0], arr[n-1]
    for i in range(1, n):
        left[i] = max(arr[i], left[i-1])    # compute tallest wall on left of ith index
        right[n-i-1] = max(arr[n-i-1], right[n-i])  # compute tallest wall on right of ith index
    water = 0
    for i in range(0, n):
        # diff b/w heights of ith index and min(tallest wall on its left, tallest wall on its right)
        water = water + (min(left[i], right[i]) - arr[i])
    return water


# Driver code:
testcases = [
    [2, 1, 2],
    [3, 0, 1, 3, 0, 5],
]
for tc in testcases:
    print(trap_water(tc))
