'''
ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

Testcase student: #1/4 1
Enter Input : 932c 832u32 2344b
2344b 932c 832u32

Testcase student: #2/4 2
Enter Input : 99a 78b c2345 11d
99a 78b c2345 11d

Testcase student: #3/4 3
Enter Input : 572z 5y5 304q2
304q2 5y5 572z
'''

def get_alphabet(words):
    for word in words:
        if word.isalpha():
            return ord(word)
        
def shell_sort(numbers):
    gap = len(numbers)
    while gap != 1:
        gap = gap // 2 + gap % 2
        for index in range(len(numbers)):
            if index + gap >= len(numbers):
                break
            if get_alphabet(numbers[index]) > get_alphabet(numbers[index + gap]):
                number = numbers[index + gap]
                numbers[index + gap] = numbers[index]
                numbers[index] = number
    return numbers

words = input("Enter Input : ").split()
for word in shell_sort(words):
    print(word, end=" ")
print()