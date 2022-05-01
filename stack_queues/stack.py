class stack:
    def __init__(self) :
        self.items= []
        self.top=-1
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.top+=1
        self.items.append(item)
    def pop(self):
        self.top-=1
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

    
#instance of stack
