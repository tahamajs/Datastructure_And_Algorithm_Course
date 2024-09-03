class Node :
    def __init__(self, key) :
        self.key = key
        self.right = None
        self.left = None

def insert(grade, node) :
    if node is None :
        return Node(grade)
    if grade > node.key :
        node.right = insert(grade, node.right)
    else :
        node.left = insert(grade, node.left)
    return node

def get_min(node) :
    tempNode = node
    while tempNode.left is not None :
        tempNode = tempNode.left
    return tempNode.key

def get_max(node) :
    tempNode = node
    while tempNode.right is not None :
        tempNode = tempNode.right
    return tempNode.key

def del_node(grade, root) :
    if root is None :
        return root
    if grade > root.key :
        root.right = del_node(grade, root.right)
    elif grade < root.key :
        root.left = del_node(grade, root.left)
    else :
        if root.right is None :
            tempNode = root.left
            root = None
            return tempNode
        elif root.left is None :
            tempNode = root.right
            root = None
            return tempNode
        tempNode = get_min(root.right)
        root.key = tempNode.key
        root.right = del_node(tempNode.key, root.right)
    return root

n = int(input())

def read_commands() :
    commands = []
    for i in range(n) :
        command = input()
        command = command.split(' ')
        commands.append(command)
    return commands

def check_commands(commands) :
    root = None
    for command in commands :
        if command[0] == '1' :
            root = insert(int(command[1]), root)
        elif command[0] == '2' :
            minGrade = get_min(root)
            print(minGrade)
            root = del_node(minGrade, root)
        else :
            maxGrade = get_max(root)
            print(maxGrade)
            root = del_node(maxGrade, root)

commands = read_commands()
check_commands(commands)