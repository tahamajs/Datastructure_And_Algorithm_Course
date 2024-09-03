l = list(input())
i = 0

while i != len(l) - 1 :
    if l[i] == l[i + 1] :
        l.pop(i)
        l.pop(i)
        if i != 0 :
            i -= 1
    else :
        i += 1

ans = ''.join(l)
print(ans)
