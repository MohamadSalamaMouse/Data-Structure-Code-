class Node:
    def __init__(self,data,next=None,pre=None):
        self.data=data
        self.next=next
        self.previous=pre
    def get_data(self):
        return self.data
    def set_data(self,newdata):
        self.data=newdata
    def get_next(self):
        return self.next
    def set_next(self,newnext):
        self.next=newnext
    def hasnext(self):
        return self.next !=None
    def get_previous(self):
        return self.previous
    def set_previous(self,newprev):
        self.previous=newprev
    def hasprevious(self):
        return self.previous !=None

    
    