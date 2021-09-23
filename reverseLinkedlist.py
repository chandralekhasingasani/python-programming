class List:
    first=last=None
    def __init__(self):
        self.next=None

    def addElementInListAtEnd(self,item):
        temp=List()
        temp.item=item
        if first == None:
            first=last=temp
        else:
            temp.next=last
            last.next=temp
            last=temp

    def printElements(self):
        temp=first
        while temp != None:
            print(temp.item)
            temp=temp.next

l=List()
l.addElementInListAtEnd(30)



