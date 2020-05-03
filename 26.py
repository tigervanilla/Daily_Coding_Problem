# This problem was asked by Google.

# Given a singly linked list and an integer k, remove the kth last element from the list.
# k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_kth_last_element(head, k):
    ptr1 = ptr2 = head
    while k > 0:
        ptr1 = ptr1.next
        k -= 1
    while ptr1.next != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    temp = ptr2.next
    ptr2.next = temp.next
    print('Deleting node with value=', temp.val)
    temp.next = None
    del temp


# Driver Code:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

remove_kth_last_element(head, 2)
while head:
    print(head.val)
    head = head.next
