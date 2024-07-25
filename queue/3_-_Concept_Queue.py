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
    
def doQueue(queues):
    q = Queue()
    errorDequeue = 0
    errorInput = 0
    queueNumber = 0
    for queue in queues:
        print("Step : " + queue)
        action = queue[0]
        number = queue[1:]
        if action == "E":
            for amount in range(int(number)):
                q.enQueue("*" + str(queueNumber))
                queueNumber += 1
            print("Enqueue : " + str(q.items))
        elif action == "D":
            for amount in range(int(number)):
                if q.size():
                    q.deQueue()
                else:
                    errorDequeue += 1
            print("Dequeue : " + str(q.items))
        else:
            errorInput += 1
            print(q.items)
        print("Error Dequeue : " + str(errorDequeue))
        print("Error input : " + str(errorInput))
        print("--------------------")
    
queues = [queue for queue in input("input : ").split(",")]
doQueue(queues)