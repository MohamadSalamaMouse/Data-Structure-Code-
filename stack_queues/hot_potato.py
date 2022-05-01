from queue import queue
def hot_potato(arr,num):
    q=queue()
    for name in arr:
        q.enqueue(name)
    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()
list1=['bil','musa','nm','kkk','k']
print(hot_potato(list1,3))