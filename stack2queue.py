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
        for item in self.items[0]:
            print(f" {item} -> {ord(item)}")
        return "".join(self.items[0][::-1])

    def printStack(self):
        return self.items


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def peek(self):
        if not self.stack2.isEmpty():
            return self.stack2.peek()
        elif not self.stack1.isEmpty():
            return self.stack1.items[0]
        else:
            return False

    def enqueue(self, item):
        return self.stack1.push(item)

    def dequeue(self):
        if(self.stack2.isEmpty()):
            for i in range(len(self.stack1.items)):
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def isEmpty(self):
        return self.stack1.items + self.stack2.items == []

    def printQueue(self):
        return self.stack1.items + self.stack2.items


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue.peek())
print(queue.dequeue())

print(queue.printQueue())
