'''
This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and
selling that stock once.
You must buy before you can sell it.

For example, given [9,11,8,5,7,10] you should return 5, since you could buy the stock at
5 dollars and sell it at 10 dollars.
'''


def maxProfit(arr):
    n = len(arr)
    if n < 2:
        return 0
    ans = 0
    for b in range(n-1):
        for s in range(b+1, n):
            ans = max(ans, arr[s]-arr[b])
    return ans


# Driver Code:
arr = [9, 11, 8, 5, 7, 10]
print(maxProfit(arr))
