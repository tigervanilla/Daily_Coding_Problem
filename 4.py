# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def shift_positive_elements_to_front(arr):
    i, n = -1, len(arr)
    positive_element_count = 0
    for j in range(n):
        if arr[j] > 0:
            positive_element_count += 1
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return positive_element_count

def find_smallest_missing_positive_integer(arr):
    positive_element_count = shift_positive_elements_to_front(arr)
    # Iterate over the positive numbers such that
    # if num > positive_element_count, then do nothing
    # if num <= positive_element_count, then make the sign of element at index num-1 negative
    for i in range(positive_element_count):
        num = abs(arr[i])
        if num <= positive_element_count:
            arr[num - 1] *= -1
    # Iterate over the array, if any positive number found then answer is its index+1
    # otherwise answer is positive_positive_element_count+1
    for i in range(positive_element_count):
        if arr[i] > 0:
            return i + 1
    return positive_element_count + 1


arr1 = [1, 2, -5 ,6 ,7 -8, -9, -10, 4]
arr2 = [3, 4, -1, 1]
arr3 = [1, 2, 0]
print(find_smallest_missing_positive_integer(arr1))
print(find_smallest_missing_positive_integer(arr2))
print(find_smallest_missing_positive_integer(arr3))