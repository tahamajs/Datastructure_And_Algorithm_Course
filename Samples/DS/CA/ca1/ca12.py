x = int(input())
l = {}
for i in range(x):
    y = input()
    if y[0] in l:
        l[y[0]]+=1
    else:
        l[y[0]] =1

r=[]
for a in l:
    if(l[a] >= 5):
        r.append(a)

r = sorted(r)

print("How long must I suffer" if not r else ''.join(r))