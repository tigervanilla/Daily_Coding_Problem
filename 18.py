# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)

# Do this in O(n) time and O(k) space.
# You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.


from collections import deque


def max_in_each_subarray(arr, k):
    n = len(arr)
    Q = deque(maxlen=k)   # Holds the indices
    for i in range(k):
        while Q and arr[Q[-1]] <= arr[i]:
            Q.pop()
        Q.append(i)
    for i in range(k, n):
        print(arr[Q[0]], end=', ')
        while Q and Q[0] <= i-k:
            Q.popleft()
        while Q and arr[Q[-1]] <= arr[i]:
            Q.pop()
        Q.append(i)
    print(arr[Q[0]])


# Driver Code:
test_cases = {
    (11, 12, 13, 12, 14, 11, 10, 9): 3,
    (10, 5, 2, 7, 8, 7): 3,
    (1, 2, 3, 1, 4, 5, 2, 3, 6): 3,
    (8, 5, 10, 7, 9, 4, 15, 12, 90, 13): 4,
    (8, 5, 10, 7, 9, 4, 15, 12, 90, 13): 4,
}

for key, val in test_cases.items():
    max_in_each_subarray(key, val)
