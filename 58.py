'''
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''


def findX(arr, x):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == x:
            return mid      # Key found
        elif arr[left] <= arr[mid]:
            # Left half is sorted
            if arr[left] <= x <= arr[mid]:  # Key is in left half
                right = mid-1
            else:   # Key is in right half
                left = mid+1
        else:
            # Right half is sorted
            if arr[mid+1] <= x <= arr[right]:   # Key is in right half
                left = mid+1
            else:   # Key is in left half
                right = mid-1
    # Key not found
    return 'Not Found'


# Driver Code
print(findX([13, 18, 25, 2, 8, 10], 8))
print(findX([1, 2, 3, 4, 5, 6], 6))
print(findX([6, 1, 2, 3, 4, 5], 6))
