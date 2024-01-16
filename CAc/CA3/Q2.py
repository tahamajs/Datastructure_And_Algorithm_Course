class Bst:
    class Node:
        def __init__(self, val):
            self.value = val
            self.left = None
            self.right = None
            self.father = None
            self.hight = 0

    def __init__(self):
        self.root = None
        self.fathers = {}
        self.hightes = {}

    def insert(self, key):
        if self.root == None:
            self.root = self.Node(key)
            self.root.hight = 0
            self.hightes[key] = 0
            return
        tmp = self.root
        
        main_hight = 1
        
        while True:
            if key >= tmp.value :
                if tmp.right:
                    tmp = tmp.right
                    main_hight +=1
                else:
                    tmp.right = self.Node(key)
                    tmp.right.hight = main_hight
                    tmp.right.father = tmp
                    self.hightes[key] = main_hight
                    self.fathers[key] = tmp.value
                    break
            else:
                if tmp.left:
                    tmp = tmp.left
                    main_hight +=1
                else:
                    tmp.left = self.Node(key)
                    tmp.left.hight = main_hight
                    self.hightes[key] = main_hight
                    tmp.left.father = tmp
                    self.fathers[key] = tmp.value
                    
                    break
        
    def get_father_ky(self,key):
        return self.get_node(key).father.value
        
    def get_father(self , key):
        return self.fathers.get(key , -100)

    
    def get_node(self,key):
        if self.root == None:
            return None
        if self.root.value == key:
            return self.root
        
        
        tmp = self.root
        while True:
            if key == tmp.value :
                return tmp
            
            if key > tmp.value :
                if tmp.right:
                    tmp = tmp.right
                
            else:
                if tmp.left:
                    tmp = tmp.left
    
    def get_jadd(self ,key1 ,key2):
        
        diff_of_hights = abs(self.hightes[key1] - self.hightes[key2])
        
        # print(diff_of_hights , "00000")
        
        
        # print(key1,key2)
        min_node = self.get_node(key1 if(self.hightes[key1] <= self.hightes[key2]) else key2)
        max_node = self.get_node(key1 if(self.hightes[key1] > self.hightes[key2]) else key2)
        # print(key1 if(self.hightes[key1] < self.hightes[key2]) else key2 , key1 if(self.hightes[key1] > self.hightes[key2]) else key2 , "esgdrtg")
        
        # print(key1 , key2)
        # print(self.hightes[key1] , self.hightes[key2])
        
        
        # print(min_node.value , max_node.value , diff_of_hights)
        
        
        for i in range(diff_of_hights):
            max_node = max_node.father
            
        # print(min_node.value , max_node.value , diff_of_hights , 'dserfsegrdrtg')
        # print(min_node==max_node)
        
        
        while (max_node.value != min_node.value):
            max_node = max_node.father
            min_node = min_node.father
        # print(min_node.value , max_node.value , diff_of_hights)
        
        return max_node.value
        
        
        
n = int(input())
all_nodes = list(map(int,input().split()))

bst = Bst()

for index, node in enumerate(all_nodes):
    bst.insert((node , index))

print(' '.join([ str(bst.get_father_ky( (all_nodes[i],i)) [0])for i in range(1 , n) ]))
# print(bst.hightes)
# print(bst.fathers)
# print(all_nodes)


a ,b = map(int , input().split())
a = a-1
b = b-1
# print(a,b)

print(bst.get_jadd((all_nodes[a],a),(all_nodes[b],b))[1]+1)