# This problem was asked by Microsoft.

# Compute the running median of a sequence of numbers.
# That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# [2, 1.5, 2, 3.5, 2, 2, 2]

def insertionSort(arr, n):
    '''arr is already sorted, except the last element'''
    temp = arr[n - 1]
    hole = n - 1
    while hole > 0 and arr[hole - 1] > temp:
        arr[hole] = arr[hole - 1]
        hole -= 1
    arr[hole] = temp


def runningMedian(stream):
    '''Using insertiong sort'''
    streamSoFar, cnt = [], 0
    for num in stream:
        streamSoFar.append(num)
        cnt += 1
        insertionSort(streamSoFar, cnt)
        if cnt % 2 != 0:
            print(streamSoFar[cnt // 2])
        else:
            print((streamSoFar[cnt // 2] + streamSoFar[cnt // 2 - 1]) * 0.5)


# Driver code:
stream = [2, 1, 5, 7, 2, 0, 5]
runningMedian(stream)
