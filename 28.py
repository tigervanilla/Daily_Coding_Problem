# This problem was asked by Palantir.

# Write an algorithm to justify text. Given a sequence of words and an integer line length k,
# return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word.
# Pad extra spaces when necessary so that each line has exactly length k.
# Spaces should be distributed as equally as possible,
# with the extra spaces, if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand side with spaces.

# Each word is guaranteed not to be longer than k.

# For example,
# given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly



def justify_text_util(line, remaining_space):
    line_length = len(line)
    guaranteed_spaces = remaining_space//(line_length - 1)
    extra_spaces_participants = remaining_space % (line_length - 1)
    ans = ''
    for i in range(line_length - 1):
        if i < extra_spaces_participants:
            ans = ans + line[i] + '='*(1 + guaranteed_spaces)
        else:
            ans = ans + line[i] + '='*guaranteed_spaces
    ans += line[-1]
    return ans


def justify_text(words, K):
    result, line, remaining_space = [], [], K
    for word in words:
        line_length, word_length = len(line), len(word)
        if line_length == 0:
            line.append(word)
            remaining_space -= word_length
        elif remaining_space > word_length + (line_length - 1): # line_length-1 is for space b/w words
            line.append(word)
            remaining_space -= word_length
        else:
            result.append(justify_text_util(line, remaining_space))
            line, remaining_space = [], K
            line.append(word)
            remaining_space -= word_length
    if line:
        result.append(justify_text_util(line, remaining_space))
    return result


words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(justify_text(words, 16))