class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def appendLeft(self, v):
        new_node = Node(v)
        new_node.next = self.head
        self.head = new_node

    def display(self, cur):
        if cur is not None:
            print(cur.data, end=' --> ')
            self.display(cur.next)

    def find_recursive(self, cur, v):
        if cur is None:
            return False

        if cur.data == v:
            return True
        return self.find_recursive(cur.next, v)

    def find(self, v):
        return self.find_recursive(self.head, v)


sll = SinglyLinkedList()
sll.appendLeft(20)
sll.appendLeft(15)
sll.appendLeft(10)
sll.appendLeft(5)
sll.display(sll.head)


def append(cur, v):
    if cur is None:
        return Node(v)
    n = append(cur.next, v)
    print('Currently at node', cur.data, 'n :', n)
    cur.next = n
    return cur


def insert_before(cur, search_value, value):
    if cur is None:
        return None

    if cur.data == search_value:
        new_node = Node(value)
        new_node.next = cur
        return new_node

    cur.next = insert_before(cur.next, search_value, value)

    return cur


def remove(cur, value):
    if cur is None:
        return None

    if cur.data == value:
        return cur.next

    cur.next = remove(cur.next, value)

    return cur


append(sll.head, 70)
append(sll.head, 80)
append(sll.head, 90)

insert_before(sll.head, 20, 100)
sll.display(sll.head)

remove(sll.head, 100)
sll.display(sll.head)
