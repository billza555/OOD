'''
ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

Testcase student: #1/5 1
Enter Input : 6 3 -2 5 -8 2 -2
2 3 -2 5 -8 6 -2

Testcase student: #2/5 2
Enter Input : 6 5 4 -1 3 0 2 -99 1
0 1 2 -1 3 4 5 -99 6
'''

def get_max_numbers(numbers):
    max_index = 0
    for index, number in enumerate(numbers):
        if number > numbers[max_index]:
            max_index = index
    return max_index

def get_negative_number(numbers):
    return [[index, number] for index,number in enumerate(numbers) if number < 0]

def check_index(numbers, value):
    for index, number in enumerate(numbers):
        if number == value:
            numbers[index] = 0
            return index
    return None

def selection_sort(numbers):
    lst = []
    box_negative = get_negative_number(numbers)
    while numbers:
        index = get_max_numbers(numbers)
        if numbers[index] < 0:
            break
        number = numbers.pop(index)
        lst.insert(0, number)
    for negative in box_negative:
        lst.insert(negative[0], negative[1])
    return lst

numbers = [int(number) for number in input("Enter Input : ").split()]
sort_number = selection_sort(numbers)
for number in sort_number:
    print(number, end=" ")
print("")