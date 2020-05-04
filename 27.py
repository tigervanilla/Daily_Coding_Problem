# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced.

# For example, given the string '([])[]({})', you should return true.
# Given the string '([)]' or '((()', you should return false.

from collections import deque


def balanced_brackets(string):
    openening_brackets = {'(', '{', '['}
    closing_brackets = {')', '}', ']'}
    stack = deque()
    for ch in string:
        if ch in openening_brackets:
            stack.append(ch)
        elif ch in closing_brackets:
            if not len(stack):
                return False
            op = stack.pop()
            if (op == '(' and ch != ')') or (op == '{' and ch != '}') or (op == '[' and ch != ']'):
                return False
    if len(stack):
        return False
    return True


# Driver code:
testcases = ['([])[]({})', '([)]', '((()', '', ']', '{']
for tc in testcases:
    print(tc, balanced_brackets(tc))
