class Queue:
    def __init__(self) :
        self.items = []

    def isEmpty(self) :
        return len(self.items) == 0

    def enQueue(self,data) :
        self.items.append(data)

    def deQueue(self) :
        self.items = sorted(self.items)
        return self.items.pop(0)

    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]
    
def doQueue(queues):
    q = Queue()
    for queue in queues:
        if " " in queue:
            value = int(queue[2:])
            q.enQueue(value)
            print(q.size())
        else:
            if q.size() > 0:
                print(str(q.deQueue()) + " 0")
            else:
                print("-1")
    words = ""
    while(not q.isEmpty()):
        words += str(q.deQueue()) + " "
    if words == "":
        print("Empty")
    else:
        print(words)

queues = [queue for queue in input("Enter Input : ").split(",")]
doQueue(queues)