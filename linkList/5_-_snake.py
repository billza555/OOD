class LinkList:
    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.count = 0

    class Node:
        __slots__ = 'previous', 'value', 'next'
        def __init__(self,previous= None, value= None, next=None):
            self.previous = previous
            self.value = value
            self.next = next

    def appendHead(self, value):
        p = self.head
        if p.next: 
            p.next = self.Node(previous= p, value=int(value), next=p.next)
            p.next.next.previous = p.next
        else: 
            p.next = self.Node(previous= p, value=int(value))
            self.tail.previous = p.next
        self.count += 1

    def appendLast(self, value):
        if not self.head.next:
            self.appendHead(value)
            return
        p = self.head.next
        while p.next:
            p = p.next
        p.next = self.Node(previous= p, value=int(value))
        self.tail.previous = p.next
        self.count += 1

    def insert(self, previous, value, next):
        if previous is None:
            self.appendHead(value)
            return
        node = self.Node(previous= previous, value=int(value), next=next)
        previous.next = node
        if next is not None:
            next.previous = node
        else:
            self.tail.previous = node
        self.count += 1
        return node
            

    def delete(self, node):
        if node == self.tail.previous:
            self.tail.previous = node.previous
        if node == self.head.next:
            self.head.next = node.next
        previous = node.previous
        next = node.next
        if previous: previous.next = next
        if next: next.previous = previous
        self.count -= 1
        return node.value

    def changePosition(self):
        p = self.head.next.next
        while p:
            if p.next:
                previous = p.previous
                next = p.next.next
                two = self.delete(p.next)
                one = self.delete(p)
                self.insert(self.insert(previous, two, next), one, next)
                p = previous.next 
            else:
                if p: self.delete(p)
                break
            p = p.next.next
        print("Swap success!")
        self.printList()

    def shake(self):
        drops = []
        p = self.head.next
        while p:
            if p.value > self.head.next.value:
                drops.append(p.value)
                self.delete(p)
            p = p.next
        print("Shake success!->", end="")
        self.printList(drops)

    def steal(self, number):
        self.appendLast(number)
        print("Steal success!->" + str(number))
        self.printList()

    def fatherAttack(self, number):
        amount = 0
        p = self.head.next
        while p:
            amount += p.value
            p = p.next
        if amount < number:
            p = self.tail.previous
            drops = []
            while p and p.previous:
                if not p.value:
                    drops.insert(0, self.delete(p))
                    p = p.previous
                elif not number % p.value:
                    break
                else:
                    q = p.previous
                    if p != self.head.next:
                        drops.insert(0, self.delete(p))
                    else:
                        for drop in drops:
                            self.appendLast(drop)
                        drops = []
                        head = self.delete(self.head.next)
                        tail = self.delete(self.tail.previous)
                        self.appendHead(tail)
                        self.insert(self.tail.previous, head, None)
                        break
                    p = q
            print("Play success!->", end="")
            self.printList(drops)
        else:
            print("Play success!->", end="")
            self.printList([])

    def printLinkList(self):
        p = self.head.next
        if self.size() < 2:
            print("(" + str(p.value) + ")->Empty")
            return
        while p.next:
            if p == self.head.next:
                print("(" + str(p.value) + ")->", end="")
            else:
                print(str(p.value) + "->", end="")
            p = p.next
        print(p.value)

    def printList(self, lists=None):
        if lists is not None:
            print("[", end="")
            for index,word in enumerate(lists):
                print(str(word), end="")
                if len(lists) - 1 != index:
                    print(", ", end="")
            print("]")
        self.printLinkList()
        print("------------------------------")

    def size(self):
        return self.count

def snakeGame(snakes, operations):
    linkList = LinkList()
    for snake in snakes:
        linkList.appendLast(snake)
    linkList.printLinkList()
    for operation in operations:
        if "SW" in operation and linkList.size() > 1:
            linkList.changePosition()
        elif "SH" in operation and linkList.size() > 1:
            linkList.shake()
        elif "F" in operation and linkList.size() > 1:
            linkList.steal(int(operation.split(" ")[1]))
        elif "D" in operation:
            linkList.fatherAttack(int(operation.split(" ")[1]))
        if linkList.size() < 2:
            print("Mom is dead")
            break
    print("Snake Game : ")
        
information = [info for info in input("Snake Game : ").split("/")]
snakes = information[0].split(" ")
operations = information[1].split(",")
snakeGame(snakes, operations)