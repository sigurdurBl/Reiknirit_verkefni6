class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value == d:              # Eru þessi gögn þegar fyrir
            return False
        elif self.value > d:             # Förum vinstra megin
            if self.left:                   # Er til leftChild
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:                               # Förum hægra megin
            if self.right:                  # Er til rightChild
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True

    def preOrderPrint(self):
        print(self.value, end=" ")
        if self.left:
            self.left.preOrderPrint()
        if self.right:
            self.right.preOrderPrint()

    def postOrderPrint(self):
        if self.left:
            self.left.preOrderPrint()
        if self.right:
            self.right.preOrderPrint()
        print(self.value, end=" ")

    def delete(self,n):
        if self.value > n:
            self.left = self.left.delete(n)
        if self.value < n:
            self.right = self.right.delete(n)
        else:
            if self.left is None:
                curr = self.right
                #self = None
                return curr

            if self.right is None:
                curr = self.left
                #self = None
                return curr

            minNode = self.right.findMinNode()
            self.value = minNode.value
            self.right = self.right.delete(minNode.value)

        return self

    def findMinNode(self):
        if self.left is None:
            return self
        else:
            return self.left.findMinNode()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,d):
        if self.root:                       # Er til rót?
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def preOrderPrint(self):
        if self.root is None:
            return self.root
        else:
            self.root.preOrderPrint()

    def postOrderPrint(self):
        if self.root is None:
            return self.root
        else:
            self.root.postOrderPrint()

    def delete(self,n):
        if self.root is None:
            return self.root
        else:
            return self.root.delete(n)


    def deleteTree(self):
        self.root = None
        return True



t = Tree()

t.insert(5)
t.insert(4)
t.insert(2)
t.insert(3)
t.insert(2)
t.insert(10)
t.insert(15)
t.insert(8)
t.insert(9)
t.preOrderPrint()
print()
t.delete(5)
t.preOrderPrint()
