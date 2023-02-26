class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if(self.stack2 != []):
            return self.stack2[-1]
        elif(self.stack1 != []):
            return self.stack1[0]
        else:
            return False

    def enqueue(self, item):
        return self.stack1.append(item)

    def dequeue(self):
        if(self.stack2 == []):
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def isEmpty(self):
        return self.stack1 + self.stack2 == []

    def reverseKth(self, value):
        queue = self.stack1 + self.stack2
        kthSlice = queue[value - 1::-1]
        remaining = queue[value:len(queue)]
        queue = remaining + kthSlice
        return queue

    def printQueue(self):
        queue = self.stack1 + self.stack2
        return queue


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
queue.enqueue(80)
queue.enqueue(90)


print(queue.peek())

print(queue.dequeue())

print(queue.printQueue())

print(queue.reverseKth(5))
