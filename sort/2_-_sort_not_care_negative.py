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