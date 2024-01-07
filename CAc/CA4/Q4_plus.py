from collections import deque

n, m, k = map(int, input().split())

edges = {tuple(map(int, input().split())): [] for i in range(k)}
edges[(n, m)] = []
edges[(1, 1)] = []
vertexes = list(edges.keys())

def are_adjacent(node1, node2):
    return (node1[0] == node2[0] and abs(node1[1] - node2[1]) == 1) or \
           (node1[1] == node2[1] and abs(node1[0] - node2[0]) == 1)

for node in vertexes:
    if node[0] <= n:
        x_values = [node[0] + i for i in range(-2, 3)]
        neare_edges = {vertex for vertex in vertexes if (vertex[0] in x_values) and vertex[1] > node[1]}
        for edg in neare_edges:
            edges[edg].append(node)
            edges[node].append(edg)

    if node[1] <= m:
        y_values = [node[1] + i for i in range(-2, 3)]
        neare_edges = {vertex for vertex in vertexes if (vertex[1] in y_values) and vertex[0] > node[0]}
        for edg in neare_edges:
            edges[edg].append(node)
            edges[node].append(edg)

def BFS():
    first_node = (1, 1)
    pedars = {first_node: (-1, -1)}
    tool = {first_node: 0}
    visited = {i: 0 for i in vertexes}
    visited[first_node] = 1
    qq = deque([first_node])

    while qq:
        main_node = qq.popleft()
        for ed in edges[main_node]:
            if not visited[ed]:
                tool[ed] = tool[main_node] + 1
                pedars[ed] = main_node
                if ed == (n, m):
                    return tool[ed]
                qq.append(ed)
                visited[ed] = 1

    return -1

print(BFS())
