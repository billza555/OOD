class Stack :

    def __init__(self,list = None) :
        self.listStack = list
        if list == None:
            self.listStack = []

    def isEmpty(self) :
        return len(self.listStack) == 0

    def push(self,data) :
        self.listStack.append(data)

    def pop(self) :
        return self.listStack.pop()

    def size(self) :
        return len(self.listStack)

    def peek(self) :
        if self.size() > 0:
            return self.listStack[-1]
        return None
    
    def checkNumber(self, opera, value) :
        for number in self.listStack:
            if opera == "D":
                if number == value:
                    return True
            elif opera == "LD":
                if number < value:
                    return True
            elif opera == "MD":
                if number > value:
                    return True
        return False
    
    def deleteNumber(self, opera, value) :
        s = Stack()
        numbers = []
        for number in self.listStack:
            if opera == "D":
                if number != value:
                    s.push(number)
                else:
                    numbers.append(number)
            elif opera == "LD":
                if number >= value:
                    s.push(number)
                else:
                    numbers.append(number)
            elif opera == "MD":
                if number <= value:
                        s.push(number)
                else:
                    numbers.append(number)
        self.listStack = s.listStack
        return sorted(numbers)
    
def ManageStack(operations):
    s = Stack()
    for operation in operations:
        func = None
        number = None
        if " " in operation:
            func, number = operation.split(" ")
        else:
            func = operation
        if func == "A":
            s.push(int(number))
            print("Add = " + number)
        elif func == "P":
            if s.peek():
                value = s.pop()
                print("Pop = " + str(value))
            else:
                print("-1")
        elif func == "D":
            if s.checkNumber(func, int(number)):
                for numbers in s.deleteNumber(func, int(number)):
                    print("Delete = " + str(numbers))
            elif not s.size():
                print("-1")
        elif func == "LD":
            if s.checkNumber(func, int(number)):
                for numbers in s.deleteNumber(func, int(number)):
                    print("Delete = " + str(numbers) + " Because " + str(numbers) + " is less than " + number)
            elif not s.size():
                print("-1")
        elif func == "MD":
            if s.checkNumber(func, int(number)):
                for numbers in s.deleteNumber(func, int(number)):
                    print("Delete = " + str(numbers) + " Because " + str(numbers) + " is more than " + number)
            elif not s.size():
                print("-1")
    return "Value in Stack = " + str(s.listStack)

operations = [operation for operation in input("Enter Input : ").split(",")]
print(ManageStack(operations))
