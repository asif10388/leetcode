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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def reverse(self):
        for item in self.items:
            item = list(item)
        return "".join(item[::-1])

    def printStack(self):
        return self.items


input = input()

stack = Stack()

stack.push(input)

print(stack.reverse())
