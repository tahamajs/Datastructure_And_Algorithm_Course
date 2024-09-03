
class Node():
    def __init__(self,value,):
        self.value= value
        self.v = []
        self.color = "white"
        self.parent = None
        self.d = None
        self.f = None

    def add_v(self,v):
        self.v += [v]
        
def BFS(graph,x):
    for u in graph:
        u.color = "white"
        u.d=0
        u.parent = None
    x.color ="gray"
    x.d = 0
    x.parent = None
    res = [x.value]
    qu = [x]
    while qu:
        t = qu.pop(0)
        for v in t.v:
            if v.color == "white":
                v.color = "gray"
                v.d = t.d +1
                v.parent = t
                qu += [v]
                res+=[v.value]
        t.color = "black"
    
    return res
def DFS_visit(x,res,time):
    res += [x.value]
    x.color = "gray"
    time +=1
    x.d = time
    for v in x.v:
        if v.color == "white":
            v.parent= x
            DFS_visit(v,res,time)
    x.color = "black"
    time+=1
    x.f = time
def DFS(graph,x):
    for u in graph:
        u.color = "white"
        u.d=0
        u.f=0
        u.parent = None
    time = 0
    res=[]
    DFS_visit(x,res,time)
    return res




n,m = list(map(int,input().split()))
graph = []
for i in range(1,n+1):
    graph.append(Node(i))

for i in range(m):
    f,e = list(map(int,input().split()))
    graph[f-1].add_v(graph[e-1])
    graph[e-1].add_v(graph[f-1])

for x in graph:
    x.v = sorted(x.v,key = lambda m: m.value)
o = int(input())
res=[]
for i in range(o):
    order = input().split()
    if order[0] == "1":
        x = int(order[2])
        if order[1] == "BFS":
            res = BFS(graph,graph[x-1])
        else:
            res = DFS(graph,graph[x-1])
        print(len(res))
    else:
        index = int(order[1])
        if res and index <= len(res) :
            print(res[index-1])
        else:
            print(-1)