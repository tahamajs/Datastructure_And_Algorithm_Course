n, m = map(int, input().split())

enemies = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    enemies[u].append(v)
    enemies[v].append(u)

visited = {i: 0 for i in range(1, n + 1)}
teams = {1: [], 2: []}


def dfs(node, team, teams, enemies, visited):
    if visited[node] != 0:
        return

    visited[node] = team
    teams[team].append(node)

    for neighbor in enemies[node]:
        # if neighbor in teams[team]:
        #     return 

        if visited[neighbor] == 0:
            dfs(neighbor, 3 - team, teams, enemies, visited)


for node in range(1, n + 1):
    if visited[node] == 0 :
        dfs(node, 2, teams, enemies, visited)

flag = True




for node in range(1, n + 1):
    ff = 0
    for enemy in enemies[node]:
        if visited[node] != visited[enemy]:
            # print([enemy], node)
            ff = 1
            break
    if not ff:
        print(enemies[node], visited[node] , 'kkkk' , ff)
        flag = False
    


if flag == True:
    print(len(teams[2]))
    print(" ".join(map(str, teams[2])))
else:
    print(-1)

# print(teams)