from itertools import permutations



def all_permutations(input_str):
    # Use permutations function from itertools
    perm_list = permutations(input_str)
    
    # Convert each permutation tuple to a string
    result = [''.join(perm) for perm in perm_list]
    
    return result



dic = {}





def get_all_reverse_intervals(n):
    intervals = []
    
    for i in range(n):
        for j in range(i, n):
            intervals.append((i, j))
    
    return intervals

def reverse_interval(arr, start, end):
    return arr[:start] + arr[start:end + 1][::-1] + arr[end + 1:]

def apply_all_reverse_intervals(s):
    n = len(s)
    all_intervals = get_all_reverse_intervals(n)
    reversed_strings = [reverse_interval(s, start, end) for start, end in all_intervals]
    
    return reversed_strings









all_results = {}

tool = {}

visited = {}


all_chileds= {}

visiiiiiited = {}

def BBFFS(string_data):
    time = 0

    visited = {}
    qq = []
    qq.append(string_data)
    visiiiiiited[string_data] = 1
    time += 1

    tool[string_data] = 0
    visited[string_data] = 1
    while(qq):
        # print(qq)
        main_node = qq.pop(0)
        all_permutations = all_chileds[main_node]
        for new_str in all_permutations:
            if not visiiiiiited[new_str]:
                visiiiiiited[new_str] = 1
                time += 1
                qq.append(new_str)
                tool[new_str] = tool[main_node]+1
                visited[new_str] = 1
        



n = int(input())

r = int(input())


alphabet = 'abcdefghijklmnopqrstuvwxyz'


inputs = []
for i in range(r):
    inputs.append(list(input().split()))


all_gens = all_permutations(inputs[0][0]) 
all_chileds= { i:apply_all_reverse_intervals(i) for i in all_gens}

visiiiiiited = { i : 0 for i in all_gens}


BBFFS(alphabet[:n])









maped_dict = {}

for node in inputs:
    maped_dict = {}
    # print(abs(tool[node[0]]- tool[node[1]]))
    for i in range(n):
        maped_dict[node[0][i]] = alphabet[i]

    final_str = []
    
    for i in range(n):
        final_str.append(maped_dict[node[1][i]])
        # maped_dict[]    
    ff = ''.join(final_str)
    
    print(tool[ff])

# print(tool)