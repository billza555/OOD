class Queue:
    def __init__(self, time) :
        self.items = []
        self.time = time
        self.timeCon = 0

    def isEmpty(self) :
        return len(self.items) == 0

    def enQueue(self,data) :
        self.items.append(data)

    def deQueue(self) :
        if self.size() > 0:
            return self.items.pop(0)

    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]
    
    def increaseTime(self):
        if self.size() > 0:
            self.timeCon += 1
        if self.timeCon >= self.time:
            self.deQueue()
            self.timeCon = 0

def wait(peopleTime):
    queue1 = Queue(3)
    queue2 = Queue(2)
    allPeople = Queue(0)
    people, time = peopleTime
    for person in people:
        allPeople.enQueue(person)
    for timer in range(int(time)):
        queue1.increaseTime()
        queue2.increaseTime()
        goQueue = allPeople.deQueue()
        goFirst = False
        if queue1.size() < 5:
            queue1.enQueue(goQueue)
            goFirst = True
        if queue2.size() < 5 and not goFirst:
            queue2.enQueue(goQueue)
        strPeople = [item for item in allPeople.items if item is not None]
        strQueue1 = [item for item in queue1.items if item is not None]
        strQueue2 = [item for item in queue2.items if item is not None]
        print(str(timer + 1) + " " + str(strPeople) + " " + str(strQueue1) + " " + str(strQueue2))


peopleTime = [word for word in input("Enter people and time : ").split()]
wait(peopleTime)