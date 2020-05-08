# This problem was asked by Jane Street.

# Suppose you are given a table of currency exchange rates, represented as a 2D array.
# Determine whether there is a possible arbitrage:
# that is, whether there is some sequence of trades you can make, starting with some amount A of any currency,
# so that you can end up with some amount greater than A of that currency.

# There are no transaction costs and you can trade fractional quantities.

from math import log, inf


def negateLog(matrix):
    '''take log of each rate in matrix and negate it'''
    result = [[-1*log(el) for el in row] for row in matrix]
    return result


def arbitrage(rateMatrix):
    '''Using Bellman Ford algo to detect negetive weight cycle'''
    transformedGraph = negateLog(rateMatrix)
    n = len(transformedGraph)
    minDistance = [inf]*n
    minDistance[0] = 0      # Taking 0th element as source

    # Iterate |V-1| times and relax edges
    for i in range(n-1):
        for srcIndx in range(n):
            for destIndx in range(n):
                if minDistance[destIndx] > minDistance[srcIndx] + transformedGraph[srcIndx][destIndx]:
                    minDistance[destIndx] = minDistance[srcIndx] + transformedGraph[srcIndx][destIndx]

    # If we can still relax edges, then we have a negative cycle
    for srcIndx in range(n):
        for destIndx in range(n):
            if minDistance[destIndx] > minDistance[srcIndx] + transformedGraph[srcIndx][destIndx]:
                return True     # Arbitrage is possible
    return False


def arbitrage2(rateMatrix, currencySymbols):
    '''If possible, then print the arbitrage cycle'''
    transformedGraph = negateLog(rateMatrix)
    n = len(transformedGraph)
    minDistance = [inf]*n
    minDistance[0] = 0
    predecessor = [-1]*n    # Predecessor chain to print the cycle.

    for i in range(n-1):
        for srcIndx in range(n):
            for destIndx in range(n):
                if minDistance[destIndx] > minDistance[srcIndx] + transformedGraph[srcIndx][destIndx]:
                    minDistance[destIndx] = minDistance[srcIndx] + transformedGraph[srcIndx][destIndx]
                    predecessor[destIndx] = srcIndx

    for srcIndx in range(n-1):
        for destIndx in range(n-1):
            if minDistance[destIndx] > minDistance[srcIndx] + transformedGraph[srcIndx][destIndx]:
                cycle = [destIndx, srcIndx]
                while predecessor[srcIndx] not in cycle:
                    cycle.append(predecessor[srcIndx])
                    srcIndx = predecessor[srcIndx]
                cycle.append(predecessor[srcIndx])
                print('Arbitrage Opportunity:')
                print('->'.join([currencySymbols[i] for i in cycle]))
                return True


# Driver Code:
rates = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]
currencySymbols = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')
print(arbitrage2(rates, currencySymbols))


# Explanation:
# Arbitrage opportunities arise when a cycle is determined such that the edge weights satisfy the following expression
# w1 * w2 * w3 * … * wn > 1

# The above constraint of finding the cycles is harder in graphs.
# Instead we must transform the edge weights of the graph such that the standard graph algorithms can be applied.

# Let’s take the logarithm on both sides, such that
# log(w1) + log(w2) + log(w3) + … + log(wn) > 0

# Taking the negative log, this becomes
# (-log(w1)) + (-log(w2)) + (-log(w3)) + … + (-log(wn)) < 0

# Therefore we can conclude that if we can find a cycle of vertices such that
# the sum of their weights is negative,
# then we can conclude there exists an opportunity for currency arbitrage.
# Luckily, Bellman-Ford algorithm can be used to easily detect negative weight cycles in O( | V*E|) time.

# To print the cycle we can use predecessor chain.
# Now that we have an edge which can be further relaxed,
# we have found the source & destination vertex of such an edge.
# Start from the source vertex and go backwards until you see the source vertex again
# or any other vertex that predecessor chain has already shown us while printing the negative weighted cycle.

# References:
# https://www.youtube.com/watch?v=FtN3BYH2Zes
# https://medium.com/@anilpai/currency-arbitrage-using-bellman-ford-algorithm-8938dcea56ea
# https://www.dailycodingproblem.com/blog/how-to-find-arbitrage-opportunities-in-python
