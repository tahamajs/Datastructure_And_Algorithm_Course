n , q = map(int,input().split())

pedars = {}
pedars[1]=0
tedad_baches = [0] *( n+1)

pedsss = list(map(int,input().split()))


for i in range(n-1):
    pedars[i+2] = pedsss[i]
    tedad_baches[pedsss[i]] += 1



querys = []
for i in range(q):
    querys.append(list(map(int,input().split())))


answares = []
for tmp in querys:
    many = tmp[0]
    sum = 0
    query = tmp[1:]
    p_list = {pedars[nod]:0 for nod in query}
    
    for j in range(many):
        sum += tedad_baches[tmp[j+1]] +1
        if pedars[tmp[j+1]] != None:
            p_list[pedars[tmp[j+1]]] += 1
    
    for i in set(query).intersection(p_list.keys()):
        
        sum -= 2*p_list[i]
    print(sum)



