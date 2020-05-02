# This problem was asked by Facebook.

# Implement regular expression matching with the following special characters:
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and
# returns whether or not the string matches the regular expression.

# For example, given the regular expression "ra." and the string "ray", your function should return true.
# The same regular expression on the string "raymond" should return false.

# Given the regular expression ".*at" and the string "chat", your function should return true.
# The same regular expression on the string "chats" should return false.


def is_match(regex, string):
    n, m = len(regex), len(string)
    i = j = 0
    while i < n and j < m:
        if (regex[i] == string[j]) or regex[i] == '.':
            i, j = i+1, j+1
        elif regex[i] == '*':
            if regex[i-1] == string[j]:
                j += 1
            elif i+1 < n and (regex[i+1] == string[j]):
                i, j = i+2, j+1
            elif regex[i-1] == '.':
                j += 1
            elif i+1 < n and (regex[i+1] == '.'):
                i, j = i+2, j+1
            else:
                return False
        elif regex[i] != string[j]:
            return False
    if j == m and i == n:
        return True
    if j == m and i == n-1 and regex[-1] == '*':
        return True
    return False


# Driver code:
test_cases = [
    {'regex': 'a', 'string': 'aa'},
    {'regex': 'a*', 'string': 'aa'},
    {'regex': '.*', 'string': 'ab'},
    {'regex': 'mis*is*p*', 'string': 'mississippi'},
    {'regex': 'ra.', 'string': 'ray'},
    {'regex': 'ra.', 'string': 'raymond'},
    {'regex': '.*at', 'string': 'chat'},
    {'regex': '.*at', 'string': 'chats'},
]

for test in test_cases:
    regex, string = test.values()
    print(is_match(regex, string))
