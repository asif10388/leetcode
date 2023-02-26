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

    def deleteChar(self):
        if not self.isEmpty():
            self.items.pop()
        return "".join(self.items)


stack = Stack()

userInput = input()

for letter in userInput:
    stack.push(letter)

flag = True


def undoAction(stack, flag):
    while(flag):
        prompt = input("Delete char? y/n \n")
        if(prompt == 'y' and not stack.isEmpty()):
            print(stack.deleteChar())
        else:
            flag = False


print(undoAction(stack, flag))
