class Node:

    def __init__(self,value=None,next=None):

        self.value = value

        self.next = next

class LinkList:

    def __init__(self):

        self.head = None

    def appendHead(self,value):

        node = Node(value,self.head)

        self.head = node


    def appendLast(self,value):

        if self.head is None:

            self.appendHead(value)

            return
        
        p = self.head
        while p.next != None:
            p = p.next

        p.next = Node(value)

    def removeLast(self):
        
        if self.head == None:
            print("Error!!!")
            return

        p = self.head
        if p.next == None:
            self.head = None
            return
        else:
            while p.next and p.next.next != None:
                p = p.next

        p.next = None

    def rename(self, newName):

        if not self.head:
            print("Error!!!")
            return

        p = self.head
        while p.next != None:
            p = p.next

        p.value = newName

    def printList(self):

        if self.head:

            p = self.head

            while p != None:
                print(p.value, end= "")
                if p.next != None:
                    print(" -> ", end="")
                p = p.next
            print("")

        else:
            print("Linklist is empty!")

    def printListWithNoDuplicate(self):

        if self.head:

            character = []

            p = self.head

            while p != None:
                if p.value not in character:
                    character.append(p.value)
                    print(p.value, end= "")
                if p.next != None and p.next.value not in character:
                    print(" -> ", end="")
                p = p.next
            print("")
        
        else:
            print("Linklist is empty!")


def convertToLinkList(ls):

    linkList = LinkList()

    for song in ls:
        linkList.appendLast(song)

    return linkList

print("*** My Favourite Keynote ***")

songAndOperation = [songOrOp for songOrOp in input("Enter Input / List of operation : ").split("/")]

listSong = [song for song in songAndOperation[0].split(" ") if song != '']
operations = songAndOperation[1].split(",")

myLinkList = convertToLinkList(listSong)

myLinkList.printList()

for operation in operations:
    if operation.split(" ")[1] == "D":
        myLinkList.removeLast()
    elif operation.split(" ")[1] == "R":
        myLinkList.rename(operation.split(" ")[2])
    else:
        myLinkList.appendLast(operation.split(" ")[2])

myLinkList.printList()

myLinkList.printListWithNoDuplicate()