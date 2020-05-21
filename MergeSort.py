def merge(arr, l, m, r):
    temp = []
    i, j = l, m + 1
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= m:
        temp.append(arr[i])
        i += 1
    while j <= r:
        temp.append(arr[j])
        j += 1
    for k in range(l, r + 1):
        arr[k] = temp[k - l]


def mergeSort(arr, l, r):
    if l >= r:
        return

    m = l + (r - l) // 2
    mergeSort(arr, l, m)
    mergeSort(arr, m + 1, r)
    merge(arr, l, m, r)


# Driver Code:
arr = [38, 27, 43, 3, 9, 82, 10]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
