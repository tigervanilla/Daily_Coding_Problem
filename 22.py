# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words(no spaces),
# return the original sentence in a list.
# If there is more than one possible reconstruction, return any of them.
# If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

dictionary1 = {'quick', 'brown', 'the', 'fox'}
dictionary2 = {'bed', 'bath', 'bedbath', 'and', 'beyond'}


def makeSentence(dictionary, string, result):
    n = len(string)
    for i in range(1, n+1):
        prefix = string[:i]
        if prefix in dictionary:
            result.append(prefix)
            return result if i == n else makeSentence(dictionary, string[i:], result)

# Driver Code:
tc1 = makeSentence(dictionary1, 'thequickbrownfox', [])
print(' '.join(tc1))
tc2 = makeSentence(dictionary2, 'bedbathandbeyond', [])
print(' '.join(tc2))
