'''
มีสินค้าอยู่ n ชิ้น โดยชิ้นที่ i (0 <= i < n) มีน้ำหนัก Wi กิโลกรัม  นำสินค้าบรรจุใส่กล่องไม่เกิน k ใบ โดยมีเงื่อนไขว่า
1. สิ่งของต้องมีน้ำหนักรวมกันไม่เกินน้ำหนักมากสุดที่กล่องรับไหว
2. หากสิ่งของชิ้นที่ a และชิ้นที่ b อยู่ในกล่องเดียวกัน (a <= b) สิ่งของทุกชิ้นที่อยู่ระหว่างสองชิ้นนี้ (ทุกชิ้นที่ i ที่ a < i < b) จะต้องอยู่ในกล่องนี้ด้วย (นั่นคือสิ่งที่ของในกล่องเดียวกันจะต้องเป็นสิ่งของที่ตำแหน่งติดกัน)

ถ้าทุกกล่องสามารถรับน้ำหนักได้เท่ากัน จงหาว่าเราสามารถใช้กล่องที่รับน้ำหนักได้น้อยสุดเท่าใด โดยที่ยังบรรจุของตามเงื่อนไขได้ และใช้กล่องครบทุกใบ

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง สินค้า n ชิ้น และแต่ละชิ้นมีน้ำหนัก W กิโลกรัม
    -   ด้านขวาหมายถึง จำนวนกล่อง k ใบ

คำใบ้  Optimization Problem


อธิบาย Test Case #1

มีสินค้าอยู่ 5 ชิ้น โดยมีน้ำหนักเป็น 6 2 4 3 7 ตามลำดับ และมีกล่องจำนวน 3 ใบ   และน้ำหนักที่น้อยที่สุดที่สามารถใส่สินค้าได้ครบทุกชิ้น และใส่ลงกล่องได้ทุกใบคือ 8 กิโลกรัม โดยในกล่องที่ 1 จะใส่สินค้า 2 ชิ้นที่มีน้ำหนัก 6 และ 2   กล่องใบที่ 2 จะใส่สินค้า 2 ชิ้นที่มำน้ำหนัก 4 และ 3  และกล่องใบที่ 3 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 7

อธิบาย Test Case #2

มีสินค้าอยู่ 10 ชิ้น โดยมีน้ำหนักเป็น 8 7 2 5 1 10 9 2 3 5 ตามลำดับ และมีกล่องจำนวน 5 ใบ   และน้ำหนักที่น้อยที่สุดที่สามารถใส่สินค้าได้ครบทุกชิ้น และใส่ลงกล่องได้ทุกใบคือ 14 กิโลกรัม โดยในกล่องที่ 1 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 8   กล่องใบที่ 2 จะใส่สินค้า 3 ชิ้นที่มีน้ำหนัก 7 2 และ 5   กล่องใบที่ 3 จะใส่สินค้า 2 ชิ้นที่มีน้ำหนัก 1 และ 10   กล่องใบที่ 4 จะใส่สินค้า 3 ชิ้นที่มีน้ำหนัก 9 2 และ 3    และกล่องใบที่ 5 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 5

Testcase student: #1/8 1
Enter Input : 6 2 4 3 7/3
Minimum weigth for 3 box(es) = 8

Testcase student: #2/8 2
Enter Input : 8 7 2 5 1 10 9 2 3 5/5
Minimum weigth for 5 box(es) = 14

Testcase student: #3/8 3
Enter Input : 19 1 2 3 4/1
Minimum weigth for 1 box(es) = 29

Testcase student: #4/8 4
Enter Input : 19 1 2 3 4/2
Minimum weigth for 2 box(es) = 19

Testcase student: #5/8 5
Enter Input : 6 4 9 3 1 8 5 2/5
Minimum weigth for 5 box(es) = 10
'''

def check_near(numbers, max, boxes):
    box = 1
    value = 0
    for number in numbers:
        if value + number <= max:
            value += number
        else:
            value = number
            box += 1
    return boxes >= box

def near_maximum(numbers, boxes):
    max_number = max(numbers)
    sum_number = sum(numbers)

    while max_number < sum_number:
        mid = (max_number + sum_number) // 2
        if check_near(numbers, mid, boxes):
            sum_number = mid
        else:
            max_number = mid + 1
    return max_number

items = input("Enter Input : ").split("/")
numbers = [int(number) for number in items[0].split()]
boxes = int(items[1])
print(f"Minimum weigth for {boxes} box(es) = {near_maximum(numbers, boxes)}")