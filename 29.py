# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.


def run_length_encoding(plaintext):
    count = 1
    for i in range(1, len(plaintext)):
        if plaintext[i] != plaintext[i-1]:
            print(count, plaintext[i-1], sep='', end='')
            count = 1
        else:
            count += 1
    print(count, plaintext[-1], sep='')


def run_length_decoding(ciphertext):
    i, n = 1, len(ciphertext)
    while i < n:
        print(ciphertext[i] * int(ciphertext[i-1]), end='')
        i += 2


# Driver code:
run_length_encoding('AAAABBBCCDAA')
run_length_decoding('4A3B2C1D2A')
