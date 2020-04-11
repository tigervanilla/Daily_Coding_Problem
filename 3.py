# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

end_marker = '-'

def serialize(root):
    if root == None:
        return end_marker
    tree_string = root.val + serialize(root.left) + serialize(root.right)
    return tree_string

def deserialize(root, tree_string, index):
    if tree_string[index] == end_marker:
        return
    root = Node(tree_string[index])
    deserialize(root.left, tree_string, index + 1)
    deserialize(root.right, tree_string, index + 2)
