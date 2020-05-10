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


class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def insert(self, val):
        self.heap.append(val)
        i = self.size() - 1
        while i > 0:
            parent = (i - 1) // 2
            if val > self.heap[parent]:
                return
            self.heap[i] = self.heap[parent]
            self.heap[parent] = val
            i = parent

    def pop(self):
        ans = self.peek()
        if self.size() > 1:
            self.heap[0] = self.heap.pop()
            i, n = 0, self.size() - 1
            while i < n:
                left, right, smallest = 2*i + 1, 2*i + 2, i
                if left <= n and self.heap[left] < self.heap[smallest]:
                    smallest = left
                if right <= n and self.heap[right] < self.heap[smallest]:
                    smallest = right
                if i == smallest:
                    break
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
        return ans

    def peek(self):
        return self.heap[0]

    def display(self):
        print(self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def insert(self, val):
        self.heap.append(val)
        i = self.size() - 1
        while i > 0:
            parent = (i-1) // 2
            if val <= self.heap[parent]:
                return
            self.heap[i] = self.heap[parent]
            self.heap[parent] = val
            i = parent

    def pop(self):
        ans = self.peek()
        if self.size() > 1:
            self.heap[0] = self.heap.pop()
            i, n = 0, self.size() - 1
            while i < n:
                left, right, largest = 2*i + 1, 2*i + 2, i
                if left <= n and self.heap[left] > self.heap[largest]:
                    largest = left
                if right <= n and self.heap[right] > self.heap[largest]:
                    largest = right
                if i == largest:
                    break
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
        return ans

    def peek(self):
        return self.heap[0]

    def display(self):
        print(self.heap)


def runningMedian2_helper(item, medianSoFar, leftMaxheap, rightMinheap):
    if leftMaxheap.size() == rightMinheap.size():
        if item < medianSoFar:
            leftMaxheap.insert(item)
            return leftMaxheap.peek()
        else:
            rightMinheap.insert(item)
            return rightMinheap.peek()
    elif leftMaxheap.size() > rightMinheap.size():
        if item < medianSoFar:
            rightMinheap.insert(leftMaxheap.pop())
            leftMaxheap.insert(item)
        else:
            rightMinheap.insert(item)
        return (leftMaxheap.peek() + rightMinheap.peek()) / 2
    else:
        if item < medianSoFar:
            leftMaxheap.insert(item)
        else:
            leftMaxheap.insert(rightMinheap.pop())
            rightMinheap.insert(item)
        return (leftMaxheap.peek() + rightMinheap.peek()) / 2


def runningMedian2(stream):
    '''
    Using minheap on left side of running median
    and maxheap on right side of running median
    '''
    leftMaxheap, rightMinheap = MaxHeap(), MinHeap()
    medianSoFar = 0
    for item in stream:
        medianSoFar = runningMedian2_helper(item, medianSoFar, leftMaxheap, rightMinheap)
        print(medianSoFar)


# Driver code:
stream = [2, 1, 5, 7, 2, 0, 5]
runningMedian(stream)
runningMedian2(stream)
