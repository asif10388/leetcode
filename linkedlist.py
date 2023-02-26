# 10 --> 15 --> 20

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f' {self.data}, {self.next}]'


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return

        currentNode = self.head

        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = newNode

    def prepend(self, value):
        pass


myLinkedList = LinkedList()

print(myLinkedList.__dict__)

myLinkedList.append(10)

print(myLinkedList.__dict__)

myLinkedList.append(20)

print(myLinkedList.__dict__)

myLinkedList.append(30)

print(myLinkedList.__dict__)

myLinkedList.append(40)

print(myLinkedList.__dict__)

myLinkedList.append(50)

print(myLinkedList.__dict__)

myLinkedList.append(60)

print(myLinkedList.__dict__)


# def asciiProgressBar(percentage):
#     digits = [*str(int(percentage))]

#     if len(digits) > 2 and digits[0] == "1":
#         digit = int(digits[0] + "0")
#     else:
#         digit = int(digits[0])

#     bar = digit * "+" + (10 - digit) * "."

#     return bar
