class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = self.setHeight()

    def __str__(self):
        return str(self.val)
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height

    def getHeight(self, node):
        return -1 if node == None else node.height
    
    def balanceValue(self):      
        return self.getHeight(self.right) - self.getHeight(self.left)
  
class AVL_Tree(object): 
    def __init__(self, root = None):
        self.root = root

    def insert(self, root, data):
        self.root = AVL_Tree._insert(root, int(data))
        return self.root
    
    def _insert(root, data):
        if root is None:
            return TreeNode(data)
        if data < root.val:
            root.left = AVL_Tree._insert(root.left, data)
        else:
            root.right = AVL_Tree._insert(root.right, data)
        root = AVL_Tree.reBalance(root)
        root.setHeight()
        return root

    def rotateLeftChild(root):
        y = root.left
        root.left = y.right
        y.right = root
        root.setHeight()
        y.setHeight()
        return y
    
    def rotateRightChild(root):
        y = root.right
        root.right = y.left
        y.left = root
        root.setHeight()
        y.setHeight()
        return y
    
    def reBalance(root):
        balance = root.balanceValue()
        if balance == 2:
            print("Not Balance, Rebalance!")
            if root.right.balanceValue() == -1:
                root.right = AVL_Tree.rotateLeftChild(root.right)
            root = AVL_Tree.rotateRightChild(root)
        elif balance == -2:
            print("Not Balance, Rebalance!")
            if root.left.balanceValue() == 1:
                root.left = AVL_Tree.rotateRightChild(root.left)
            root = AVL_Tree.rotateLeftChild(root)
        return root

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")