# This problem was asked by Google.

# The edit distance between two strings refers to the minimum number of
# character insertions, deletions, and substitutions required to change one string to the other.
# For example, the edit distance between “kitten” and “sitting” is three:
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.


def editDistance(str1, str2):
    l1, l2 = 1+len(str1), 1+len(str2)
    dp = [[0]*l2 for i in range(l1)]
    for i in range(l1):
        for j in range(l2):
            if i == 0:      # str1 is empty
                dp[i][j] = j
            elif j == 0:    # str2 is empty
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:    # ith char of str1 matches jth char of str2
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insertion
                                   dp[i-1][j],      # Deletion
                                   dp[i-1][j-1]     # Modification
                                   )
    return dp[-1][-1]


# Space optimized solution
def editDistance2(str1, str2):
    l1, l2 = 1 + len(str1), 1 + len(str2)
    dp = [[0]*l1 for i in range(2)]    # row for str2, column for str1
    for j in range(l1):
        dp[0][j] = j
    for i in range(1, l2):
        for j in range(l1):
            if j == 0:
                dp[i % 2][j] = i
            elif str1[j-1] == str2[i-1]:
                dp[i % 2][j] = dp[(i-1) % 2][j-1]
            else:
                dp[i % 2][j] = 1+min(dp[(i-1) % 2][j],    # Insertion
                                     dp[i % 2][j-1],      # Deletion
                                     dp[(i-1) % 2][j-1])  # Modification
    return dp[(l2-1) % 2][-1]


# Driver Code:
print(editDistance('kitten', 'sitting'), editDistance2('kitten', 'sitting'))
print(editDistance('sunday', 'saturday'), editDistance2('sunday', 'saturday'))
print(editDistance('food', 'money'), editDistance2('food', 'money'))


# Reference:
# https://www.geeksforgeeks.org/edit-distance-dp-5/
