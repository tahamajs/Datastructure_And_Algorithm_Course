import unittest
import sys
import functools

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if attr == 'Node':
                setattr(cls, attr, getattr(cls, attr))
            elif callable(getattr(cls, attr)) :
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

@for_all_methods(staticmethod)
class Utils():
    def parse_line(line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def delete_end_char(line):
        return line.rstrip(line[-1])

    def get_attribute_pointer(object, attribute):
        return getattr(object, attribute)

    def get_args(argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def run_function(attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)
      
    def covert_args_to_int(args):
        newArgsList = list(args[1:])
        for i in range(1, len(args)):
            if isinstance(args[i], str) and (args[i].isnumeric() or args[i][0] == '-'):
                newArgsList[i - 1] = int(args[i])
        return tuple([args[0]] + newArgsList)
    
    def delete_quotation(args):
        newArgsList = list(args)
        for i in range(1,len(args)):
            if isinstance(newArgsList[i], str):
                newArgsList[i] = newArgsList[i].replace('\'', '')
        return tuple(newArgsList)

def fix_str_arg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(len(args) > 1):
            args = Utils.delete_quotation(args)
            args = Utils.covert_args_to_int(args)
        return func(*args, **kwargs)
    return wrapper

def print_raised_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            if val != None:
                return val
        except Exception as e:
            print(str(e))
    return wrapper

class MainEmu():
    def __init__(self):
        self.items = dict()

    def start_program(self):
        for line in sys.stdin:
            line = Utils.delete_end_char(line)
            action, line = Utils.parse_line(line)
            actionPointer = Utils.get_attribute_pointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = Utils.parse_line(line)
        itemName, line = Utils.parse_line(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = Utils.parse_line(line, '.')
        funcName, line = Utils.parse_line(line, '(')
        argsLine, line = Utils.parse_line(line, ')')
        args = Utils.get_args(argsLine)
        attribute = Utils.get_attribute_pointer(self.items[itemName],
                                                   funcName)

        Utils.run_function(attribute, args)

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class MinHeap:
    def __init__(self):
        self.heap =[]
        self.NOE =0
    
    class Node:
        def __init__(self,val):
            self.val = val
            
    def bubble_up(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        if not self.NOE:
            raise Exception('empty')
        if index < 0 or index >= self.NOE:
            raise Exception('out of range index')
    
        while index >0:
            if (index-1)//2 >=0 and self.heap[(index-1)//2].val > self.heap[index].val:
                self.heap[(index-1)//2].val,self.heap[index].val=self.heap[index].val,self.heap[(index-1)//2].val
            else: break
            index =(index-1)//2
            
# make min_heap m1
# call m1.heapify(10,5,30,50)
# call m1.find_min_child(0)
# call m1.heap_pop()
# call m1.heap_pop()
# call m1.heap_pop()
# call m1.heap_pop()
# call m1.find_min_child(-1)
# call m1.find_min_child(1)
# call m1.find_min_child('salap')


    def bubble_down(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        if not self.NOE:
            raise Exception('empty')
        if index < 0 or index >= self.NOE:
            raise Exception('out of range index')


        min = index
        while 2*index < self.NOE:
            if 2*index+1 < self.NOE and self.heap[min].val > self.heap[2*index+1].val:
                min = 2*index+1
            if 2*index+2 < self.NOE and self.heap[min].val > self.heap[2*index+2].val:
                min = 2*index+2
            if min != index:
                self.heap[min].val,self.heap[index].val=self.heap[index].val,self.heap[min].val
                index = min
            else: break
    
    def heap_push(self, value):
        new = self.Node(value)
        self.heap.append(new)
        self.NOE +=1
        self.bubble_up(self.NOE-1)
        
        
    def heap_pop(self):
        if not self.NOE:
            raise Exception('empty')
        popped = self.heap[0].val
        self.heap[0].val = self.heap[self.NOE-1].val
        self.NOE -=1
        self.heap.pop()
        if self.NOE:self.bubble_down(0)
        return popped

    def find_min_child(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        if index < 0 or index >= self.NOE:
            raise Exception('out of range index')
        if not self.NOE:
            raise Exception('empty')

        if 2*index < self.NOE:
            min = 2*index+1
            if self.heap[2*index+1].val > self.heap[2*index+2].val:
                 min = 2*index+2
        return min            

    def heapify(self, *args):
        for val in args:
            self.heap_push(val)


class HuffmanTree:
    def __init__(self):
        self.letters= []
        self.freqs=[]
        self.head = None
        self.encoded = None

    @fix_str_arg    
    def set_letters(self,*args):
        self.letters=args
        self.encoded = {i:None for i in self.letters }

    @fix_str_arg    
    def set_repetitions(self,*args):
        self.freqs=args

    class Node:
        def __init__(self,lett,freq,left=None,right=None):
            self.letter = lett
            self.freq = freq
            self.left = left
            self.right = right
            self.dir=""
            #for 1 or 0

    def build_huffman_tree(self):
        nodes = list(zip(self.freqs,self.letters))
        
        nodes = [self.Node(i,j) for j,i in nodes]
        nodes.sort(key = lambda x : (x.freq,x.letter),reverse=True)
        while len(nodes)>1:
           nodes.sort(key = lambda x : (x.freq),reverse=True)
           r = nodes[-1]
           l = nodes[-2]
           nodes = nodes[:-2]
           r.dir="0"
           l.dir="1"
           new_head= self.Node("",r.freq+l.freq,l,r)
           nodes = [new_head] + nodes
           self.head = new_head
        self.encoding(node = self.head)

    def encoding(self,node,huff =""):
        
        n = huff + node.dir
        if node.right:
            self.encoding(node.right,n)
        if node.left:
            self.encoding(node.left,n)
        
        if not node.right and not node.left:
            self.encoded[node.letter] = n

        
    def get_huffman_code_cost(self):
        res =0
        index =0
        for i in self.encoded:
            res += self.freqs[index]*len(self.encoded[i])
            index+=1
        return res
        

    @fix_str_arg
    def text_encoding(self, text):
        let = {}
        for i in text:
            let[i] = let[i]+1 if i in let else 1
        self.letters= list(let.keys())
        self.freqs = list(let.values())
        self.encoded = {i:None for i in self.letters }
        self.build_huffman_tree()
        

        

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class RedBlackTree():
    def __init__(self):
        self.root=self.Node(None)

        
    class Node:
        def __init__(self,parent,val =None,left = None,right =None,color="BLACK"):
            self.value = val
            self.color = color
            self.parent = parent 
            self.left = left
            self.right = right

    def fix_insert(self, node):
        while node.parent and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle= node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color ="BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        self.left_rotate(node.parent)
                        # self.right_rotate(node.parent)
                        node = node.left
                    else:
                         self.right_rotate(node.parent.parent)
                         node.parent.color = "BLACK"
                         node.parent.right.color="RED"
            else:
                uncle= node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color ="BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        self.right_rotate(node.parent)
                        node = node.right
                    else:
                         self.left_rotate(node.parent.parent)
                         node.parent.color = "BLACK"
                         node.parent.left.color="RED"
            
        self.root.color = "BLACK"
        
    def find_node_color(self, value):
        if not self.root.value:
            return None
        x = self.root
        while x:
            if x.value > value:
                x = x.left
            elif x.value == value:
                return x.color
            else:x=x.right
        
        
        

    def left_rotate(self, node):
        rc =node.right
        node.right = rc.left
        if  rc.left:
            rc.left.parent = node
        rc.parent = node.parent
        if not node.parent:
            self.root = rc
        elif node.parent.left == node:
            node.parent.left = rc
        else: node.parent.right = rc
        rc.left = node
        node.parent = rc

    def right_rotate(self, node):
        lc =node.left
        node.left = lc.right
        if  lc.right:
            lc.right.parent = node
        lc.parent = node.parent
        if not node.parent:
            self.root = lc
        elif node.parent.left == node:
            node.parent.left = lc
        else: node.parent.right = lc
        lc.right = node
        node.parent = lc
        
    def insert(self, value):
        y = None
        x = self.root
        while x.value != None:
            y = x
            if value < x.value:
                x =x.left
            else: x = x.right
        new = self.Node(y,value,self.Node(self),self.Node(self),"RED")
        if not y: self.root = new
        elif new.value < y.value:
            y.left = new
        else: y.right = new
        self.fix_insert(new)


classDict = { "min_heap": MinHeap, "red_black_tree": RedBlackTree, "huffman_tree": HuffmanTree}
    
if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.start_program()
