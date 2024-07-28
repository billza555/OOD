def check_digit(numbers, start=0):
    if start > len(numbers) - 1:
        return 0
    if not numbers[start].isdecimal():
        return 1
    if int(numbers[start]) > 9:
        return 1
    return check_digit(numbers, start+1)

def permute(numbers, start=0):
    if start == len(numbers) - 1:
        return [numbers[:]]
    permutations = []
    for i in range(start, len(numbers)):
        numbers[start], numbers[i] = numbers[i], numbers[start]
        permutations += permute(numbers, start + 1)
        numbers[start], numbers[i] = numbers[i], numbers[start]
    return permutations   

def create_number(numbers, stop):
    if stop == 0:
        return [int(numbers[stop])]
    else:
        return [int(''.join(numbers[:stop]))] + create_number(numbers, stop-1)
    
def check_number(alphabets, now=0):
    if len(alphabets) - 1 == now:
        return alphabets[now].isdecimal()
    return check_number(alphabets, now+1) + alphabets[now].isdecimal()
    
def search_number(numbers):
    is_number = check_number(numbers)
    is_digit = check_digit(numbers)
    if is_number != len(numbers) or is_digit:
        return "Invalid input"
    possible_number = permute(numbers)
    all_number = [] 
    for number in possible_number:
        all_number += create_number(number, len(number))
    all_number = sorted(list(set(all_number)))
    return f"Output : {all_number}"

numbers = [number for number in input("Enter digits : ").split(" ")]
print(search_number(numbers))