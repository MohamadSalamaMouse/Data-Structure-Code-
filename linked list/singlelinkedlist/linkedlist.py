from node import Node

class linkedList:
    def __init__(self):
        self.head=None    
    def is_empty(self):
        return self.head==None
    def addAtBeginning(self,item):
        temp=Node(item)
        temp.set_next(self.head)
        self.head=temp
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.get_next()
        return count
    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.get_data()==item:
                found=True
            else:
                current=current.get_next()
        return found 
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.get_data()==item:
                found=True
            else:
                previous=current
                current=current.get_next()
        if previous==None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())
    def addAtEnd(self,item):
        newNode=Node(item)
        current=self.head
        while current.get_next()!=None:
            current=current.get_next()
        current.set_next(newNode)
    
    def addAtPosition(self,item,pos):
        if pos>self.size()or pos<0:
            return None
        else:
            newNode=Node(item)
            count=0
            current=self.head
            while count<pos-1:
                count+=1
                current=current.get_next()
            newNode.set_next(current.get_next())
            current.set_next(newNode)
        
    def printList(self):
        current=self.head
        print("list Data")
        while current!=None:
            print(current.get_data(),end=" ")
            current=current.get_next()
    def clear(self):
        self.head=None 
        
        
mylist=linkedList()
print(mylist.is_empty())
mylist.addAtBeginning(54)
mylist.addAtBeginning(26)
mylist.addAtBeginning(93)
mylist.addAtBeginning(17)
mylist.addAtBeginning(77)
print("size of mylist is ",mylist.size())
print("IS 17 is in mylist: ",mylist.search(17))
mylist.addAtEnd(40)
mylist.printList()
mylist.remove(17)
mylist.printList()