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

    def printQueue(self):
        queue = self.stack1 + self.stack2
        return queue


queueA = Queue()
queueB = Queue()


def assignID(id, queueA, queueB):
    if id % 2 == 0:
        queueA.enqueue(id)
        return queueA.printQueue()
    else:
        queueB.enqueue(id)
        return queueB.printQueue()


print(assignID(2, queueA, queueB))
print(assignID(4, queueA, queueB))
print(assignID(7, queueA, queueB))
print(assignID(10, queueA, queueB))
print(assignID(1, queueA, queueB))
print(assignID(9, queueA, queueB))
print(assignID(11, queueA, queueB))
