class AVLTree:

    class AVLNode:

        def __init__(self, data, left = None, right = None):

            self.data = data

            self.left = None if left is None else left

            self.right = None if right is None else right

            self.height = self.setHeight()

        

        def __str__(self):

            return str(self.data)

        

        def setHeight(self):

                a = self.getHeight(self.left)

                b = self.getHeight(self.right)

                self.height = 1 + max(a,b)

                return self.height

            

        def getHeight(self, node):

            return -1 if node == None else node.height

            

        def balanceValue(self):      

            return self.getHeight(self.right) - self.getHeight(self.left)

    

    def __init__(self, root = None):

        self.root = None if root is None else root

    

    def add(self, data):
        self.root = AVLTree._add(self.root, int(data))
 

    def _add(root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)
        root = AVLTree.reBalance(root)
        root.setHeight()
        return root

    def rotateLeftChild(root) :
        y = root.left
        root.left = y.right
        y.right = root
        root.setHeight()
        y.setHeight()
        return y



    def rotateRightChild(root) :
        y = root.right
        root.right = y.left
        y.left = root
        root.setHeight()
        y.setHeight()
        return y
    
    def reBalance(root) :
        balance = root.balanceValue()
        if balance == 2:
            if root.right.balanceValue() == -1:
                root.right = AVLTree.rotateLeftChild(root.right)
            root = AVLTree.rotateRightChild(root)
        elif balance == -2:
            if root.left.balanceValue() == 1:
                root.left = AVLTree.rotateRightChild(root.left)
            root = AVLTree.rotateLeftChild(root)
        return root

    def postOrder(self):
        print("AVLTree post-order : ",end="")
        AVLTree._postOrder(self.root)
        print("")



    def _postOrder(root):
        if root:
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root, end=" ")



    def printTree(self):

        AVLTree._printTree(self.root)

        print()

    

    def _printTree(node , level=0):

        if not node is None:

            AVLTree._printTree(node.right, level + 1)

            print('     ' * level, node.data)

            AVLTree._printTree(node.left, level + 1)

 

avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:

    if i[:2] == "AD":

        avl1.add(i[3:])

    elif i[:2] == "PR":

        avl1.printTree()

    elif i[:2] == "PO":

        avl1.postOrder()

