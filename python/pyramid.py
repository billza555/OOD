def pyramid(number):
    lenght = number * 4 - 3
    center = (lenght - 1) / 2
    for column in range(lenght):
        for row in range(lenght):
            if not column or not row or column == lenght - 1 or row == lenght - 1:
                print("#", end="")
            elif row > 1 and row < lenght - 2 and column > 1 and column < lenght - 2:
                if not column % 2:
                    if not row % 2:
                        print("#", end="")
                    elif column < center and row >= column and row <= lenght - column - 1:
                        print("#", end="")
                    elif column > center and row + column > center * 2 and row + column < center + 2 * (column - center / 2):
                        print("#", end="")
                    else:
                        print(".", end="")
                else:
                    if (row > column and row < lenght - column) or row == 1 or row == lenght - 2 or row % 2:
                        print(".", end="")
                    elif column > center and row >= center * 2 - column and row <= column:
                        print(".", end="")
                    else:
                        print("#", end="")
            else:
                print(".", end="")
        print("")

print("*** Fun with Drawing ***")
number = int(input("Enter input : "))
pyramid(number)