def bubble_Sort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range (passnum):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

arr=[4,1,7,2,5,8,3]

print(bubble_Sort(arr))