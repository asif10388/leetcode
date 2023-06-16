# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#         self.prev = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0

#     def append(self, value):
#         new_node = Node(value)

#         if self.head is None:
#             self.head = new_node
#             return

#         cur = self.head

#         while cur.next is not None:
#             cur = cur.next

#         cur.next = new_node
#         new_node.prev = cur
#         new_node.next = None

#     def add_node_after_value(self, given_value, new_value):

#         if self.head is None:
#             print(f'Error: List is empty')

#         new_node = Node(new_value)

#         cur = self.head

#         while cur.next is not None:
#             if cur.value == given_value:
#                 break

#             cur = cur.next

#         if cur.value != given_value:
#             print(f'Value does not exist')

#         new_node.next = cur.next
#         new_node.prev = cur
#         cur.next = new_node
#         if new_node.next is not None:
#             new_node.next.prev = new_node

#     def display(self):
#         if self.head is None:
#             print("List is empty")
#             return

#         cur = self.head

#         while cur is not None:
#             print(f'<-- {cur.value} --> ', end="")
#             cur = cur.next


# sll = LinkedList()

# sll.append(5)
# sll.append(6)
# sll.append(7)
# sll.append(8)

# sll.add_node_after_value(5, 10)

# sll.display()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_LL = LinkedList(4)

print(my_LL.head.value)
