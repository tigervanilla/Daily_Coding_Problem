def GCD_extendedEuclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = GCD_extendedEuclidean(b, a % b)
    x = y1
    y = x1 - (a//b)*y1
    return gcd, x, y


# Driver code:
print('gcd=%d, x=%d, y=%d' % GCD_extendedEuclidean(7, 5))


# Explanation:
# The extended euclidean algorithm says that
# GCD(a, b) = ax + by         ----(1)

# We know that GCD(a, b) = GCD(b, a % b)
# GCD(a, b) = GCD(b, a % b)
#           = b*x1 + (a % b)*y1
#           = b*x1 + (a - floor(a/b)*b)*y1
#           = a*y1 + (x1 - floor(a/b)*y1)       -----(2)

# From (1) and (2):
# x = y1
# y = x1 - floor(a/b)*y1
