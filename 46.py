'''
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
'''


def longestPalindromSubstring(S):
    n = len(S)

    # matrix[i][j] is True iff S[i..j] is palindrom
    matrix = [[False]*n for i in range(n)]

    # Single character is a pallindrom
    for i in range(n):
        matrix[i][i] = True

    longestPalindrom = S[0]
    longestPalindromLength = 1

    # Check substrings of length = 2
    for i in range(n-1):
        if S[i] == S[i+1]:
            matrix[i][i+1] = True
            longestPalindrom = S[i:i+2]
            longestPalindromLength = 2
        else:
            matrix[i][i+1] = False

    # Check substrings of length > 2
    for k in range(3, n+1):     # checking substrings of length k ie 3 to n
        for i in range(n-k+1):
            for j in range(i+k-1, n):
                if S[i] == S[j] and matrix[i+1][j-1]:
                    matrix[i][j] = True
                    if k > longestPalindromLength:
                        longestPalindrom = S[i:j+1]
                        longestPalindromLength = k
                else:
                    matrix[i][j] = False

    return (longestPalindromLength, longestPalindrom)


# Driver Code:
testcases = ['GPFKFUG', 'aabcdcb', 'banana']
for tc in testcases:
    print(longestPalindromSubstring(tc))


'''
Reference:
https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
'''
