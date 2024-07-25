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


    def append(self,value):

        if self.head is None:

            self.appendHead(value)

            return
        
        p = self.head

        if value < p.value:
            node = Node(value, p)
            self.head = node
            return
        else:
            while p.next != None:
                if value < p.next.value:
                    node = Node(value, p.next)
                    p.next = node
                    return
                p = p.next
        p.next = Node(value)

        p.next = Node(value)

    def printList(self):

        print("After : ", end="")
        p = self.head

        while p != None:
            print(p.value, end= "")
            if p.next != None:
                print(" -> ", end="")
            p = p.next
        print("")


def sorting(numbers):
    linkList = LinkList()
    for number in numbers:
        linkList.append(number)
    linkList.printList()

def printing(numbers):
    print("Before: ", end="")
    for amount in range(len(numbers)):
        print(numbers[amount], end="")
        if len(numbers) - 1 != amount:
            print(" -> ", end="")
    print("")

numbers = [number for number in input("Enter unsorted Linked List: ").split(" ")]
printing(numbers)
sorting(numbers)