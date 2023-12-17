import sys
import re


class Queue:
    def __init__(self):
        self.qq = []

    def getSize(self):
        return len(self.qq)

    def enqueue(self, value):
        self.qq = [value] +self.qq

    def dequeue(self):
        if(len(self.qq) <1):
            return None
        return self.qq.pop()

    def isEmpty(self):
        if (len(self.qq) < 1):
            return True
        return False
        
    def getInOneLine(self):
        return ' '.join(map(str, reversed(self.qq)))


class Stack:
    def __init__(self, size=10):
        self.ss = []
        self.maxSize = size
    
    def isEmpty(self):
        if(len(self.ss) <1):
            return True
        return False

    def push(self, value):
        if(len(self.ss) >= self.maxSize):
            self.expand()
        self.ss.append(value)

    def pop(self):
        if(len(self.ss) < 1):
            return None
        return self.ss.pop()

    def put(self,value_):
        if(len(self.ss) > 0):
            self.ss.pop()
        self.ss.append(value_)
        
    def peek(self):
        if(len(self.ss) <1):
            return None
        return self.ss[len(self.ss)-1]

    def expand(self):
        self.maxSize *=2

    def getInOneLine(self):
        return " ".join(self.ss)

    def getSize(self):
        return len(self.ss)
    
    def getCapacity(self):
        return self.maxSize

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.count = 0
    
    def getList(self):
        res= []
        buffer = self.head
        while buffer :
            res.append(buffer.val)
            
            buffer = buffer.next
        return " ".join(res)
    
    def insertFront(self, new_data):
        new = Node(new_data)
        
        if(self.head == None):
            self.head = new
            return
        new.next = self.head
        self.head = new

    
    def insertEnd(self, new_data):
        new = Node(new_data)
        buffer = self.head
        if(buffer == None):
            self.head = new
            return
        while(buffer.next != None):
            buffer = buffer.next
        buffer.next = new
        
    
    def reverse(self):
        per = None
        if(self.head == None):
            return
        current = self.head
        next = current.next
        while next:
            current.next = per
            per = current
            current = next
            if next:
                next = current.next
        current.next = per
        self.head = current
            
            


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
