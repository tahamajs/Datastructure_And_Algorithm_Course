import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


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
    class Node:
        def __init__(self,symbol , probability, left = None, right = None) -> None:
            # the tree direction (0 or 1)  
            self.code = ''
            
            self.probability = probability 
            self.symbol = symbol 
            self.right = right
            self.left = left
            
    def __init__(self):
        self.root = None
        # we have dictionary for that codes 
        self.codes = {}
        

    def set_letters(self, *args):
        self.letters =  list(args)

    def set_repetitions(self, *args):
        self.repetitions = list(args)

    def build_huffman_tree(self):
        self.nodes = [self.Node(self.letters[i], self.repetitions[i]) for i in range(len(self.letters)) ]
        self.freq = {self.letters[i]:self.repetitions[i] for i in range(len(self.letters))}
        while len(self.nodes) > 1:
            self.nodes.sort(key=lambda x:x.probability)
            left = self.nodes.pop(0)
            right = self.nodes.pop(0)
            merged_node = self.Node(probability= left.probability + right.probability , symbol=None,left=left ,right=right)
            self.nodes.append(merged_node)
        
        
        self.root = self.nodes[0]
        # print(len(self.nodes))
        self._generate_code(self.root,'')
    
    def _generate_code(self, node, code):
        if node == None :
            return 
        if node.symbol:
            self.codes[node.symbol] = code
        
        self._generate_code(node.left,code+'0')
        self._generate_code(node.right , code + '1')
        
        

    def get_huffman_code_cost(self):
        total_cost = 0
        # print(self.codes)
        for i in self.codes :
            # print(i)
            total_cost += len(self.codes[i])*self.freq[i]
            
        return total_cost
    
    def get_codes(self):
        return self.codes
        

    def text_encoding(self, text):
        let = {}
        for i in text:
            let[i] = let[i]+1 if i in let else 1
        self.letters= list(let.keys())
        self.repetitions = list(let.values())
        self.build_huffman_tree()
    
    def print_hafman_tree(self , node):
        if node == None:
            return
        print(node.probability , node.symbol)
        
        self.print_hafman_tree(node.left)
        self.print_hafman_tree(node.right)



class Bst:
    class Node:
        def __init__(self, val):
            self.value = val
            self.left = None
            self.right = None
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = self.Node(key)
            return
        tmp = self.root
        while True:
            left_chiled = tmp.left
            right_child  = tmp.right
            if key > tmp.value :
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = self.Node(key)
                    break
            else:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left = self.Node(key)
                    break
        
    
    
                
    def _inOrder(self,node):
        if node == None :
            return
        self._inOrder(node.left)
        print(node.value , end=' ')
        self._inOrder(node.right)
            

    def inorder(self):
        self._inOrder(self.root)
        


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

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

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()



# Create m1 MinHeap instance
# m1 = MinHeap()

# # Call heapify
# m1.heapify(10, 5, 30, 50)

# # Call find_min_child
# min_child_index_0 = m1.find_min_child(0)
# print("Min child index for index 0:", min_child_index_0)

# # Call heap_pop multiple times
# popped_value_1 = m1.heap_pop()
# popped_value_2 = m1.heap_pop()
# popped_value_3 = m1.heap_pop()
# popped_value_4 = m1.heap_pop()

# print("Popped values:", popped_value_1, popped_value_2, popped_value_3, popped_value_4)

# # Call find_min_child with invalid index
# min_child_index_neg_1 = m1.find_min_child(-1)
# min_child_index_1 = m1.find_min_child(1)

# print("Min child index for index -1:", min_child_index_neg_1)
# print("Min child index for index 1:", min_child_index_1)
