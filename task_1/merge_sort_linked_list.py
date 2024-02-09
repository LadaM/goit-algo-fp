from linked_list import LinkedList, Node
from numpy import random


def merge_sort_linked_list(ll: LinkedList) -> LinkedList:
    if ll.is_empty() or ll.head.next is None:
        return ll

    # Find the middle of the linked list
    middle = find_middle(ll.head)
    left_half = LinkedList(ll.head)
    right_half = LinkedList(middle.next)
    middle.next = None  # Split the linked list into two halves

    # Recursively sort the two halves
    left_sorted = merge_sort_linked_list(left_half)
    right_sorted = merge_sort_linked_list(right_half)

    # Merge the sorted halves
    sorted_list = merge(left_sorted, right_sorted)

    return sorted_list


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left, right) -> LinkedList:
    """
    Merge two sorted linked lists into a new linked list.

    Args:
    - left: The head node of the first linked list.
    - right: The head node of the second linked list.

    Returns:
    - LinkedList: A new linked list containing all the nodes from the input linked lists in sorted order.
    """
    dummy = Node(None)  # Dummy node with an empty value
    current = dummy

    while left.head and right.head:
        if left.head.data < right.head.data:
            current.next = left.head
            left.head = left.head.next
        else:
            current.next = right.head
            right.head = right.head.next

        current = current.next

    # Append the remaining nodes from either left or right
    if left.head:
        current.next = left.head
    elif right.head:
        current.next = right.head

    return LinkedList(dummy.next)  # Return the head of the merged list


if __name__ == "__main__":
    test_data = random.random_integers(1, 100, size=20)
    print("Test data:", test_data)
    ll = LinkedList()
    for d in test_data:
        ll.add(d)
    
    print("Original linked list:")
    print(ll)

    # Sort the linked list using merge sort
    sorted_ll = merge_sort_linked_list(ll)

    print("\nSorted linked list:")
    print(sorted_ll)

    # check if merge function can merge two sorted linked lists into one correctly sorted
    list1 = LinkedList()
    items1 = [3, 6, 10, 23, 89]
    for i in items1:
        list1.add(i)

    print("\nList 1:", list1)
    
    list2 = LinkedList()
    items2 = [1, 5, 8, 12, 27]
    for i in items2:
        list2.add(i)

    print("List 2:", list2)

    merged_list = merge(list1, list2)
    print("\nMerged list:", merged_list)
