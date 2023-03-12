class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def printStack(self):
        return self.items


stack = Stack()

stack.push(23)
stack.push(53)
stack.push(56)
stack.push(19)
stack.push(44)
stack.push(99)
stack.push(22)
stack.push(44)

print(stack.printStack())


def keepLargestOnTop(stack):
    largest = max(stack.items)
    helpingStack = Stack()

    while not stack.isEmpty():
        popped = stack.pop()
        if popped < largest:
            helpingStack.push(popped)

    while not helpingStack.isEmpty():
        stack.push(helpingStack.pop())

    stack.push(largest)

    return stack.items


print(keepLargestOnTop(stack))
