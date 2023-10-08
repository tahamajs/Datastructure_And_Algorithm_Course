class Node :
    def __init__(self, key) :
        self.key = key
        self.right = None
        self.left = None

def add_node(key, node) :
    if node is None :
        return Node(key)
    if key > node.key :
        node.right = add_node(key, node.right)
    else :
        node.left = add_node(key, node.left)
    return node

def find_least_diff(root, y) :
    tempNode = root
    leastDiff = abs(y - root.key)
    while tempNode is not None :
        if leastDiff > abs(y - tempNode.key) :
            leastDiff = abs(y - tempNode.key)
        if y > tempNode.key :
            tempNode = tempNode.right
        else :
            tempNode = tempNode.left
    return leastDiff

q = int(input())

def read_commands() :
    commands = []
    for i in range(q) :
        command = input()
        command = command.split(' ')
        commands.append(command)
    return commands

def check_commands(commands) :
    root = None
    for command in commands :
        if command[0] == '1' :
            root = add_node(int(command[1]), root)
        else :
            print(find_least_diff(root, int(command[1])))

commands = read_commands()
check_commands(commands)
