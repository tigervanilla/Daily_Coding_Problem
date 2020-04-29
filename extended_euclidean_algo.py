def GCD_extendedEuclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = GCD_extendedEuclidean(b, a % b)
    x = y1
    y = x1 - (a//b)*y1
    return gcd, x, y


# Driver code:
print('gcd=%d, x=%d, y=%d' % GCD_extendedEuclidean(7, 5))
