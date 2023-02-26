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


def keepLargestOnTop(stack):
    largest = max(stack.items)

    for i in range(len(stack.items) - 1):
        if stack.items[i] == largest:
            stack.items.pop(i)
            stack.items.append(largest)
            break
    return stack.items


print(keepLargestOnTop(stack))
