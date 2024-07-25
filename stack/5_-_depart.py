class Stack :

    def __init__(self,list = None) :
        self.listStack = list
        if list == ['0']:
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
        return self.listStack[-1]
    
    def checkStack(self, carNumber):
        for number in self.listStack:
            if number == carNumber:
                return True
        return False
    
    def removeStack(self, carNumber):
        for number in self.listStack:
            if number == carNumber:
                self.listStack.remove(carNumber)
    
def car(actions):
    max, cars, action, actionCar = actions
    stack = Stack(list(cars.split(",")))
    if action == "arrive":
        if stack.checkStack(actionCar):
            print("car " + actionCar + " already in soi")
        elif stack.size() < int(max):
            stack.push(actionCar)
            print("car " + actionCar + " arrive! : Add Car " + actionCar)
        else:
            print("car " + actionCar + " cannot arrive : Soi Full")
    else:
        if not stack.size():
            print("car " + actionCar + " cannot depart : Soi Empty")
        elif stack.checkStack(actionCar):
            stack.removeStack(actionCar)
            print("car " + actionCar + " depart ! : Car " + actionCar + " was remove")
        else:
            print("car " + actionCar + " cannot depart : Dont Have Car " + actionCar)
    listStack = [int(newStack) for newStack in stack.listStack]
    return listStack
            
    
print("******** Parking Lot ********")
actions = [action for action in input("Enter max of car,car in soi,operation : ").split(" ")]
print(car(actions))