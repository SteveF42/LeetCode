import heapq

def func(start,end):
    # O(n + m) n being the start and end array size and m being the size of the heap, potentially being the size of the array
    # O(n logn) because we have to sort the array
    arr = []
    for i in range(len(start)):
        arr.append([start[i],end[i]])
    
    minHeap = []
    arr.sort(key=lambda x : x[0])
    machines = 0
    for task in arr:
        while minHeap and minHeap[0] <= task[0]:
            heapq.heappop(minHeap)
        heapq.heappush(minHeap,task[1])
        machines = max(machines,len(minHeap))
    
    return machines
print(func([1,8,3,9,6],[8,9,6,14,7]))
print(func([0,5,10,30],[10,20,25,40])) #2
print(func([1,2,3],[5,4,4])) #3
print(func([5,2],[10,8])) #2
print(func([10],[11])) #1