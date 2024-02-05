class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, head=None):
        if head is None:
            self.head = None
        elif type(head) is Node:
            self.head = head
        else:
            self.head = Node(head)

    def is_empty(self):
        return self.head is None
    
    
    def add(self, data):
        if self.is_empty():
            self.head = Node(data)
            return
        
        node = self.get_last()
        node.next = Node(data)
    

    def get_last(self):
        if self.is_empty():
            return None
        node = self.head
        while node.next:
            node = node.next
        return node
    
    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def remove(self, data = None, node = None):
        if self.is_empty():
            print("List is empty")
            return
        if data is None and node is None:
            print("Provide data or node")
            return
        data = data if data is not None else node.data

        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next


    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next


    def __str__(self):
        return "Linked list is empty" if self.is_empty() else ' -> '.join([str(x) for x in self])
    

if __name__ == "__main__":
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    print(ll)
    ll.remove()
    while not ll.is_empty():
        print(ll.get_last().data)
        last_node = ll.get_last()
        ll.remove(node=last_node)
    print(ll)
