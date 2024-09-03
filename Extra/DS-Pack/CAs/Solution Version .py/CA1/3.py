def calc_mvn(r, l) :
    rBitsCount = len(bin(r)) - 2
    lBitsCount = len(bin(l)) - 2

    if bin(l).count('1') == lBitsCount :
        return l

    if lBitsCount != rBitsCount :
        return (2 ** (lBitsCount - 1)) - 1
    else :
        rr = list(bin(r)[2:])
        for i in range(len(rr) - 1, -1, -1) :
            if rr[i] == '0' :
                rr[i] = '1'
                if int(''.join(rr), 2) > l :
                    rr[i] = '0'
                    return int(''.join(rr), 2)

def find_answers(lines) :
    for line in lines :
        print(calc_mvn(int(line[0]), int(line[1])))

t = int(input())
lines = []

for i in range(t) :
    line = []
    line = input()
    line = line.split()
    lines.append(line)

find_answers(lines)