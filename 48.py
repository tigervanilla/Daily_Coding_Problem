'''
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree,
write a function to reconstruct the tree.

For example, given the following preorder traversal:
[a, b, d, e, c, f, g]
And the following inorder traversal:
[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def constructTree(root, preorder, inorder):
    i = 0
    while i < len(inorder) and inorder[i] != root.val:
        i += 1
    if len(preorder) > 0:
        root.left = Node(preorder.pop(0))
        constructTree(root.left, preorder, inorder[:i])
        if len(preorder) > 0:
            root.right = Node(preorder.pop(0))
            constructTree(root.right, preorder, inorder[i+1:])


def preorderTraversal(root):
    if not root:
        return
    print(root.val, end=',')
    preorderTraversal(root.left)
    preorderTraversal(root.right)


# Driver Code:
preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
root = Node(preorder.pop(0))
constructTree(root, preorder, inorder)
preorderTraversal(root)
print()

in2 = ['D', 'B', 'E', 'A', 'F', 'C']
pre2 = ['A', 'B', 'D', 'E', 'C', 'F']
root2 = Node(pre2.pop(0))
constructTree(root2, pre2, in2)
preorderTraversal(root2)
print()
