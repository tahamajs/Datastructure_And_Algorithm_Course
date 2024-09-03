import math

n = int(input())

arr = list()
for _ in range(n): arr.append(list(input()))

totalOfB = 0

for i in range(n):
    countOfB = 0
    for c in arr[i]:
        if c == "B":
            countOfB += 1
    totalOfB += math.comb(countOfB, 2)

for col in range(n):
    countOfB = 0
    for row in range(n):
        if arr[row][col] == "B":
            countOfB += 1
    totalOfB += math.comb(countOfB, 2)

print(totalOfB)