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
        return self.listStack[-1]

def infix2postfix(exp) :
    postfix = ""
    action = {"+" : 1, "-" : 1, "/" : 2, "*" : 2, "^" : 3}
    stack = Stack()
    for charac in exp:
        if charac.isalpha():
            postfix += charac
        else:
            if not stack.size():
                stack.push(charac)
            elif charac in "+-*/^":
                while(stack.size()):
                    if stack.peek() in "(":
                        break
                    elif action[charac] <= action[stack.peek()]:
                        postfix += stack.pop()
                    else:
                        break
                stack.push(charac)
            else:
                if charac in "(":
                    stack.push(charac)
                else:
                    while(stack.size()):
                        if stack.peek() != "(":
                            postfix += stack.pop()
                        else:
                            stack.pop()
                            break
    postfix += ''.join(stack.listStack[::-1])
    return postfix

print(" ***Infix to Postfix***")
token = input("Enter Infix expression : ")
print("PostFix : ")
print(infix2postfix(token))