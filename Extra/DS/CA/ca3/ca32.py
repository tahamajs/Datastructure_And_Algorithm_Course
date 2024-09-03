import heapq
n,q,k= list(map(int,input().split()))
numbers = list(map(int,input().split()))


numbers.sort()
sa = numbers[:k-1]
numbers = numbers[k-1:]
heapq.heapify(numbers)


for i in range(q):
    s = input().split()
    if s[0] == "print":
        if len(numbers):
            print(numbers[0])
        else: print(-1)
    elif s[0] == "+":
        x = int(s[1])
        l = len(sa)
    
        if l == k-1:
            if not k-1 or x >= sa[l-1]:
                heapq.heappush(numbers,x)
            else:
                heapq.heappush(numbers,sa[l-1])
                sa[l-1] = x
            
        else:
            sa += [x]
        sa.sort()

    else:
        if numbers:
            heapq.heappop(numbers)


