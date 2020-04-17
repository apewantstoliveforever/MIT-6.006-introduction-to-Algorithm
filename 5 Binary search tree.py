class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value is None:
            self = Node(data)
        else:
            if self.value > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    return self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                    return True
                else:
                    return self.right.insert(data)

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.value))
            if self.right:
                self.right.inorder()

    def preorder(self):
        if self:
            print(str(self.value))
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))
    def min(self):
        if self.left is not None:
            self.left.min()
        else:
            print(str(self.value))
            return True
    def max(self):
        if self.right is not None:
            self.right.max()
        else:
            print(str(self.value))
            return True


class Tree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root is not None:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def inorder(self):
        if self.root is not None:
            self.root.inorder()

    def preorder(self):
        if self.root:
            self.root.preorder()

    def postorder(self):
        if self.root:
            self.root.postorder()
    def min(self):
        return self.root.min()
    def max(self):
        return self.root.max()

t = Tree()
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(1)
t.insert(3)
t.insert(7)
t.insert(15)
t.insert(8)