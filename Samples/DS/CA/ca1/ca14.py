a, b ,c= input().split()
a, b ,c= int(a), int(b),int(c)

def get_prime(n):
    prime = [ True for i in range(661000)]
    res =[]
    

   
    for i in range(2,int(661000**0.5)):
      if prime[i]:
        for j in range(i,int(661000/i)):
          prime[j * i] = False
        

      
    

    count = 0
    for i in range(2,661000):
      if prime[i]:
        res.append(i)
        count+=1
      if count >= n:
        break
     
    return res
      
    
primee= get_prime(b)
people = [i for i in range(1,a+1)]

for i in range(b):
    l = primee[i] % (a*(a-1))
    step = l//a
    people = people[0:1] + people[step+1:]+people[1:step+1]
    
    f = people.pop(0)
    people.insert(l%a, f)
    

index = people.index(c)
print(people[index + 1 if index != a-1 else 0],people[index - 1 if index else a-1])