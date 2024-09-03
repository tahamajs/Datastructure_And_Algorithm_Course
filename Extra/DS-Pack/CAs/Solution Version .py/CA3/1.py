info = input()
info = info.split(' ')
h = int(info[0])
leaf = int(info[1])

visitedNodes = 0
lowerBound = 1
upperBound = 2 ** h
switchSide = False

def count_visited_nodes(leaf, h, lowerBound, upperBound, switchSide) :
    global visitedNodes
    n = 2 ** (h - 1)
    if lowerBound == upperBound :
        return
    if not switchSide :
        if leaf >= lowerBound and leaf <= upperBound - n :
            visitedNodes += 1
            switchSide = True
            count_visited_nodes(leaf, h - 1, lowerBound, upperBound - n, switchSide)
        else :/Users/tahamajs/Documents/uni/DS/Note/DS-Pack/CAs/Solution Version .py/CA3/3.py
            visitedNodes += 2 * n
            count_visited_nodes(leaf, h - 1, lowerBound + n, upperBound, switchSide)
    elif switchSide :
        if leaf >= lowerBound + n and leaf <= upperBound :
            visitedNodes += 1
            switchSide = False
            count_visited_nodes(leaf, h - 1, lowerBound + n, upperBound, switchSide)
        else :
            visitedNodes += 2 * n
            count_visited_nodes(leaf, h - 1, lowerBound, upperBound - n, switchSide)

count_visited_nodes(leaf, h, lowerBound, upperBound, switchSide)
print(visitedNodes)
