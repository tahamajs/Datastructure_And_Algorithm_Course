
x, y = input().split()
x, y = int(x), int(y)
key = input().split(',')
data = []
for i in range(x):
    data.append(input().split(','))

sort = (input().split(' '))[2]
data = sorted(data, key=lambda x: x[key.index(sort)])
for i in data:
    print(','.join(i))
