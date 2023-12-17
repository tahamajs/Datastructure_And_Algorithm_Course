
class Stack_implimantation:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop(len(self.stack) - 1)

    def put(self, value):
        if not self.isEmpty():
            self.pop()
        self.push(value)

    def peek(self):
        if(not self.isEmpty()):
            return self.stack[len(self.stack) - 1]
        else:
            return 0
        #for return 0 if empty 
        


# n = int(input())


# lis = list(map(int, input().split()))



dict = {}





# prev = []
# stack = []

# for num in lis:
#     while stack and stack[-1] <= num:
#         stack.pop()

#     if stack:
#         prev.append(dict[stack[-1]])
#     else:
#         prev.append(-1)

#     stack.append(num)



n = int(input())
inp = [int(i) for i in input().split()]
pos = {inp[i]:i for i in range(len(inp))}




for i,nod in enumerate(pos):
    dict[nod] = i


prev = {0:-2}

first_stack = Stack_implimantation()
for i in range(n, 0, -1):
    if(first_stack.isEmpty()):
        first_stack.push(pos[i])
        prev[pos[i]] = -1
    else:
        while(first_stack.peek() > pos[i]):
            first_stack.pop()
        
        if(first_stack.isEmpty()):
            first_stack.push(pos[i])
            prev[pos[i]] = -1
            
        else:
            
            prev[pos[i]] = first_stack.peek()
            first_stack.push(pos[i])



second_stack = []




# sumsss = 0
# print(0)
# for i in range(1,n+1):
    
        
#     while(second_stack):
#         if (dict[i] < second_stack[-1]):
#             second_stack.pop()
#             sumsss -= 1
#         else:
#             break



#     if (prev[dict[i]] != -1) :
#         if(not second_stack) :
#             sumsss += 1
#             second_stack.append(dict[i])
#         elif (second_stack and prev[(second_stack[-1])] != prev[dict[i]]) :
#             sumsss += 1
#             second_stack.append(dict[i])



#     print(sumsss)
                
            

answers = [0] * (n+1)


second_stack = Stack_implimantation()

flag = True

for i in range(1,n+1):
    answers[i] = answers[i-1]
    
    
    while( not second_stack.isEmpty() and pos[i] < second_stack.peek()):
        second_stack.pop()
        answers[i]-=1
    if(prev[pos[i]] != -1 and (second_stack.isEmpty()) ):
        flag = True
    elif(( prev[pos[i]] != -1 and prev[pos[i]] != prev[second_stack.peek()])):
        flag = True
    else:
        flag = False
    
    if flag :
        answers[i]+=1
        second_stack.push(pos[i])

for i in range(len(answers)):
    print(answers[i])
            