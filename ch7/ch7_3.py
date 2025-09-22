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
    
    def search(self, node, k, level = 0):
        if node == None:
            return 0
        count = self.search(node.right, k, level + 1)
        if node.data <= k:
            count += 1
        print('     ' * level, node)
        count += self.search(node.left, k, level + 1)
        return count
    
T = BST()
inp, k = input("Enter Input : ").split("/")
k = int(k)
inp = inp.split()
for i in inp:
    i = int(i)
    root = T.insert(i)
count = T.search(root, k)
print("--------------------------------------------------")
print(count)




