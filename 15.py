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

# Explanation:
# Reservoir sampling is a family of randomized algorithms
# for randomly choosing k samples from a list of n items,
# where n is either a very large or unknown number.
# Typically n is large enough that the list doesn’t fit into main memory. 

# Probablity of choosing ith element is
# = 1/i * (1 - 1/(i+1)) * (1 - 1/(i+2)) * ... * (1 - 1/(n-1)) * (1 - 1/n)
# = 1/i * i/i+1 * i+1/i+2 * ... * n-2/n-1 * n-1/n
# = 1/n

# here, 1/i = probability of choosing ith element from i elements
#     (1 - 1/(i+1)) = probability of not choosing i+1th element
#     and so on..