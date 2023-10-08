NEIGHBOURS_COUNT = 8
inputStr = input()
inputStr = inputStr.split(',')
n = int(inputStr[0])
word = inputStr[1]
max_index = len(word) - 1

table = []

for i in range(n) :
    line = input()
    line = line.split(',')
    table.append(line)

#top : x = x - 1 , y = y + 0
#down : x = x + 1, y = y + 0
#right : x = x + 0, y = y + 1
#left : x = x + 0, y = y - 1
#top_left : x = x - 1, y = y - 1
#top_right : x = x - 1, y = y + 1
#down_left : x = x + 1, y = y - 1
#down_right : x = x + 1, y = y + 1

delta_x = [-1, 1, 0, 0, -1, -1, 1, 1]
delta_y = [0, 0, 1, -1, -1, 1, -1, 1]

def can_move(x, y, previous_x, previous_y) :
    if (x == previous_x and y == previous_y) or x < 0 or y < 0 or x > n - 1 or y > n - 1 :
        return False
    return True

def find_word(x, y, previous_x, previous_y, table, index, word_location) :
    if table[x][y] != word[index] or index > max_index :
        return

    word_location += '(' + str(x) + ',' + ' ' + str(y) + ')'
    if index != max_index :
        word_location += ','
    
    if index == max_index :
        print(word_location)
        return

    for i in range(NEIGHBOURS_COUNT) :
        if can_move(x + delta_x[i], y + delta_y[i], previous_x, previous_y) :
            find_word(x + delta_x[i], y + delta_y[i], x, y, table, index + 1, word_location)

def find_all_words(table) :
    for i in range(n) :
        for j in range(n) :
            if table[i][j] == word[0] :
                find_word(i, j, -1, -1, table, 0, '')

find_all_words(table)
