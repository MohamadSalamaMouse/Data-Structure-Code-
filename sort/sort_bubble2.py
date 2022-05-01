def bubbelsort2(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[1,5,3,2,6,0,-1]
print(bubbelsort2(arr))
