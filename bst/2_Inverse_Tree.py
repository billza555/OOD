class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def is_empty(self):
        return self.items == []

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
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data and cur.left != None:
                    cur = cur.left
                elif data >= cur.data and cur.right != None:
                    cur = cur.right
                elif data < cur.data:
                    cur.left = Node(data)
                    break
                else:
                    cur.right = Node(data)
                    break
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def reverseTree(self, node):
        queue = Queue()
        queue.enqueue(node)
        while not queue.is_empty():
            node = queue.dequeue()
            left = node.left
            right = node.right
            node.left = right
            node.right = left
            if node.left:
                queue.enqueue(node.left) 
            if node.right:
                queue.enqueue(node.right)             

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Before:")
T.printTree(root)
T.reverseTree(root)
print("After:")
T.printTree(root)