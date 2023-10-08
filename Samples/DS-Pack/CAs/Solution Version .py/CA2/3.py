l = list(input())
i = 0
j = 1

senators_type_count = []
senators_type_count.append(l.count('R'))
senators_type_count.append(l.count('D'))

j_passed_end = 0
i_passed_end = 0

def del_senator(l, index, senators_type_count) :
    if l[index] == 'R' :
        senators_type_count[0] -= 1
    else :
        senators_type_count[1] -= 1
    l.pop(index)
     
while senators_type_count[0] != 0 and senators_type_count[1] != 0 :
    if j >= len(l) :
        j = 0
        j_passed_end += 1
    if i >= len(l) :
        i = 0
        i_passed_end += 1
    if l[i] != l[j] :
        del_senator(l, j, senators_type_count)
        if i_passed_end == j_passed_end :
            i += 1
    else :
        j += 1

if l.count('R') == 0 :
    print('Dire')
else :
    print('Radiant')