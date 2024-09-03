import sys
import re


class Queue:
    def __init__(self):
        self.qq = []

    def getSize(self):
        return len(self.qq)

    def enqueue(self, value):
        self.qq.append(value)

    def dequeue(self):
        del self.qq[0]

    def isEmpty(self):
        if not self.qq :
            return True
        else:
            return False
        
    def getInOneLine(self):
        return ' '.join(map(str, self.qq))


class Stack:
    def __init__(self, size=10):
        self.top = -1
        self.ss = []
        self.size = 10

    def isEmpty(self):
        if self.top != (-1):
            return False
        return True

    def push(self, value):
        
        self.top += 1
        self.ss.push(value)

    def pop(self):
        self.top -= 1
        return self.ss.pop()

    def put(self, value):
        self.ss[self.top] = value

    def peek(self):
        return self.ss.top()

    def expand(self):
        self.size *= 2

    def getInOneLine(self):
        return ' '.join([str(i) for i in self.ss[:self.top+1]])

    def getSize(self):
        return self.top +1

    def getCapacity(self):
        return self.size


class Node:
    def __init__(self, val):
        self.next = None
        self.data = val


class LinkedList:
    def __init__(self):
        self.head = Node(0)

    def getList(self):
        result = ''
        current = self.head.next
        while current:
            result += str(current.data) + ' '
            current = current.next
        return result
        return self.head.next.data

    
    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head.next
        self.head.next = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if not self.head.next.next:
            self.head.next.next = new_node
        else:
            current = self.head.next
            while current.next:
                current = current.next
            current.next = new_node


    def reverse(self):
        prev = None
        current = self.head.next

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head.next = prev
            
            

            
