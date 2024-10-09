'''
เขียน function bubble sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***
Testcase student: #1/6
Enter Input : 4 3 2 1
[1, 2, 3, 4]

Testcase student: #2/6
Enter Input : 3 2 1 5 6 7
[1, 2, 3, 5, 6, 7]

Testcase student: #3/6
Enter Input : 1 2 3 4 5
[1, 2, 3, 4, 5]
'''

def lest_to_most(numbers, index = 0):
    if index == len(numbers) - 1:
        return True
    if numbers[index] > numbers[index+1]:
        return False
    return lest_to_most(numbers, index+1)

def bubble_sort(numbers, index=0):
    if index == len(numbers) - 1:
        if lest_to_most(numbers):
            return numbers
        else:
            return bubble_sort(numbers, 0)
    if numbers[index] > numbers[index+1]:
        number = numbers[index]
        numbers[index] = numbers[index+1]
        numbers[index+1] = number
    return bubble_sort(numbers, index+1)

numbers = [int(number) for number in input("Enter Input : ").split()]
print(bubble_sort(numbers))