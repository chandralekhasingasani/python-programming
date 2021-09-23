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

    def deleteMatchingElementsInList(self):
        dict={}
        present=List.first
        preceeding=None
        while present is not None:
            if present.item in dict.keys():
                preceeding.next=present.next
            else:
                dict[present.item]=1
                preceeding=present
            present=present.next

l=List()
l.addElementInListAtEnd(30)
l.addElementInListAtEnd(20)
l.addElementInListAtEnd(10)
l.addElementInListAtEnd(30)
#l.printElements()
l.deleteMatchingElementsInList()
l.printElements()



