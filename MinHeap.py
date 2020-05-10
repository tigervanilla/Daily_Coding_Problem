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

myMinheap = MinHeap()
for i in range(6, 0, -1):
    myMinheap.insert(i)
myMinheap.display()
for i in range(6):
    print(myMinheap.pop())