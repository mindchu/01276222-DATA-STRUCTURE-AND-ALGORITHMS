class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        else:
            return self.branch(self.root, data)
        
    def branch(self, root, data):
        if data < root.data:
            if root.left == None:
                root.left = Node(data)
            else:
                self.branch(root.left, data)
        else:
            if root.right == None:
                root.right = Node(data)
            else:
                self.branch(root.right, data)
        return self.root

    def height(self, node, result, level = 0):
        if node != None:
            self.height(node.right, result, level + 1)
            result.append(level)
            self.height(node.left, result, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
result = list()
T.height(root, result)
result.sort()
print(f"Height of this tree is : {result[-1]}")