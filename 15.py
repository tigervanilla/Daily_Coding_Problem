# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

from random import randint

def pick_random(big_stream):
    count, random_element = 0, None
    for ele in big_stream:
        count += 1
        if count == 1:
            random_element = ele
        elif randint(1, count) == count:
            random_element = ele
    return random_element

# Driver code
data_stream = [i for i in range(1000)]
random_element = pick_random(data_stream)
print(random_element)
            