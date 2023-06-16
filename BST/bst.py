class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        new_node = Node(value)

        if(self.root == None):
            self.root = new_node
            return
        else:

            if value < root.value:
                if root.left is None:
                    root.left = new_node
                else:
                    self.insert(root.left, value)
            else:
                if root.right is None:
                    root.right = new_node
                else:
                    self.insert(root.right, value)

    def visit(self, node):
        print(str(node.value), end="-")

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)

        self.visit(root)

        if root.right:
            self.inorder(root.right)

    def preorder(self, root):
        self.visit(root)

        if root.left:
            self.preorder(root.left)

        if root.right:
            self.preorder(root.right)

    def postorder(self, root):
        if root.left:
            self.postorder(root.left)

        if root.right:
            self.postorder(root.right)

        self.visit(root)

    def find(self, root, value):
        if root.value == value:
            return True

        if value < root.value:
            if root.left:
                return self.find(root.left, value)
            else:
                return False

        if value > root.value:
            if root.right:
                return self.find(root.right, value)
            else:
                return False

    def largestEven(self, root):
        evens = []

        if root.left:
            evens += self.largestEven(root.left)

        if root.value % 2 == 0:
            evens.append(root.value)

        if root.right:
            evens += self.largestEven(root.right)

        return str(evens[-1])

    def findRange(self, root):
        numbers = []

        if root is None:
            return numbers

        if root.left:
            numbers.extend(self.findRange(root.left))

        numbers.append(root.value)

        if root.right:
            numbers.extend(self.findRange(root.right))

        sRange = numbers[-1] - numbers[0]

        print(sRange)

        return numbers


bst = BinarySearchTree()

bst.insert(bst.root, 10)
bst.insert(bst.root, 5)
bst.insert(bst.root, 13)
bst.insert(bst.root, 3)
bst.insert(bst.root, 7)
bst.insert(bst.root, 9)
bst.insert(bst.root, 12)

bst.inorder(bst.root)
print("\n")
bst.preorder(bst.root)
print("\n")
bst.postorder(bst.root)

print(bst.find(bst.root, 12))

# print(bst.largestEven(bst.root))
print(bst.findRange(bst.root))
