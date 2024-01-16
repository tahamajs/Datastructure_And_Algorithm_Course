import heapq

# Create an empty heap
valid_heap = []

not_valid_heap = []

d ,n = map(int, input().split())


for i in range(d):
    tmp_lis = list(map(int,input().split()))
    not_valid_heap.append(tmp_lis)

heapq.heapify(not_valid_heap)

# print(not_valid_heap)

# print(not_valid_heap[0][0])

for day in range(1,n+1):
    while not_valid_heap and (not_valid_heap[0][0] == day) :
        pushed_element = heapq.heappop(not_valid_heap)
        heapq.heappush(valid_heap,[-pushed_element[2], pushed_element[1]])
    
    
    # print(valid_heap[0][1])
    if(valid_heap):
        valid_heap[0][1] -= 1
        if valid_heap[0][1] == 0:
            heapq.heappop(valid_heap)


angry_result = 0

while valid_heap:
    pop_element = valid_heap.pop()
    angry_result += pop_element[0] * pop_element[1]

print(-angry_result)
    