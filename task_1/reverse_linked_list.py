from linked_list import LinkedList

def reverse(list: LinkedList) -> LinkedList:
    reversed = LinkedList()

    while not list.is_empty():
        last_node = list.get_last()
        reversed.add(last_node.data)
        list.remove(node=last_node)

    return reversed


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    print(ll)
    print(reverse(ll))