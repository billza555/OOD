class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        def __init__(self,previous=None, value=None,next=None):
            self.previous = previous
            self.value = value
            self.next = next

    def appendHead(self,value):
        node = self.Node(value=value, next=self.head)
        self.head = node

    def appendLast(self,value):
        if self.head is None:
            self.appendHead(value)
            if self.tail is None:
                self.tail = self.head
            return
        p = self.head
        while p.next != None:
           p = p.next
        p.next = self.Node(previous=p, value=value)
        self.tail = p.next

    def getNode(self,value):
        if not self.head:
            return
        p = self.head
        while p.next != None and p.value != value:
            p = p.next
        if p.value == value:
            return p
        return

    def goRight(self, start, stop):
        station  = []
        startNode = self.getNode(start)
        stopNode = self.getNode(stop)
        if startNode.value == stopNode.value:
            return [startNode.value]
        if not startNode.next:
            station.append(startNode.value) 
            startNode = self.head
        while startNode.value != stopNode.value:
            station.append(startNode.value)
            if not startNode.next:
                startNode = self.head
            else:
                startNode = startNode.next
        station.append(startNode.value)
        return station
    
    def goLeft(self, start, stop):
        station  = []
        startNode = self.getNode(start)
        stopNode = self.getNode(stop)
        if startNode.value == stopNode.value:
            return [startNode.value]
        if not startNode.previous:
            station.append(startNode.value) 
            startNode = self.tail
        while startNode.value != stopNode.value:
            station.append(startNode.value)
            if not startNode.previous:
                startNode = self.tail
            else:
                startNode = startNode.previous
        station.append(startNode.value)
        return station

def trainGo(stations, destinations):
    linkList = LinkList()
    for station in stations:
        linkList.appendLast(station)
    if len(destinations) < 3:
        destinations.append("FB")
    goRight = linkList.goRight(destinations[0], destinations[1])
    goLeft = linkList.goLeft(destinations[0], destinations[1])
    trainPassStation = [[], []]
    if "F" in destinations[2]:
        trainPassStation[0] = goRight
    if "B" in destinations[2]:
        trainPassStation[1] = goLeft
    return trainPassStation

def printStation(stations, word):
    print(word, end="")
    for amount in range(len(stations)):
        print(stations[amount], end="")
        if len(stations) - 1 > amount:
            print("->", end="")
    print("," + str(len(stations) - 1))

def findWay(stations, destinations):
    goRight, goLeft = trainGo(stations, destinations)
    if len(goRight) == len(goLeft):
        printStation(goRight, "Forward Route: ")
        printStation(goLeft, "Backward Route: ")
    elif len(goRight) > 1 and (len(goRight) < len(goLeft) or len(goLeft) < 2):
        printStation(goRight, "Forward Route: ")
    else:
        printStation(goLeft, "Backward Route: ")

print("***Railway on route***")
railway = [rail for rail in input("Input Station name/Source, Destination, Direction(optional): ").split("/")]
stations = railway[0].split(",")
destinations = railway[1].split(",")
findWay(stations, destinations)