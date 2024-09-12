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