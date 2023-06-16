class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return "{value:% s, next:% s}" % (self.value, self.next)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def find(self, value):
        cur = self.head

        while cur is not None:
            if cur.value == value:
                break
            cur = cur.next

        if cur is None:
            print(f'Value not present: {value}')
            return

        return cur.value

    def insert_at_index(self, index, value):
        new_node = Node(value)
        cur = self.head
        cur_index = 0

        while cur is not None:
            if cur_index == (index - 1):
                break

            cur = cur.next
            cur_index += 1

        new_node.next = cur.next
        cur.next = new_node

    def insert_after_value(self, value, value_to_add):
        if self.head is None:
            print(f'Error: {value} not in the list')
            return

        new_node = Node(value_to_add)

        cur = self.head

        while cur.next is not None:
            if cur.value == value:
                break

            cur = cur.next

        if cur.value != value:
            print(f'Error: {value} not in the list')
            return

        new_node.next = cur.next
        cur.next = new_node

    def insert_before_value(self, value, value_to_add):
        if self.head is None:
            print(f'Error: {value} not in the list')
            return

        new_node = Node(value_to_add)

        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return

        cur = self.head  # insert_before_value(20, 80)

        while cur.next is not None:
            if cur.next.value == value:
                break

            cur = cur.next

        if cur is None:
            print(f'Error: {value} not in the list')
            return

        new_node.next = cur.next
        cur.next = new_node

    def pop(self, index):  # pop(3)
        if self.head is None:
            print(f'Error: index out of range: {index}')
            return

        if index == 0:
            self.head = self.head.next

        cur = self.head
        cur_index = 0

        while cur.next is not None:
            if cur_index == (index - 1):
                break

            cur = cur.next
            cur_index += 1

        if cur.next is None:
            print(f'Error: index out of range: {index}')
            return

        cur.next = cur.next.next

    def remove(self, value):  # remove(20)
        if self.head is None:
            print(f'List is empty')
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        cur = self.head

        while cur.next is not None:
            if cur.next.value == value:
                break

            cur = cur.next

        if cur.next.value != value:
            print(f'Error: {value} not in the list')
            return

        cur.next = cur.next.next

        return cur

    def size(self):
        cur = self.head

        while cur is not None:
            cur = cur.next
            self.length += 1

        return self.length

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        print(self.head)

        print("\n")

        cur = self.head
        while cur is not None:
            print(cur.value, end=" --> ")
            cur = cur.next

        print("\n")


sll = LinkedList()

sll.append(5)
sll.append(6)
sll.append(7)
sll.append(8)

sll.display()
