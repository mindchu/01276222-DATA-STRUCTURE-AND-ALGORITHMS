class node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
    
    def __str__(self):
        return str(self.data)
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        point = node(data)
        if self.head == None:
            self.head = point
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = point

    def insert_head(self, data):
        point = node(data, self.head)
        self.head = point

    def delete(self, data):
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev = self.head
        curr = self.head.next
        while curr != None:
            if curr.data == data:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

linklist = LinkedList()
inp = input("Enter Commands: ").split()
i = 0
while i < len(inp):
    if inp[i] in ["append", "insert_head", "delete"]:
        data = inp[i + 1]
        if inp[i] == "append":
            linklist.append(data)
        elif inp[i] == "insert_head":
            linklist.insert_head(data)
        elif inp[i] == "delete":
            linklist.delete(data)
    elif inp[i] == "print":
        linklist.print_list()
    i += 1
