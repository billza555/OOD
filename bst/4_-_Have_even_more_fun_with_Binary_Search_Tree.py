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
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def append(self, data):
        if not self.root:
            self.root = Node(data)
            return
        root = self.root
        while root:
            if ascii(data) < ascii(root.data):
                if not root.left:
                    root.left = Node(data)
                    break
                root = root.left
            else:
                if not root.right:
                    root.right = Node(data)
                    break
                root = root.right

    def cut(self, data):
        if not self.root:
            return
        root = self.root
        while ascii(data) != ascii(root.data):
            if ascii(data) < ascii(root.data):
                root = root.left     
            else:
                root = root.right   
        if root.right:
            root.right = None 
        elif root.left:
            root.left = None
        else:
            print("Not thing change")

    def preorder(self, node,stop):
        if node:
            if ascii(node.data) > ascii(stop):
                print(node.data, end=" ")
            else:
                print(f"{''.join(str(ord(node.data[data])) for data in range(len(node.data)))}", end=" ")
            self.preorder(node.left, stop)
            self.preorder(node.right, stop)

    def inorder(self, node,stop):
        if node:
            self.inorder(node.left, stop)
            if ascii(node.data) > ascii(stop):
                print(node.data, end=" ")
            else:
                print(f"{''.join(str(ord(node.data[data])) for data in range(len(node.data)))}", end=" ")
            self.inorder(node.right, stop)

    def postorder(self, node,stop):
        if node:
            self.postorder(node.left, stop)
            self.postorder(node.right, stop)
            if ascii(node.data) > ascii(stop):
                print(node.data, end=" ")
            else:
                print(f"{''.join(str(ord(node.data[data])) for data in range(len(node.data)))}", end=" ")

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
            
    def printMirrorTree(self, node, level=0):
        self.reverseTree(self.root)
        self.printTree(node, level)
        self.reverseTree(self.root)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
print("What is this a plum tree")
first,inp = input('Enter Input : ').split('/')
first = first.split()
for i in first:
    T.append(i)
print("FIrst look of this plum tree")
T.printTree(T.root)
print("********************************************")
inp = inp.split(',')
for i in inp:
    print(i)
    if i[:2] == "AP":
        T.append(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CU":
        T.cut(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CH":
        print('preorder  :',end=' ')
        T.preorder(T.root,i[3:])
        print('\ninorder   :',end=' ')
        T.inorder(T.root,i[3:])
        print('\npostorder :',end=' ')
        T.postorder(T.root,i[3:])
        print()
    elif i[:2] == "MI":
        T.printMirrorTree(T.root)
    print("********************************************")
print("the last result")
T.printTree(T.root)