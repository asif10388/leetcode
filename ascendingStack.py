# class Stack:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self, data):
#         self.items.append(data)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[len(self.items) - 1]

#     def size(self):
#         return len(self.items)

#     def pushStack(self, value):
#         if self.isEmpty():
#             self.push(value)
#         else:
#             for i in range(len(self.items)):
#                 if self.items[i] > value:
#                     self.items.insert(i, value)
#                     break


# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(4)
# stack.push(6)
# stack.push(7)

# print(stack.items)

# stack.pushStack(3)
# stack.pushStack(5)


# print(stack.items)


def balancedBrackets(string):
    stack = []
    for char in string:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ')' or char == '}' or char == ']':
            if not stack:
                return False
            sequence = stack.pop()
            if (sequence == '(' and char != ')') or (sequence == '{' and char != '}') or (sequence == '[' and char != ']'):
                return False

    if not stack:
        return True
    else:
        return False


print(balancedBrackets("([])(){}(())()()"))
