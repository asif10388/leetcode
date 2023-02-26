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

stackA.push(10)
stackA.push(25)
stackA.push(70)

stackB.push(10)
stackB.push(20)
stackB.push(30)


def balanceSum(stackA, stackB):
    sumDifference = sum(stackA.items) - sum(stackB.items)

    if(sumDifference > 0):
        stackB.push(abs(sumDifference))
    else:
        stackA.push(abs(sumDifference))

    return stackA.items, stackB.items


print(balanceSum(stackA, stackB))
