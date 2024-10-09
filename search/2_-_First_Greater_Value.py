'''
ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value

Testcase student: #1/4 1
Enter Input : 3 2 7 6 8/5
6

Testcase student: #2/4 2
Enter Input : 3 2 7 6 8/5 6 12
6
7
No First Greater Value
'''

def sentinel_search(arr, value):
    arr.append(value)
    i = 0
    while arr[i] <= value and i != len(arr) - 1:
        i += 1
    if i == len(arr) - 1:
        arr.pop()
        return "No First Greater Value"
    arr.pop()
    return arr[i]

number_list = [number for number in input("Enter Input : ").split("/")]
lst1, lst2 = sorted(map(int, number_list[0].split())), number_list[1].split()
for number in lst2:
    print(sentinel_search(lst1, int(number)))