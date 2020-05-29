'''
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache.
It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.

get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''


class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRU:
    def __init__(self, size):
        self.cache = {}
        self.cacheSize = size
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            return self.cache[key].val

    def setValue(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(key)
        elif len(self.cache) == self.cacheSize:
            node = self.head.next
            self.cache.pop(node.key)
            self.remove(node)
            self.cache[key] = self.add(key)
        else:
            self.cache[key] = self.add(key)

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        # self.cache.pop(node.val)
        del node

    def add(self, key):
        node = Node(key, key)
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node
        return node


# Driver Code
myLRU = LRU(3)
for item in [1, 2, 3, 4, 2, 4, 5]:
    myLRU.setValue(item)
    print(myLRU.cache.keys())
