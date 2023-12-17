

def fun(tmp_nods):




    stack = []
    dict_ends = {}
    dict_starts = {}
    nodes = []




    cnt = 0
    for i , nod in enumerate(tmp_nods) :
        if cnt != 0:
            if nod == nodes[cnt-1]:
                continue

        nodes.append(nod)

        
        
        dict_ends[nod] = cnt
        
        if not nod in dict_starts :
            dict_starts[nod] = cnt

        cnt +=1
            

    # print(nodes)
            
    # print(dict_ends)
    # print(dict_starts)





    # print(nodes)



    max = 0
    count = 0

    bad_value = False

    for i , nod in enumerate(nodes):
        if i == dict_ends[nod] and  i == dict_starts[nod]:
            count +=1
            if max < count :
                max = count
            count -=1
            continue

        
        if(i == dict_starts[nod]):    
            stack.append(nod)
            count +=1
        

        
        if i == dict_ends[nod] :
            # print(stack , count)
            if stack[count - 1] == nod:
                stack.pop()
                count -=1
            else:
                bad_value = False
                
                
                
        if max < count :
            max = count
    
    if(stack):
        bad_value = True
    
    
    
    
    
    if not bad_value : 
        return (max)
    else:
        return (-1)
    
    







n = int(input())






# stack = []
# dict_ends = {}
# dict_starts = {}
tmp_nods = []
# nodes = []


flag = False



maxx = 0
for i in range(n):
    tmp = int(input())
    if tmp == 0:
        ret = fun(tmp_nods)
        if ret == -1:
            flag = True
            break
        maxx = max(maxx , ret)
        # print(maxx , 'maxx')
        tmp_nods = []
        
        continue
    tmp_nods.append(tmp)


ret = fun(tmp_nods)
if ret == -1:
    flag = True
maxx = max(maxx , ret)
# print(maxx , 'maxx')
tmp_nods = []

if not flag :
    print(maxx)
else: 
    print(-1)


# cnt = 0
# for i , nod in enumerate(tmp_nods) :
#     if cnt != 0:
#         if nod == nodes[cnt-1]:
#             n -= 1
#             continue

#     nodes.append(nod)

    
    
#     dict_ends[nod] = cnt
    
#     if not nod in dict_starts :
#         dict_starts[nod] = cnt

#     cnt +=1
        

# # print(nodes)
        
# # print(dict_ends)
# # print(dict_starts)





# # print(nodes)



# max = 0
# count = 0

# bad_value = False

# for i , nod in enumerate(nodes):
#     if i == dict_ends[nod] and  i == dict_starts[nod]:
#         count +=1
#         if max < count :
#             max = count
#         count -=1
#         continue

    
#     if(i == dict_starts[nod]):    
#         stack.append(nod)
#         count +=1
    

    
#     if i == dict_ends[nod] :
#         print(stack , count)
#         if stack[count - 1] == nod:
#             stack.pop()
#             count -=1
#         else:
#             bad_value = False
            
            
            
#     if max < count :
#         max = count






# print(stack)










# if not bad_value : 
#     print(max)
# else:
#     print(-1)



    
    
    
    
    


