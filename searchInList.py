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

    def lenoflist(self):
        temp=List.first
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        return count

    def searchInlist(self,ele):
        temp=List.first
        while temp is not None:
            if temp.item == ele:
                return True
            temp=temp.next
        return False

l=List()
l.addElementInListAtEnd(30)
l.addElementInListAtEnd(20)
l.addElementInListAtEnd(10)
print(l.lenoflist())
print(l.searchInlist(1))



