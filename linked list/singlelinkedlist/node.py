class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def get_data(self):
        return self.data
    def set_data(self,newData):
        self.data=newData
    def get_next(self):
        return self.next 
    def set_next(self,newNext):
        self.next=newNext