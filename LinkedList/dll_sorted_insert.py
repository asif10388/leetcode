class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = new_node
        new_node.prev = cur
        new_node.next = None

    def insert_sorted(self, value):

        if self.head is None:
            print(f'Error: List is empty')

        new_node = Node(value)

        cur = self.head

        while cur is not None:
            if cur.value < value and cur.next.value > value:
                new_node.next = cur.next
                new_node.prev = cur
                cur.next = new_node
                if new_node.next is not None:
                    new_node.next.prev = new_node
                break

            cur = cur.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        cur = self.head

        while cur is not None:
            print(f'<-- {cur.value} --> ', end="")
            cur = cur.next


dll = DoublyLinkedList()

dll.append(3)
dll.append(5)
dll.append(8)
dll.append(10)
dll.append(12)

dll.insert_sorted(11)

dll.display()
