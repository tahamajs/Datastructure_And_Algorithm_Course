def findd(li, want):
    for x in li:
        if want in x:
            return x
    return None
first = input()
second = input()
res = []


l = len(first)

for i in range(l):
    if first[i] == second[i]:
        continue
    new = {first[i],second[i]}
    tempF = findd(res,first[i])
    tempS = findd(res,second[i])

    if not tempF and not tempS:
        res.append(new)

    elif not tempF and tempS:
        tempS.add(first[i]) 

    elif tempF and not tempS:
        tempF.add(second[i])
    
    elif  tempF != tempS:
        res.pop(res.index(tempS))
        tempF.update(tempS)




min_res = 0
for x in res:
    min_res += len(x)

print(min_res - len(res))
