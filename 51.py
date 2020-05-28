'''
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''

from random import randint


def shuffle(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        j = randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# Driver Code
arr = [i for i in range(1, 53)]
print('before shuffling', arr)
print('after shuffling', arr)
