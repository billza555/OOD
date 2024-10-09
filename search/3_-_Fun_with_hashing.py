'''
ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ



class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    # Code Here

Testcase student: #1/3 1
 ***** Fun with hashing *****
Enter Input : 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
#1	(1+1, I)
#2	None
#3	None
---------------------------
collision number 1 at 0
#1	(1+1, I)
#2	(OnE, Love)
#3	None
---------------------------
collision number 1 at 0
collision number 2 at 1
Max of collisionChain
#1	(1+1, I)
#2	(OnE, Love)
#3	None
---------------------------
#1	(1+1, I)
#2	(OnE, Love)
#3	(#$ew2, KMITL)
---------------------------
This table is full !!!!!!

Testcase student: #2/3 2
***** Fun with hashing *****
Enter Input : 5 5/one Un,two Deux,three Trois,four Quatre,five Cinq,ten Dix,eleven Onze
#1	None
#2	None
#3	(one, Un)
#4	None
#5	None
---------------------------
#1	None
#2	(two, Deux)
#3	(one, Un)
#4	None
#5	None
---------------------------
collision number 1 at 1
collision number 2 at 2
#1	(three, Trois)
#2	(two, Deux)
#3	(one, Un)
#4	None
#5	None
---------------------------
#1	(three, Trois)
#2	(two, Deux)
#3	(one, Un)
#4	None
#5	(four, Quatre)
---------------------------
collision number 1 at 1
collision number 2 at 2
collision number 3 at 0
collision number 4 at 0
collision number 5 at 2
Max of collisionChain
#1	(three, Trois)
#2	(two, Deux)
#3	(one, Un)
#4	None
#5	(four, Quatre)
---------------------------
collision number 1 at 2
#1	(three, Trois)
#2	(two, Deux)
#3	(one, Un)
#4	(ten, Dix)
#5	(four, Quatre)
---------------------------
This table is full !!!!!!

'''
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
