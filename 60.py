'''
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
'''


def func(arr, n, sum1, sum2):
    if n == 0:
        return sum1 == sum2
    if func(arr, n-1, sum1+arr[n-1], sum2):
        return True
    elif func(arr, n-1, sum1, sum2+arr[n-1]):
        return True
    else:
        return False


# Driver Code
testcases = [
    [15, 5, 20, 10, 35, 15, 10],
    [15, 5, 20, 10, 35],
    [1, 5, 11, 5],
    [1, 5, 3],
    [1, 2, 4, 9, 14],
]
for tc in testcases:
    print(func(tc, len(tc), 0, 0))
