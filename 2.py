# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def prodArr(arr):
    nonZeroProduct = 1
    isZero, numOfZero = False, 0
    for num in arr:
        if num == 0:
            isZero = True
            numOfZero += 1
        else:
            nonZeroProduct *= num
    if numOfZero > 1:
        return [0]*len(arr)
    elif numOfZero == 1:
        return [0 if num != 0 else nonZeroProduct for num in arr]
    else:
        return [nonZeroProduct // num for num in arr]


arr1, arr2, arr3 = [1, 2, 3, 4, 5], [8, 9, 0, 7], [0 ,0, 88, 98]
print(prodArr(arr1), prodArr(arr2), prodArr(arr3), sep='\n')