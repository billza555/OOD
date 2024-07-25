numbers = sorted([int(number) for number in input("Enter Your List : ").split()])
if len(numbers) < 3:
    print("Array Input Length Must More Than 2")
else:
    listSum5 = []
    for number1 in range(len(numbers)):
        for number2 in range(number1+1, len(numbers)):
            for number3 in range(number2+1, len(numbers)):
                if numbers[number1] + numbers[number2] + numbers[number3] == 5:
                    if [numbers[number1],numbers[number2],numbers[number3]] not in listSum5:
                        listSum5.append([numbers[number1],numbers[number2],numbers[number3]])
    print(listSum5)