# def is_match(regex, string):
#     i = j = 0
#     n, m = len(regex), len(string)
#     while i < n and j < m:
#         if regex[i] == string[j]:
#             i, j = i+1, j+1
#         elif regex[i] == '.':
#             i, j = i+1, j+1
#         elif regex[i] == '*':
#             i += 1
#             if i == n:
#                 return True
#             while i < n and regex[i] == '.':
#                 i += 1
#             while i < n and j < m and regex[i] != string[j]:
#                 j += 1
#             if j==m:
#                 return False
#         elif regex[i] != '.' and regex[i] != '*' and regex[i] != string[j]:
#             return False
#     if i<n and j==m:
#         return False
#     if i==n and j<m:
#         return True if regex[i-1]=='*' else False
    # if i<n and j==m:
    #     return False
    # return True

# print(is_match('ra.', 'ray'))
# print(is_match('ra.', 'raymond'))
# print(is_match('.*at', 'chat'))
# print(is_match('.*at', 'chats'))
# print(is_match('*at*', 'at'))
# print(is_match('*at*', '123at'))
# print(is_match('*at*', 'at123'))
# print(is_match('*at*', '123at123'))
# print(is_match('*at*5', '123at1'))
# print(is_match('*at*15', '123at1'))