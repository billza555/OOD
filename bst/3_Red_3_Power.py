class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
           self.root = Node(data)
           return self.root
        node = self.root
        while node:
            if data < node.data:
               if not node.left:
                   node.left = Node(data)
                   break
               node = node.left
            else:
               if not node.right:
                   node.right = Node(data)
                   break
               node = node.right 
        node = Node(data)
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def inorder(self, node, data):
        if node:
            self.inorder(node.left, data)
            if node.data > data:
                node.data *= 3
            self.inorder(node.right, data)

T = BST()
items = [i for i in input('Enter Input : ').split("/")]
inp = [int(i) for i in items[0].split()]
k = int(items[1])
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
T.inorder(root, k)
T.printTree(root)