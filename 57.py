'''
This problem was asked by Amazon.

Given a string s and an integer k,
break up the string into multiple lines such that each line has a length of k or less.
You must break it up so that words don't break across lines.
Each line has to have the maximum possible amount of words.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string
and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"].
No string in the list has a length of more than 10.
'''


def split(S, K):
    ans = []
    n, i, j = len(S), 0, 0
    while i < n:
        j = i+9
        if j >= n:
            ans.append(S[i:])
            i = j+1
        elif S[j] == ' ':
            ans.append(S[i:j])
            i = j+1
        elif S[j+1] == ' ':
            ans.append(S[i:j+1])
            i = j+2
        else:
            while j >= i and S[j] != ' ':
                j -= 1
            if j < i:
                return None
            ans.append(S[i:j])
            i = j+1
    return ans


# Driver Code:
S = 'the quick brown fox jumps over the lazy dog'
print(split(S, 10))
print(split('ABCDEFGHIJKLMNOP', 10))
