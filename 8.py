# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

# This tree has 3 unival subtrees: the two ‘a’ leaves and the one ‘A’ leaf.
#   a
#  / \
# a   a
#     /\
#    a  a
#        \
#         A

# This tree has 5 unival subtrees: the leaf at ‘c’, and every ‘b’.
#   a
#  / \
# c   b
#     /\
#    b  b
#         \
#          b

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Approach 1,  O(n^2) 
def is_unival(root, value):
    if root == None:
        return True
    if root.value == value:
        return is_unival(root.left, value) and is_unival(root.right, value)
    return False

def count_unival_subtree(root):
    if root == None:
        return 0
    left = count_unival_subtree(root.left)
    right = count_unival_subtree(root.right)
    if is_unival(root, root.value):
        return 1 + left + right
    else:
        return left + right
# Approach 1 end

# Approach 2, O(n)
def find_number_of_univalue_subtree(root):
    # returns number of unival subtrees, and whether it is itself a unival subtree.
    if root == None:
        return 0, True

    left_count, is_left_subtree_univalue = find_number_of_univalue_subtree(root.left)
    right_count, is_right_subtree_univalue = find_number_of_univalue_subtree(root.right)
    total_count = left_count + right_count

    if is_left_subtree_univalue and is_right_subtree_univalue:
        if root.left != None and root.value != root.left.value:
            return total_count, False # current tree IS NOT UNIVALUED
        if root.right != None and root.value != root.right.value:
            return total_count, False # current tree IS NOT UNIVALUED
        return 1 + total_count, True # current tree IS UNIVALUED
    return total_count, False # current tree IS NOT UNIVALUED

# Approach 2 end

# Driver code to check program
root = Node('a')
root.left = Node('c')
root.right = Node('b')
root.right.left = Node('b')
root.right.right = Node('b')
root.right.right.right = Node('b')

print(count_unival_subtree(root))
print(find_number_of_univalue_subtree(root))

root2 = Node(0)
root2.left = Node(1)
root2.right = Node(0)
root2.right.right = Node(0)
root2.right.left = Node(1)
root2.right.left.left = Node(1)
root2.right.left.right = Node(1)

print(count_unival_subtree(root2))
print(find_number_of_univalue_subtree(root2))

root3 = Node('a')
root3.left = Node('a')
root3.right = Node('a')
root3.right.left = Node('a')
root3.right.right = Node('a')
root3.right.right.right = Node('A')

print(count_unival_subtree(root3))
print(find_number_of_univalue_subtree(root3))