'''
ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

***** อธิบาย Input
1. ด้านซ้าย  จะเป็น list ของ Data
2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา

def bi_search(l, r, arr, x):
    # Code Here

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))

Testcase student: #1/4 1
Enter Input : 33 2 11 82 77 28 15 76 9 64/28
True

Testcase student: #2/4 2
Enter Input : 33 2 11 82 77 28 15 76 9 64/50
False
'''

def bi_search(l, r, arr, x):
    if l > r:
        return False
    medium = (l + r) // 2
    if x < arr[medium]:
        return bi_search(l, medium-1, arr, x)
    elif x > arr[medium]:
        return bi_search(medium+1, r, arr, x)
    else:
        return True

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))