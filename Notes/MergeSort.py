A= [4,6,4,3,2,1,1,2,4,5]



def merge_sort(A):
    
    if(len(A) > 1):

        r = len(A)//2
        A1 = A[:r]
        A2 = A[r:]
        
        A1 = merge_sort(A1)
        A2 = merge_sort(A2)
        
        print(A1,A2)
        
        
        AA = []
        
        i = 0
        j = 0
        while (i < len(A1) and j < len(A2)):
            if A1[i] > A2[j]:
                AA.append(A1[i])
                i+=1
            else:
                AA.append(A2[j])
                j+=1
        
        
        while i < len(A1) :
            AA.append(A1[i])
            i+=1
        
        while j < len(A2):
            AA.append(A2[j])
            j+=1
        
        print(AA)
        return(AA)
    return A
print(merge_sort(A))