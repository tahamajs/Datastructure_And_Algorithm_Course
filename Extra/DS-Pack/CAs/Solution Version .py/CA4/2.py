delta_x = [1, -1, 1, 1, -1, -1, 0, 0]
delta_y = [0, 0, 1, -1, 1, -1, 1, -1]

info = input().split()
n = int(info[0])
m = int(info[1])

visitStatus = [[False for i in range(m)] for j in range(n)]

def read_map () :
    map = []
    for i in range(n) :
        map.append(input())
    return map

def find_crystal (map) :
    crystalPlace = []
    for i in range(n) :
        for j in range(m) :
            if map[i][j] == '$' :
                crystalPlace.append(j)
                crystalPlace.append(i)
                return crystalPlace


def is_exit_point (xp, yp) :
    if (xp <= 0 or xp >= m - 1) or (yp <= 0 or yp >= n - 1) :
        return True
    else : 
        return False

def can_move (map, xp, yp) :
    if map[yp][xp] == '#' or visitStatus[yp][xp] == True :
        return False
    else :
        return True

def find_shortest_path (map, xp, yp) :
    visitStatus[yp][xp] = True
    verticesQueue = []
    verticesQueue.append([yp, xp, 1])

    while len(verticesQueue) != 0 :
        currPoint = verticesQueue.pop(0)
        if is_exit_point(currPoint[1], currPoint[0]) :
            return currPoint[2]
        for i in range(8) :
            if can_move(map, currPoint[1] + delta_x[i], currPoint[0] + delta_y[i]) :
                visitStatus[currPoint[0] + delta_y[i]][currPoint[1] + delta_x[i]] = True
                verticesQueue.append([currPoint[0] + delta_y[i], currPoint[1] + delta_x[i], currPoint[2] + 1])
    
    return -1

map = read_map()
crystalPlace = find_crystal(map)
print(find_shortest_path(map, crystalPlace[0], crystalPlace[1]))
