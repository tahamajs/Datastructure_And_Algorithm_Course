from collections import deque


n, m, k = map(int,input().split())

edges = {tuple(map(int, input().split())): set() for _ in range(k)}
edges[(n, m)] = set()
edges[(1, 1)] = set()
vertexes = set(edges.keys())

def are_adjacent(node1, node2):
    return (node1[0] == node2[0] and abs(node1[1] - node2[1]) == 1) or \
           (node1[1] == node2[1] and abs(node1[0] - node2[0]) == 1)


for node in vertexes :
    if node[0] <= n:
        
        x_value_1 = node[0] + 2
        x_value_2 = node[0]+1
        x_value_3 = node[0]
        x_value_4 = node[0]-1
        x_value_5 = node[0]-2
        neare_edges = [vertex for vertex in vertexes if (vertex[0] == x_value_1 or vertex[0] == x_value_2 or vertex[0] == x_value_3 or vertex[0] == x_value_4 or vertex[0] == x_value_5) and vertex[1] >= node[1]]
        for edg in neare_edges:
            # print(edg,node)
            # if not (edg in edges[node]):
            edges[edg].add(node)
            edges[node].add(edg)
            
            
    
    if node[1] <= m :
        y_value_1 = node[1] + 2
        y_value_2 = node[1] +1
        y_value_3 = node[1]
        y_value_4 = node[1] -1
        y_value_5 = node[1] -2
        neare_edges = [vertex for vertex in vertexes if (vertex[1] == y_value_1 or vertex[1] == y_value_2 or vertex[1] == y_value_3 or vertex[1] == y_value_4 or vertex[1] == y_value_5) and vertex[0] >= node[0]]
        for edg in neare_edges:
            if not (edg in edges[node]):
            # print(edg , node)
                edges[edg].add(node)
                edges[node].add(edg)

adjacent_pairs = [(node1, node2) for i, node1 in enumerate(vertexes) for node2 in vertexes - {node1} if are_adjacent(node1, node2)]
for nod in adjacent_pairs:
    tmpp = list(tuple(edges[nod[0]]+edges[nod[1]]))
    edges[nod[0]] = tmpp
    edges[nod[1]] = tmpp

visited = {i:0 for i in vertexes}
tool = {}

pedars = {}

def BFS():
    first_node = (n,m)
    pedars[first_node] = (-1,-1)
    tool[first_node] = 0
    visited[first_node] = 1
    qq = []
    qq.append(first_node)
    
    while(qq):
        main_node = qq.pop(0)
        for ed in edges[main_node]:
            if not visited[ed]:
                # print(ed)
                tool[ed]= tool[main_node] + 1
                pedars[ed] = main_node
                if ed == (1,1):
                    return tool[ed]
                qq.append(ed)
                visited[ed] = 1
    
    
    
    return -1
    

# print(edges)
# print(vertexes)

# tmp = BFS()
# if tmp != -1:
#     cnt = 0
#     nodddee = (n,m)
#     while(nodddee != (1,1)):
#         print(nodddee, pedars[nodddee] , (nodddee[0] == pedars[nodddee][0] and abs(nodddee[1] - pedars[nodddee][1])==1)  ,(nodddee[1] == pedars[nodddee][1] and abs(nodddee[0] - pedars[nodddee][0]) == 1)  )
#         if not ((nodddee[0] == pedars[nodddee][0] and abs(nodddee[1] - pedars[nodddee][1])==1)  or (nodddee[1] == pedars[nodddee][1] and abs(nodddee[0] - pedars[nodddee][0]) == 1) ):
#            cnt += 1
#         nodddee = pedars[nodddee]
#     print(cnt)
# else:
#     print(-1)

print(BFS())


# ((nodddee[0] == pedars[nodddee][0] and abs(nodddee[1] - pedars[nodddee][1])==1)  or (nodddee[1] == pedars[nodddee][1] and abs(nodddee[0] - pedars[nodddee][0]) == 1) )
