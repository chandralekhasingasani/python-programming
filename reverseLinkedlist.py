class List:
    first=None
    last=None
    def __init__(self):
        self.next=None

    def addElementInListAtEnd(self,item):
        temp=List()
        temp.item=item
        if List.first is None:
            List.first=temp
            List.last=temp
        else:
            List.last.next=temp
            List.last=temp

    def printElements(self):
        temp=List.first
        while temp is not None:
            print(temp.item)
            temp=temp.next

    def reverseLinkedList(self):
        temp=None
        curl=None

        while List.first is not None:
            temp=List.first
            List.first=List.first.next
            temp.next=curl
            curl=temp

        List.first=curl
        return List.first

l=List()
l.addElementInListAtEnd(30)
l.addElementInListAtEnd(20)
l.addElementInListAtEnd(10)
l.printElements()
l.reverseLinkedList()
l.printElements()



