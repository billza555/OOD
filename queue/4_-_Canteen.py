class Queue:
    def __init__(self, items = None) :
        self.items = items
        if items is None:
            self.items = []

    def isEmpty(self) :
        return len(self.items) == 0

    def enQueue(self,data) :
        if self.size() > 1:
            for amount in range(self.size() - 1):
                if int(self.items[amount][0]) == int(data[0]) != int(self.items[amount + 1][0]):
                    self.items.insert(amount + 1, data)
                    break
                elif amount == self.size() - 2:
                    self.items.append(data)
        else:
            self.items.append(data)

    def deQueue(self) :
        return self.items.pop(0)

    def size(self) :
        return len(self.items)

    def peek(self) :
        return self.items[-1]
    
def canteen(workers, queues):
    q = Queue()
    for queue in queues:
        action = None
        id = None
        if len(queue) > 1:
            action, id = queue.split(" ")
        else:
            action = queue
        if action == "E":
            for worker in workers:
                if id == worker[2:]:
                    q.enQueue(worker)
        else: 
            if q.size():
                worker = q.deQueue()
                print(worker[2:])
            else:
                print("Empty")
    
everything = [thing for thing in input("Enter Input : ").split("/")]
workers = everything[0].split(",")
queues = everything[1].split(",")
canteen(workers, queues)