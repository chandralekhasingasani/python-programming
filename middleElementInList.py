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

    def middleElement(self):
        slow=List.first
        fast=List.first

        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next

        return slow.item


l=List()
l.addElementInListAtEnd(30)
l.addElementInListAtEnd(20)
l.addElementInListAtEnd(10)
l.printElements()
print(l.middleElement())



