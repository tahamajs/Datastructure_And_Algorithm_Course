def find_shortest_path(start, end): 
    if start == end:
        return 0
    node_queue = [[start, 0]]
    while len(node_queue) != 0:
        node, par = node_queue.pop(0)
        for adj in adjes[node - 1]:
            if not(visited[adj - 1][node - 1] > visited[node - 1][par - 1] + 1):
                continue
            if (par, node, adj) in problems:
                continue
            if adj == end:
                return visited[node - 1][par - 1] + 1
            node_queue.append([adj, node])
            visited[adj - 1][node - 1] = visited[node - 1][par - 1] + 1
    return -1
        
n, m = list(map(int, input().split()))
adjes = [[] * n for i in range(n)]
for i in range(m):
    n1, n2 = list(map(int, input().split()))
    adjes[n1 - 1].append(n2)
    adjes[n2 - 1].append(n1)
start, end = list(map(int, input().split()))
q = int(input())
problems = set()
for i in range(q):
    problems.add(tuple(map(int, input().split())))
visited = [[10000000]*n for i in range(n)] 
visited[start - 1] = [0]*n
#print(-1)
print(find_shortest_path(start, end))    