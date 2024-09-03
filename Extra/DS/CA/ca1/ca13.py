
x, y = input().split()
x, y = int(x), int(y)
gcd = 1
for i in range(1,min(x,y)+1):
    if x % i == 0 and y % i == 0 :
        gcd = i
print(y - gcd)
