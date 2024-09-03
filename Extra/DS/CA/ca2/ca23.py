number = int(input())
num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
ress =[]
def find_max(arr,n):
    stack =[]
    if n == 0:
        return []
    index = 0
    la = len(arr)
    ls = 0
    for i in arr:
        index+=1
        if ls >= n and i <= stack[ls-1]:
            continue
        while ls >=1 and i > stack[ls-1] and ls +la - index >= n:
               stack.pop()
               ls -=1
        stack+=[i]
        ls +=1
    return stack
    
for i in range(max(number-len(num2),0),min(len(num1),number)+1):
    x1 = find_max(num1,i)
    x2 = find_max(num2,number - i)
    x = len(x1)+ len(x2)
    x3 = [max(x1,x2).pop(0) for _ in range(x)] 
    if x3 > ress:
        ress = x3
print(*ress) 

    


            

