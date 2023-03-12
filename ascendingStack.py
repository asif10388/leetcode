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

    def pushStack(self, value):
        helpingStack = Stack()

        if self.isEmpty():
            self.push(value)
        else:
            while not self.isEmpty() and value < self.peek():
                helpingStack.push(self.pop())

            stack.push(value)

            while not helpingStack.isEmpty():
                stack.push(helpingStack.pop())


stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(4)
# stack.push(6)
# stack.push(7)

print(stack.items)

stack.pushStack(3)
stack.pushStack(5)
stack.pushStack(11)

print(stack.items)
