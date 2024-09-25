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