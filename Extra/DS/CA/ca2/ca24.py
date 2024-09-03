 
a = []
t = {}
def is_motagharen(p):
    l= len(p)
    for i in range(l//2):
        if p[i] != p[l -1 - i]:
            return False
    return True

step = int(input())

while step:
    s = input().split()
    if s[0] == "push":
        a.append(s[1])
        l = len(a)
        r = ""
        for i in range (l):
            r += a[l-i-1]
            if is_motagharen(r):
                if r not in t:
                    t[r]=1
                else: t[r]+=1
        

    else:
        
        l = len(a)
        r = ""
        for i in range (l):
            r += a[i]
            if is_motagharen(r):
                 t[r]-=1
                 if not t[r]:
                    del t[r]
        a.pop(0)
    print(len(t))
    step -=1
