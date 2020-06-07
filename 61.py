'''
Implement integer exponentiation.
That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''


def pow(x, y):
    if y == 0:
        return 1
    temp = pow(x, y//2)
    if y % 2 == 0:
        return temp*temp
    else:
        return x*temp*temp


# Driver Code:
print(pow(2, 10))
print(pow(5, 5))
