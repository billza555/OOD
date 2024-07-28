def fibonacci(number):
    if number == 0 or number == 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

number = int(input("Enter Number : "))
print(f"fibo({number}) = {fibonacci(number)}")