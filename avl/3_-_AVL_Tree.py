class AvlTree:

    class NodeTree:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.height = self.setHeight()

        def setHeight(self):
            a = self.getHeight(self.right)
            b = self.getHeight(self.left)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.height

        def __str__(self):
            return str(self.data)
        
        def balanceValue(self):
            return self.getHeight(self.left) - self.getHeight(self.right)

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        self.root = AvlTree._insert(self.root, data)
        return self.root

    def _insert(root, data):
        if root is None:
            return AvlTree.NodeTree(data)
        if data < root.data:
            root.left = AvlTree._insert(root.left, data)
        else:
            root.right = AvlTree._insert(root.right, data)
        root = AvlTree.reBalance(root)
        root.setHeight()
        return root

    def rotateRightChild(root):
        y = root.right
        root.right = y.left
        y.left = root
        y.setHeight()
        root.setHeight()
        return y
    
    def rotateLeftChild(root):
        y = root.left
        root.left = y.right
        y.right = root
        y.setHeight()
        root.setHeight()
        return y
    
    def reBalance(root):
        balance = root.balanceValue()
        if balance == -2:
            print("Left Left Rotation")
            if root.right.balanceValue() == 1:
                root.right = AvlTree.rotateLeftChild(root.right)
            root = AvlTree.rotateRightChild(root)
        elif balance == 2:
            print("Right Right Rotation")
            if root.left.balanceValue() == -1:
                root.left = AvlTree.rotateRightChild(root.left)
            root = AvlTree.rotateLeftChild(root)
        return root

    def printTree(node, level=0):
        if node:
            AvlTree.printTree(node.right, level+1)
            print('     '*level, node)
            AvlTree.printTree(node.left, level+1)

print(" *** AVL Tree Insert Element ***")
numbers = [int(number) for number in input("Enter Input : ").split()]
tree = AvlTree()
for number in numbers:
    print(f"insert : {number}")
    root = tree.insert(number)
    AvlTree.printTree(root)
    print("====================")