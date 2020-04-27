# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node.
# The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_beginning(val, head):
    n = Node(val)
    n.next = head
    return n


def print_linked_list(head):
    while head:
        print(head.value, end='-->')
        head = head.next
    print(head)


def find_intersection(head1, head2):
    ptr1, ptr2 = head1, head2
    cnt1, cnt2 = 0, 0
    while ptr1:
        cnt1 += 1
        ptr1 = ptr1.next
    while ptr2:
        cnt2 += 1
        ptr2 = ptr2.next

    ptr1, ptr2 = head1, head2
    if cnt1 > cnt2:
        diff = cnt1 - cnt2
        while diff:
            ptr1 = ptr1.next
            diff -= 1
    elif cnt1 < cnt2:
        diff = cnt2 - cnt1
        while diff:
            ptr2 = ptr2.next
            diff -= 1

    while ptr1 and ptr2:
        if ptr1.value == ptr2.value:
            print(ptr1.value)
            break
        ptr1, ptr2 = ptr1.next, ptr2.next


linked_list1 = insert_beginning(10, None)
linked_list1 = insert_beginning(8, linked_list1)
linked_list1 = insert_beginning(7, linked_list1)
linked_list1 = insert_beginning(3, linked_list1)

linked_list2 = insert_beginning(10, None)
linked_list2 = insert_beginning(8, linked_list2)
linked_list2 = insert_beginning(1, linked_list2)
linked_list2 = insert_beginning(99, linked_list2)

linked_list3 = insert_beginning(10, None)
linked_list3 = insert_beginning(1, linked_list3)
linked_list3 = insert_beginning(4, linked_list3)

linked_list4 = insert_beginning(14, None)
linked_list4 = insert_beginning(12, linked_list4)
linked_list4 = insert_beginning(10, linked_list4)
linked_list4 = insert_beginning(1, linked_list4)
linked_list4 = insert_beginning(3, linked_list4)
linked_list4 = insert_beginning(8, linked_list4)

linked_list5 = insert_beginning(14, None)
linked_list5 = insert_beginning(12, linked_list5)
linked_list5 = insert_beginning(4, linked_list5)

print_linked_list(linked_list1)
print_linked_list(linked_list2)
print_linked_list(linked_list3)
print_linked_list(linked_list4)
print_linked_list(linked_list5)

find_intersection(linked_list1, linked_list2)
find_intersection(linked_list1, linked_list3)
find_intersection(linked_list4, linked_list5)
