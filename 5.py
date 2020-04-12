# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

def car(pair):
    def get_first(a, b):
        return a
    return pair(get_first)

def cdr(pair):
    def get_second(a, b):
        return b
    return pair(get_second)


test1 = car(cons(3, 4))
test2 = cdr(cons(3, 4))
print(test1, test2)