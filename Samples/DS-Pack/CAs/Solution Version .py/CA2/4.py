allMembers = input()
gpMembers = input()
allMembers = allMembers.split(',')
gpMembers = gpMembers.split(',')
gpCount = 0
maxIndex = len(allMembers) - 1

def in_range(indInAll) :
    return indInAll >= 0 and indInAll <= maxIndex

def del_forward(indInAll) :
    if in_range(indInAll + 1) and allMembers[indInAll + 1] in gpMembers :
        gpMembers.remove(allMembers[indInAll + 1])
        del_forward(indInAll + 1)

def del_backward(indInAll) :
    if in_range(indInAll - 1) and allMembers[indInAll - 1] in gpMembers :
        gpMembers.remove(allMembers[indInAll - 1])
        del_backward(indInAll - 1)
    
while len(gpMembers) != 0 :
    indInAll = allMembers.index(gpMembers[0])
    gpMembers.pop(0)
    if in_range(indInAll + 1) and allMembers[indInAll + 1] in gpMembers :
        del_forward(indInAll)
    if in_range(indInAll - 1) and allMembers[indInAll - 1] in gpMembers :
        del_backward(indInAll)
    gpCount += 1

print(gpCount)