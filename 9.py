# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def max_sum_non_adjacent(arr):
    n = len(arr)

    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    
    two_back = arr[0]
    one_back = max(arr[0], arr[1])
    for i in range(2, n):
        curr_max_sum = max(arr[i], one_back, two_back + arr[i])
        two_back, one_back = one_back, curr_max_sum

    return curr_max_sum

# Driver code to test 
arr1 = [2, 4, 6, 2, 5]
arr2 = [5, 1, 1, 5]
arr3 =  [-1, -1, 3, 9, 2]
print(max_sum_non_adjacent(arr1))
print(max_sum_non_adjacent(arr2))
print(max_sum_non_adjacent(arr3))

# Explanation:
# For this problem we want to store the Max Sum possible for each position in the array.
# We need to figure out the max values for the first 2 positions manually.
# The max position for the first value can only be the first value (since the problem specifies it must be a subset of the array)
# The max position for the second value can only be either the current value or the previous value.
# From there we need to iterate over the remain values, and calulate their max possible sum

# The max possible value for the current position can only be 3 things.
# 1. The Current Element Plus the Max Value from 2 positions ago (This handles the Adjacent)
# 2. The last max Value e.g(imagine the first value in the array was negative, and the second value was positive, and the current value is 0)
# 3. The current element e.g(the max value from 2 positions ago could have been negative)

