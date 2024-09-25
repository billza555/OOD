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