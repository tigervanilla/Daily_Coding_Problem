'''
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack

pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return null.

max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
'''


class Stack:
    def __init__(self):
        '''
        main is used as the main stack
        maxTrack is used to track the max element so far
        '''
        self.main = []
        self.maxTrack = []

    def push(self, element):
        self.main.append(element)
        if len(self.main) == 1:
            self.maxTrack.append(element)
        elif element >= self.maxTrack[-1]:
            self.maxTrack.append(element)
        else:
            self.maxTrack.append(self.maxTrack[-1])

    def pop(self):
        if len(self.main) == 0:
            return None
        self.maxTrack.pop()
        return self.main.pop()

    def max(self):
        if len(self.main) == 0:
            return None
        return self.maxTrack[-1]


# Driver code:
myStack = Stack()
arr = [4, 2, 14, 1, 18]
for i in range(len(arr)):
    myStack.push(arr[i])
    print('Push =', arr[i], ' Max =', myStack.max())
print('------------')
for i in range(len(arr)):
    print('Pop =', myStack.pop(), ' Max =', myStack.max())
