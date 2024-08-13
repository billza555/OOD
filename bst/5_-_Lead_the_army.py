class Node:
    def __init__(self, data, father=None):
        self.data = data
        self.left = None
        self.right = None
        self.father = father
    
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
                   node.left = Node(data, node)
                   break
               node = node.left
            else:
               if not node.right:
                   node.right = Node(data, node)
                   break
               node = node.right 
        node = Node(data)
        return self.root
    
    def more_preorder(self, node, value, number=[0]):
        if node:
            check_node = node
            while not check_node.left and not check_node.right:
                amount = self.get_amount_from_root(check_node)
                if amount > value:
                    number[0] += 1
                    print(f"{number[0]}) {'->'.join(self.get_value_from_root(check_node))} = {amount}")
                    self.delete_child(check_node)
                    check_node = check_node.father
                    if not check_node:
                        return
                else:
                    break 
            self.more_preorder(node.left, value, number)
            self.more_preorder(node.right, value, number)
            return number
    
    def equal_preorder(self, node, value, number=[0]):
        if node:
            check_node = node
            while not check_node.left and not check_node.right:
                amount = self.get_amount_from_root(check_node)
                if amount == value:
                    number[0] += 1
                    print(f"{number[0]}) {'->'.join(self.get_value_from_root(check_node))} = {amount}")
                    self.delete_child(check_node)
                    check_node = check_node.father
                    if not check_node:
                        return
                else:
                    break
            self.equal_preorder(node.left, value, number)
            self.equal_preorder(node.right, value, number)
            return number
    
    def less_preorder(self, node, value, number):
        if node:
            check_node = node
            while not check_node.left and not check_node.right:
                amount = self.get_amount_from_root(check_node)
                if amount < value:
                    number[0] += 1
                    print(f"{number[0]}) {'->'.join(self.get_value_from_root(check_node))} = {amount}")
                    self.delete_child(check_node)
                    check_node = check_node.father
                    if not check_node:
                        return
                else:
                    break
            self.less_preorder(node.left, value, number)
            self.less_preorder(node.right, value, number)
            return number

    def get_value_from_root(self, node):
        all_node = [str(node.data)]
        while node != self.root:
            node = node.father
            all_node.append(str(node.data))
        return reversed(all_node)

    def get_amount_from_root(self, node):
        amount = node.data
        while node != self.root:
            node = node.father
            amount += node.data
        return amount
    
    def delete_child(self, node):
        if not node:
            return
        if node == self.root:
            self.root = None
            return 
        father = node.father
        if father.left == node:
            father.left = None
        if father.right == node:
            father.right = None

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        elif not level:
            print("City A has fallen!")

def create_city(cities):
    T = BST()
    for city in cities:
        T.insert(city)
    print("(City A) Before the war:")
    T.printTree(T.root)
    print("--------------------------------------------------")
    return T

def after_war(bst, last):
    print("(City A) After the war:")
    bst.printTree(bst.root)
    if not last and bst.root:
        print("--------------------------------------------------")

def lead_army(bst, conditions):
    for index, condition in enumerate(conditions):
        char,number = condition.split()
        if not bst.root:
            return
        elif char == "M":
            print(f"Removing paths where the sum is greater than {number}:")
            remove = bst.more_preorder(bst.root, int(number), [0])
            if remove == [0]:
                print("No paths were removed.")
            print("--------------------------------------------------")
            after_war(bst, index == len(conditions) - 1)
        elif char == "L":
            print(f"Removing paths where the sum is less than {number}:")
            remove = bst.less_preorder(bst.root, int(number), [0])
            if remove == [0]:
                print("No paths were removed.")
            print("--------------------------------------------------")
            after_war(bst, index == len(conditions) - 1)
        elif char == "EQ":
            print(f"Removing paths where the sum is equal to {number}:")
            remove = bst.equal_preorder(bst.root, int(number), [0])
            if remove == [0]:
                print("No paths were removed.")
            print("--------------------------------------------------")
            after_war(bst, index == len(conditions) - 1)

inp = [i for i in input('Enter <Create City A (BST)>/<Create conditions and deploy the army>: ').split("/")]
cities = [int(i) for i in inp[0].split()]
conditions = [i for i in inp[1].split(",")]
bst = create_city(cities)
lead_army(bst, conditions)