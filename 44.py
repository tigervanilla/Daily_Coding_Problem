'''
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has.
Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
[2,4,1,3,5] has 3 inversions: (2,1), (4,1), and (4,3).
[5,4,3,2,1] has ten inversions: every distinct pair forms an inversion
'''


def merge(arr, left, mid, right):
    inversionCount = 0
    tempArr = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tempArr.append(arr[i])
            i += 1
        else:
            inversionCount += mid - i + 1
            print(arr[i], arr[j], mid-i+1)
            tempArr.append(arr[j])
            j += 1
    while i <= mid:
        tempArr.append(arr[i])
        i += 1
    while j <= right:
        tempArr.append(arr[j])
        j += 1
    for k in range(left, right + 1):
        arr[k] = tempArr[k - left]
    # print(tempArr, inversionCount)
    return inversionCount


def mergeSort(arr, left, right):
    inversionCount = 0
    if left >= right:
        return inversionCount
    mid = left + (right - left) // 2
    inversionCount += mergeSort(arr, left, mid)
    inversionCount += mergeSort(arr, mid + 1, right)
    inversionCount += merge(arr, left, mid, right)
    return inversionCount


# Driver code:
arr = [2, 4, 1, 3, 5]
arr2 = [5, 4, 3, 2, 1]
print(mergeSort(arr, 0, len(arr) - 1))
