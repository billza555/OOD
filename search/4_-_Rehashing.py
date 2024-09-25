class Order:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Hash:
    def __init__(self, table_size, max_collision, threshold):
        self.table_size = table_size
        self.max_collision = max_collision
        self.threshold = threshold
        self.size = 0
        self.table = [None] * table_size
        self.order = None

    def add_order(self, data):
        if self.order:
            order = self.order
            while order.next:
                order = order.next
            order.next = Order(data)
        else:
            self.order = Order(data)

    def add(self, data, table=None):
        if not table: table = self.table
        probe = data % self.table_size
        collsion = 0
        while table[probe] and collsion != self.max_collision:
            collsion += 1
            print(f"collision number {collsion} at {probe}")
            probe = (probe - ((collsion - 1) ** 2)  + (collsion ** 2)) % self.table_size
        if collsion == self.max_collision:
            print("****** Max collision - Rehash !!! ******")
            self.table = self.rehash()
            self.add(data)  
            return
        if self.table_size * self.threshold < (self.size + 1) * 100:
            print("****** Data over threshold - Rehash !!! ******")
            self.table = self.rehash()
            self.add(data)
            return
        if table[probe] is None:
            if table == self.table:
                self.add_order(data)
            table[probe] = data
            self.size += 1

    def rehash(self):
        self.table_size = self.table_size * 2
        while not prime(self.table_size):
            self.table_size += 1
        new_table = [None] * self.table_size
        self.size = 0
        order = self.order
        while order:
            self.add(order.data, new_table)
            order = order.next
        return new_table

    def __str__(self):
        output = ""
        for index in range(len(self.table)):
            output += f"#{index+1}\t{self.table[index]}"
            if index < len(self.table) - 1:
                output += "\n"
        return output

def prime(numbers):
    for i in range(numbers-1, 1, -1):
        if not numbers % i:
            return False
    return True

print(" ***** Rehashing *****")
orders = [order for order in input("Enter Input : ").split("/")]
init, data = list(map(int, orders[0].split())), list(map(int, orders[1].split()))
hash_table = Hash(init[0], init[1], init[2] if init[2] else 100)
print("Initial Table :")
print(hash_table)
print("----------------------------------------")
for d in data:
    print(f"Add : {d}")
    hash_table.add(d)
    print(hash_table)
    print("----------------------------------------")