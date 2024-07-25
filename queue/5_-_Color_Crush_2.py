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
    
    def insert(self,data) :
        self.listStack.insert(self.size(), data)
    
class Queue:
    def __init__(self) :
        self.items = []

    def isEmpty(self) :
        return len(self.items) == 0

    def enQueue(self,data) :
        self.items.append(data)

    def deQueue(self) :
        return self.items.pop(0)

    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]
    
def mirrorCrush(bombs):
    stack = Stack()
    queue = Queue()
    for bomb in bombs:
        if stack.size() > 1:
            color1, color2 = stack.peek()
            if color1 == color2 == bomb:
               queue.enQueue(bomb)
               stack.pop()
               stack.pop()
            else:
               stack.push(bomb)
        else:
            stack.push(bomb)
    return stack,queue

def normalCrush(bombs, interrupt):
    stack = Stack()
    failed = 0
    crush = 0
    for bomb in bombs:
        if stack.size() > 1:
            color1, color2 = stack.peek()
            if color1 == color2 == bomb:
                if interrupt.size():
                    enemy = interrupt.deQueue()
                    stack.insert(enemy)
                    color1, color2 = stack.peek()
                    if color1 == color2 == bomb:
                        stack.pop()
                        stack.pop()
                        failed += 1
                    else:
                        stack.push(bomb)
                else:
                    stack.pop()
                    stack.pop()
                    crush += 1
            else:
               stack.push(bomb)
        else:
            stack.push(bomb)
    return stack, failed, crush
    
def colorCrush2(bombs):
    mirror, interrupt = mirrorCrush(bombs[1][::-1])
    mirrorBomb = len(interrupt.items)
    normal, failed, normalBomb = normalCrush(bombs[0], interrupt)
    print("NORMAL :")
    print(len(normal.listStack))
    if not len(normal.listStack):
        print("Empty")
    else:
        print(''.join(normal.listStack[::-1]))
    print(str(normalBomb) + " Explosive(s) ! ! ! (NORMAL)")
    if failed:
        print("Failed Interrupted " + str(failed) + " Bomb(s)")
    print("------------MIRROR------------")
    print(": RORRIM")
    print(len(mirror.listStack))
    if not len(mirror.listStack):
        print("ytpmE")
    else:
        print(''.join(mirror.listStack[::-1]))
    print("(RORRIM) ! ! ! (s)evisolpxE " + str(mirrorBomb))
    
bombs = [bomb for bomb in input("Enter Input (Normal, Mirror) : ").split(" ")]
colorCrush2(bombs)