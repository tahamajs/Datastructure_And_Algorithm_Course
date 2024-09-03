import sys
sys.setrecursionlimit(10 ** 6)

delta_x = [1, -1, 0, 0]
delta_y = [0, 0, 1, -1]

info = input().split()

n = int(info[0])
m = int(info[1])
k = int(info[2])

visitStatus = []

for i in range(n) :
    v = []
    for j in range(m) :
        v.append(False)
    visitStatus.append(v)

def read_map (parkMap) :
    for i in range(n) :
        parkMap.append(input())

def can_move (parkMap, xp, yp) :
    if  (xp >= m or xp < 0) or (yp >= n or yp < 0) or (parkMap[yp][xp] == '0') or (visitStatus[yp][xp] == True) :
        return False
    else :
        return True

def count_connected_trees (parkMap, xp, yp, treesCount) :
    for i in range(4) :
        if can_move(parkMap, xp + delta_x[i], yp + delta_y[i]) :
            visitStatus[yp + delta_y[i]][xp + delta_x[i]] = True
            treesCount[0] += 1
            count_connected_trees(parkMap, xp + delta_x[i], yp + delta_y[i], treesCount)
    return treesCount

def save_paths_length (parkMap, visitStatus) :
    pathsLength = []
    for i in range(n) :
        for j in range(m) :
            if parkMap[i][j] == '1' and visitStatus[i][j] == False :
                visitStatus[i][j] = True
                pathsLength.append(count_connected_trees(parkMap, j, i, [1])[0])

    pathsLength.sort(reverse = True)
    return pathsLength

def calc_result (pathsLength) :
    maxTrees = 0
    for i in range(min(len(pathsLength), k)) :
        maxTrees += pathsLength[i]
    return maxTrees
    
parkMap = []
read_map(parkMap)
pathsLength = save_paths_length(parkMap, visitStatus)
print(calc_result(pathsLength))
