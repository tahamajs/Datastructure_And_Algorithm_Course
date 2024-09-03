import heapq

n,t = list(map(int,input().split()))
x = list(map(int,input().split()))
index = [i for i in range(n)]
lit = list(zip(x,index))
lit = list(map(list,lit))
lit.sort(key = lambda x:(x[0],x[1]),reverse=True)
res={i:None for i in index}
heap = []
heapq.heapify(heap)

queue =[]
time =0
while lit or heap or queue:
    if not heap and not queue and lit:
        time = lit[-1][0]+t
    for j in range(len(lit)-1,-1,-1):
        if lit[j][0] <= time:
            h = lit.pop()[1]
            if queue and h > queue[-1]:
                     heapq.heappush(heap,h)
            else:
                queue.append(h)
        else:
            break
    if queue:
        x = queue.pop(0)
        res[x] = time
    if heap and not queue:
        queue += [heapq.heappop(heap)]
        
    time += t


print(*res.values())

