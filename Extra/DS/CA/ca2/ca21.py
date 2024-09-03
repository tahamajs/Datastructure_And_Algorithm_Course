import sys

class Queue:
    def __init__(self):
        self.queue = []

    def getSize(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue = [value] +self.queue

    def dequeue(self):
        if(len(self.queue) <1):
            return None
        return self.queue.pop()

    def isEmpty(self):
        if (len(self.queue) < 1):
            return True
        return False

    def getInOneLine(self):
        return " ".join(list(reversed(self.queue)))

class Stack:
    def __init__(self, size=10):
        self.stack = []
        self.maxSize = size
    
    def isEmpty(self):
        if(len(self.stack) <1):
            return True
        return False

    def push(self, value):
        if(len(self.stack) >= self.maxSize):
            self.expand()
        self.stack.append(value)

    def pop(self):
        if(len(self.stack) < 1):
            return None
        return self.stack.pop()

    def put(self,value_):
        if(len(self.stack) > 0):
            self.stack.pop()
        self.stack.append(value_)
        
    def peek(self):
        if(len(self.stack) <1):
            return None
        return self.stack[len(self.stack)-1]

    def expand(self):
        self.maxSize *=2

    def getInOneLine(self):
        return " ".join(self.stack)

    def getSize(self):
        return len(self.stack)
    
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


        

classDict = { "stack": Stack, "queue": Queue, "linked_list": LinkedList}

class Utils():
    def __init__(self):
        pass

    def parseLine(self, line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def deleteEndChar(self, line):
        return line.rstrip(line[-1])

    def getAttributePointer(self, object, attribute):
        return getattr(object, attribute)

    def getArgs(self, argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def runFunction(self, attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)

class MainEmu():
    def __init__(self):
        self.utils = Utils()
        self.items = dict()

    def startProgram(self):
        for line in sys.stdin:
            line = self.utils.deleteEndChar(line)
            action, line = self.utils.parseLine(line)
            actionPointer = self.utils.getAttributePointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = self.utils.parseLine(line)
        itemName, line = self.utils.parseLine(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = self.utils.parseLine(line, '.')
        funcName, line = self.utils.parseLine(line, '(')
        argsLine, line = self.utils.parseLine(line, ')')
        args = self.utils.getArgs(argsLine)
        attribute = self.utils.getAttributePointer(self.items[itemName],
                                                   funcName)

        self.utils.runFunction(attribute, args)

if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.startProgram()