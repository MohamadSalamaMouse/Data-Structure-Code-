class Node: 
    def __init__(self,data=None,next=None,Pre=None): 
        self.data=data 
        self.next=next 
        self.pre=Pre
    def getdata(self): 
        return self.data 
    def setdata(self,item): 
        self.data=item 
    def getnext(self): 
        return self.next 
    def hasnext(self): 
        return self.next !=None 
    def setnext(self,newnext): 
        self.next=newnext 
    def getpre(self): 
        return self.pre 
    def haspre(self): 
        return self.pre !=None 
    def setpre(self,newpre): 
        self.pre=newpre 
class DoubleLinkedList: 
    def __init__(self): 
        self.head=None 
        self.tail=None 
 
    def size(self): 
        pointer=self.head 
        count=0 
        while pointer !=None: 
            count=count+1 
            pointer=pointer.getnext() 
        return count 
 
    def addAtBeginning(self,item): 
        node=Node(item)
        if self.head==None: 
            self.head=self.tail=node 
        else: 
             
            node.setpre(None) 
            node.setnext(self.head) 
            self.head.setpre(node) 
            self.head=node 
 
    def addAtend(self,item): 
        node=Node(item) 
        pointer=self.head 
        while pointer.getnext()!=None: 
            pointer=pointer.getnext() 
        pointer.setnext(node) 
        self.tail=node 
 
    def addAtmiddle(self,item,pos): 
        if pos>self.size() or pos<0: 
            return None 
        else: 
            node=Node(item) 
            count=0 
            pointer=self.head 
            while count<pos-1: 
                count+=1 
                pointer=pointer.getnext() 
            node.setnext(pointer.getnext()) 
            node.setpre(pointer) 
            pointer.getnext().setpre(node) 
            pointer.setnext(node) 
 
    def remove(self,item): 
        pointer=self.head 
        found=False 
        while not found: 
            if pointer.getdata()==item: 
                found =True 
            else:  
                pointer=pointer.getnext() 
        if pointer.getpre()==None: 
            self.head=pointer.getnext() 
        else: 
            pointer.getpre().setnext(pointer.getnext()) 
            pointer.getnext().setpre(pointer.getpre())
n=DoubleLinkedList()
n.addAtBeginning(12)
n.addAtend(35)
n.addAtmiddle(67,1)
