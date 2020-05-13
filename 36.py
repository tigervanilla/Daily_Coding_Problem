# This problem was asked by Dropbox.

# Given the root to a binary search tree, find the second largest node in the tree.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def secondLargestNodeInBST(root, c):
    '''
    Use reverse inorder traversal
    right -> root -> left
    '''
    if not root or c[0] >= 2:
        return

    if root.right:
        secondLargestNodeInBST(root.right, c)

    c[0] += 1
    if c[0] == 2:
        print(root.val)
        return

    if root.left:
        secondLargestNodeInBST(root.left, c)


# Driver Code:
# Let us create following BST
#         50
#       /   \
#    30     70
#   / \     / \
#  20 40   60 80

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

secondLargestNodeInBST(root, [0])
