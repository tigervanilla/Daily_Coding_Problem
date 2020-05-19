'''
This problem was asked by Google.

Given a list of integers S and a target number k,
write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list.
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24
return [12, 9, 2, 1] since it sums up to 24.
'''


def utilSubsetWithSumK(arr, i, K, ans):
    if K == 0:
        return True

    if i < 0 and K != 0:
        return False

    ans.append(arr[i])
    sumWithI = utilSubsetWithSumK(arr, i-1, K-arr[i], ans)
    if sumWithI:
        return True
    ans.pop()
    sumWithoutI = utilSubsetWithSumK(arr, i-1, K, ans)
    return sumWithoutI


def subsetWithSumK(arr, K):
    ans = []
    isPossible = utilSubsetWithSumK(arr, len(arr)-1, K, ans)
    if isPossible:
        print(ans)
    else:
        print('No Subset Found')


# Driver code:
subsetWithSumK([12, 1, 61, 5, 9, 3], 24)
subsetWithSumK([12, 1, 61, 5, 9, 3], 89)