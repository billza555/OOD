class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def ascii_key(self):
        value = 0
        for word in self.key:
            value += ord(word)
        return value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, max, max_collision):
        self.table = [None for i in range(max)]
        self.max = max
        self.max_collision = max_collision
        self.size = 0
    
    def __str__(self):
        output = ""
        for i in range(self.max):
            output += f"#{i + 1}\t{self.table[i]}"
            if i < self.max - 1:
                output += "\n"
        return output
    
    def add(self, data):
        probe = data.ascii_key() % self.max
        collision = 0
        while self.table[probe] and collision != self.max_collision:
            collision += 1
            print(f"collision number {collision} at {probe}")
            probe = (probe - ((collision - 1) ** 2) + (collision ** 2)) % self.max
        if collision == self.max_collision:
            print("Max of collisionChain")
        elif self.table[probe] is None:
            self.table[probe] = data
            self.size += 1

    def is_full(self):
        if self.size >= self.max:
            return True
        return False

print(" ***** Fun with hashing *****")
informations =  [information for information in input("Enter Input : ").split("/")]
table, info = list(map(int, informations[0].split())), list(informations[1].split(","))
hast_table = hash(table[0], table[1])
for i in info:
    if not hast_table.is_full():
        i = i.split()
        data = Data(i[0], i[1])
        hast_table.add(data)
        print(hast_table)
        print("---------------------------")
    else:
        print("This table is full !!!!!!")
        break
