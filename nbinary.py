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


queue = Queue()


def nToBinary(n, queue):
    for i in range(n + 1):
        queue.enqueue(bin(i).replace("0b", ""))
    return "\n\n".join([*queue.printQueue()])


print(nToBinary(5, queue))
