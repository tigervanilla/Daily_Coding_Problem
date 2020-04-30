# This problem was asked by Google.

# Implement locking in a binary tree.
# A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

# is_locked(), which returns whether the node is locked

# lock(), which attempts to lock the node.
# If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.

# unlock(), which unlocks the node.
# If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

# You may augment the node to add parent pointers or any other property you would like.
# You may assume the class is used in a single-threaded program,
# so there is no need for actual locks or mutexes.
# Each method should run in O(h), where h is the height of the tree.


class Locking_Binary_Tree_Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.is_node_locked = False
        self.locked_descendant_count = 0

    def is_locked(self):
        return self.is_node_locked

    def can_lock_or_unlock(self):
        if self.locked_descendant_count > 0:
            return False
        p = self.parent
        while p:
            if p.is_node_locked:
                return False
            p = p.parent
        return True

    def lock(self):
        if not self.can_lock_or_unlock():
            return False
        self.is_node_locked = True
        p = self.parent
        while p:
            p.locked_descendant_count += 1
            p = p.parent
        return True

    def unlock(self):
        if not self.can_lock_or_unlock():
            return False
        self.is_node_locked = False
        p = self.parent
        while p:
            p.locked_descendant_count -= 1
            p = p.parent
        return True


# References:
# https://www.dailycodingproblem.com/blog/lockable-binary-trees/
# https://www.geeksforgeeks.org/locking-and-unlocking-of-resources-in-the-form-of-n-ary-tree/
