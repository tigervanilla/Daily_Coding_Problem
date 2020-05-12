# This problem was asked by Google.

# Given an array of strictly the characters 'R', 'G', and 'B',
# segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last.
# You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G']
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].


def segregateRGB(arr):
    i, j, k = -1, 0, len(arr)
    while j < k:
        if arr[j] == 'R':
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        elif arr[j] == 'G':
            j += 1
        else:
            k -= 1
            arr[k], arr[j] = arr[j], arr[k]
    return arr


# Driver Code:
testcases = [
    ['G', 'R'],
    ['B', 'R'],
    ['G', 'B', 'R'],
    ['G', 'R', 'B'],
    ['G', 'B', 'R', 'R', 'B', 'R', 'G']
]
for tc in testcases:
    print(segregateRGB(tc))
