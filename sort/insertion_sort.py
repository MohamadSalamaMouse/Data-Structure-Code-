
def insertionSort(alist):
    for step in range(1, len(alist)):
        key = alist[step]
        j = step - 1
        # Compare key with each element on the left of it 
        # until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        alist[j + 1] = key
        
testlist = [9, 5, 1, 4, 3]
insertionSort(testlist)
print('Sorted list in Ascending Order:',testlist)

