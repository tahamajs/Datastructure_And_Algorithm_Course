size  = int(input())
line = input().split()
line =[0]+ [int(x) for x in line]
stack =[]
res =[]
for i in range(1,size+1):
    dif = abs(line[i] - line[i-1])
    if(line[i]> line[i-1]):
        stack +=[i]*dif

    elif(line[i] < line[i-1]):
         for j in range(dif):
            res.append([stack.pop(),i-1])

ll = len(stack)         
for i in range(ll):
     res.append([stack.pop(),size])
res.sort()
for i in res:
    print(i[0],i[1])
