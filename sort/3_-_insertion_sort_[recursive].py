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