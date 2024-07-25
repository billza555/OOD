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
        return self.listStack[-1], self.listStack[-2]

def colorCrush(colors):
    combo = 0
    stack = Stack()
    for color in colors:
        if stack.size() > 1:
            one, two = stack.peek()
            if one == color == two:
                for amount in range(2):
                    stack.pop()
                combo += 1
            else:
                stack.push(color)
        else:
            stack.push(color)
    word = ""
    for number in range(len(stack.listStack)):
        word += stack.listStack[-(number+1)]
    return word, combo, len(stack.listStack)

colors = [color for color in input("Enter Input : ").split()]
stack, combo, number = colorCrush(colors)
print(number)
if number:
    print(stack)
else:
    print("Empty")
if combo > 1:
    print("Combo : "+ str(combo) + " ! ! !")
