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


myMaxheap = MaxHeap()
for i in range(1, 7):
    myMaxheap.insert(i)
myMaxheap.display()
for i in range(1, 7):
    print(myMaxheap.pop())
