'''
ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด


Testcase student: #1/7 1
 ***** Rehashing *****
Enter Input : 5 1 67/1 6
Initial Table :
#1	None
#2	None
#3	None
#4	None
#5	None
----------------------------------------
Add : 1
#1	None
#2	1
#3	None
#4	None
#5	None
----------------------------------------
Add : 6
collision number 1 at 1
****** Max collision - Rehash !!! ******
#1	None
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
----------------------------------------

Testcase student: #2/7 2
 ***** Rehashing *****
Enter Input : 5 1 10/1 6
Initial Table :
#1	None
#2	None
#3	None
#4	None
#5	None
----------------------------------------
Add : 1
****** Data over threshold - Rehash !!! ******
#1	None
#2	1
#3	None
#4	None
#5	None
#6	None
#7	None
#8	None
#9	None
#10	None
#11	None
----------------------------------------
Add : 6
****** Data over threshold - Rehash !!! ******
#1	None
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
#12	None
#13	None
#14	None
#15	None
#16	None
#17	None
#18	None
#19	None
#20	None
#21	None
#22	None
#23	None
----------------------------------------

Testcase student: #3/7 3
 ***** Rehashing *****
Enter Input : 5 1 10/0 1 6 20
Initial Table :
#1	None
#2	None
#3	None
#4	None
#5	None
----------------------------------------
Add : 0
****** Data over threshold - Rehash !!! ******
#1	0
#2	None
#3	None
#4	None
#5	None
#6	None
#7	None
#8	None
#9	None
#10	None
#11	None
----------------------------------------
Add : 1
****** Data over threshold - Rehash !!! ******
#1	0
#2	1
#3	None
#4	None
#5	None
#6	None
#7	None
#8	None
#9	None
#10	None
#11	None
#12	None
#13	None
#14	None
#15	None
#16	None
#17	None
#18	None
#19	None
#20	None
#21	None
#22	None
#23	None
----------------------------------------
Add : 6
****** Data over threshold - Rehash !!! ******
#1	0
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
#12	None
#13	None
#14	None
#15	None
#16	None
#17	None
#18	None
#19	None
#20	None
#21	None
#22	None
#23	None
#24	None
#25	None
#26	None
#27	None
#28	None
#29	None
#30	None
#31	None
#32	None
#33	None
#34	None
#35	None
#36	None
#37	None
#38	None
#39	None
#40	None
#41	None
#42	None
#43	None
#44	None
#45	None
#46	None
#47	None
----------------------------------------
Add : 20
#1	0
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
#12	None
#13	None
#14	None
#15	None
#16	None
#17	None
#18	None
#19	None
#20	None
#21	20
#22	None
#23	None
#24	None
#25	None
#26	None
#27	None
#28	None
#29	None
#30	None
#31	None
#32	None
#33	None
#34	None
#35	None
#36	None
#37	None
#38	None
#39	None
#40	None
#41	None
#42	None
#43	None
#44	None
#45	None
#46	None
#47	None
----------------------------------------

Testcase student: #4/7 4
 ***** Rehashing *****
Enter Input : 7 6 70/13 15 6 24 23
Initial Table :
#1	None
#2	None
#3	None
#4	None
#5	None
#6	None
#7	None
----------------------------------------
Add : 13
#1	None
#2	None
#3	None
#4	None
#5	None
#6	None
#7	13
----------------------------------------
Add : 15
#1	None
#2	15
#3	None
#4	None
#5	None
#6	None
#7	13
----------------------------------------
Add : 6
collision number 1 at 6
#1	6
#2	15
#3	None
#4	None
#5	None
#6	None
#7	13
----------------------------------------
Add : 24
#1	6
#2	15
#3	None
#4	24
#5	None
#6	None
#7	13
----------------------------------------
Add : 23
****** Data over threshold - Rehash !!! ******
collision number 1 at 6
collision number 2 at 7
#1	None
#2	None
#3	None
#4	None
#5	None
#6	None
#7	6
#8	24
#9	None
#10	None
#11	23
#12	None
#13	None
#14	13
#15	None
#16	15
#17	None
----------------------------------------

'''

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