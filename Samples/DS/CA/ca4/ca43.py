import sys
sys.setrecursionlimit(15000)
class Node():
    def __init__(self,value):
        self.value= value
        self.v = []
        self.color = "white"
        self.parent = None
        self.d = None
        
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
        t = qu.pop()
        for v in t.v:
            if v.color == "white":
                v.color = "gray"
                v.d = t.d +1
                v.parent = t
                qu += [v]
                res +=[v.value]
        t.color = "black"
    
    return res

n = int(input())

def dfs_cycle(u, p,cycles):
    if u.color == "black":
        return False
    if u.color == "gray":
        v = []
        cur = p
        v.append(cur)
        while cur != u:
            cur = cur.parent
            v.append(cur)
        cycles[0] = v
        return True
    u.parent = p
    u.color = "gray"
    for v in u.v:
        if v == u.parent:
            continue
        ee = dfs_cycle(v,u,cycles)
        if ee == True:
            return True

    u.color = "black"
cycles = [[]]
graph = []
for i in range(1,n+1):
    graph.append(Node(i))
for i in range(n):
    f,e = list(map(int,input().split()))
    graph[f-1].add_v(graph[e-1])
    graph[e-1].add_v(graph[f-1])
for u in graph:
    u.color = "white"
    u.d=0
    u.parent = None

dfs_cycle(graph[0],None,cycles)

graph.append(Node(n+1))
graph[n].v = cycles[0]
for x in cycles[0]:
    x.add_v(graph[n])
final = [0]*n


BFS(graph,graph[n])

for x in range(n):
    final[x] = graph[x].d -1

print(*final)
