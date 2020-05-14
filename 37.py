'''
This problem was asked by Google

The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set

For example, given the set {1, 2, 3},
it should return { {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3} }
'''

def powerSet(arr, ss):
    ''' Recursive solution '''
    if not arr:
        print('{' + ss + ' }', end=', ')
        return

    powerSet(arr[1:], ss)
    powerSet(arr[1:], ss + ' ' + str(arr[0]))


def powerSet2(arr):
    ''' Iterative solution '''
    n = len(arr)
    for i in range(2**n):
        subset = '{'
        for j in range(n):
            if i & (1 << j) != 0:
                subset = subset + ' ' + str(arr[n-1-j])
        subset += ' }'
        print(subset, end=' ')


# Driver code:
powerSet2([1, 2, 3])
print()
