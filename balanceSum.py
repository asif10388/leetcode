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


stackA = Stack()
stackB = Stack()

stackA.push(1)
stackA.push(5)
stackA.push(11)
stackA.push(4)

stackB.push(4)
stackB.push(32)
stackB.push(1)
stackB.push(-1)


def balanceSum(stackA, stackB):
    sumDifference = sum(stackA.items) - sum(stackB.items)

    if(sumDifference > 0):
        stackB.push(abs(sumDifference))
    else:
        stackA.push(abs(sumDifference))

    return stackA.items, stackB.items


print(balanceSum(stackA, stackB))
