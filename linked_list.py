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

    def insert_at_index(self, value, index):
        new_node = Node(value)
        cur = self.head
        cur_index = 0

        while cur is not None:
            cur = cur.next
            cur_index += 1
            if cur_index == (index - 1):
                new_node.next = cur.next
                cur.next = new_node
                break

    def pop(self):
        cur = self.head

        while cur.next is not None:
            if cur.next == None:
                cur = None
            cur = cur.next

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


sll = LinkedList()

sll.append(50)
sll.append(60)
sll.append(70)
sll.append(80)
sll.append(90)

# sll.prepend(30)
# sll.prepend(20)
# sll.prepend(10)

sll.insert_at_index(40, 4)

print(sll.pop())

sll.display()
