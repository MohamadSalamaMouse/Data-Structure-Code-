import ctypes
class MyArray:
    def __init__(self, size):
        assert size > 0, 'Array size must be > 0'
        self._size = size
        self._next_item = -1

        array_type = ctypes.py_object * size
        self._elements = array_type()

        self.clear(None)

    def __len__(self):
        return self._size

    def clear(self,value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_item < len(self) - 1:
            self._next_item += 1
            return self._elements[self._next_item]
        else:
            raise StopIteration
    
    # Makes our array subscriptable
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), 'Array subscript out of range'
        return self._elements[index]

    # Makes our array subscriptable
    def __setitem__(self, index, value):
        assert index >=0 and index < len(self), 'Array subscript out of range'
        self._elements[index] = value
c1=MyArray(3)
c1.__setitem__(0,10)
c1.__setitem__(1,20)
c1.__setitem__(2,1)
print(c1.__len__())
print(c1.__getitem__(1))
print(c1.__next__())
print(c1.__next__())
print(c1.__next__())