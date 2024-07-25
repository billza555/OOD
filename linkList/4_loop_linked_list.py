class LinkList:

    def __init__(self):

        self.head = None

    class Node:

        def __init__(self,value=None,next=None):

            self.value = value

            self.next = next


    def appendHead(self,value):

        node = self.Node(value,self.head)

        self.head = node


    def appendLast(self,value):

        if self.head is None:

            self.appendHead(value)

            return
        
        p = self.head
        while p.next != None:
            p = p.next

        p.next = self.Node(value)

    def changeIndex(self, index, indexChange):
        tail = self.getTail()
        if not tail:
            print("Error! {list is empty}")
            return
        firstNode = self.getNode(index)
        if not firstNode:
            print("Error! {index not in length}: " + str(index))
            return
        secondNode = self.getNode(indexChange)
        if not secondNode:
            print("index not in length, append : " + str(indexChange))
            tail.next = self.Node(indexChange)
            return
        print("Set node.next complete!, index:value = " + str(index) + ":" + str(firstNode.value) + " -> " + str(indexChange) + ":" + str(secondNode.value))
        firstNode.next = self.Node(secondNode.value)

        
    def getNode(self, value):
        if self.head == None:
            return None
        else:
            p = self.head
            count = 0
            while p.next != None and count != int(value):
                p = p.next
                count += 1
            if count == int(value):
                return p
            else:
                return None
        
    def getTail(self):
        if self.head == None:
            return None

        p = self.head

        while p.next != None:
            p = p.next

        return p
    
    def checkLoop(self):
        if self.head == None:
            print("No Loop")
            print("Empty")
            return
        numbers = []
        p = self.head
        tail = self.getTail()
        if not p.next:
            if tail.value is p.value and tail != p:
                print("Found Loop")
            else:
                print("No Loop")
                self.printList()
            return
        while p.next.next != None:
            numbers.append(p.value)
            p = p.next
        numbers.append(p.value)
        if tail.value in numbers:
            print("Found Loop")
        else:
            print("No Loop")
            self.printList()

    def printList(self):
        if self.head == None:
            print("Empty")
        else:
            p = self.head

            while p != None:
                print(p.value, end= "")
                if p.next != None:
                    print("->", end="")
                else:
                    break
                p = p.next
            print("")

def doOpertion(operations):
    linkList = LinkList()
    for operation in operations:
        opera, numbers = operation.split(" ")
        if opera == "A":
            linkList.appendLast(numbers)
            linkList.printList()
        else:
            linkList.changeIndex(numbers[0], numbers[-1])
    linkList.checkLoop()

operations = [operation for operation in input("Enter input : ").split(",")]
doOpertion(operations)