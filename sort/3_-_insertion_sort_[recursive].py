'''
เขียน function insertion sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

และแสดงขั้นตอนของ insertion sort ตามตัวอย่าง

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

Testcase student: #1/8
Enter Input : 1 2 3 4
insert 2 at index 1 : [1, 2] [3, 4]
insert 3 at index 2 : [1, 2, 3] [4]
insert 4 at index 3 : [1, 2, 3, 4] 
sorted
[1, 2, 3, 4]

Testcase student: #2/8
Enter Input : 1 3 4 2
insert 3 at index 1 : [1, 3] [4, 2]
insert 4 at index 2 : [1, 3, 4] [2]
insert 2 at index 1 : [1, 2, 3, 4] 
sorted
[1, 2, 3, 4]
'''

def check_position_value(numbers, value, start):
    if start == 0:
        return start
    if numbers[start-1] <= value:
        return start
    else:
        return check_position_value(numbers, value, start-1)

def insetion_sort(numbers, start=0, lst=None):
    if not lst:
        lst = []
    if len(numbers) == 0:
        print("sorted")
        return lst
    position = check_position_value(lst, numbers[0], start)
    number = numbers.pop(0)
    lst.insert(position, number)
    if start > 0:
        print(f"insert {number} at index {position} : {lst}", end=" ")
        print(numbers) if numbers else print("")   
    return insetion_sort(numbers, start+1 ,lst)

numbers = [int(number) for number in input("Enter Input : ").split()]
print(insetion_sort(numbers))