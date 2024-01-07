n= int(input())

edges = {i:[] for i in range(1,n+1)}
# visited  = {i:0 for i in range(1,n+1)}
ertefah = {}
father = {}

for _ in range(n-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
    

    
final_order = list(map(int, input().split()))








visit = [0]*(n+1)

# qqq = []
def DFS(time ,node , search_node , list_):
    # print(visit , node)
    time = time +1
    list_.append(node)
    # print(list_,  time , 'time')
    if len(edges[node]) == 1 and (time != 1) or (node == search_node == 1):
        if node == search_node:
            # print('kkkkjsjf')
            # qqq.append(search_node)
            return True
        else:
            return False
        
    flag = True
    for nn in edges[node]:
        # print('hellp',nn)
        if visit[nn]==0:
            visit[nn] = 1
            
            state = DFS(time,nn,search_node , list_)
            # print(state , list_ , nn , search_node)
            if ( state == False):
                list_.pop()
            else:
                flag = False
    if not flag:
        return True
    return False


# lis = []
# visit[1] = 1
# DFS(0,1, final_order[0] , lis)

# print(1 , final_order[0] , lis)


# lis = []
# visit = [0]*(n+1)
# DFS(0,final_order[0] , final_order[1] , lis)

# print(final_order[0] , final_order[1] , lis)

# edges = {i for i in range(1,n+1)}

path_resalt = []


# lis = []
# visit[1] = 1
# DFS(0,1, final_order[0] , lis)
# print(lis , 'aval')
# path_resalt = path_resalt + (lis)

lis = []
visit[1] = 1
DFS(0,1, final_order[0] , lis)
# print(lis , final_order[0], final_order[1],'dovom')
path_resalt = path_resalt + (lis)


for i in range(1,len(final_order)):
    lis = []
    visit = [0]*(n+1)
    DFS(0,final_order[i-1] , final_order[i] , lis)
    path_resalt = path_resalt + lis[1:]
    # print(lis , final_order[i-1] , final_order[i] , i , 'srsrt' )



lis = []
visit = [0]*(n+1)
visit[final_order[len(final_order)-1]] = 1
DFS(0, final_order[len(final_order)-1] , 1 , lis)
# print(lis ,final_order[len(final_order)-1], 'avadrtgkjrtkjghdrhtgkjdrthgl')
path_resalt = path_resalt + lis[1:-1]
# print(lis)


# print(path_resalt)

if len(path_resalt) != (2*n -2):
    print(-1)
    # print(*path_resalt)
else:
    print(*path_resalt)