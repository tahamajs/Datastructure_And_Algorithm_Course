n,m,t = list(map(int,input().split()))
res =0
map = {}
while t:
    x,y = input().split()
    x,y = int(x),int(y)
    
    if (x,y) not in map :
        map[(x,y)] = True
        res +=2
        if (x-1,y) in map: res-=1  
        if (x+1,y) in map: res-=1 
        if (x,y-1) in map: res-=1 
        if (x,y+1) in map: res-=1 
    print(res)
    t-=1