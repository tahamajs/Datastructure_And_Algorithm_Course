class Queue:

    def __init__(self):
        self.qq = []
    
    def getSize(self):
        return len(self.qq)
    
    def enqueue(self,value):
        self.qq.append(value)
    
    def dequeue(self):
        del self.qq[0]
    
    def isEmpty(self):
        if not self.qq :
            return True
        else:
            return False
        
    def getInOneLine(self):
        return ' '.join([str(i) for i in self.qq])




class Stack:
    def __init__(self,size = 10):
        self.top = -1
        self.ss = [0]*size
        self.size = 10 
    
    def isEmpty(self):
        if self.top != (-1):
            return False
        return True
    
    def push(self, value):
        if self.size == (self.top -1):
            ss = ss + [0]*self.size
            self.size *=2
        
        self.top += 1
        self.ss[self.top] = value
        
    
    def pop(self):
        self.top -= 1
        return self.ss[self.top+1]
    
    def put(self,value_):
        
        self.ss[self.top] = value_
        
    def peek(self):
        return self.ss[-1]
    
    def expand(self):
        self.size *= 2
    
    def getInOneLine(self):
        return ' '.join([str(i) for i in self.ss[:self.top+1]])
    
    def getSize(self):
        return self.top +1
    
    def getCapacity(self):
        return self.size
    

class Node():
    def __init__(self ,data, next = None ):
        self.next = next
        # self.prev = None
        self.data = data
        
class LinkedList():
    def __init__(self):
        self.head = Node()
    
    def getList(self):
        str = ''
        current = self.head.next
        while current != None:
            str = str + current.data + ' '
        return str
    
    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    
link = LinkedList()
link.insertFront(33)

