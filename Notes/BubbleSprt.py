


A = [2,32,2,2,2,33,4,4,4,4,23]
for i in range(1,len(A)-1):
    for j in range(i,len(A)-1):
        if A[j]<A[j-1]:
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
            
            


print(A)