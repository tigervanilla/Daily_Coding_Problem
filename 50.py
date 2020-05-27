'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def evaluate(root):
    if not root:
        return
    if not root.left and not root.right:
        return root.val
    l = evaluate(root.left)
    r = evaluate(root.right)
    if root.val == '+':
        return l+r
    elif root.val == '-':
        return l-r
    elif root.val == '*':
        return l*r
    elif root.val == '/':
        return l/r


# Driver Code:
root = Node('*')
root.left = Node('+')
root.right = Node('+')
root.left.left = Node(3)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(5)
print(evaluate(root))
