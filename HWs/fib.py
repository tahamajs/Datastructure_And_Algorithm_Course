def DFS(v):
    sub[v] = [v]
    for u in children[v]:
        DFS(u)
        for x in sub[v]:
            for y in sub[u]:
                print('hello')
        sub[v] += sub[u]