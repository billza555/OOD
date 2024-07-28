def number_to_max(number, start_number = 0):
    if number < 0:
        print("Only Positive & Zero Number ! ! !")
        return
    max_number = pow(2, number) - 1
    binary = bin(start_number).lstrip("0").lstrip("b")
    need_zero = number - len(binary)
    if need_zero <= 0:
        print(binary)
    else:
        add_zero = bin(pow(2, need_zero-1)).lstrip("0b").replace("1", "0")
        print(f"{add_zero}{binary}")
    if start_number < max_number:
        return number_to_max(number, start_number+1)

number = int(input("Enter Number : "))
number_to_max(number)