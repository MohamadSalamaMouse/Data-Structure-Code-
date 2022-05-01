def search_item(list_value,target):
    low=0
    high=len(list_value)
    while low<=high:
        mid=(low+high)//2
        guess=list_value[mid]
        if guess==target:
            return mid
        elif guess >target:
            high=mid-1
        else:
            low=mid+1
    return False
list1=[1,2,3,4,5,6,7,8,10]

print(search_item(list1,-1))