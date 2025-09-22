class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            return self.branch(self.root, val)

    def delete(self, r, data):
        #code here
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
#code here