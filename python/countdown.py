def countdownNumber(listNumber):
    if len(listNumber) == 1:
        return [1]
    listCountdown = []
    for number in range(len(listNumber)):
        if listNumber[number] == listNumber[number+1] + 1:
            listCountdown.append(listNumber[number])
        if listNumber[number+1] == 1:
            listCountdown.append(1)
            break
    return listCountdown

print("*** Fun with countdown ***")
numbers = [int(number) for number in input("Enter List : ").split()]
listNumber = []
listCountdown = [0, []]
for number in numbers:
    listNumber.append(number)
    if number == 1:
        listCountdown[0] += 1
        listCountdown[1].append(countdownNumber(listNumber))
        listNumber = []
print(listCountdown)