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


def dailyTemperatures(temperatures):
    n = len(temperatures)
    stack = []
    res = [0] * n
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
