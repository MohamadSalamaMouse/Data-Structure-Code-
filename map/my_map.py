from _typeshed import Self


class mymap:
    def __init__(self) -> None:
        self.keys=[]
        self.values=[]
        self.indx=-1
    def __len__(self):
        return len(self.keys)
    def __contains__(self,key):
        if key in self.keys:
            return True
    def add(self ,key,value):

        if key in self.keys:
            i =self.get_index(key)
            self.values[i]=value
        else: 
            self.keys.append(key)
            self.values.append(value)
         
    def get_index(self,key):
        for i,v in enumerate(key):
            if v ==key:
                return i
        
        
    def remove(self,key):
        pass
    def valueof(self,key):
        pass 
    def __inter__(self):
        pass
    def __next__(self):
        pass
        
    