class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        # This will help you when debugging later.
        return f"Node({self.data})"

    def height(self):
        return (max(Node.height(self.left), Node.height(self.right)) + 1) if self else -1
    
    def balance(self):
        return Node.height(self.left) - Node.height(self.right) if self else 0

    def leftRotate(x):
        ... # Left rotatet
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def rightRotate(y):
        ... # Left rotatet
        x = y.right
        y.right = x.left
        x.left = y
        return x
    
    def reBalance(root):
        balance = root.balance()
        if balance == -2:
            if root.right.balance() == 1:
                root.right = Node.leftRotate(root.right)
            root = Node.rightRotate(root)
        if balance == 2:
            if root.left.balance() == -1:
                root.left = Node.rightRotate(root.left)
            root = Node.leftRotate(root)
        return root

    def insert(root, data):
        if root is None:
            return Node(data)
        branch = "left" if data < root.data else "right"
        root.__dict__[branch] = Node.insert(root.__dict__[branch], data)
        # Balance this tree
        root = Node.reBalance(root)
        return root

    def _gen_display(self) -> 'tuple[list, int, int, int]':
        '''
        return
        - tree image: list[str]
        - left spacing: int
        - value width: int
        - right spacing: int
        '''
        if self is None:
            return [], 0, 0, 0
        lt, lf, lv, lb = Node._gen_display(self.left)
        rt, rf, rv, rb = Node._gen_display(self.right)
        data = str(self.data)
        if not lt and not rt:
            return [data], 0, len(data), 0
        add_left, add_right = int(bool(lt)), int(bool(rt))
        line = ((' '*(lf+lv) + '/' + ' '*(lb)) * add_left +
                ' ' * len(data) +
                (' '*rf + '\\' + ' '*(rv+rb)) * add_right)
        out = [' '*(lf+lv+add_left) + '_'*lb + data +
               '_'*rf + ' '*(rv+rb+add_right), line]
        if len(lt) > len(rt):
            rt.extend([' ' * (rf+rv+rb)] * (len(lt) - len(rt)))
        elif len(lt) < len(rt):
            lt.extend([' ' * (lf+lv+lb)] * (len(rt) - len(lt)))
        for l, r in zip(lt, rt):
            out.append(l + ' '*(len(data)+add_left+add_right) + r)
        return out, (lf+lv+lb+add_left), len(data), (rf+rv+rb+add_right)
    
    def _inorder(root):
        return Node.inorder(root, [])
    
    def inorder(root, orders):
        if root:
            Node.inorder(root.left, orders)
            orders.append(root.data)
            Node.inorder(root.right, orders)
        return orders
    
    def find_node_and_delete_child(root, data, new=None, last=None,):
        if root.data == data:
            if last:
                direction = "left" if data < last.data else "right"
                last.__dict__[direction] = None
            return root, new
        if not new:
            new = root
        if data < root.data:
            return Node.find_node_and_delete_child(root.left, data, new, root)
        return Node.find_node_and_delete_child(root.right, data, new, root)
    
    def _insert_bad(root, orders, direction):
        return Node.insert_bad(root, orders, direction)

    def insert_bad(root, orders, direction):
        if root:
            node = root
            d = None
            while node:
                if orders[-1] < node.data:
                    d = "left"
                    if not node.left:
                        break
                    node = node.left
                else:
                    d = "right"
                    if not node.right:
                        break
                    node = node.right
            node.__dict__[d] = Node(orders.pop())
            node = node.__dict__[d]
            while orders:
                node.__dict__[direction] = Node(orders.pop())
                node = node.__dict__[direction]
            return root
        else:
            root = Node(orders.pop())
            node = root
            while orders:
                node.__dict__[direction] = Node(orders.pop())
                node = node.__dict__[direction]
            return root
    
# rotate = node to be rotate
# direction = 'left' or 'right'
rotate, direction, inp = input('Enter input: ').split(',')
rotate = int(rotate)
root = None
for i in map(int, inp.split()):
    root = Node.insert(root, i)
tree_image = root._gen_display()
print("Before")
print(*tree_image[0], sep='\n')
print("-" * sum(tree_image[1:]))

# Straighten a specified node with specified direction
# Generate new display: tree_image = Node._gen_display(<Node object at 0x80085>)

check = Node._inorder(root)
if rotate in check:
    root, top = Node.find_node_and_delete_child(root, rotate)
    orders = (Node._inorder(root)) if direction == "left" else list(reversed(Node._inorder(root)))
    new = Node._insert_bad(top, orders, direction) 
    tree_image = new._gen_display()
    print("After")
    print(*tree_image[0], sep='\n')
else:
    print(f"No {rotate} in this tree")
