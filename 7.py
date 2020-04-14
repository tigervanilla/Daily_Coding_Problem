# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
# count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def count_decoding(msg, n):
    # only one way to decode a msg of length 0 or 1
    if n == 0 or n == 1:
        return 1
    
    count = 0

    # If last digit isn't zero then it can form a character alone
    # Ex. In '10' 0 can't be a character, but in '12' 2 can be B
    if msg[n - 1] > '0':
        count += count_decoding(msg, n - 1)
    
    # Check if last two digits together can make a character
    if (msg[n - 2] == '1') or (msg[n - 2] == '2' and msg[n - 1] < '7'):
        count += count_decoding(msg, n - 2)
    
    return count

msg1 = '111'
msg2 = '120'
msg3 = '130'
msg4 = '1234'
print(msg1, count_decoding(msg1, len(msg1)))
print(msg2, count_decoding(msg2, len(msg2)))
print(msg3, count_decoding(msg3, len(msg3)))
print(msg4, count_decoding(msg4, len(msg4)))