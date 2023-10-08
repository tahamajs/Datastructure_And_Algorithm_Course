def read_table(n) :
    table = []
    for i in range(n) :
        table.append(input())
    return table

def calc_row_points(table) :
    blueCount = 0
    row_points = 0
    for row in table :
        for character in row :
            if character == 'B' :
                blueCount += 1
        row_points += ((blueCount) * (blueCount - 1)) // 2
        blueCount = 0

    return row_points

def calc_col_points(table) :
    blueCount = 0
    col_points = 0
    for i in range(len(table)) :
        for row in table :
            if row[i] == 'B' :
                blueCount += 1
        col_points += ((blueCount) * (blueCount - 1)) // 2
        blueCount = 0

    return col_points

t = read_table(int(input()))
print(calc_row_points(t) + calc_col_points(t))
