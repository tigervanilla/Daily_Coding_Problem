'''
This problem was asked by Apple.

Implement a queue using two stacks.

Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and
dequeue, which removes it.
'''


from collections import deque


class Queue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def enqueue(self, item):
        self.s1.append(item)

    def deque(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return 'Queue is empty'
        if len(self.s2) == 0:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        return self.s2.pop()


# Driver Code
myQueue = Queue()
print(myQueue.deque())
for i in [1, 2, 3]:
    myQueue.enqueue(i)
print(myQueue.deque())
for i in [7, 8]:
    myQueue.enqueue(i)
print(myQueue.deque())
print(myQueue.deque())
print(myQueue.deque())
