def selection_sort(arr):
    for step in range (len(arr)):
        min=step
        for i in range (step+1,len(arr)):
            if arr[i]<arr[min]:
                min=i
        arr[step],arr[min]=arr[min],arr[step]
    return arr

arr=[4,1,7,2,5,8,3]
print(selection_sort(arr))