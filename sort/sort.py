
list1=[3,6,4,9,5,8,10]
def FindSmallest(list1):
    smallest=list1[0]
    smallest_index=0
    for i in range(1,len(list1)):
        if list1[i]<smallest:
            smallest=list1[i]
            smallest_index=i
    return smallest_index
def selectionsort(list1):
    arrnew=[]
    for i in range(len(list1)):
        smallest=FindSmallest(list1)
        arrnew.append(list1.pop(smallest))
    return arrnew
print(selectionsort(list1))

            
